# statistikk.py

import pandas as pd
import altair as alt

# Load and clean data
kgdata = pd.read_excel("ssb-barnehager.xlsx", sheet_name="KOSandel120000",
                       header=3, names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
                       na_values=['.', '..'])

# Handle NaN values in 'kom' before split
kgdata["kom"] = kgdata['kom'].apply(lambda x: x.split(" ")[1] if isinstance(x, str) and len(x.split(" ")) > 1 else "")

for coln in ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']:
    kgdata.loc[kgdata[coln] > 100, coln] = float("nan")

renset_kb = kgdata.drop(kgdata.index[724:])

# Function to generate Altair chart
def create_altair_chart(kommune):
    kommune_data = renset_kb[renset_kb['kom'] == kommune]
    if kommune_data.empty:
        return None

    år = ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']
    prosent = kommune_data[år].melt(var_name="År", value_name="Prosent")
    prosent["År"] = prosent["År"].apply(lambda x: f"20{x[1:]}")  # Format year

    chart = alt.Chart(prosent).mark_line(point=True).encode(
        x='År:O',
        y='Prosent:Q',
        tooltip=['År', 'Prosent']
    ).properties(
        title=f'Prosent av barn i ett- og to-årsalderen i barnehagen for {kommune}',
        width=600,
        height=400
    )
    return chart.to_json()
