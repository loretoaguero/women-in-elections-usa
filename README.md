# Women in U.S. Politics: 2024–2026

🚧 **Work in progress**

An exploratory project on women's representation in U.S. politics, focusing on Congress and comparisons across states and political parties in 2024 and 2026.

The analysis uses Python, pandas, and Plotly. Data cleaning, comparisons, and maps are still being developed, so results are preliminary and the notebook may not yet run from start to finish.

## Project files

- [`notebooks/EDA.ipynb`](notebooks/EDA.ipynb): main analysis notebook.
- `data/`: local datasets and exports.
- `notebooks/*.png`: exploratory maps.

## Getting started

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --dev
uv run jupyter lab
```

Open `notebooks/EDA.ipynb` using the project environment. The notebook expects `notebooks/` as its working directory to load data from `../data`.

## Data sources

Women's representation and candidate data come from the **Center for American Women and Politics (CAWP), Eagleton Institute of Politics, Rutgers University**:

- CAWP. [*Women in the 120th Congress*](https://cawp.rutgers.edu/candidates-2026-election-results-tracker/women-120th-congress).
- CAWP. [*Women Elected Officials Database — By Party*](https://cawp.rutgers.edu/data/women-elected-officials-database?tab=ByParty).
- CAWP. [*Women Candidates in 2026 — Candidate List*](https://cawp.rutgers.edu/data/candidates-women-candidates-2026?tab=CandidateList).
- CAWP. [*Women Candidates in 2026 — Rebound Candidates*](https://cawp.rutgers.edu/data/candidates-women-candidates-2026?tab=ReboundCandidates).
- CAWP. [*2024 Summary of Women Candidates*](https://cawp.rutgers.edu/data/candidates-election-results-and-analysis-0/2024-summary-women-candidates).

Election returns are hosted on **Harvard Dataverse**:

- MIT Election Data and Science Lab. 2017. *U.S. House 1976–2024*. Harvard Dataverse, V15. [doi:10.7910/DVN/IG0UN2](https://doi.org/10.7910/DVN/IG0UN2). The local file is `1976-2024-house.tab`; its download version has not been confirmed.
- Senate data (`senate_2022.csv`): [Harvard Dataverse, file ID 7412054, version 3.0](https://dataverse.harvard.edu/file.xhtml?fileId=7412054&version=3.0). Full dataset citation and coverage are still to be verified.

References reviewed on November 5, 2026. CAWP's live data may change as election results and officeholder records are updated. Candidate lists and elected-member counts need to be distinguished when making comparisons.
