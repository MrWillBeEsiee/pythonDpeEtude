from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import json

if __name__ == '__main__':

    app = Dash(__name__)


    app.layout = html.Div([
        html.H4('Répartition des habitations françaises en fonction de leur classe de consommation energétique'),
        html.P("Selectionnez une classe de consommation d'energie:"),
        dcc.RadioItems(
            id='Selection',
            options=["consommation_energie", "estimation_ges"],
            value="consommation_energie",
            inline=True
        ),
        dcc.Graph(id="graph"),
    ])


    @app.callback(
        Output("graph", "figure"),
        Input("Selection", "value"))
    def display_choropleth(Selection):
        df = pd.read_csv("dpe-france.csv")
        with open('departements.geojson') as mon_fichier:
            geojson = json.load(mon_fichier)

        fig = px.choropleth(
            df, geojson=geojson, color=Selection,
            locations="tv016_departement_code", featureidkey="properties.code",
            projection="mercator", range_color=[0, df[Selection].quantile(0.85)])
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig


    app.run_server(debug=True)

