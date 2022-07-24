
**4) Relationship tracing**

Skript sucht nach allen Elternbeziehungen und konstruiert daraus die Gruppe der Geschwister.

Dann erstellt das Skript aus der Liste der Kinder alle möglichen Geschwisterpaare (im Moment auch mit der Person selbst), die dann entsprechend in EXCEL geschrieben werden.

Analog rekonsturiert das Skript Beziehungen zu den Großeltern.

Ich glaube, diese beiden Ebenen reichen als EXPLIZITE Ebenen aus.

Cousins etc. könnte man einfacher über die DB abfragen.

Script searches for all parent relationships and constructs the group of siblings from this.

<hr>

Then the script creates all possible sibling pairs from the list of children (at the moment also with the person himself), which are then written accordingly in EXCEL.

Similarly, the script reconstructs relationships with the grandparents.

I think these two levels are sufficient as EXPLICIT levels.

Cousins etc. could be queried more easily via the DB.

<hr>

**In progress:**

- "BIOGRAPHY TRACING": select person by ID, match name variants, find all life events recorded, narrow down events by time limits if necessary, put events in chronological order
- "DISAMBIGUATION": script to compare similar names of people and places and assign unique IDs (human intervention necessary), e.g. using Python's fuzzy wuzzy package.
- "SPATIAL EVOLUTION": extracts events coinciding in specific places, reconstruct political / cultural role of places through human agency

<hr>
