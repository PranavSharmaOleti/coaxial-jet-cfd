# 6. Unknowns, research trail, and questions for the professor

## 6.1 Open geometry unknowns (see 01 for full list)

- Convergent/divergent half-angles and axial lengths of the primary C-D nozzle.
- Secondary nozzle length and convergent angle.
- Tab thickness (streamwise).
- Absolute tab azimuth vs measurement planes (we chose; document).

## 6.2 Data gaps

- No raw measurement files (paper: data available on request only, not publicly). Validation is via digitized figures + reported L*c scalars.
- Operating temperatures (T0, T∞) not stated; assumed 300 K (cold jet). Affects density/Re/mass flow but Mach numbers are pressure-ratio driven.
- Ambient pressure not stated; assumed 1 atm.

## 6.3 Inconsistencies found in the paper (flag to professor)

1. **Table II vs text:** At Us/Up = 0.94, text states L*c(C0) ≈ 18 and L*c(C1) = 24.7. Table II lists C0 = 18.7, C1 Lc/Dp = 15.4 and Lc/Deq = 30.2. Since Deq > Dp, Lc/Deq must be < Lc/Dp, so the two C1 columns appear swapped; and neither equals 24.7. Treat the explicitly stated L*c values (24.7, 11.4, 18.2, 9.3, 15.0) as authoritative.
2. **Reynolds numbers:** Sec II.C reports Rep = 3.5e5 and 7e5 (at p0p/pa = 3 and 8) while Table I conditions are p0p/pa = 2.5–6.0. Minor.
3. **Lip thickness:** stated as 3.2 mm (Sec II.B) and 2.65 mm (tab mounting paragraph). Use 3.2 for outer diameter; note discrepancy.
4. **pe/pa vs Mp:** Table I pairs are not exactly isentropic-consistent (paper acknowledges actual Mach differs from design Mach). We use p0 ratios as inputs.

## 6.4 Research trail (updated with provided papers)

Provided papers and what they gave:
- **2020 coaxial jet paper** (main target) ✓ — all geometry/conditions/results.
- **2014 triangular tabs paper** (Aeronaut. J.) ✓ — same facility; Mach 2 nozzle geometry (7° semi-divergence, D* = 10.02, De = 13.02, lip 5 mm); tabs 1 mm brass / 4 mm.
- **2018 fluidic injectors paper** (Phys. Fluids 30, 126101) ✓ — same facility + Mach 2 nozzle; no Mach 1.4 nozzle.
- **2019 shifted-tab paper** (Phys. Fluids 31, 076104) ✓ — same facility + Mach 2 nozzle; tab-location study (0–0.95 De downstream).
- **Papamoschou 1997** (Mach wave elimination) ✓ — theory for Mcps/Mcs∞ criteria.
- **Murakami & Papamoschou 2002** (dual-stream) ✓ — growth-rate model; coaxial core elongation.
- **Papamoschou & Rostamimonjezi 2010** ✓ — core length vs velocity ratio; noise source location.
- Textbooks: Anderson (compressible flow), Versteeg & Malalasekera (CFD) ✓.

**Still missing / not applicable:**
- No source in the provided set documents the Mach 1.4 nozzle's cone angles or axial lengths. Ref. 89 in the 2014 paper (a PhD thesis) is cited only for uncertainty-calculation procedures, not nozzle geometry; I cannot confirm it contains or would resolve the Mach 1.4 nozzle details. Treat as unverified.
- Zaman 1999, Samimy 1993, Bradbury & Khadem 1975 (tab mechanism/optimization) — optional.

**Conclusion:** the Mach 1.4 nozzle geometry (cone angles, lengths) is undocumented in all available sources. We proceed with the 7° semi-divergence inference (from the Mach 2 nozzle, same lab) and document it as an assumption with a sensitivity note. No external document is known to resolve it.

- **2014 paper (Ref 23) now available** in `Downloads/Project_Official/`: Kumar & Rathakrishnan, "Triangular tabs for supersonic jet mixing enhancement," Aeronaut. J. 118(1209), 1245–1278 (2014). Gave: same IIT Kanpur facility (settling chamber 300×600 mm, wire mesh, diffuser), and a Mach 2.0 C-D nozzle with semi-divergence angle 7°, D* = 10.02, De = 13.02, expansion length 12.22 mm, lip 5 mm, tabs 1 mm brass / 4 mm long. **No Mach 1.4 nozzle details and no coaxial setup** — the 2020 paper's nozzle is different.
- **No remaining source identified for Mach 1.4 nozzle geometry.** Ref. 89 in the 2014 paper cites a PhD thesis (Arun Kumar P., 2013, IIT Kanpur) only for uncertainty-calculation procedures. I cannot confirm it contains nozzle drawings. Treat as unverified; do not depend on it.
- **2019 paper (Ref 29):** Kumar, Aileni & Rathakrishnan, "Impact of tab location relative to the nozzle exit on the shock structure of a supersonic jet," Phys. Fluids 31(7), 076104 (2019) — same facility; may use the Mach 1.4 or Mach 2 nozzle. Not yet obtained.
- 2018 fluidic injectors paper (Ref 30) and Papamoschou 1997 (Ref 2) also not obtained.

- 2020 paper Ref 23: Kumar & Rathakrishnan, "Triangular tabs for supersonic jet mixing enhancement," Aeronaut. J. 118(1209), 1245–1278 (2014) — nozzle calibration + facility details. Paywalled (Cambridge Core).
- 2020 paper Ref 29: Kumar, Aileni & Rathakrishnan, "Impact of tab location relative to the nozzle exit on the shock structure of a supersonic jet," Phys. Fluids 31(7), 076104 (2019) — same facility.
- 2014 paper Ref 89: Arun Kumar P., "Triangular Tabs for Supersonic Jet Control," PhD Thesis, 2013, IIT Kanpur — likely contains the nozzle drawing (angles, lengths).
- These sources are not freely available online (thesis not on Shodhganga/IITK repos reachable; papers paywalled on Cambridge Core / AIP). **If you have institutional library access, fetching the 2013 PhD thesis is the highest-value action.**

## 6.5 Questions to settle with the professor (per the paper's own suggestion)

1. Which operating condition is the primary comparison target? (We default to Us/Up = 0.94 / Fig. 10, as the paper's headline.)
2. Should C0 (single jet) be a required deliverable or just a sanity check?
3. Acceptable level of geometry assumption (assumed cone angles) vs. requiring exact nozzle drawing.
4. Expected fidelity: RANS core length ±? %, or is a qualitative shock-structure match acceptable?
5. Is a written reconstruction report (this folder) the deliverable, or also a running case? (OpenFOAM not yet installed.)