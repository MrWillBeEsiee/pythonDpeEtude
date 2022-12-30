User Guide
=============================================
!(https://www.esiee.fr/sites/all/themes/custom/esiee_theme/logo.png)
Ce guide vous permettra de déployer et d'utiliser le dashboard sur une autre machine.

Prérequis
-----------------------------------------------
Pour pouvoir utiliser le dashboard, vous aurez besoin d'installer les librairies suivantes :
* plotly (version 5.11 mini)
* dash
* pandas
* json

Vous pouvez les installer en utilisant la commande pip install comme ceci :
    pip install dash pandas plotly json

>Si vous avez déjà plotly mais dans une version inférieur à 5.11 vous pouvez le mettre à jour comme ceci :
    pip install plotly -U

Utilisation
-----------------------------------------------
Une fois les dépendances installées, vous pouvez lancer le dashboard en exécutant le fichier >main.py.
Vous devriez voir s'ouvrir une fenêtre de votre navigateur avec le dashboard.

Le dashboard vous permet de visualiser différentes informations sur les maisons consommatrices d'énergie
et polluantes en France.
Vous pouvez sélectionner différents éléments sur chaque graphique pour filtrer les données affichées.

Par exemple, vous pouvez sélectionner un département dans la liste déroulante pour afficher l'histogramme
de la répartition des classes de consommation d'énergie ou d'émission de gaz à effet de serre pour ce département.
Vous pouvez également utiliser la barre de recherche pour rechercher un département en particulier.


Rapport d'analyse
=============================================
A partir de cette étude, nous pouvons en tirer plusieurs conclusions :

* La répartition des maisons consommatrices d'énergie est inégale dans l'ensemble de la France. En effet, certaines régions
comme la Normandie ou la Bretagne ont une proportion significativement plus élevée de maisons classées dans les catégories
"A" et "B" en termes de consommation d'énergie, tandis que d'autres régions comme l'Île-de-France ou la région PACA ont une
proportion plus importante de maisons classées dans les catégories "E", "F" et "G".
* La majorité des maisons françaises sont classées dans la catégorie "D" en termes de consommation d'énergie. Cela montre que
la consommation moyenne en énergie des maisons en France se situe autour de la moyenne nationale.
* Le Calvados possède une moyenne d'émission de gaz à effet de serre anormalement grande 479 kw/h et 94
