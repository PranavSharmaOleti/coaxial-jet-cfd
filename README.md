# Coaxial jet passive control — reconstruction project

Reconstruction of the experiment in:

> Perumal, A. K., Singh, H., & Rathakrishnan, E. (2020). *Passive control of coaxial jet with supersonic primary jet and sonic secondary jet.* Physics of Fluids, 32(7), 076101. https://doi.org/10.1063/5.0012468

IIT Kanpur coaxial jet facility. Primary jet Mach 1.4 (under-expanded at several NPRs), sonic secondary jet, rectangular tabs in 5 configurations (C0–C5). Validation metric: supersonic core length L*c (and centerline Pitot pressure decay).

**Important framing:** the paper is purely experimental — there is no CFD, no mesh, no numerical method in it. We are building our own simulation and validating against their measurements. The goal is a defensible, documented reconstruction, not a contour plot.

## Index

| File | Content |
|---|---|
| `01_geometry_and_assumptions.md` | Reconstructed geometry, dimension table, assumption log |
| `02_operating_conditions.md` | Table I + derived quantities (isentropic) |
| `03_physics_and_method.md` | Physics the experiment relies on; what our CFD must capture |
| `04_numerical_plan.md` | Solver, turbulence, BCs, mesh strategy, case sequence |
| `05_validation_targets.md` | L*c targets, digitization plan |
| `06_unknowns_and_research.md` | Open gaps, research trail, questions for the professor |
| `tools/` | Isentropic calculator, (later) digitization scripts |

## Case sequence (agreed)

1. **C1** — uncontrolled coaxial jet (primary + secondary, no tabs). First real deliverable.
2. **C2–C5** — add tabs (primary only, secondary only, both 0°, both 90°).
3. **C0** — single primary jet, run as a cheap sanity check before C1 (de-risks the nozzle), and as the reference for tab benefit.

## Status

- OpenFOAM: **not installed** (install in progress / failed on mirror 404). Prep work only until it is available. Source cached at `~/.cache/yay/openfoam/src/OpenFOAM-13`.
- Geometry: partially reconstructed from the paper; missing details logged in `06_unknowns_and_research.md`.
- No raw data available (paper states data on request only). Validation via digitized figures + reported L*c scalars.