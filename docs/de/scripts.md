## Code für Datenerfassung, Datenbereinigung und Datenanalyse

In DigiKAR haben wir auch mit Python-Code für Datenerfassung, Datenbereinigung und Datenanalyse experimentiert, insbesondere in unserem Mainzer Arbeitspaket. Das [pandas](https://pandas.pydata.org/) Paket in Python wird häufig verwendet, um mit zweidimensionalen [Dataframes](https://www.databricks.com/glossary/what-are-dataframes) zu arbeiten, und hat uns geholfen, EXCEL- und CSV-Dateien zu lesen, zu manipulieren und zu schreiben. Wir haben auch mit Paketen für XML, HTML, JSON und [Geokodierung](https://monikabarget.github.io/GeoHumTutorials/) gearbeitet.

:::info
Skripte und deren Anwendungsfälle werden in den detaillierten [*Workflow* Abschnitten] unten erklärt. In den meisten Fällen ist eine kurze Beschreibung auf Englisch sowie auf Deutsch und Französisch verfügbar.
:::

## Bearbeiten und Ausführen von Code in verschiedenen Umgebungen

Einige der [Jupyter Notebook](https://jupyter.org/) Dateien (Endung `.ipynb`) in unserem Repository wurden ursprünglich für [Google Colab](https://colab.google/) erstellt und müssen angepasst werden, wenn sie in anderen Umgebungen verwendet werden. Im DigiKAR-Projekt wurde Google Colab anfänglich für die kollaborative Codebearbeitung verwendet, da wir keinen Zugang zu einer institutionellen Forschungssoftware-Infrastruktur hatten. Idealerweise sollte Code in nicht-kommerziellen Umgebungen gehostet werden, wie z.B. von Universitäten gehosteten Computing-Infrastrukturen für Data Science.

![Screenshot Google Colab](https://github.com/ieg-dhr/DigiKAR/assets/38257338/72173520-9cf1-4dc7-be6e-4f8b25ee97b8)

Um die Colab-Notebooks für Sie funktionsfähig zu machen, führen Sie bitte die folgenden Schritte durch:

1. Legen Sie das Notebook auf Ihrem eigenen Google Drive ab, idealerweise in einem Ordner, dessen Name "Colab" enthält, damit Sie es später leicht identifizieren können.
2. Öffnen Sie das Notebook und passen Sie den Verzeichnispfad entsprechend Ihrem eigenen Dateispeicherort an. Möglicherweise müssen Sie auch die Pfade der Eingabe- und Ausgabedaten im Skript ändern, je nach Ihrer bevorzugten Ordnerstruktur. Stellen Sie sicher, dass alle Ordner, die Sie im Skript benennen, auf Google Drive existieren, bevor Sie das Skript ausführen.
3. Wählen Sie "Öffnen mit" und verbinden Sie sich mit der Google Colab App. Wenn Sie Google Colab noch nicht verwendet haben, wählen Sie die Option "Weitere Apps verbinden" und finden Sie dort Colab.
4. Stellen Sie sicher, dass Colab alle notwendigen Berechtigungen erhält, um das Skript auszuführen und Dateien zu lesen/schreiben. Wenn Sie nicht möchten, dass Colab auf ein privates Google Drive zugreift, können Sie ein neues Google-Konto ausschließlich für Forschungszwecke erstellen.
