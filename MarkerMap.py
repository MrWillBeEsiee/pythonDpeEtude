import plotly.express as px

class MarkerMap:

    def CreateMarkerMap(Selection2, france):
        map_point = px.scatter_mapbox(france, lat="latitude", lon="longitude", zoom=5,
        color=france["classe_consommation_energie"],
        category_orders={
        "classe_consommation_energie": ("A", "B", "C", "D", "E", "F", "G")},
        color_discrete_sequence=(
        "#82a6fb", "#aac7fd", "#cdd9ec", "#ead4c8", "#f7b89c", "#f18d6f", "#d95847"),
        opacity=0.6)

        map_point.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        map_point.update_layout(autosize=True)
        if(Selection2 == "Carte avec clusters"):
            map_point.update_traces(cluster=dict(enabled=True))
        return map_point