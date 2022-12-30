import plotly.express as px
import json

class DepartementsFig:

    def CreateDepFig(Selection, france):
        data = france.groupby(['tv016_departement_code']).mean(numeric_only=True)
        with open('departements.geojson') as mon_fichier:
            geojson = json.load(mon_fichier)
        fig = px.choropleth(
            data, geojson=geojson, color=Selection,
            locations=data.index, featureidkey="properties.code",
            projection="mercator", range_color=[0, france[Selection].quantile(0.85)])
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig