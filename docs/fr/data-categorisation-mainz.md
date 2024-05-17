# Catégorisation des données à Mayence

## Défis généraux

Un défi majeur dans le lot de travail de Mayence, qui a collecté des données de différentes sources, était la **normalisation des descriptions d'événements et la modélisation de leurs relations**. Les études, par exemple, ont été initialement enregistrées avec ou sans dates de début et de fin connues comme des événements continus, mais aussi comme des inscriptions universitaires. Une inscription est bien sûr un événement ponctuel qui déclenche un processus d'étude plus long, pour lequel seule la date de début est connue. Pour rendre les informations biographiques collectées plus uniformes et plus faciles à interroger, il était donc nécessaire de reconstruire des événements de processus à partir d'événements ponctuels si possible et de fusionner des événements ponctuels successifs en événements continus plus longs, par exemple si les informations provenaient de calendriers annuels. À cette fin, un script de "consolidation" a été écrit en Python et exécuté sur tous nos ensembles de données collectés.

## Catégorisation des données dans Metaphacts

Afin d'interroger et de regrouper les données du lot de travail de Mayence, nous avons expérimenté avec le système propriétaire [Metaphacts](https://metaphacts.com/), qui "soutient la modélisation collaborative des connaissances et la génération de connaissances". Dans Metaphacts, des catégories de niveau supérieur pour les données collectées peuvent être définies comme `skos:Collections`. Par exemple, Ingo Frank (IOS Regensburg) a pris tous nos termes pour `événements` et `fonctions` que nous avons collectés pour les professeurs de la première modernité actifs à Mayence et a créé des relations hiérarchiques à partir des entrées séparées par des virgules :

- [Système de classification pour les événements biographiques](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Fevent)
- [Classification des rôles / fonctions des personnes](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Ffunction)

Seuls les termes de niveau supérieur sont inclus dans la collection (catégorie) car la recherche est ensuite simplement étendue aux sous-termes respectifs.

## Catégorisation des données via Python

Une autre façon de catégoriser les données consiste à définir des clusters et des hiérarchies dans des dictionnaires Python ou des tableaux CSV simples dont les informations peuvent ensuite être ajoutées à la structure factuelle de base de nos données. La cartographie des données vers des feuilles de calcul existantes est très facile en Python car le package pandas permet une manipulation flexible des données tabulaires sous forme de dataframes. Chaque élément d'une colonne de feuille de calcul sélectionnée peut ainsi être assigné à différentes catégories de niveau supérieur, en fonction des questions de recherche et des contextes théoriques dans lesquels les données sont analysées. Pour des exemples de catégorisation des données en Python, veuillez consulter le dossier [Data Categorisation](https://github.com/ieg-dhr/DigiKAR/tree/main/Data%20Categorisation) dans ce dépôt GitHub.

## Catégories pertinentes pour l'analyse des données dans le WP3

- Fonctions ecclésiastiques en général (toutes les fonctions exercées dans les monastères et les administrations diocésaines)
- Fonctions cléricales (nécessitant des ordres sacrés, par exemple des fonctions sacerdotales dans les diocèses et les paroisses)
- Enseignement (dans les universités, mais aussi dans les séminaires et les collèges)
- Fonctions politiques (par exemple en tant qu'administrateurs, envoyés ou fonctionnaires gouvernementaux)
- Activités médicales (par exemple en tant que médecins personnels pour les aristocrates, médecins de ville, médecins des pauvres ou médecins militaires)
- Activités juridiques (par exemple en tant qu'avocats ou juges)
- Service militaire (par exemple en tant que soldats, ingénieurs militaires ou médecins militaires)

Certaines des activités dans ces catégories se chevauchent naturellement. Pour des raisons de visualisation, cependant, il est nécessaire de fonctionner avec sept à dix catégories dans chaque graphique en réseau ou carte, en particulier lorsque les catégories doivent être mises en évidence en différentes couleurs.
