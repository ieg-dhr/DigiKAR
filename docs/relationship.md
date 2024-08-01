---
authors:
  - Florian Stabel (Mainz)
  - Monika Barget (Maastricht)
---

# Relationship tracing

Our general approach in DigiKAR is to be as implicit as possible when collecting data. Relationships between entities that can be deducted from a combination of other entities do not need to be explicitly included in the data model. In AP2, we focus on five rights out of many, and DigiKAR generally does not pretend that we can model the Holy Roman Empire with all its administrative bodies. Therefore, we also do not do any “nested modelling” in AP3. For example, we do not explicitly relate monasteries to religious orders or parishes to bishoprics. This is information that would have to be linked to our data from external sources in the future or that can be computationally deducted from the frequency of direct relationships that our data already contain.

To give another example, we do not need to add sibling names to persons in our data if mothers and fathers are known. Specifically for the tracing of relationships between humans, we have also created a Python script that can be run to re-construct some of the implicit connections from the existing data:

::: info
ADD SCRIPT
:::

This script searches for all parent relationships and constructs the group of siblings from this. Then the script creates all possible sibling pairs from the list of children (at the moment also with the person himself), which are then written accordingly in EXCEL. Similarly, the script reconstructs relationships with the grandparents. Based on these relations, the data could also be queried with SPARQL when ingested into a database.

## In progress

- "BIOGRAPHY TRACING": select person by ID, match name variants, find all life events recorded, narrow down events by time limits if necessary, put events in chronological order
- "DISAMBIGUATION": script to compare similar names of people and places and assign unique IDs (human intervention necessary), e.g. using Python's fuzzy wuzzy package.
- "SPATIAL EVOLUTION": extracts events coinciding in specific places, reconstruct political / cultural role of places through human agency
