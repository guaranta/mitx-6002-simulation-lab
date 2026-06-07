#!/usr/bin/env python3
"""Climate trend analysis — MITx 6.00.2x pset4."""

import numpy as np
from ps4 import Climate, generate_models, r_squared, INTERVAL_1

def main():
    print("MITx 6.00.2x — Climate trends (Boston, Jan 10)")
    raw = Climate("data.csv")
    y = [raw.get_daily_temp("BOSTON", 1, 10, year) for year in INTERVAL_1]
    x = list(INTERVAL_1)
    models = generate_models(x, y, [1])
    coef = models[0]
    estimated = np.polyval(coef, x)
    r2 = r_squared(y, estimated)
    print(f"Linear model degree 1: R² = {r2:.4f}")
    print(f"Coefficients (high→low): {coef}")

if __name__ == "__main__":
    main()
