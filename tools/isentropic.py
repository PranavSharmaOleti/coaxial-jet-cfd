#!/usr/bin/env python3
"""Isentropic flow calculator for the coaxial jet operating conditions.

Inputs: stagnation pressure ratio p0/pa, exit Mach M, T0 (K), D (m).
Outputs: T, p, a, U, rho, Re (Sutherland viscosity).
Used to derive Table-I quantities and bypass ratio B.
"""
import math, argparse

def sutherland(T):
    return 1.716e-5*(T/273.15)**1.5*(273.15+110.4)/(T+110.4)

def exit_state(M, p0_over_pa, T0, D, pa=101325.0):
    p0 = p0_over_pa*pa
    T = T0/(1+0.2*M*M)
    p = p0/((1+0.2*M*M)**3.5)
    a = math.sqrt(1.4*287.0*T)
    U = M*a
    rho = p/(287.0*T)
    mu = sutherland(T)
    Re = rho*U*D/mu
    return dict(T=T, p=p, a=a, U=U, rho=rho, Re=Re, p_over_pa=p/pa)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("M", type=float)
    ap.add_argument("p0_over_pa", type=float)
    ap.add_argument("--T0", type=float, default=300.0)
    ap.add_argument("--D", type=float, default=0.01124)
    a = ap.parse_args()
    s = exit_state(a.M, a.p0_over_pa, a.T0, a.D)
    for k,v in s.items():
        print(f"{k}: {v:.4g}")
PY
chmod +x /home/sankara/Projects/coaxial-jet-cfd/tools/isentropic.py