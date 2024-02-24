import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv"
)

columnDefs = [
    {"field": "Name", "sortable": False},
    {"field": "SepalWidth"},
    {"field": "PetalLength"},
    {"field": "PetalWidth"},
    {"field": "SepalLength"},
]

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}


app.layout = html.Div(
    [
        dag.AgGrid(
            id="column-definitions-basic",
            rowData=df.to_dict("records"),
            defaultColDef={"filter": True},
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": False}
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
