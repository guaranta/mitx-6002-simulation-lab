# mitx-6002-simulation-lab

**MITx 6.00.2x — Introduction to Computational Thinking and Data Science**

Pensamento computacional aplicado: simulação estocástica de epidemias, random walks e análise de tendências climáticas.

---

## Análises técnicas

### Simulação SIR (virus spread)

![Curvas S, I, R ao longo do tempo](docs/figures/virus_sir.png)

Modelo discreto com β=0.3 (taxa de infecção) e γ=0.1 (recuperação). Pico de infectados ~dia 25 — sensível a R₀ = β/γ.

### Tendência climática (climate trends)

![Scatter temperatura vs ano com reta de tendência](docs/figures/climate_trend.png)

Regressão linear sobre série sintética de 34 anos — framework do ps4 (21 cidades no curso original).

---

## Módulos

| Módulo | Origem | Comando |
|--------|--------|---------|
| `virus_spread/` | pset3 — simulação estocástica | `python virus_spread/run.py` |
| `robot_clustering/` | pset2 — random walks | `python robot_clustering/demo_robots.py` |
| `climate_trends/` | pset4 — tendências | `python climate_trends/run.py` |

## Setup

```bash
pip install -r requirements.txt
python docs/generate_figures.py
```

## Autor

**Guarantã Almeida** — [github.com/guaranta](https://github.com/guaranta)
