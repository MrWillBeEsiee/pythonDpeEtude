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


        after = 105
        csv_file = open('dpe-france.csv', 'wb')
        req = requests.get(f'https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france/lines?size=10000&format=csv')
        url_content = req.content
        csv_file.write(url_content)

        #augmenter la valeur de la range pour avoir plus de valeurs attention les exceptions n'ont pas été implémentés
        for i in range(15):
            req = requests.get(
                f'https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france/lines?size=10000&after={after}&format=csv&header=false')
            after += 105
            url_content = req.content
            csv_file.write(url_content)

        csv_file.close()







        #Initilisation et trie des donnés
        france = pd.read_csv("dpe-france.csv", low_memory=False)
        france = france.drop(["date_etablissement_dpe", "nom_methode_dpe", "version_methode_dpe",
                                    "annee_construction", "surface_thermique_lot",
                                    "tr001_modele_dpe_type_libelle", "tr002_type_batiment_description",
                                    "code_insee_commune_actualise", "geo_adresse", "geo_score"], axis=1)
        france = france.drop(france[(france['classe_consommation_energie'] == 'N')].index)
        france = france.drop(france[(france['classe_consommation_energie'] == 'H')].index)
        france = france.drop(france[(france['classe_consommation_energie'] == 'I')].index)
        france = france.drop(france[(france['consommation_energie'] > 1000)].index)
        france = france.drop(france[(france['estimation_ges'] > 1000)].index)
        france = france.dropna(axis=0)
        return france