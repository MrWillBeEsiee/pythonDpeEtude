import numpy as np

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

        import requests
        import csv

        # Nombre total de lignes à récupérer
        n = 10000

        # Initialisation du compteur de lignes
        count = 0

        # Initialisation du fichier CSV
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Boucle jusqu'à ce que toutes les lignes soient récupérées
            while count < n:
                # Envoi de la requête à l'API
                response = requests.get(
                    f'https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france/lines?size=10000&after={count}&select=consommation_energie%2Cclasse_consommation_energie%2Cestimation_ges%2Cclasse_estimation_ges%2Ctv016_departement_code%2Clatitude%2Clongitude')

                # Vérification de la réponse de l'API
                if response.status_code == 200:
                    # Récupération des données de la réponse
                    data = response.json()['results']

                    # Parcours des lignes de données
                    for row in data:
                        # Ajout de la ligne au fichier CSV
                        writer.writerow(row.values())

                        # Incrémentation du compteur de lignes
                        count += 1

                        # Si toutes les lignes ont été récupérées, on arrête la boucle
                        if count == n:
                            break
                else:
                    # Si la réponse de l'API est incorrecte, on affiche un message d'erreur
                    print(f'Erreur {response.status_code}: {response.reason}')
                    break

        # Message de confirmation
        print(f'{count} lignes ont été écrites dans le fichier CSV.')



        france = pd.read_csv("dpe-france.csv", low_memory=False)

        france = france.drop(france[(france['classe_consommation_energie'] == 'N')].index)
        france = france.drop(france[(france['classe_consommation_energie'] == 'H')].index)
        france = france.drop(france[(france['classe_consommation_energie'] == 'I')].index)
        france = france.drop(france[(france['consommation_energie'] > 1000)].index)
        france = france.drop(france[(france['estimation_ges'] > 1000)].index)
        france = france.dropna(axis=0)
        return france