import pandas as pd

class DataService:
    @staticmethod
    def InitData():
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
        france = france.dropna(axis=0)
        return france