# 3. Physics the experiment relies on (what our CFD must capture)

## 3.0 Theory from the provided papers (Papamoschou et al.)

**Mach wave elimination (Papamoschou 1997):** For a primary jet at Mach Mp enveloped by a secondary flow at Mach Ms, Mach wave radiation is eliminated when both convective Mach numbers are subsonic: Mcps < 1 (primary–secondary) and Mcs∞ < 1 (secondary–ambient). The paper derives relations between Ms, Ts/T∞, and Us/Up satisfying these. Present study: Mcps < 1 always; Mcs∞ < 1 only for Us/Up ≤ 0.85 → tabs less effective for Us/Up ≥ 0.91.

**Growth rate model (Murakami & Papamoschou 2002):** δ′/δ0′ = 0.23 + 0.77·exp(−3.5·Mcp²), with δ0′ = 0.14·√((1−R)(1+S)/(1+RS)). Compressibility suppresses shear-layer growth; secondary flow reduces δ′ → core elongation. Matches Eq. 5/6 in the 2020 paper.

**Coaxial core length vs velocity ratio (Papamoschou & Rostamimonjezi 2010):** Primary core length rises from ~8 Dp at Us/Up = 0 to ~13 Dp at Us/Up = 1 (their Dp = 14.2 mm, Ds = 23.4 mm). Peak noise location tracks the end of the primary core — relevant to the 2020 paper's Sec. III/IV discussion.

Primary jet is under-expanded at several NPRs (pe/pa < 1 for over-expanded low NPR; pe/pa > 1 for under-expanded high NPR). At p0p/pa = 5.0, pe/pa = 1.57 (under-expanded M 1.4 jet): expansion fans at the lip, Mach disk / barrel shocks downstream, quasi-periodic shock-cell pattern. Shock-cell length and strength are visible in centerline Pitot oscillations (Fig. 6, 10) and shadowgraphs (Fig. 7, 17).

## 3.2 Why the secondary stream affects the primary jet

Co-flow shear layer between primary and secondary. Secondary flow reduces the growth rate of the primary shear layer (Murakami & Papamoschou, Papamoschou & Rostamimonjezi) → primary potential/supersonic core elongates. The paper measures δ′ (growth rate) for C0 and C1 (Table III): δ′ drops from 0.048 to 0.044 at Mcp∞ = 0.95. Core length C1 (24.7) > C0 (18). The secondary core also shields the primary core from decaying (Fig. 8 contours).

## 3.3 Mach wave elimination

Convective Mach numbers Mcps and Mcs∞ must both be < 1 to eliminate Mach wave radiation. Present study: Mcps < 1 always; Mcs∞ < 1 only for Us/Up ≤ 0.85. For Us/Up ≥ 0.91, Mach waves exist between secondary and ambient → reduced mixing benefit from tabs. This is the paper's central physical claim and our key interpretation target.

## 3.4 How tabs work

- Rectangular tabs generate streamwise vortices (Bradbury & Khadem) → enhanced entrainment and mixing.
- Tabs bifurcate the jet (two pressure peaks off-axis), emulate non-circular (elliptic) jet behavior, possible axis-switching.
- Tab blockage ~2.5% per tab, ~5% per set; height must exceed BL thickness (0.04 Dp) for mixing (not just BL control).
- Primary tabs (AR = 2, narrow/tall) are more effective than secondary tabs (AR = 0.75, wide/short) for coaxial jet mixing.
- C4 (both sets, 0° alignment) gives strongest bifurcation and best mixing (L*c = 9.3); C5 (90°) coalesces earlier → less mixing (L*c = 15.0).

## 3.5 Supersonic core length definition

L*c = axial distance from nozzle exit to where local Mach = 1 on the centerline, estimated from centerline Pitot pressure. Cut-off: p0t/p0p = 1.89/p0p/pa (e.g. 0.37 at p0p/pa = 5.0). Pitot behind bow shock under-reads actual total pressure by <5%; acceptable for core length and shock structure. Paper normalizes by Dp (not Deq) for consistency with literature; ΔL*c is normalization-independent.

## 3.6 What "validation" means here

We cannot get raw data. Validation path:
1. Scalar L*c values (reported: C0 18/18.7, C1 24.7, C2 11.4, C3 18.2, C4 9.3, C5 15.0 at Us/Up = 0.94) — primary gate.
2. Centerline Pitot decay curves (Fig. 6, 10) — shape, shock-cell count/spacing, Mach disk location.
3. Transverse profiles (Fig. 13, 14) — bifurcation, differential spread.
4. Iso-Pitot contours (Fig. 8, 15, 16) and shadowgraphs (Fig. 7, 17) — qualitative shock structure.

Digitize (1)–(2) with a Python script; (3)–(4) qualitative. Report discrepancies honestly with likely causes (RANS smearing, geometry assumptions, tab thickness).