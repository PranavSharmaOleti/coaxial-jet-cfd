# 4. Numerical plan (prep — no run yet)

## 4.1 Solver

- **rhoCentralFoam** (density-based, OpenFOAM): shock-capturing via central-upwind (Kurganov) scheme. Appropriate for supersonic flows with shocks. Alternative: sonicFoam (pressure-based) — less suited to strong shocks; avoid.
- Compressible, ideal gas, γ = 1.4, R = 287. Sutherland viscosity (μ0 = 1.716e-5, T0 = 273.15, S = 110.4) to match Re.

## 4.2 Turbulence

- RANS k-ω SST (default first pass). Justification: affordable on a single workstation, reasonable for core length and shock structure.
- Known limitation: RANS smears shock cells and under-predicts streamwise-vortex mixing from tabs. Core length may be within ~10–20%; tab benefit (ΔL*c) may be under-predicted. State this in the report. LES is the refinement step, not the first pass.

## 4.3 Boundary conditions

| Patch | Type | Value |
|---|---|---|
| Primary plenum inlet | totalPressure / totalTemperature (or fixedValue stagnation) | p0p/pa, T0 = 300 K per Table I |
| Secondary plenum inlet | totalPressure / totalTemperature | p0s/pa, T0 = 300 K |
| Outlet (far field) | waveTransmissive (nonReflecting) or pressureOutlet | pa, T∞ |
| Nozzle walls | noSlip, adiabatic | — |
| Tabs | noSlip (part of wall) | — |
| Symmetry (if used) | symmetryPlane | only if geometry permits; tabs break azimuthal symmetry → full 360° domain likely needed |

Note: secondary feed holes (25 × Ø2.5) are homogenized — treat secondary plenum as a stagnation reservoir feeding the convergent nozzle. Document.

## 4.4 Mesh strategy

- Structured-ish via blockMesh around the nozzle + snappyHexMesh for tabs and walls, or pure blockMesh with grading. Tabs are small (h = 2.2 mm) and need local refinement.
- Refinement zones: nozzle lip, shear layers (primary–secondary, secondary–ambient), shock-containing region (to ~15 Dp), tab wakes.
- Target: y+ ~ 30–100 with wall functions (or y+ ~ 1 with resolved BL if affordable). Given tab size, aim for ~20–40 cells across tab height.
- Domain: radius ≥ 5 Ds (≈ 130 mm), length ≥ 30 Dp (≈ 340 mm). Paper measures to 25 Dp.

## 4.5 Numerics

- Time: steady RANS (SIMPLE) first; if unsteady shocks/screech dominate, switch to PIMPLE/transient. Start steady.
- Schemes: limitedLinear for convective (TVD), Gauss linear for diffusion, local time stepping (pseudo-transient) to accelerate.
- Convergence: residuals < 1e-4, plus monitor L*c (core length) and mass flow balance until stable.

## 4.6 Case sequence (prep order)

1. C1 geometry + mesh (no tabs).
2. C1 run, extract L*c, compare to 24.7; iterate mesh/BCs.
3. C0 run (primary only) as sanity check (~18–18.7).
4. Add tabs → C2, C3, C4, C5.
5. Digitize validation data; quantify discrepancies.

## 4.7 Post-processing

- Centerline: sample p0 (Pitot) along x-axis; compute L*c where Mach = 1 (or p0t/p0p crosses cut-off). Use OpenFOAM `sample` or ParaView.
- Transverse profiles at x* = 2, 6, 8, 11 in xy and xz planes.
- Iso-contours of p0t/p0p in xy and xz planes.
- Shadowgraph-style density gradient (schlieren) visualization for qualitative shock structure.