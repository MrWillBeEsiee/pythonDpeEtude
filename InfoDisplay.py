from dash.dash_table import DataTable
class InfoDisplay:



    @staticmethod
    def InitRecap(france):

        """
        Initialise un tableau de récapitulatif des données de consommation d'énergie en France.

        Parameters:
        france (DataFrame): Données de consommation d'énergie en France.

        Returns:
        DataTable: Tableau de récapitulatif.
        """

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
        return d_recap

    @staticmethod
    def InitdataSetFig(france):

        """
        Initialise un tableau de données du dataset.

        Parameters:
        france (DataFrame): Données de consommation d'énergie en France.

        Returns:
        DataTable: Tableau de données.
        """

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
        return d_table