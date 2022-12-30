import dash
from dash import dcc, Output, Input
from dash import html
import plotly.express as px
from dash.dash_table import DataTable
from DepartementsFig import DepartementsFig
from Histogramme import Histogramme
from InfoDisplay import InfoDisplay
from Utils import Utils
from MarkerMap import MarkerMap
from DataService import DataService

if __name__ == '__main__':

    px.set_mapbox_access_token(open(".mapbox_token").read())

    france = DataService.InitData()

    app = dash.Dash(__name__)


    d_table = InfoDisplay.InitdataSetFig(france)
    d_recap = InfoDisplay.InitRecap(france)


    app.layout = html.Div([
        #mon logo
        Utils.add_logo(),
        #des espaces
        *Utils.make_break(2),
        #Titre de mon dashboard
        html.H1(children='Etude des dpe en France', style={'textAlign': 'center', 'color': '#7FDBFF'}),
        *Utils.make_break(3),
        html.Div(
            children=[
                html.Div(
                    children=[
                    html.H2(children='Avant-propos',
                    style={'textAlign': 'center', 'color': '#7FDBFF'})],
                ),
                html.Div(
                    children=[
                        html.Plaintext(children='Cette étude est l\'objet d\'un devoir scolaire réalisé par deux étudiants de deuxième'
                                         'année en informatique.\n'
                                         'Le dataset comporte 100 000 valeurs.\n'
                                         'vous trouverez ci-dessous plusieurs graphiques interactifs qui tentent d\'apporter de la\n'
                                         'visibilité quand à la répartition des maisons consommatrices d\'energie et polluante en France\n'
                                         'Bonne lecture !',
                        style={'textAlign': 'center', 'color': '#7FDBFF'})],
                ),

                html.Div(
                    html.H2(children='Les classes de consommation DPE et GES en france',
                            style={'textAlign': 'center', 'color': '#7FDBFF'}),
                ),

                Utils.addConsommationImage(),

                html.Div(
                    children=[
                        html.H1(children='Histogramme des classes de consommations DPE et GES françaises',
                        style={'textAlign': 'center', 'color': '#7FDBFF'}),
                ]),
                html.Div(
                    children=[
                        html.H2('Département', style=Utils.style_c()),
                        html.H3('Rechercher par departements'),
                        *Utils.make_break(2),
                        dcc.Input(id='search_dep', type='text',
                            placeholder='Rechercher par departements',
                            debounce=True,
                            required=False,
                            persistence=True,
                            style={"width":'200px', 'height':'30px'})
                    ],
                style={'width':'350px', 'height':'300px','vertical-align':'-275px', 'border':'1px solid black',
                    'display':'inline-block', 'margin':'0px 80px'}
                ),

                html.Div(
                    children=[
                        dcc.RadioItems(
                            id='Selection3',
                            options=["Classe DPE", "Classe GES"],
                            value="Classe DPE",
                            persistence=True,
                            inline=True
                        ),
                        dcc.Graph(id="bar_graph"),
                    ],
                style={'width':'700px', 'display':'inline-block'}
                ),
            ],
        style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
        ),
        *Utils.make_break(2),
        html.Div(
            children=[
                html.H1(children='Cartographie des habitations et de leur consommation en France',
                        style={'textAlign': 'center', 'color': '#7FDBFF'}),
                dcc.RadioItems(
                    id='Selection2',
                    options=["Carte avec marqueurs", "Carte avec clusters"],
                    value="Carte avec marqueurs",
                    persistence=True,
                    inline=True
                ),
                dcc.Graph(id="graph2"),
            ],
            style={'width': '800px', 'display': 'inline-block'},
        ),

        *Utils.make_break(2),
        html.Div(
            children=[html.H1('Régions françaises en fonction de leur DPE ou GES',
                        style={'textAlign': 'center', 'color': '#7FDBFF'}),
            dcc.RadioItems(
                id='Selection',
                options=["consommation_energie", "estimation_ges"],
                value="consommation_energie",
                persistence=True,
                inline=True
            ),
            dcc.Graph(id="graph"),
        ]),
        html.Div(
            children=[html.H1('Chiffres clef',
            style={'textAlign': 'center', 'color': '#7FDBFF'})]
        ),
        html.Div(
        children=[d_recap],
        style={'width': '850px', 'height': '300px', 'margin': '0 auto'}
        ),
        html.Div(
            children=[html.H1('Dataset',
            style={'textAlign': 'center', 'color': '#7FDBFF'})]
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
        Input(component_id='search_dep', component_property='value'),
        Input(component_id="Selection3", component_property="value")
    )
    def update_bar(search_dep, Selection3):
        bar_fig = Histogramme.CreateHist(search_dep, Selection3, france)
        return bar_fig


    @app.callback(
        Output("graph", "figure"),
        Input("Selection", "value"))
    def display_choropleth(Selection):
        choropleth = DepartementsFig.CreateDepFig(Selection, france)
        return choropleth


    @app.callback(
        Output("graph2", "figure"),
        Input("Selection2", "value"))
    def display_marker(Selection2):
        markermap = MarkerMap.CreateMarkerMap(Selection2, france)
        return markermap

    app.run_server(debug=True)
































