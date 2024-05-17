## Code pour la collecte de données, le nettoyage de données et l'analyse de données

Dans DigiKAR, nous avons également expérimenté avec du code Python pour la collecte de données, le nettoyage de données et l'analyse de données, notamment dans notre lot de travail à Mayence. Le package [pandas](https://pandas.pydata.org/) en Python est largement utilisé pour travailler avec des [dataframes](https://www.databricks.com/glossary/what-are-dataframes) bidimensionnels et nous a aidés à lire, manipuler et écrire des fichiers EXCEL et CSV. Nous avons également travaillé avec des packages pour XML, HTML, JSON et [le géocodage](https://monikabarget.github.io/GeoHumTutorials/).

:::info
Les scripts et leurs cas d'utilisation sont expliqués dans les [sections *workflow*] détaillées ci-dessous. Dans la plupart des cas, une courte description est disponible en anglais ainsi qu'en allemand et en français.
:::

## Édition et exécution de code dans différents environnements

Certains des fichiers [Jupyter Notebook](https://jupyter.org/) (se terminant par `.ipynb`) dans notre dépôt ont été initialement créés pour [Google Colab](https://colab.google/) et doivent être ajustés lorsqu'ils sont utilisés dans d'autres environnements. Dans le projet DigiKAR, Google Colab a été initialement utilisé pour l'édition collaborative de code parce que nous n'avions pas accès à une infrastructure logicielle de recherche institutionnelle. Idéalement, le code devrait être hébergé dans des environnements non commerciaux, tels que les infrastructures informatiques hébergées par les universités pour la science des données.

![capture d'écran google colab](https://github.com/ieg-dhr/DigiKAR/assets/38257338/72173520-9cf1-4dc7-be6e-4f8b25ee97b8)

Pour que les notebooks Colab fonctionnent pour vous, veuillez suivre les étapes suivantes :

1. Mettez le Jupyter notebook sur votre propre Google Drive, de préférence dans un dossier dont le nom contient "Colab" afin que vous puissiez facilement l'identifier plus tard.
2. Ouvrez le notebook et ajustez le chemin du répertoire en fonction de votre propre emplacement de fichier. Vous devrez peut-être également changer les chemins des données d'entrée et de sortie dans le script, en fonction de votre propre structure de dossier préférée. Assurez-vous que tous les dossiers que vous nommez dans le script existent également sur Google Drive avant d'exécuter le script.
3. Sélectionnez "ouvrir avec" et connectez-vous à l'application Google Colab. Si vous n'avez pas utilisé Google Colab auparavant, sélectionnez l'option "connecter plus d'applications" et trouvez Colab là-bas.
4. Assurez-vous de donner à Colab toutes les permissions nécessaires pour exécuter le script et lire/écrire des fichiers. Si vous ne voulez pas que Colab accède à un Google Drive privé, vous pouvez créer un nouveau compte Google exclusivement à des fins de recherche.
