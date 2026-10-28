#!/usr/bin/env python3
"""Generate blockMeshDict for C1 coaxial jet: exit-plane inlets, axisymmetric wedge.

No nozzle geometry resolved; primary & secondary jets specified as inlet patches at x=0.
Domain: x in [0, L], r in [0, R]. Wedge 5 deg.
"""
import math

L1 = 0.05
L2 = 0.3372          # 30 Dp
xs = [0.0, L1, L2]

rp = 0.01124/2       # primary exit radius
rlip = rp + 0.0032   # lip outer radius
rs = 0.0257/2        # secondary exit radius
Rdom = 0.15
rlist = [0.0, rp, rlip, rs, Rdom]

half = math.radians(2.5)
cosH = math.cos(half); sinH = math.sin(half)

verts = []; idx = {}
def add(x, r, side):
    # side: 0 axis, 1 front (z=+), 2 back (z=-)
    key = (x, r, 0) if r == 0.0 else (x, r, side)
    if key in idx: return idx[key]
    if r == 0.0:
        y, z = 0.0, 0.0
    else:
        y = r*cosH
        z = r*sinH if side == 1 else -r*sinH
    i = len(verts); verts.append((x,y,z)); idx[key]=i; return i

for x in xs:
    for r in rlist:
        if r == 0.0:
            add(x, r, 0)
        else:
            add(x, r, 1); add(x, r, 2)

# blocks
blocks = []
for i in range(len(xs)-1):
    for j in range(len(rlist)-1):
        r0, r1 = rlist[j], rlist[j+1]
        b0=add(xs[i],   r0, 2); b1=add(xs[i+1], r0, 2)
        b2=add(xs[i+1], r1, 2); b3=add(xs[i],   r1, 2)
        f0=add(xs[i],   r0, 1); f1=add(xs[i+1], r0, 1)
        f2=add(xs[i+1], r1, 1); f3=add(xs[i],   r1, 1)
        blocks.append((b0,b1,b2,b3,f0,f1,f2,f3,i,j))

# cell counts
n_ax = [30, 80]   # axial cells per segment
n_rad = [8, 6, 8, 25]  # radial cells per radial segment

def left_face(i,j):
    r0,r1 = rlist[j], rlist[j+1]
    a=add(xs[i], r0, 2); d=add(xs[i], r1, 2)
    e=add(xs[i], r0, 1); h=add(xs[i], r1, 1)
    return (a,d,h,e)
def right_face(i,j):
    r0,r1 = rlist[j], rlist[j+1]
    b=add(xs[i+1], r0, 2); c=add(xs[i+1], r1, 2)
    f=add(xs[i+1], r0, 1); g=add(xs[i+1], r1, 1)
    return (b,c,g,f)

out = []
out.append("/*--------------------------------*- C++ -*----------------------------------*\\")
out.append("\\*---------------------------------------------------------------------------*/")
out.append("FoamFile { format ascii; class dictionary; object blockMeshDict; }")
out.append("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //")
out.append("")
out.append("convertToMeters 1;")
out.append("")
out.append("vertices")
out.append("(")
for (x,y,z) in verts:
    out.append(f"    ({x:.6g} {y:.6g} {z:.6g})")
out.append(");")
out.append("")
out.append("blocks")
out.append("(")
for (b0,b1,b2,b3,f0,f1,f2,f3,i,j) in blocks:
    na = n_ax[i]; nr = n_rad[j]
    out.append(f"    hex ({b0} {b1} {b2} {b3} {f0} {f1} {f2} {f3}) ({na} {nr} 1) simpleGrading (1 1 1)")
out.append(");")
out.append("")
out.append("edges ( );")
out.append("")
out.append("boundary")
out.append("(")
# inletPrimary: x=0, r 0->rp  => i=0,j=0 left face
out.append("    inletPrimary { type patch; faces ( (" + " ".join(str(x) for x in left_face(0,0)) + ") ); }")
# lip: x=0, r rp->rlip => i=0,j=1
out.append("    lip { type wall; faces ( (" + " ".join(str(x) for x in left_face(0,1)) + ") ); }")
# inletSecondary: x=0, r rlip->rs => i=0,j=2
out.append("    inletSecondary { type patch; faces ( (" + " ".join(str(x) for x in left_face(0,2)) + ") ); }")
# inletAmbient: x=0, r rs->Rdom => i=0,j=3
out.append("    inletAmbient { type patch; faces ( (" + " ".join(str(x) for x in left_face(0,3)) + ") ); }")
# outlet: x=L2, all radial => i=1, all j
out.append("    outlet { type patch; faces (")
for j in range(4):
    out.append("        (" + " ".join(str(x) for x in right_face(1,j)) + ")")
out.append("    ); }")
# top (r=Rdom): all axial segments, j=3 right... actually top face is r=Rdom side: for each axial block, face (b2 b3 f3 f2)? 
# top face of block (i,j=3): vertices at r=Rdom: b2=(x_i+1,Rdom,back), b3=(x_i,Rdom,back), f3=(x_i,Rdom,front), f2=(x_i+1,Rdom,front)
# = (b2 b3 f3 f2). Let's compute per axial segment.
out.append("    top { type patch; faces (")
for i in range(2):
    j = 3
    r0, r1 = rlist[j], rlist[j+1]
    # top face: b2 b3 f3 f2  (back-tr, back-tl, front-tl, front-tr)
    a = add(xs[i+1], r1, 2); b = add(xs[i], r1, 2)
    c = add(xs[i], r1, 1); d = add(xs[i+1], r1, 1)
    out.append(f"        ({a} {b} {c} {d})")
out.append("    ); }")
# axis: r=0 faces (empty) for all axial segments
out.append("    axis { type empty; faces (")
for i in range(2):
    j = 0
    r0, r1 = rlist[j], rlist[j+1]  # 0, rp
    # axis face (r=0): b0 b1 f1 f0
    a = add(xs[i],   0, 2); b = add(xs[i+1], 0, 2)
    c = add(xs[i+1], 0, 1); d = add(xs[i],   0, 1)
    out.append(f"        ({a} {b} {c} {d})")
out.append("    ); }")
# front/back wedge faces
out.append("    front { type wedge; faces (")
for i in range(2):
    for j in range(4):
        r0, r1 = rlist[j], rlist[j+1]
        b0=add(xs[i],r0,2); b1=add(xs[i+1],r0,2); b2=add(xs[i+1],r1,2); b3=add(xs[i],r1,2)
        # front face of block = (f0 f1 f2 f3) = (add front r0 i, front r0 i+1, front r1 i+1, front r1 i)
        f0=add(xs[i],r0,1); f1=add(xs[i+1],r0,1); f2=add(xs[i+1],r1,1); f3=add(xs[i],r1,1)
        out.append(f"        ({f0} {f1} {f2} {f3})")
out.append("    ); }")
out.append("    back { type wedge; faces (")
for i in range(2):
    for j in range(4):
        r0, r1 = rlist[j], rlist[j+1]
        b0=add(xs[i],r0,2); b1=add(xs[i+1],r0,2); b2=add(xs[i+1],r1,2); b3=add(xs[i],r1,2)
        out.append(f"        ({b0} {b1} {b2} {b3})")
out.append("    ); }")
out.append(");")
out.append("")
out.append("mergePatchPairs ( );")
out.append("// ************************************************************************* //")

with open("/home/sankara/Projects/coaxial-jet-cfd/2_cases/C1/system/blockMeshDict","w") as fh:
    # ensure dir
    import os
    os.makedirs("/home/sankara/Projects/coaxial-jet-cfd/2_cases/C1/system", exist_ok=True)
    fh.write("\n".join(out))
print("written")
