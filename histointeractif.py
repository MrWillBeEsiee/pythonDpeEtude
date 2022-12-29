import json

import dash
from dash import dcc, Output, Input
from dash import html
import plotly.express as px
import requests
import pandas as pd
from dash.dash_table import DataTable


# fonction qui définit le nombre de lignes vides à insérer
def make_break(numBreaks):
    br_list = [html.Br()] * numBreaks
    return br_list


# fonction d'ajout du logo
def add_logo():
    corp_logo = html.Img(
        src='https://www.usinenouvelle.com/mediatheque/4/3/0/000271034_image_600x315.jpg',
        style={'margin': '20px 20px 5px 5px',
               'border': '1px dashed lightblue',
               'display': 'inline-block'})
    return corp_logo

def addConsommationImage():
    corp_logo = html.Img(
        src='https://www.mesdepanneurs.fr/sites/default/files/blog/etiquette-energie-GES.jpeg',
        style={'margin': '20px 20px 5px 5px',
               'border': '1px dashed lightblue',
               'display': 'inline-block'})
    return corp_logo


def style_c():
    layout_style = {
        'display': 'inline-block',
        'margin': '0 auto',
        'padding': '20px',
    }
    return layout_style




if __name__ == '__main__':

    px.set_mapbox_access_token(open(".mapbox_token").read())
    """
    req = requests.get(
        "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/lines?size=10000&format=csv&select=nom_methode_dpe"
        "%2Cdate_etablissement_dpe%2Cconsommation_energie%2Cclasse_consommation_energie%2Cestimation_ges%2Cclasse_estimation_ges"
        "%2Cannee_construction%2Ctv016_departement_code%2Clatitude%2Clongitude")
    url_content = req.content
    csv_file = open('dpe-france.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
    """
    france = pd.read_csv("dpe-france.csv")

    france = france.drop(france[(france['classe_consommation_energie'] == 'N')].index)
    france = france.drop(france[(france['classe_consommation_energie'] == 'H')].index)
    france = france.drop(france[(france['classe_consommation_energie'] == 'I')].index)

    app = dash.Dash(__name__)


    #Création de la carte qui répertorie les maison par couleur en fonction de leur classe de consommation
    map_point = px.scatter_mapbox(france, lat="latitude", lon="longitude",zoom=5,
        color=france["classe_consommation_energie"],
        category_orders={"classe_consommation_energie":("A", "B", "C", "D", "E", "F", "G")},
        color_discrete_sequence=("#82a6fb", "#aac7fd", "#cdd9ec", "#ead4c8", "#f7b89c", "#f18d6f", "#d95847"),
        opacity=0.6)

    map_point.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    map_point.update_layout(autosize=True)

    recap = france.describe()
    recap['index'] = recap.index
    column_to_move = recap.pop("index")
    recap.insert(0, "index", column_to_move)
    recap = recap.drop(['longitude', 'latitude'], axis=1)
    recap = recap.drop(['max', 'min'], axis=0)

    d_columns = [{'name': x, 'id': x} for x in recap.columns]

    d_recap = DataTable(
        columns=d_columns,
        data=recap.to_dict('records'),
        cell_selectable=True,
        sort_action='native',
        filter_action='native'
    )

    data = france
    data = data.drop(['longitude', 'latitude'], axis=1)
    d_columns = [{'name': x, 'id': x} for x in data.columns]

    d_table = DataTable(
        columns=d_columns,
        data=data.to_dict('records'),
        cell_selectable=True,
        sort_action='native',
        filter_action='native',
        page_action='native',
        page_current=0,
        page_size=10
    )


    app.layout = html.Div([
        #mon logo
        add_logo(),
        #des espaces
        *make_break(2),
        #Titre de mon dashboard
        html.H1('Etude des dpe en France'),
        *make_break(3),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H2('Département', style=style_c()),
                        html.H3('Rechercher par departements'),
                        *make_break(2),
                        #Ajout de l'entrée requise
                        dcc.Input(id='search_dep', type='text',
                            placeholder='Rechercher par departements',
                            debounce=True,
                            required=False,
                            persistence=True,
                            style={"width":'200px', 'height':'30px'})
                    ],
                style={'width':'350px', 'height':'350px','vertical-align':'top', 'border':'1px solid black',
                    'display':'inline-block', 'margin':'0px 80px'}
                ),

                html.Div(
                    children=[
                        dcc.Graph(id='bar_graph')
                    ],
                style={'width':'700px', 'display':'inline-block'}
                ),
            ],
        style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
        ),
        *make_break(2),
        html.Div(
            children=[
                html.H1(children='Cartographie des habitations et de leur consommation en France',
                        style={'textAlign': 'center', 'color': '#7FDBFF'}),
                dcc.Graph(
                    id='map_point',
                    figure=map_point
                ),
            ],
            style={'width': '1200px', 'display': 'inline-block'},
        ),
        *make_break(2),
        html.Div([
            html.H4('Répartition des habitations françaises en fonction de leur classe de consommation energétique'),
            html.P("Selectionnez une classe de consommation d'energie:"),
            dcc.RadioItems(
                id='Selection',
                options=["consommation_energie", "estimation_ges"],
                value="consommation_energie",
                persistence=True,
                inline=True
            ),
            dcc.Graph(id="graph"),
        ]),
        addConsommationImage(),
        html.Div(
            children=[d_recap],
            style={'width': '850px', 'height': '450px', 'margin': '0 auto'}
        ),
        html.Div(
            children=[d_table],
            style={'width': '850px', 'height': '750px', 'margin': '0 auto'}
        ),
    ],
        style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
    )

    @app.callback(
        Output(component_id='bar_graph', component_property='figure'),
        Input(component_id='search_dep', component_property='value')
    )
    def update_bar(search_value):
        title_value = 'Toues les descriptions'

        data = france.copy(deep=True)

        #le tri est effectué ici à l'aide de la saisi utilisateur
        if search_value:
            title_value = search_value

            data = data[data['tv016_departement_code'].str.contains(search_value, case=False)]


        bar_fig = px.histogram(
            data_frame=data, x='classe_consommation_energie', color='classe_consommation_energie',
            title='Répartition dpe 77',
            category_orders={"classe_consommation_energie": ("A", "B", "C", "D", "E", "F", "G")},
            color_discrete_sequence=("#82a6fb", "#aac7fd", "#cdd9ec", "#ead4c8", "#f7b89c", "#f18d6f", "#d95847"),
        )
        return bar_fig


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
































