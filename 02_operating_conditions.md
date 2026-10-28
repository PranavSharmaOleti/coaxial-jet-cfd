# 2. Operating conditions (Table I + derived)

Source: paper Table I. Ambient: pa = 1 atm, T∞ = T0 = 300 K (cold jet; paper discusses hot jets in literature but present jets are cold; T0 not stated — assumption). γ = 1.4, R = 287 J/kgK. Isentropic relations used for derived columns; Sutherland for μ.

## 2.1 Table I (as reported)

| p0p/pa | pe/pa | Mp | Up (m/s) | p0s/pa | p0s/p0p | Ms | Us (m/s) | Us/Up | Mcps | Mcs∞ |
|---|---|---|---|---|---|---|---|---|---|---|
| 2.5 | 0.79 | 1.25 | 380 | 1.5 | 0.60 | 0.84 | 274 | 0.72 | 0.17 | 0.57 |
| 2.8 | 0.88 | 1.33 | 399 | 1.8 | 0.64 | 1.00 | 315 | 0.80 | 0.14 | 0.71 |
| 3.18 | 1.0 | 1.42 | 418 | 2.2 | 0.69 | 1.15 | 356 | 0.85 | 0.10 | 0.86 |
| 4.0 | 1.26 | 1.57 | 448 | 3.0 | 0.75 | 1.38 | 410 | 0.91 | 0.07 | 1.06 |
| 5.0 | 1.57 | 1.72 | 475 | 4.0 | 0.80 | 1.57 | 448 | 0.94 | 0.05 | 1.23 |
| 6.0 | 1.89 | 1.83 | 494 | 5.0 | 0.83 | 1.72 | 475 | 0.96 | 0.03 | 1.36 |

Note: pe/pa and Mp are reported measured values; they are not exactly isentropic-consistent (e.g. at p0p/pa = 2.5, isentropic pe/pa for M = 1.43 is 0.79, but reported Mp = 1.25). The paper acknowledges actual Mach differs from design Mach. For CFD we treat p0p/pa and p0s/pa as inputs (stagnation) and Up/Mp/Ms/Us/pe as validation outputs.

## 2.2 Derived (isentropic, T0 = 300 K)

| p0p/pa | Up calc (m/s) | Tp (K) | pe/pa calc | Rep | ρp (kg/m³) | p0s/pa | Us calc (m/s) | B | Deq/Dp | Us/Up |
|---|---|---|---|---|---|---|---|---|---|---|
| 2.50 | 379 | 228.6 | 0.965 | 4.27e5 | 1.491 | 1.50 | 273 | 1.70 | 1.642 | 0.721 |
| 2.80 | 397 | 221.6 | 0.970 | 4.76e5 | 1.545 | 1.80 | 317 | 1.92 | 1.708 | 0.799 |
| 3.18 | 416 | 213.8 | 0.971 | 5.34e5 | 1.604 | 2.20 | 355 | 2.12 | 1.766 | 0.853 |
| 4.00 | 446 | 200.9 | 0.984 | 6.50e5 | 1.728 | 3.00 | 408 | 2.30 | 1.818 | 0.914 |
| 5.00 | 473 | 188.5 | 0.983 | 7.76e5 | 1.841 | 4.00 | 446 | 2.45 | 1.856 | 0.942 |
| 6.00 | 492 | 179.7 | 0.997 | 8.95e5 | 1.960 | 5.00 | 473 | 2.50 | 1.871 | 0.963 |

Calculated Up/Us agree with the reported values within ~1%, supporting T0 ≈ 300 K and the annular secondary area (Section 1). B agrees with the paper's 1.9–2.5 for the higher NPRs; lower NPRs are slightly below (likely due to T0 and tp assumptions).

## 2.3 Key condition for headline comparison

Fig. 10 / 11 / Table targets use **Us/Up = 0.94** (p0p/pa = 5.0, Mp = 1.72, Ms = 1.57, pe/pa = 1.57 — under-expanded Mach 1.4 jet; Mach wave radiation present between secondary and ambient since Mcs∞ = 1.23 > 1).

## 2.4 Convective Mach numbers (as reported)

- Mcps (primary–secondary) < 1 for all rows → no Mach wave between primary and secondary.
- Mcs∞ (secondary–ambient) < 1 only for rows 1–3 (Mp ≤ 1.42); Mach wave radiation present for rows 4–6. This is the paper's central observation: tabs are more effective when Mach waves are absent (Us/Up ≤ 0.85).

## 2.5 Reynolds numbers

Rep ≈ 4.3e5 – 9.0e5 (min to max condition). Turbulent; wall functions or resolved BL at nozzle walls. Note paper also reports Rep = 3.5e5 and 7e5 (at p0p/pa 3 and 8) for the shadowgraph runs — slightly different from Table I's 3/6; minor inconsistency to note.