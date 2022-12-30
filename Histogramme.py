import plotly.express as px


class Histogramme:

    def CreateHist(search_value, Selection3, france):

        title_value = 'tous départements'

        data = france.copy(deep=True)

        if search_value:
            title_value = search_value

            data = data[data['tv016_departement_code'].str.contains(search_value, case=False)]

        if(Selection3 == "Classe DPE"):
            bar_fig = px.histogram(
                data_frame=data, x='classe_consommation_energie', color='classe_consommation_energie',
                title=f'Répartition des classes DPE : {title_value}',
                category_orders={"classe_consommation_energie": ("A", "B", "C", "D", "E", "F", "G")},
                color_discrete_sequence=("#82a6fb", "#aac7fd", "#cdd9ec", "#ead4c8", "#f7b89c", "#f18d6f", "#d95847"),
            )
            return bar_fig
        else:
            bar_fig = px.histogram(
                data_frame=data, x='classe_estimation_ges', color='classe_estimation_ges',
                title=f'Répartition des classes d\'estimation GES : {title_value}',
                category_orders={"classe_consommation_energie": ("A", "B", "C", "D", "E", "F", "G")},
                color_discrete_sequence=("#82a6fb", "#aac7fd", "#cdd9ec", "#ead4c8", "#f7b89c", "#f18d6f", "#d95847"),
            )
            return bar_fig