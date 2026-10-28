# 5. Validation targets

## 5.1 Reported L*c (headline, Us/Up = 0.94)

| Config | Description | Reported L*c/Dp |
|---|---|---|
| C0 | Single primary jet (reference) | 18.0 (Table II: 18.7) |
| C1 | Coaxial, no tabs | 24.7 |
| C2 | Tabs in primary only | 11.4 |
| C3 | Tabs in secondary only | 18.2 |
| C4 | Tabs in both, 0° relative | 9.3 |
| C5 | Tabs in both, 90° relative | 15.0 |

Note: C0/C1 values come from Fig. 6 text ("L*c of C0 and C1 is 18 and 24.7"). Table II lists C0 = 18.7, C1 = 15.4/28.2 (inconsistent with text; see `06_unknowns_and_research.md`).

## 5.2 Pass/fail gates (first pass)

- C0: L*c within ±15% of 18.7; Mach disk near x* ≈ 1.75; shock-cell count ~3–4 in core.
- C1: L*c within ±20% of 24.7; core elongated vs C0; Mach disk moves upstream (x* ≈ 1.0); strong waves to x* ≈ 16.5.
- C2/C4: substantial reduction (target ~11.4/9.3); bifurcation visible in xy profile.
- C3: modest reduction (~18.2); no bifurcation.
- C5: intermediate (~15.0); coalescence earlier than C4.

## 5.3 Digitization plan

1. Render paper figures to PNG: `pdftoppm -r 300 "coaxial jet .pdf" fig` (figures on pp. 9–17).
2. Digitize centerline curves (Fig. 6, 10) with a Python script (manual click via matplotlib ginput, or WebPlotDigitizer). Save as CSV in `3_validation/`.
3. Digitize transverse profiles (Fig. 13, 14) at x* = 2, 6, 8, 11.
4. Qualitative comparison only for contours (Fig. 8, 15, 16) and shadowgraphs (Fig. 7, 17).

## 5.4 Figures to extract

- Fig. 1: nozzle schematic (geometry reference).
- Fig. 2: p0s/p0p and Us/Up vs p0p/pa.
- Fig. 6: C0 vs C1 centerline decay (Us/Up = 0.94).
- Fig. 7: shadowgraphs C0, C1.
- Fig. 8: iso-Pitot contours C0, C1.
- Fig. 10: C1–C5 centerline decay.
- Fig. 11: L*c vs Us/Up; ΔL*c,C1.
- Fig. 13/14: transverse profiles.
- Fig. 15/16/17: contours and shadowgraphs.