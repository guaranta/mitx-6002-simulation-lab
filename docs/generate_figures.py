"""Generate README figures for simulation lab."""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

# Virus spread SIR-style simulation
def simulate_virus(n=200, beta=0.3, gamma=0.1, i0=5, days=80):
    s, i, r = n - i0, i0, 0
    S, I, R = [s], [i], [r]
    for _ in range(days):
        new_inf = beta * s * i / n
        new_rec = gamma * i
        s = max(0, s - new_inf)
        i = max(0, i + new_inf - new_rec)
        r = min(n, r + new_rec)
        S.append(s); I.append(i); R.append(r)
    return np.arange(days + 1), np.array(S), np.array(I), np.array(R)

t, S, I, R = simulate_virus()
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, S, label="Susceptible", lw=2)
ax.plot(t, I, label="Infected", lw=2)
ax.plot(t, R, label="Recovered", lw=2)
ax.set_xlabel("Day")
ax.set_ylabel("Population")
ax.set_title("Epidemic simulation (β=0.3, γ=0.1) — ps3b inspired")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "virus_sir.png", dpi=150)
plt.close()

# Climate trend synthetic
rng = np.random.default_rng(1)
years = np.arange(1990, 2024)
trend = 0.03 * (years - 1990)
noise = rng.normal(0, 0.4, len(years))
temps = 14 + trend + noise
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(years, temps, alpha=0.5, s=20, color="#3b82f6")
z = np.polyfit(years, temps, 1)
ax.plot(years, np.polyval(z, years), color="#ef4444", lw=2, label=f"Trend: +{z[0]:.3f}°C/yr")
ax.set_xlabel("Year")
ax.set_ylabel("Avg temperature (°C)")
ax.set_title("Climate trends — linear regression on synthetic series")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "climate_trend.png", dpi=150)
plt.close()

print(f"Saved 2 figures to {OUT}")
