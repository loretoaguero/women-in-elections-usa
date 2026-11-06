from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA = Path(__file__).resolve().parent / "data"
STATE = "State"
WOMEN_2024 = "Women in 2024"
WOMEN_2026 = "Women in 2026"
SEATS = "Seats in 2024"
PERCENT = "Women in 2026 (%)"
CHANGE = "Difference (2026 − 2024)"


@st.cache_data
def load_data():
    results = pd.read_csv(
        DATA / "1976-2024-house.tab",
        usecols=["year", "state_po", "district"],
    )
    seats = (
        # DC has a representative, but a special one, not a state representative, so we exclude it from the count of seats.
        results.loc[(results["year"] == 2024) & (results["state_po"] != "DC")]
        .drop_duplicates(["state_po", "district"])
        .groupby("state_po")
        .size()
        .rename(SEATS)
    )

    candidates = pd.read_excel(DATA / "women_candidates_2024.xlsx", sheet_name="Data")
    women_2024 = candidates.loc[
        candidates["Office"].eq("U.S. Rep.")
        & candidates["General Election Result"].eq("W")
    ]

    congress = pd.read_excel(DATA / "2026 Women congress.xlsx", sheet_name="Data")

    women_2026 = congress.loc[congress["Office"].eq("U.S. Representative")]

    keys = ["State", "First Name", "Last Name", "Party"]

    states = seats.to_frame()
    for label, rows in [(WOMEN_2024, women_2024), (WOMEN_2026, women_2026)]:
        counts = rows.drop_duplicates(keys).groupby("State").size()
        states[label] = counts.reindex(states.index, fill_value=0)

    # Note: The number of seats by state in 2026 is the same as the 2024.
    states[PERCENT] = 100 * states[WOMEN_2026] / states[SEATS]
    states[CHANGE] = states[WOMEN_2026] - states[WOMEN_2024]
    return states.rename_axis(STATE).reset_index()


def main():
    st.set_page_config(
        page_title="Women in the U.S. House of Representatives", layout="wide"
    )
    st.title("Women in the U.S. House of Representatives")
    mode = st.radio("View", ["Percentage", "Absolute Difference"], horizontal=True)
    states = load_data()

    if mode == "Percentage":
        metric = PERCENT
        hover = [WOMEN_2024, SEATS]
        colors = {"color_continuous_scale": "Purples", "range_color": (0, 100)}
        st.metric(
            "National Percentage in 2026",
            f"{states[WOMEN_2026].sum() / states[SEATS].sum():.1%}",
        )
        st.caption("Percentage of seats won by women in 2026, by state.")
        number_format = "%.1f %%"
    else:
        metric = CHANGE
        hover = [WOMEN_2024, WOMEN_2026]
        limit = max(1, int(states[CHANGE].abs().max()))
        colors = {
            "color_continuous_scale": ["#b2182b", "#f7f7f7", "#542788"],
            "range_color": (-limit, limit),
        }
        st.metric("National Change between 2024 and 2026", f"{states[CHANGE].sum():+d}")
        st.caption(
            "Women in 2026 minus women in 2024. A positive value indicates an increase."
        )
        number_format = "%+d"

    fig = px.choropleth(
        states,
        locations=STATE,
        locationmode="USA-states",
        scope="usa",
        color=metric,
        hover_name=STATE,
        hover_data={
            STATE: False,
            metric: ":.1f" if metric == PERCENT else ":+d",
            **dict.fromkeys(hover, True),
        },
        **colors,
    )
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})
    st.dataframe(
        states[[STATE, *hover, metric]].sort_values(metric, ascending=False),
        hide_index=True,
        column_config={metric: st.column_config.NumberColumn(format=number_format)},
    )
    st.caption(
        "Sources: CAWP (Rutgers University) and MIT Election Data and Science Lab. Local data from the notebook."
    )


if __name__ == "__main__":
    main()
