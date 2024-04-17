# Managing Time

## Overall challenges

::: info
Focusing on the event-related date columns event_after_date, event_before_date, event_date, event_end, and event_start in a project with fuzzy and uncertain data had the following advantages:
:::

- By including event_after_date and event_before_date, the dataset can capture the uncertainty around the exact timing of events. If the precise date of an event is unknown but it's known to have occurred after a certain date or before a certain date, these columns can represent that uncertainty.
- The columns event_start and event_end provide information about the duration of events, which is crucial for understanding their impact and scope. This can help in analyzing the temporal extent of events and their relationship with other events.
- Using varchar data type for these columns allows for flexibility in representing uncertain or ambiguous date information. It accommodates various date formats, partial dates, or textual descriptions of dates, which is common in historical or fuzzy datasets.

::: info
While focusing on these columns addresses certain forms of uncertainty, there are still some challenges that remain:
:::

- The level of granularity provided by these columns may not always be sufficient to capture the full extent of uncertainty. For example, if events are known to have occurred within a certain timeframe but the exact dates are unknown, representing this level of uncertainty may require additional techniques such as interval-based representations.
- Uncertainty in the data itself, such as missing or inconsistent values in these columns, can still pose challenges.
- While these columns provide information about the timing and duration of events, interpreting and making meaningful inferences cannot be taken for granted. This requires careful consideration of context and potentially the integration of external sources of information, including the various historiographical and editorial comments in the factoid lists.

Overall, focusing on event-related date columns allows us to handle temporal uncertainty per archival factoid but may not be the ideal solution for all projects.

## Differentiating temporal information in the factoid model (WP3)

::: info
This part of the documentation is still missing.
:::

## Additional temporal information collected as free-text comments

Allowing a free-text entry for comments on date (un)certainty gave as the opportunity to express additional data problems beyond fuzzy dating and highlight dates from primary and secondary sources whose validity we doubted. The disadvantage, however, was that it was difficult to regulate what data collectors wrote and to find clear conventions for identical issues. The first attempt to add free-text descriptions to our Jahns data set during data collection, for example, resulted in comments that were inconsistent, contained spelling mistakes, or were difficult to interpret by other team members looking at the data later. We, therefore, made the attempt to normalise the free-text comments to a degree that will still permit some NLP or AI processing in the future. The original Jahns comments and the new normalised versions are in the table below.

| Text                                                                                | Occurrence |
| ----------------------------------------------------------------------------------- | ---------- |
| Alternativdatum                                                                     | 1          |
| Alternatives Startdatum                                                             | 1          |
| Datierung inkonsistent, siehe Praktika                                              | 1          |
| exclude                                                                             | 1          |
| Datierung unklar                                                                    | 2          |
| Datierung unsicher                                                                  | 19         |
| Datierung unsicher und vage                                                         | 8          |
| Datierung unsicher, "offenbar vor Erwerb des Lic. iur."                             | 1          |
| Datierung unsicher, Alternativdaten                                                 | 1          |
| Datierung unsicher, Alternativdatum                                                 | 7          |
| Datierung vage                                                                      | 85         |
| Datierung vage / Noch 1766 (Promotion)                                              | 5          |
| Datierung vage / Ort unsicher                                                       | 2          |
| Datierung vage / Zeitdauer                                                          | 3          |
| Datierung vage und unsicher                                                         | 1          |
| Datierung vage, "1 1/2 J. Praktikant am RKG und am RHR"                             | 1          |
| Datierung vage, "1 1/2 J. Praktikant am RKG und am RHR", Station nach Wetzlar       | 1          |
| Datierung vage, "ca. 1737 ff", "anfangs über 14 J. lang"                            | 1          |
| Datierung vage, Zeitdauer                                                           | 1          |
| Datierung vage: "Ende 1775/Anf. 1776"                                               | 1          |
| Einzelbeleg                                                                         | 7          |
| Einzelbeleg, Funktion wahreschinlich auch vor- und nachher                          | 2          |
| Enddatum mglw. später; letzter Beleg                                                | 8          |
| Enddatum möglicherweise später                                                      | 3          |
| Enddatum unklar, Nachweis noch für 1809/10                                          | 1          |
| Enddatum unsicher                                                                   | 5          |
| Enddatum unsicher, Alternativdatum                                                  | 4          |
| Enddatum unsicher, evtl. auch später                                                | 1          |
| Enddatum unsicher, letzter Beleg                                                    | 1          |
| Enddatum vage                                                                       | 4          |
| Enddatum vage / Zeitdauer                                                           | 1          |
| Enddatum vage und unsicher                                                          | 1          |
| Enddatum vage, "bis ca. Anf. 1706"                                                  | 1          |
| Enddatum vage, Nachweis noch für 1815                                               | 2          |
| Enddatum vage.                                                                      | 1          |
| Enddatumg mglw. später, letzter Beleg                                               | 4          |
| frühestes Belegdatum = 1751                                                         | 1          |
| Funktionsausübung "daneben"                                                         | 1          |
| Geheimer Rat                                                                        | 2          |
| Inauguraldisputation am 12.09.1736                                                  | 1          |
| n/a1737                                                                             | 1          |
| punktueller Nachweis                                                                | 3          |
| Reihenfolge, Datierung unklar; Enddatum taq                                         | 3          |
| saisonales Datum                                                                    | 1          |
| Stardatum vage                                                                      | 1          |
| Start- und Enddatum frühester bzw. spätester Beleg                                  | 3          |
| Start- und Enddatum mglw. früher bzw. später                                        | 1          |
| Start- und Enddatum mglw. früher bzw. später, punktueller Nachweis                  | 6          |
| Start- und Enddatum mglw. früher bzw. später. Frühester/spätester Beleg             | 1          |
| Start- und Enddatum mglw. früher/später, frühester bzw. spätester Beleg             | 1          |
| Start- und Enddatum möglicherweise früher bzw. später, punktueller Nachweis         | 2          |
| Start- und Enddatum möglicherweise früher, punktueller Nachweis                     | 1          |
| Start- und Enddatum vage                                                            | 2          |
| Start- und Enddatum vage / Alternatives Startdatum                                  | 2          |
| Start- und Enddatum vage, möglicherweise früher bzw. später. Sicher nicht mehr 1751 | 1          |
| Start- und Enddatum vage: "ca. 1753- ca. Anf. 1757; Zeitdauer vier Jahre            | 1          |
| Startdatierung vage                                                                 | 2          |
| Startdatum frühester Beleg, Enddatum vage.                                          | 2          |
| Startdatum Alternativdatum                                                          | 2          |
| Startdatum eventuell früher                                                         | 3          |
| Startdatum mglw. früher, frühester Beleg                                            | 17         |
| Startdatum mglw. früher, frühester Beleg / Alternativdatum                          | 2          |
| Startdatum mglw. früher, frühester Beleg; Enddatum Alternativdatum                  | 2          |
| Startdatum mglw. früher, frühester Beleg.                                           | 4          |
| Startdatum mglw. früher.                                                            | 1          |
| Startdatum möglicherweise frühe, frühester Beleg                                    | 1          |
| Startdatum möglicherweise früher, frühester Beleg                                   | 2          |
| Startdatum möglicherweise früher.                                                   | 2          |
| Startdatum unsicher                                                                 | 4          |
| Startdatum unsicher und vage.                                                       | 2          |
| Startdatum unsicher, Alternativdatum                                                | 6          |
| Startdatum unsicher, erster Beleg.                                                  | 1          |
| Startdatum unsicher, Immatrikulation erst 1724 sicher nachgewiesen                  | 1          |
| Startdatum unsicher, punktueller                                                    | 2          |

## Managing fuzzy time in data analysis and data visualisation

::: info
This part of the documentation is still missing.
:::
