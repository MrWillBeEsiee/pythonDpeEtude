from dash.dash_table import DataTable
import pandas as pd
class InfoDisplay:



    @staticmethod
    def InitRecap(france):
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