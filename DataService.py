import pandas as pd
import requests


class DataService:
    @staticmethod
    def InitData():

        """
            Initialise les données de consommation d'énergie en France à partir d'un fichier CSV.

            Returns:
            DataFrame: Données de consommation d'énergie en France.
        """
        #########################################################################################################
        # Pour remplacer le fichier local par un fichier provenant d'une API de L'ademe décommenter le code ci-dessous
        #########################################################################################################

        global f
        start = 0
        for i in range(2):
            rcomp = requests.get(f"https://koumoul.com/data-fair/api/v1/datasets/dpe-france/lines?size=10000"
                                 f"&format=csv&select=consommation_energie%2Cclasse_consommation_energie%2Cestimation_ges%2Cclasse_estimation_ges"
                                 f"%2Ctv016_departement_code%2Clatitude%2Clongitude")
            f = open('caca.csv', "w")
            start += 10000
            print("chargement")
            f.write(rcomp.text)
        f.close()

        france = pd.read_csv("dpe-france.csv")

        france = france.drop(france[(france['classe_consommation_energie'] == 'N')].index)
        france = france.drop(france[(france['classe_consommation_energie'] == 'H')].index)
        france = france.drop(france[(france['classe_consommation_energie'] == 'I')].index)
        france = france.drop(france[(france['consommation_energie'] > 1000)].index)
        france = france.drop(france[(france['estimation_ges'] > 1000)].index)
        france = france.dropna(axis=0)
        return france