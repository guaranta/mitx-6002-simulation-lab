#!/usr/bin/env python3
"""Run virus spread simulation (MITx 6.00.2x pset3) — headless summary."""

import matplotlib
matplotlib.use("Agg")

import ps3b

if __name__ == "__main__":
    print("MITx 6.00.2x — Virus spread simulation")
    print("Running simulationWithoutDrug (10 trials, 300 steps)...")
    # Saves plot if matplotlib backend allows; main output is console
    ps3b.simulationWithoutDrug(
        numViruses=50, maxPop=1000,
        maxBirthProb=0.1, clearProb=0.05, numTrials=5
    )
    print("Done. See plot window or re-run with interactive backend.")
