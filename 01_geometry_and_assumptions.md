# 1. Reconstructed geometry and assumption log

Source: paper Sec. II.B (experimental model) + Fig. 1. All dimensions in mm unless noted. Dp = 11.24 mm is the reference length scale (x* = x/Dp).

## 1.1 Known dimensions (from the paper)

| Component | Quantity | Value | Source |
|---|---|---|---|
| Primary nozzle | Inner exit diameter Dp | 11.24 | Sec II.B |
| Primary nozzle | Throat diameter D* | 10.56 | Sec II.B |
| Primary nozzle | Design exit Mach (choked) | 1.43 | Sec II.B |
| Primary nozzle | Lip thickness tp | 2.65–3.2 | Sec II.B (2.65 for tabs; 3.2 stated) |
| Primary nozzle | Type | conical C-D | Sec II.B |
| Secondary nozzle | Inner diameter Ds | 25.7 | Sec II.B |
| Secondary nozzle | Ds/Dp | 2.3 | Sec II.B |
| Secondary nozzle | Lip thickness ts | 5.0 | Sec II.B |
| Secondary nozzle | Type | conical convergent | Sec II.B |
| Annular gap | between primary and secondary | 4.0 | Sec II.B |
| Base plate | thickness | 12 | Sec II.B |
| Base plate | feed holes | 25 × Ø2.5 at radius 20 | Sec II.B |
| Tabs | height h | ~2.2 | Sec II.B |
| Tabs | primary AR = h/w | 2.0 → w ≈ 1.1 | Sec II.B |
| Tabs | secondary AR = h/w | 0.75 → w ≈ 3.0 | Sec II.B |
| Tabs | count per set | 2, diametrically opposite | Sec II.B |
| Tabs | blockage per set | ~5% (2.5% per tab) | Sec II.B |
| Tabs | primary mounting | pasted on lip (adhesive) | Sec II.B |
| Tabs | secondary mounting | screwed on lip | Sec II.B |

## 1.2 Derived / reconstructed dimensions

| Quantity | Value | How |
|---|---|---|
| Primary outer diameter | 17.64 mm (= Dp + 2·tp) | from tp = 3.2 mm |
| Secondary exit (annular) area | π/4·(Ds² − 17.64²) | primary occupies center |
| Secondary exit area / primary exit area | 2.77 | computed |
| Annular gap check | (25.7 − 17.64)/2 = 4.03 mm ≈ 4.0 | consistent with stated gap |
| Bypass ratio B = ṁs/ṁp | 1.70–2.50 (Table I conditions) | isentropic, annular area; paper reports 1.9–2.5 ✓ |
| Deq/Dp | 1.64–1.87 | from B |
| Area ratio A/A* (design M 1.43) | 1.132 | isentropic; D*/Dp = 0.940 (given 0.9395) ✓ |
| Primary nozzle outer diameter | 17.64 mm | assumed tp = 3.2 mm on both sides |

## 1.2a Facility and nozzle details confirmed across the provided papers

Four of the provided papers (2014 triangular tabs, 2018 fluidic injectors, 2019 shifted tab, 2020 coaxial) use the **same IIT Kanpur open-jet facility**: cylindrical settling chamber 300 mm ID × 600 mm length, two wire-mesh screens, wide-angle diffuser, mixing tube, control valve, stagnation pressure/temperature tapings, O-ring slot holder. This is now well-established.

**However, every paper that gives nozzle geometry uses the Mach 2.0 nozzle** (D* = 10.02 mm, De = 13.02 mm, semi-divergence 7°, area ratio 1.688, design NPR 7.824, lip 5 mm). The 2020 paper's Mach 1.43 nozzle (D* = 10.56, Dp = 11.24) has **no published geometry details** — no cone angles, no lengths, no lip thickness specification beyond "3.2 mm (or 2.65 mm)". The 7° semi-divergence angle used in our reconstruction is therefore an **inference from the Mach 2 nozzle**, not a confirmed value. The PhD thesis (Arun Kumar P., 2013, IIT Kanpur) is the only remaining source that might contain the Mach 1.4 nozzle drawing; it was **not among the papers provided**.

This is a legitimate and important finding for the reconstruction report: the experimental nozzle geometry is partially undocumented, and we state our assumptions explicitly.

The 2014 paper (Kumar & Rathakrishnan, Aeronaut. J.) uses the **same IIT Kanpur facility** and a Mach 2.0 C-D nozzle with these stated details:
- Semi-divergence angle: **7°** (divergent section).
- Throat D* = 10.02 mm, exit De = 13.02 mm, expansion section axial length = 12.22 mm, area ratio 1.688, design NPR 7.824.
- Lip thickness = 5 mm.
- Tabs: 1 mm brass strips, 4 mm length.
- Settling chamber: 300 mm ID × 600 mm length, two wire-mesh screens, wide-angle diffuser, mixing tube, control valve.

For the 2020 paper's Mach 1.43 nozzle (D* = 10.56, Dp = 11.24), the 7° semi-divergence angle is the **leading assumption** (same facility/design philosophy): divergent section length ≈ (11.24 − 10.56)/(2·tan 7°) ≈ 2.77 mm. Plausible given the small area ratio (1.132). **Not confirmed** — the 2020 paper does not state its angle. The PhD thesis (2013, IIT Kanpur) is the authoritative source (not yet obtained).

| Item | Status | Assumption / plan |
|---|---|---|
| Convergent/divergent half-angles of primary C-D nozzle | **Unknown** | Assume conical with half-angles ~15° (convergent) and ~7° (divergent). Compute axial lengths from D* and Dp. Document. Sensitivity on divergent angle. |
| Axial lengths of primary nozzle (convergent + divergent) | **Unknown** | Derived from assumed angles: L_conv = (Dp? no) ... L = (D_exit − D_throat)/(2·tan θ) for each section. With D_inlet unknown, assume inlet diameter ~2·Dp or set plenum directly upstream of convergent section. |
| Primary nozzle inlet diameter / plenum | **Unknown** | Skip the inlet cone: set a stagnation plenum face just upstream of the convergent section (short approach length) or use a large inlet diameter. |
| Secondary nozzle length and convergent angle | **Unknown** | Assume conical convergent with half-angle ~15–20°, length giving Ds at exit and a plenum at base plate. |
| Secondary nozzle outer diameter / wall thickness | **Unknown** | Not needed for fluid domain; wall is a boundary. |
| Tab thickness (into flow / streamwise) | **Unknown** | Assume thin plate ~1 mm (or 0.5 mm). Flag as sensitivity; tabs are small so thickness mainly affects blockage. |
| Tab azimuthal position (absolute) | **Our choice** | Primary tabs on ±y axis; secondary tabs at 0° (C4, +y) or 90° (C5, +z) relative. Matches paper's xy/xz measurement planes. |
| Domain outer boundary shape/size | **Our choice** | Cylindrical or box, radius ≥ 5 Ds, length ≥ 30 Dp (paper measures to 25 Dp). |
| Tab leading-edge rounding | **Unknown** | Assume sharp (as paper describes rectangular tabs). |

## 1.4 Geometry parametrization strategy

Keep the unknowns above as named variables in a single parameter file (OpenFOAM `#calc` or a Python generator) rather than hard-coding, so a sensitivity run changes one number. Priority variables: divergent half-angle, tab thickness, domain length.

## 1.5 Research trail (nozzle geometry)

- The 2020 paper cites Ref 23 (Kumar & Rathakrishnan, Aeronaut. J. 2014) for nozzle calibration and Ref 29 (Kumar, Aileni & Rathakrishnan, Phys. Fluids 2019) for the same facility.
- Ref 23 (2014 paper) cites Ref 89: "Arun Kumar, P. *Triangular Tabs for Supersonic Jet Control*, PhD Thesis, 2013, IIT Kanpur" — this thesis is the likely source of the nozzle drawing (convergent/divergent angles, lengths).
- Neither the thesis nor the 2014 paper is freely available online (thesis not on Shodhganga/IITK repos we could reach; 2014 paper paywalled on Cambridge Core). The 2019 and 2020 papers are on AIP (may be accessible with institutional login).
- **Action for the user:** if you have IIT Kanpur / institutional library access, fetch the 2013 PhD thesis (highest value) and the 2014 Aeronaut. J. paper. Otherwise the assumed angles above stand and must be declared in the report.