import pandas as pd
import plotly.express as px


if __name__ == '__main__':
    px.set_mapbox_access_token(open(".mapbox_token").read())
    france = pd.read_csv("dpe-france.csv")
    france = france.drop(france[(france['classe_consommation_energie'] == 'N')].index)
    france = france.drop(france[(france['classe_consommation_energie'] == 'H')].index)
    france = france.drop(france[(france['classe_consommation_energie'] == 'I')].index)

    fig = px.scatter_mapbox(france, lat="latitude", lon="longitude",zoom=5,
                            color=france["classe_consommation_energie"],
                            category_orders={"classe_consommation_energie":("A", "B", "C", "D", "E", "F", "G")},
                            color_discrete_sequence=("#82a6fb", "#aac7fd", "#cdd9ec", "#ead4c8", "#f7b89c", "#f18d6f", "#d95847"),
                            opacity=0.6)

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(autosize=True)
    fig.show()