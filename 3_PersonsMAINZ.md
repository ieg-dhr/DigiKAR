**Process of person identification and disambiguation**

<p align="jusitfy>"The challenges of working with (German and Latinised) person names in DigiKAR has been described in one of my blog post. In the process, we first experimented with a Python script performing the following actions:</p>

1) Read all names from PersonList into memory
2) Ask the user to enter a name
3) Search for the name in PersonList
4) Ask for confirmation
5) On confirmation, match all variants of the name with EventList persons
6) Show complete matches with all event info
7) Search for similar names on user request

<p align="justify">To search for potentially identical names, we tried calculating the name strings' <a href="https://www.sciencedirect.com/topics/computer-science/cosine-similarity#:~:text=Cosine%20similarity%20measures%20the%20similarity,document%20similarity%20in%20text%20analysis.">Cosine Similarity</a>, and specified, for that it must be at least 80% to consider two strings a match. If only a person's 1st name, surname, and only one of several middle names per person are in one subset of our data, however, the string similarity is far below that threshold when the person's full name is present in another subset. If we assume that at least the family name is always present, and that it must be the last word in an n-gram, then one could begin with matching the last names to identify persons in one family, and then consider identifical first and middle names in a second step. If father and son have the same name and the year of birth is known for both, we can use additional person attributes to assess whether a study period in the year YYYY concerns the father or the son.</p>

<p align="justify">Combining automated string comparisons with manual checks, we have been able to create a person list with unique IDs and name variants as the basis for the data visualisations in our project. IDs from that person list are added to all our factoid lists so that our static and interactive map can be based on the IDs rather than the person names.</p>

**Working with related persons**

<p align="justify">Our so-called <a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_relationship-tracer.py>
"Relationship Tracer"</a> script, which we updated several times, helped us identify family connections between persons based on a smaller number of known relationships (e.g. marriages and births) collected from our sources. The script's workflow can be described as follows:
<ul>
    <li>The script initiates a search for all parent relationships and subsequently assembles a group of siblings based on this information.</li>
    <li>Following this, the script generates all potential sibling pairs from the list of children, including the individual themself. These pairings are then documented in an EXCEL file.</li>
    <li>In a similar fashion, the script reconstructs relationships with grandparents.</li>
</ul>

<p align="justify">Per person, we aimed to record the following data:</p>

<ul>
  <li>Name</li>
  <li>GND ID</li>
  <li>Possibly other IDs?</li>
  <li>Internal project ID of @fstabel</li>
  <li>Father</li>
  <li>Mother</li>
  <li>Grandfather via mother</li>
  <li>Grandmother via mother</li>
  <li>Grandfather via father</li>
  <li>Grandmother via father</li>
  <li>All known siblings</li>
</ul>

The initial test run, which focused on siblings, correctly identified the following men as brothers and the following women as sisters:
<ul style="list-style-type: none;">
  <li>1048 Karl Strecker sibling Alexander Bernhard Strecker unknown no info</li>
  <li>1049 Alexander Bernhard Strecker sibling Karl Strecker unknown no info</li>
  <li>1050 Karl Strecker sibling Karl Friedrich Strecker unknown no info</li>
  <li>1051 Karl Friedrich Strecker sibling Karl Strecker unknown no info</li>
  <li>1052 Karl Strecker sibling Ernst Wilhelm Strecker unknown no info</li>
  <li>1053 Ernst Wilhelm Strecker sibling Karl Strecker unknown no info</li>
  <li>1054 Alexander Bernhard Strecker sibling Karl Friedrich Strecker unknown no info</li>
  <li>1055 Karl Friedrich Strecker sibling Alexander Bernhard Strecker unknown no info</li>
  <li>1056 Alexander Bernhard Strecker sibling Ernst Wilhelm Strecker unknown no info</li>
  <li>1057 Ernst Wilhelm Strecker sibling Alexander Bernhard Strecker unknown no info</li>
  <li>1058 Karl Friedrich Strecker sibling Ernst Wilhelm Strecker unknown no info</li>
  <li>1059 Ernst Wilhelm Strecker sibling Karl Friedrich Strecker unknown no info</li>
  <li>1060 Joachim Andreas Meyer sibling Johann Andreas Meyer unknown no info</li>
</ul>

<ul style="list-style-type: none;">
  <li>1089 Maria Josepha Rotermund sibling Theresia Rotermund unknown no info</li>
  <li>1090 Theresia Rotermund sibling Maria Josepha Rotermund unknown no info</li>
  <li>1091 Maria Josepha Rotermund sibling Sophia Josepha Rotermund unknown no info</li>
  <li>1092 Sophia Josepha Rotermund sibling Maria Josepha Rotermund unknown no info</li>
  <li>1093 Theresia Rotermund sibling Sophia Josepha Rotermund unknown no info</li>
  <li>1094 Sophia Josepha Rotermund sibling Theresia Rotermund unknown no info</li>
  <li>1095 Susanna Christina Weltz sibling Friederike Eleonore Weltz unknown no info</li>
  <li>1096 Friederike Eleonore Weltz sibling Susanna Christina Weltz unknown no info</li>
</ul>

<p align="justify">Unfortunately, we could not distinguish sisters and brothers without massive additional effort (e.g. an automated identification of the gender commonly associated with certain first names). So we decided to work with gender-neutral relationship markers. Florian expressed willingness to add an additional column with explicit gender details to our final person list if necessary, indicating its potential usefulness for specific prosopographic queries.</p>

<p align="justify">The relationship between the Streckers as brothers was also confirmed in research literature. The two Meyers, however, were most likely misidentified in the original data, so they may have been different people after all. This problem also occurred in our Erfurt data. Definitely not all assignments made by ID are correct. Here it would be necessary to look at the data as a whole. In case of doubt, two different persons must be assumed. And probably the calculation of relationships only makes sense after more general data cleaning. Conversely, it would be helpful for the overview to have as many relationships as possible explicitly... having siblings explicitly is not so decisive for our question. More distant relations, such as cousins, can be retrieved through more complex dataqueries.</p>

<p align="justify">Our first kinship reconstruction for the Erfurt sample (created in April 2022) was called "Parents-and-siblings". Here, both sides of any <code>Rel_Pers</code> relationship in our data table were made explicit and new relationships (parents and siblings) were calculated. The entries for 'parent' or 'sibling' in the column <code>Rel_type</code> are thus reconstructed -- the others (e.g. 'wife' or more distant relations like 'instructor', 'godfather', etc.) are relationship types already given in the input data.</p> 

<p align="justify">In a cursory examination, Florian noticed that not all relationships were inverted, and he provided Jost Brochhausen as an example. Florian also mentioned that the existing inversions were explicitly available in the raw data. Furthermore, he highlighted cases in the first list that featured an empty relationship column or contained meaningless information, marking these instances in yellow within the "Parents-and-siblings_fs.xlsx" list located in the output folder. Florian speculated that typographical errors might be responsible for such occurrences, and he suggested the inclusion of the source factoid's ID, especially in cases of deleted duplicate information. Additionally, Florian marked other instances where certain relation types were used infrequently (likely to become irrelevant in the future) and also marked typographical errors in orange.</p>

<h3>Tracing grandparent-grandchild relationships</h3>

<p align="justify">In the first version of the script, there was an issue related to the format of tuples within the code, which has been successfully resolved with the assistance of the Stack Overflow community. Grandparent relations were added in the second version of the script. In our new file "GRANDPARENTS_GRANDCHILDREN", various grandparent relationships from the Erfurt sample (FactoidList_Erfassung_Erfurt_Master_2022-04-18.xlsx) were recorded. Where the file says "grandchild", the script extracted a known grandparent relationship. Where it says "grandparent-gandchild", the script reconstructed a relationship, so I am not sure whether these are grandparents, grandchildren or even both types of relationships. I need feedback on what happened so that I can make it clear or improve it in the script.</p>

<p align="justify">Florian reported that grandparent relationships were checked and commented upon in a file named "GRANDPARENTS_GRANDCHILDREN_FS.xlsx." He mentioned encountering cases where individuals shared the same name but indicated that he could disambiguate them and assign different IDs. Florian raised the question of whether the script could potentially indicate the lineage (maternal or paternal) through which family relationship was established. Additionally, Florian observed that the IDs he assigned were sporadically included, emphasizing their importance for orientation.</p>

<h3>Integration timeless and temporary person attributes in the data model</h3>

<p align="justify">What needed to consider were the effects of the person data reconstructions on Ingo's data models. Ingo, at a previous point in time, had intentions to establish links between roles and the individuals. However, these links were subject to frequent changes. Consequently, it was decided to diligently document only the unchanging aspects of people's lives in the person model, treating all temporary attributes as factoid information. Time-dependent roles or activities, complete with role-related information when applicable, were to be structured within the data model. Naturally, the end goal involved the ability to establish connections between activities and the individuals.</p>

<p align="justify">For reference, preliminary data models were available on Metaphacts at the following links: EntwurfsmusterAP3 and EntwurfsmusterAP2.</p>

<h3>Challenges of using the Mainz person data for prosopographic research</h3>

<p align="justify">Florian also raised a broader question regarding when and how to handle the removal or exclusion of "data clutter" and individuals who are no longer of interest or serve solely as intermediaries in our project, particularly in the case of women. Florian clarified that the initial objective was to focus on a select group of government and council members, specifically in the Erfurt case. The aim was to explore intergenerational patterns by examining the life stages of fathers, fathers-in-law, grandfathers, sons-in-law, and sons. Florian, however, expressed concerns about the feasibility of this approach due to the escalating research demands. He suggested a possible limitation of this inquiry to Jahns, where the data had already been "researched" and only required capture. Florian underscored the importance of implementing a mechanism to filter out persons of interest and restrict automatic calculations to specific individuals, thus minimizing the oversight needed. Florian also emphasized the need to expand the data model to encompass not only grandfathers, fathers, and sons but also sons-in-law and fathers-in-law.</p>

**Preliminary overview of persons in the data and number of (initial) events associated with them**

So far, we have collected **48497 rows of events** (excluding reconstructed information). These events relate to **2566 person names** (prior to normalisation, disambiguation and ID-assignment). The majority of persons have less than 10 recorded biographic events. For some individuals, we have more than 100 entries (resulting from repeated mentions in annual lists of office holders).

<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
</style>
</head>
<body>

<table id="data-table">
  <thead>
    <tr>
      <th>Index</th>
      <th>Person's Name</th>
      <th>Frequency</th>
    </tr>
  </thead>
  <tbody>
    <table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Person's Name</th>
      <th>Frequency</th>
    </tr>
  </thead>
    <tr>
      <td>0</td>
      <td>Wendelin Wendelin Dietes</td>
      <td>3</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Matthäus Anton Chrysostomus Eberwein</td>
      <td>2</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Johann Friedrich Wüstefeld</td>
      <td>7</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bertold Georg Gothelp</td>
      <td>6</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Johann Franz Asmut</td>
      <td>8</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Alexander Günther Samhaber</td>
      <td>5</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Friedrich Franz Thyri</td>
      <td>8</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Amandus Clemens Schell</td>
      <td>7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Samuel Thomas Sömmering</td>
      <td>13</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Johannes Jacobus von Lasser</td>
      <td>9</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Damian Friedrich Boost</td>
      <td>7</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Heinrich Ignaz Joseph Vogelmann</td>
      <td>5</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Johann Heinrich Hessenhover</td>
      <td>7</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Johann Philipp Fibig</td>
      <td>7</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Petrus Nikolaus Unkraut</td>
      <td>7</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Wendelin Wilhelm Josef Braunschiedel</td>
      <td>5</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Franz Valentin Woger</td>
      <td>6</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Johann Rudolf Will</td>
      <td>9</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Heinrich Ernst Herold</td>
      <td>5</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Johannes Friedrich Unckel</td>
      <td>6</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Petrus Michael Ignaz Ravennas</td>
      <td>8</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Matthias Joseph Hagen</td>
      <td>8</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Johannes Claudius Renard</td>
      <td>6</td>
    </tr>
    <tr>
      <td>23</td>
      <td>Georg Christian Gottlieb Theophil Wedekind</td>
      <td>11</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Peter Joseph Leydig</td>
      <td>7</td>
    </tr>
    <!-- Row 25 will be the last one before "Read More" -->
    <tr>
      <td>25</td>
      <td>Johannes Jochem Hans Höglein</td>
      <td>5</td>
    </tr>
    <!-- Add more rows below this point -->
    <tr class="hidden-row">
        <td>26</td>
        <td>Christoph Ignaz  Wiese</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>27</td>
        <td>Johann Gottfried  Schweickard</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>28</td>
        <td>Johann Kaspar Anton  Hartmann</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>29</td>
        <td>Josef Theobald  Vogt</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>30</td>
        <td>Jakob Franz Xaver  Koch</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>31</td>
        <td>Johann Heinrich  Faber</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>32</td>
        <td>Johann Philipp  Hahn</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>33</td>
        <td>Johannes Wilhelm  Beusser</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>34</td>
        <td>Lambert Christoph  Richtergin</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>35</td>
        <td>Raymund Theodor  Peetz</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>36</td>
        <td>Valentin Amandus  Bleidenstatt</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>37</td>
        <td>Albert Friedrich  von Minsingen</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>38</td>
        <td>Johann Baptist  von Horix</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>39</td>
        <td>Franz Ulrich  Megele</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>40</td>
        <td>Johann Stephan Valentin  Burckard</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>41</td>
        <td>Johann Richard  von Roth</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>42</td>
        <td>Peter Nikolaus  Söhnchen</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>43</td>
        <td>Peter Anton  Freiherr von Frank</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>44</td>
        <td>Gerhard Anton  Gerresheim</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>45</td>
        <td>Philipp Karl  von Fugger</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>46</td>
        <td>Christoph Siegfried  Faber</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>47</td>
        <td>Cyprian Kardinal  Vomelius</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>48</td>
        <td>Johannes Rudolf Dubslaff  Eler</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>49</td>
        <td>Hieronymus Maria Joseph Alexander  von Ludolph</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>50</td>
        <td>Franz Erwin Sebastian  Itzstein</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>51</td>
        <td>Johann Adam  Krebs</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>52</td>
        <td>Johann Anton  Antzmann</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>53</td>
        <td>Johann Josef  Schönhuber</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>54</td>
        <td>Johann Wendelin  Dictes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>55</td>
        <td>Anselm Franz Joseph  Ernst</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>56</td>
        <td>Franz Phillipp  Frank</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>57</td>
        <td>Peter Jakob  Ostermann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>58</td>
        <td>Johann Philipp  Dirolf</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>59</td>
        <td>Jakob Fidelis  Ackermann</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>60</td>
        <td>Johann Christoph  Freiherr von Gudenus</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>61</td>
        <td>Carolus Siegfried  Faber</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>62</td>
        <td>Dionysius Hans Fritz Philipp  Campius</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>63</td>
        <td>Johannes Adolf  Mergentheim</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>64</td>
        <td>Ludwig Konstantin  Reichsfreiherr von Welden</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>65</td>
        <td>Johann Ernst  Neusesser gen\. Leibelbacher</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>66</td>
        <td>Franz Ignaz Joseph  Bodmann</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>67</td>
        <td>Joseph Nikolaus  Moser</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>68</td>
        <td>Jakob Walther  Kühorn</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>69</td>
        <td>Johann Kraffto  Hiegell</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>70</td>
        <td>Adam Anton Chrysostomus  Ebersheim</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>71</td>
        <td>Georg Joseph  Westhofen</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>72</td>
        <td>Johann Babtist Joseph  Dilenius</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>73</td>
        <td>Nikolaus Karl  Molitor</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>74</td>
        <td>Franz Joseph  Wittmann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>75</td>
        <td>Franz Philipp  Beusser</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>76</td>
        <td>Ludwig Philipp  Behlen</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>77</td>
        <td>Bernhard Baptist  Kühorn von Feuerfeld</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>78</td>
        <td>Georg Friedrich  Franck</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>79</td>
        <td>Karl Joseph Hieronymus  Windischmann</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>80</td>
        <td>Joseph William Mulvany  Seubert</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>81</td>
        <td>Johann Friedrich  Michael</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>82</td>
        <td>Johann Wendelin  Wasmuth</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>83</td>
        <td>Philipp Friedrich  Waldmann</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>84</td>
        <td>Heinrich Otto  Holtzgreven</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>85</td>
        <td>Friedrich Rudolf  Moll</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>86</td>
        <td>Joseph Thomas  Mantz</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>87</td>
        <td>Franz Anton Chrysostomus  Dürr</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>88</td>
        <td>Antonius Quirinus Hans Fritz Philipp  Campius</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>89</td>
        <td>Jakob Heinrich  Reuter</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>90</td>
        <td>Karl Joseph  Koelsch</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>91</td>
        <td>Dietrich Joachim  Kauff</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>92</td>
        <td>Philipp Paul  Koltz</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>93</td>
        <td>Bernhard Max  Schöfferlin</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>94</td>
        <td>Philipp Franz  Dünwald</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>95</td>
        <td>Anton Franz  Metternich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>96</td>
        <td>Theodor Konrad  Hartleben</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>97</td>
        <td>Johann Valentin  Strauss</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>98</td>
        <td>Johann Joachim  Becher</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>99</td>
        <td>Lorenz Rudolf  Wilthelm</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>100</td>
        <td>Johannes Wilhelm  Langen</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>101</td>
        <td>Andreas Rudolf Dubslaff  Eler</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>102</td>
        <td>Michael Kardinal  Voss</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>103</td>
        <td>Jacob Kardinal  Vosbach</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>104</td>
        <td>Johannes Ambrosius  Höglein</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>105</td>
        <td>Kaspar Gottfried  Schweickardt</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>106</td>
        <td>Anton Jochem Hans  Hoffmann</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>107</td>
        <td>Johannes Petrus  Menshengen</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>108</td>
        <td>Johann Conrad  Moeller</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>109</td>
        <td>Kaspar Hermann Joseph  von Westhausen</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>110</td>
        <td>Ludwig Baptist  von Hörnigk</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>111</td>
        <td>Markus Karl Klaus  Bausmann</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>112</td>
        <td>Georg Leonhard  Schraub</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>113</td>
        <td>Laurentius Heinrich  Faber</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>114</td>
        <td>Cornelius Peter  Montfort</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>115</td>
        <td>Friedrich Lorenz Theodor  Langen</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>116</td>
        <td>Jakob Georg  Goy</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>117</td>
        <td>Franz Peter  Straub</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>118</td>
        <td>Johannes Georg  Thevern</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>119</td>
        <td>Johann Kaspar Ignatz Anton  Creve</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>120</td>
        <td>Jakob Adolf  Merstetter</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>121</td>
        <td>Johann Christoph  Richter</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>122</td>
        <td>Franz Joseph  Hartleben</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>123</td>
        <td>Simon Heinrich  Bagen</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>124</td>
        <td>Anton Philipp Thomas  Köhler</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>125</td>
        <td>Nikolaus Otto  Rücker</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>126</td>
        <td>Nikolaus Otto  Rucker</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>127</td>
        <td>Johannes Fritz Konrad  Wahinger</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>128</td>
        <td>Martin Simplicius  Mayer</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>129</td>
        <td>Johann Jakob  Oppenheimer</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>130</td>
        <td>Johann Georg Wilhelm  Reineck</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>131</td>
        <td>Heinrich Franz Xaver  Knodt</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>132</td>
        <td>Karl Dieter  Strack</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>133</td>
        <td>Johann Jakob  Nauheimer</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>134</td>
        <td>Georg Joseph  Wagner</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>135</td>
        <td>Lubentius Friedrich  Pfingsthorn</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>136</td>
        <td>Georg William Mulvany  Seiler</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>137</td>
        <td>Johann Hermann Joseph  Werren</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>138</td>
        <td>Friedrich Anton  Schmidt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>139</td>
        <td>Johann Valentin  Jäger</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>140</td>
        <td>Georg Wilhelm  Moll</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>141</td>
        <td>Philipp Anton Ignaz  Ruth</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>142</td>
        <td>Emanuel Theodor  Moerzer</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>143</td>
        <td>Johannes Bartholomaeus  Appelius</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>144</td>
        <td>Joseph Matthias  Rosmann</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>145</td>
        <td>Johann Peter  Bentzel</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>146</td>
        <td>Franz Georg Ignaz  Ittner</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>147</td>
        <td>Bernhard Gottfried  Reider</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>148</td>
        <td>Johannes Ignaz Joseph  Vogelmann</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>149</td>
        <td>Quirinus Adolf  von Mertz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>150</td>
        <td>Josef Franz  Wenzel</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>151</td>
        <td>Johann Christian  von Ottendal</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>152</td>
        <td>Lubertus Martin  Erbenius</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>153</td>
        <td>Georg Karl  Heilmann</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>154</td>
        <td>Johann Leonhard  Schörly</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>155</td>
        <td>Karl Veit  Weidner</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>156</td>
        <td>Jodocus Georg Wilhelm  Reis</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>157</td>
        <td>Peter Joseph  Daniels</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>158</td>
        <td>Friedrich Wilhelm  Rüding</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>159</td>
        <td>Dietrich Franz  Flachsweiler</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>160</td>
        <td>Gerhard Anton Chrysostomus  Ebersheim</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>161</td>
        <td>Kaspar Baptist  Kuhn</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>162</td>
        <td>Johann Karl  Fichard</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>163</td>
        <td>Georg Ferdinand  Honcamp</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>164</td>
        <td>Johann Friedrich  von Pfeiffer</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>165</td>
        <td>Johannes Otto  Fürderer \(genannt Kühorn\)</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>166</td>
        <td>Gottfried Ferdinand  von Buckisch und Löwenfels</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>167</td>
        <td>Georg Ludwig  Koeler</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>168</td>
        <td>Sebastian Maria Joseph Alexander  Loth</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>169</td>
        <td>Franz Philipp  von Faust</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>170</td>
        <td>Franz Anton  Rhodius</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>171</td>
        <td>Justus Jodocus  Hartlieb</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>172</td>
        <td>Johannes Otto Constantin  Berneburger</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>173</td>
        <td>Johannes Peter  Möring</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>174</td>
        <td>Johann Jakob  Lipp</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>175</td>
        <td>Gottfried Christian  Lieb</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>176</td>
        <td>Karl Anton  Schaab</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>177</td>
        <td>Anton Franz  Ittstein</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>178</td>
        <td>Johann Peter  Fried</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>179</td>
        <td>Philipp Theodor  Mohr</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>180</td>
        <td>Dietrich Heinz Walter Hans Ludwig  Gresemund d\. Ä\.</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>181</td>
        <td>Dietrich F\.  Gresemund d\. J\.</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>182</td>
        <td>Anselm Franz  Lieb d\. Ä\.</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>183</td>
        <td>Peter Ernst  Hernssheimer</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>184</td>
        <td>Johann Michael  Dahm</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>185</td>
        <td>Peter Christoph  Brahm</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>186</td>
        <td>Leonhard Otto Constantin  Nimis</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>187</td>
        <td>Johann Peter  Molstetter</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>188</td>
        <td>Lukas Otto  Arabier</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>189</td>
        <td>Johann Christoph  Riedesel von Camberg zu Nassau</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>190</td>
        <td>Georg Anna  Schlör</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>191</td>
        <td>Philipp Adam  Schultheiss</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>192</td>
        <td>Rolinus Günther  Tinctoris</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>193</td>
        <td>Adolf Georg Hugo Samuel  von Pempelfurt</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>194</td>
        <td>Adam Georg  Gotlip</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>195</td>
        <td>Albert Wilhelm  Linde</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>196</td>
        <td>Eucharius Alexander  Schlaun</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>197</td>
        <td>Franz Adolph  Vogt</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>198</td>
        <td>Georg Friedrich  Hornung</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>199</td>
        <td>Johann Christoph  Jaeger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>200</td>
        <td>Johann Joseph Hieronymus  Wink</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>201</td>
        <td>Joseph Leopold  Roth</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>202</td>
        <td>Mercurius Rudolf  Wilthelm</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>203</td>
        <td>Paul Kardinal  Volmar</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>204</td>
        <td>Johann Diether  Weidmann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>205</td>
        <td>Andreas Karl  von Joss</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>206</td>
        <td>Anselm Franz  Lieb d\. J\.</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>207</td>
        <td>Ivo Walter Wilhelm  Wittich</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>208</td>
        <td>Johann Wilhelm  Delvaux</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>209</td>
        <td>Jakob Christoph  Bourdon</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>210</td>
        <td>Damian Hartard  Dünwald</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>211</td>
        <td>Jakob Kaspar Ignatz Anton  Curio</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>212</td>
        <td>Peter Nikolaus  Viersen</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>213</td>
        <td>Nikolaus Karl Anton  Heusser</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>214</td>
        <td>Johann Franz  Gergens</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>215</td>
        <td>Johann Wilhelm Heinrich  Jäger</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>216</td>
        <td>Johannes Walther  Kühorn d\. J\.</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>217</td>
        <td>Andreas Franz  Birnbeck</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>218</td>
        <td>Jakob Hans Fritz Philipp  Campius</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>219</td>
        <td>Nikolaus Philipp  Lisignolo</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>220</td>
        <td>Johann Martin Franz  Koeler</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>221</td>
        <td>Johannes Christoph  Vogelmann</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>222</td>
        <td>Johannes Friedrich  Bertram</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>223</td>
        <td>Johann Franz  Schlaun</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>224</td>
        <td>Josef Franz Ignaz Aloys  Wenzel</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>225</td>
        <td>Nikolaus Gerhard  Finck</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>226</td>
        <td>Johann Siegfried  Faber</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>227</td>
        <td>Urban Ferdinand  Gudenus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>228</td>
        <td>Johann Anton  Caprano</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>229</td>
        <td>Jodocus William Mulvany  Selbach</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>230</td>
        <td>Melchior Adolph  Vogelmann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>231</td>
        <td>Johann Hugo  Widt</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>232</td>
        <td>Jakob Philipp Thomas  Koler</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>233</td>
        <td>Bernhard Max  Scholl</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>234</td>
        <td>Johann Christoph  von Gudenus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>235</td>
        <td>Johann Kaspar  Müller</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>236</td>
        <td>Quirinus E\.  Kunckel</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>237</td>
        <td>Nikolaus Friedrich Michael  Capito</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>238</td>
        <td>Johann Adam  Freisbach</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>239</td>
        <td>Balthasar Heinrich  Geier</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>240</td>
        <td>Nikolaus Theodor  Pauli</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>241</td>
        <td>Dietrich Friedrich  Ulsenius</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>242</td>
        <td>Michael Anna  Schleiffert</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>243</td>
        <td>Daniel Erwin Sebastian  Jaeger</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>244</td>
        <td>Karl Maria Anton  Andre</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>245</td>
        <td>Philipp Lambert  Wolf von Rosenbach</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>246</td>
        <td>Anton Erwin Sebastian  Bayer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>247</td>
        <td>Heinrich Siegfried  Faber</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>248</td>
        <td>Johannes Wendelin  Diel</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>249</td>
        <td>Johann Friedrich Michael  Capitel</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>250</td>
        <td>Justus Philipp Wilhelm  Moll</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>251</td>
        <td>Gottlieb Friedrich  Ungleich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>252</td>
        <td>Kilian Rudolf Dubslaff  Eler</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>253</td>
        <td>Franz Gottfried  Weinzürl</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>254</td>
        <td>Johann Baptist  Krick</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>255</td>
        <td>Jakob Konstantin  Welder</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>256</td>
        <td>Johannes Walther  Kühorn d\. Ä\.</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>257</td>
        <td>Karl August  Wenzel</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>258</td>
        <td>Johann Georg  Neureuther</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>259</td>
        <td>Wigand Christoph Chrysostomus  Kenniken</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>260</td>
        <td>Johannes Franz Joseph  Eseler</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>261</td>
        <td>Johann Peter  Weidmann</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>262</td>
        <td>Johann Philipp Franz  Jaeger</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>263</td>
        <td>Johannes Wolfgang  Munck</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>264</td>
        <td>Christian Franz  Ittstein</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>265</td>
        <td>Johann Christoph  Külsheimer</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>266</td>
        <td>Karl Franz  Fischer</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>267</td>
        <td>Johann Martin  Engelhardt</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>268</td>
        <td>Bernhard Gottfried  Mandel</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>269</td>
        <td>Valentin Friedrich  Molitor</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>270</td>
        <td>Ferdinand Heinrich  von Dünwald</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>271</td>
        <td>Philipp Ludwig  König</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>272</td>
        <td>Friedrich Kaspar Ignatz Anton  Cronberg</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>273</td>
        <td>Johann Martin  Hohenstatt</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>274</td>
        <td>Johannes Magnus  Baimer</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>275</td>
        <td>Johann Michael Ignaz  Ratzen</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>276</td>
        <td>Philipp Wilhelm Karl  Horcher</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>277</td>
        <td>Thomas Karl  Zenzen</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>278</td>
        <td>Anton Kardinal  Voltz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>279</td>
        <td>Anton Maria  Marchand</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>280</td>
        <td>Bartholomaeus Franz Joseph  von Ethen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>281</td>
        <td>Franz Michael  Hoepffner</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>282</td>
        <td>Franz Otto  Holthof</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>283</td>
        <td>Franz Peter  Dürr</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>284</td>
        <td>Franz Rüdiger  von Haren</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>285</td>
        <td>Georg Friedrich  Medicus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>286</td>
        <td>Johann Theodor  Moeren</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>287</td>
        <td>Johannes Ernst Alexander  Schwartzman</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>288</td>
        <td>Johannes Friedrich  Püchler</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>289</td>
        <td>Johannes Veit  Bondius</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>290</td>
        <td>Philipp Wilhelm  Bucheimer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>291</td>
        <td>Philippus Friedrich  von Schwalbach</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>292</td>
        <td>Philippus Willi Otto  Beckardus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>293</td>
        <td>Wendelinus Wilhelm  Ruf</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>294</td>
        <td>Wilhelm Jakob  Sattler</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>295</td>
        <td>Lothar Clemens Joseph Emil  Dulog</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>296</td>
        <td>Stephan Felix  Steick</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>297</td>
        <td>Florentin Otto  Holtzweiler</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>298</td>
        <td>Augustinus Peter  Berchem</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>299</td>
        <td>Georg Konrad  Breuel</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>300</td>
        <td>Sebastianus Friedrich  Plest</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>301</td>
        <td>Georg Nikolaijewitsch  Blum</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>302</td>
        <td>Martin Martin  Hohenstatt</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>303</td>
        <td>Johann Emmerich  Gries</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>304</td>
        <td>Edmund Georg Ferdinand Hans  von Hagen</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>305</td>
        <td>Johannes Heinrich  Fabri</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>306</td>
        <td>Conrad Peter  Weidmann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>307</td>
        <td>Gabriel Friedrich  Mintzenthaler</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>308</td>
        <td>Johannes Karl  Jung</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>309</td>
        <td>Johann Wolfgang  Krapff</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>310</td>
        <td>Johann Georg  Thein</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>311</td>
        <td>Johann Valentin  Knaud</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>312</td>
        <td>Anton Valentin  Knauer</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>313</td>
        <td>Michael Karl Max  Foresii</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>314</td>
        <td>Johannes Thomas  Sorbillo</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>315</td>
        <td>Christian Maria Joseph Alexander  Beinhauer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>316</td>
        <td>Johannes Anton  Carben</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>317</td>
        <td>Wilhelm Jakob  Osterrod</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>318</td>
        <td>Johannes Georg  Wonecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>319</td>
        <td>Johannes Alexander  Schilling</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>320</td>
        <td>Johann Maria Hugo  Kranebieter</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>321</td>
        <td>Johannes Walther  Kühorn</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>322</td>
        <td>Martin Karl  Bechel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>323</td>
        <td>Balthasar Philipp  Distelhusen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>324</td>
        <td>Leonhard Albertinus  de Alten</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>325</td>
        <td>Hermann Franz Dionys  Kämmerer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>326</td>
        <td>ACKER, Philipp</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>327</td>
        <td>ACKERMANN, Jakob Fidelis</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>328</td>
        <td>ADEL\(T\), Peter</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>329</td>
        <td>AGRICOLA, Christian</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>330</td>
        <td>ALICH, Werner</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>331</td>
        <td>ALTEN, Leonhard Albertinus de</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>332</td>
        <td>ALTENBERG, Johann Georg</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>333</td>
        <td>AMBACH, Melchior</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>334</td>
        <td>AMELON, Heinrich</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>335</td>
        <td>ANDLAU, Johann Ulrich von</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>336</td>
        <td>ANDRE, Karl Maria Anton</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>337</td>
        <td>ANTONI, Friedrich</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>338</td>
        <td>ANTZ, Johann Wolfgang</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>339</td>
        <td>ANTZMANN, Johann</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>340</td>
        <td>APPEL, Christian, SJ</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>341</td>
        <td>APPELIUS, Johannes Bartholomaeus</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>342</td>
        <td>ARABIER, Lukas</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>343</td>
        <td>ARAND, Karl Melchior</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>344</td>
        <td>ARETZ, Jakob</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>345</td>
        <td>ARNOLDI, Nicolaus, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>346</td>
        <td>ARTOPOEUS, Georg</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>347</td>
        <td>ARTOPOEUS, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>348</td>
        <td>ASMUT, Johann Franz</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>349</td>
        <td>AUER, Lambert, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>350</td>
        <td>BACHERELIUS , Ludwig, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>351</td>
        <td>BADERUS, Georg, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>352</td>
        <td>BAGEN, Simon</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>353</td>
        <td>BAIMER, Johannes Magnus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>354</td>
        <td>BAIUMVILLE, Wilhelm, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>355</td>
        <td>BALISTA, Lorenz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>356</td>
        <td>BANNIZA, Johann Peter Joseph, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>357</td>
        <td>BAUR, Philipp, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>358</td>
        <td>BAUSMANN, Markus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>359</td>
        <td>BAYER, Anton</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>360</td>
        <td>BAYER, Jakob, SJ</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>361</td>
        <td>BECANUS, Martin, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>362</td>
        <td>BECHEL, Martin</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>363</td>
        <td>BECHER, Johann Joachim</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>364</td>
        <td>BECKARDUS, Philippus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>365</td>
        <td>BECKER, \(Joh\.\) Leonhard</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>366</td>
        <td>BECKER, Johannes Aloysius</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>367</td>
        <td>BEERSCHMITT, Georg, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>368</td>
        <td>BEGER, Peter \(Petrus\)</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>369</td>
        <td>BEHEIM, Georg</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>370</td>
        <td>BEHLEN, Ludwig Philipp</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>371</td>
        <td>BEHRS, Philipp, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>372</td>
        <td>BEINHAUER, Christian</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>373</td>
        <td>BENCKESER, Martin, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>374</td>
        <td>BENTZEL, Balthasar, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>375</td>
        <td>BENTZEL, Franz Kuno</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>376</td>
        <td>BENTZEL, Ignaz von, SJ</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>377</td>
        <td>BENTZEL, Johann Baptist Karl Fortunat von</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>378</td>
        <td>BENTZEL, Johann Peter \(von\)</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>379</td>
        <td>BERCHEM, Augustinus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>380</td>
        <td>BERGMANN, Joseph</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>381</td>
        <td>BERINGER, Sigismund</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>382</td>
        <td>BERNEBURGER, Johannes</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>383</td>
        <td>BERTRAM, Johannes</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>384</td>
        <td>BETTINGEN, Johannes, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>385</td>
        <td>BEUSSER, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>386</td>
        <td>BEUSSER, Caspar</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>387</td>
        <td>BEUSSER, Franz Philipp</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>388</td>
        <td>BEUSSER, Johann Heinrich</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>389</td>
        <td>BIBER, Nithardus, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>390</td>
        <td>BIBER, Wolfgang, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>391</td>
        <td>BIBERUS, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>392</td>
        <td>BIEGEISEN, Johannes, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>393</td>
        <td>BIRNBECK, Andreas</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>394</td>
        <td>BLAU, Felix Anton</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>395</td>
        <td>BLEIDENSTADT, Johannes</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>396</td>
        <td>BLEY, Johannes Jodocus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>397</td>
        <td>BLÖCHINGER, Johann Bernhard</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>398</td>
        <td>BLUM, Georg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>399</td>
        <td>BODMANN, Franz Ignaz Joseph</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>400</td>
        <td>BONDIUS, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>401</td>
        <td>BOOST, Damian Friedrich</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>402</td>
        <td>BORG, Heinrich</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>403</td>
        <td>BORLER, Augustin, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>404</td>
        <td>BOSENDORFF, Hermann, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>405</td>
        <td>BOURDON, Jakob Christoph</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>406</td>
        <td>BRAHM, Peter</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>407</td>
        <td>BRAUN, Quirinus Lorenz</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>408</td>
        <td>BRAUNSCHIEDEL, Wendelin</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>409</td>
        <td>BREITHARDT, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>410</td>
        <td>BRENEISEN, Johannes, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>411</td>
        <td>BRENTANO, Joseph, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>412</td>
        <td>BREUEL, Georg</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>413</td>
        <td>BREUNIG, Conradus, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>414</td>
        <td>BROCKAEUS, Guilielmus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>415</td>
        <td>BROCKARD, Aloysius, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>416</td>
        <td>BROICH, Heinrich</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>417</td>
        <td>BRORBELL, Jeremias</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>418</td>
        <td>BROWERUS, Eberhard, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>419</td>
        <td>BRUCH, Kaspar, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>420</td>
        <td>BRUDER, Johann</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>421</td>
        <td>BRUNHEIMER, Stephan Dominikus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>422</td>
        <td>BUCHEIMER, Philipp \(Jodocus\)</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>423</td>
        <td>BÜCHELMANN, Melchior, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>424</td>
        <td>BUCKISCH und Löwenfels, Gottfried Ferdinand von</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>425</td>
        <td>BURANUS, Leonhard</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>426</td>
        <td>BURCKARD, Johann Stephan Valentin</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>427</td>
        <td>BURGER, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>428</td>
        <td>BUSAEUS, Johannes, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>429</td>
        <td>BUSZLER Urbanus, Johann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>430</td>
        <td>CAMPIUS, Dionysius</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>431</td>
        <td>CAMPIUS, Jakob</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>432</td>
        <td>CAMPIUS, Antonius Quirinus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>433</td>
        <td>CAPITEL, Johann Friedrich Michael</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>434</td>
        <td>CAPITO, Nikolaus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>435</td>
        <td>CAPRANO, Johann Anton</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>436</td>
        <td>CARBEN, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>437</td>
        <td>CELLARIUS, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>438</td>
        <td>CETTI, Joseph, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>439</td>
        <td>CHYLENUS, Martinus, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>440</td>
        <td>COCI, Kaspar</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>441</td>
        <td>COLBINUS, Philipp</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>442</td>
        <td>COLONIA, Johannes</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>443</td>
        <td>CONRADI, Adam</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>444</td>
        <td>CONTZEN, Adam, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>445</td>
        <td>CORNAEUS, Melchior, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>446</td>
        <td>CORSMICH, Heinrich, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>447</td>
        <td>CORVINUS, Arnold</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>448</td>
        <td>COSTER, Franciscus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>449</td>
        <td>CRAFFTO, Michael, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>450</td>
        <td>CRATZ, Johann Baptist \(Peter\)</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>451</td>
        <td>CREMERIUS, Johannes, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>452</td>
        <td>CREUTZNACH, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>453</td>
        <td>CREVE, Johann Kaspar Ignatz Anton</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>454</td>
        <td>CROEFF, Johannes, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>455</td>
        <td>CRONBERG, Friedrich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>456</td>
        <td>CRONENBURG, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>457</td>
        <td>CURIO, Jakob</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>458</td>
        <td>DABUTZ, Florinus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>459</td>
        <td>DAHL, Thomas</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>460</td>
        <td>DAHM, Jacob, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>461</td>
        <td>DAHM, Johann Michael</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>462</td>
        <td>DANIELS, Peter \(Philipp\) Joseph</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>463</td>
        <td>DAUDE, Adrianus, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>464</td>
        <td>DAUDE, Joseph, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>465</td>
        <td>DECIUS, Franz Peter</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>466</td>
        <td>DECIUS, Johann Rudolph Heinrich</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>467</td>
        <td>DEGENHARDT, Georg, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>468</td>
        <td>DELVAUX, Johann Wilhelm</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>469</td>
        <td>DICHTEL, Franz Christoph</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>470</td>
        <td>DICHTELBACH, Tilmann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>471</td>
        <td>DICTES, Johann \(Franz\) Wendelin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>472</td>
        <td>DIEL, Conrad</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>473</td>
        <td>DIEL, Florentin</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>474</td>
        <td>DIEL, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>475</td>
        <td>DIEMER, Johann Kaspar \(Konrad\)</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>476</td>
        <td>DIETENBERGER, Johannes</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>477</td>
        <td>DIETES, Wendelin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>478</td>
        <td>DIETRICH, Alexander</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>479</td>
        <td>DIETZ, Andreas</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>480</td>
        <td>DIETZ, Johann Valentin</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>481</td>
        <td>DIEZE, Andreas</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>482</td>
        <td>DILENIUS, Johann Baptist Joseph</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>483</td>
        <td>DIPPERT, Joseph, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>484</td>
        <td>DIROLF, Johann Philipp</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>485</td>
        <td>DISTELHUSEN, Balthasar</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>486</td>
        <td>DITTLER, Wilhelm</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>487</td>
        <td>DONUNG, Stephan, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>488</td>
        <td>DÖPPELIUS, Wilhelm</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>489</td>
        <td>DORN, Franz, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>490</td>
        <td>DORN, Ignaz, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>491</td>
        <td>DORN, Petrus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>492</td>
        <td>DORSCH, Anton Joseph</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>493</td>
        <td>DRAPP, Anton</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>494</td>
        <td>DREIS, Wilhelm, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>495</td>
        <td>DRIEL, Gottfried von</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>496</td>
        <td>DÜCKER, Heinrich, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>497</td>
        <td>DUDEN, Jakob</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>498</td>
        <td>DÜNWALD, Damian Hartard</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>499</td>
        <td>DÜNWALD, Philipp Franz</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>500</td>
        <td>DÜNWALD, Ferdinand Heinrich von</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>501</td>
        <td>DÜRKHEIMER, Nikolaus</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>502</td>
        <td>DÜRR, Franz Anton Chrysostomus</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>503</td>
        <td>EBEL, Anton \(Franz\)</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>504</td>
        <td>EBERSHEIM, Ludwig</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>505</td>
        <td>EBERSHEIM, Wilhelm</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>506</td>
        <td>EBERSHEIM, Adam</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>507</td>
        <td>EBERSHEIM, Gerhard</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>508</td>
        <td>EBERWEIN, Matthäus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>509</td>
        <td>ECKARDT, Georg \[auch Johannes Georg\), SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>510</td>
        <td>ECKART, Johann Georg Joseph von</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>511</td>
        <td>EGEL, Ambrosius, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>512</td>
        <td>EHMICH, Matthias</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>513</td>
        <td>EICKEMEYER, Johann Heinrich Rudolf</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>514</td>
        <td>EIMER, Jodocus, SJ</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>515</td>
        <td>EIMER, Ludwig, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>516</td>
        <td>ELER, Andreas</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>517</td>
        <td>ELER, Johannes</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>518</td>
        <td>ELER, Kilian</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>519</td>
        <td>EMUNTS, Johannes Thomas</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>520</td>
        <td>ENGEL, Johann Michael \[Melchior\)</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>521</td>
        <td>ENGELHARDT, Johann Martin</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>522</td>
        <td>ENGELMOHR, \(Georg\) Joseph, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>523</td>
        <td>ERBENIUS, Lubertus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>524</td>
        <td>ERBERMANN, Vitus, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>525</td>
        <td>ERBIUS, Peter, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>526</td>
        <td>ERNFELDERUS, Jacobus, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>527</td>
        <td>ERNST, Anselm Franz Joseph</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>528</td>
        <td>ESELER, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>529</td>
        <td>ETHEN, Bartholomaeus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>530</td>
        <td>ETTINGSHAUSEN, Fridericus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>531</td>
        <td>ETTINGSHAUSEN, Georg</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>532</td>
        <td>ETZELIUS, Balthasar, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>533</td>
        <td>EULER, Johannes Philipp</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>534</td>
        <td>FABER, Carolus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>535</td>
        <td>FABER, Christoph</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>536</td>
        <td>FABER, Heinrich</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>537</td>
        <td>FABER, Johann \(Jonas\)</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>538</td>
        <td>FABER, Johann Heinrich</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>539</td>
        <td>FABER, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>540</td>
        <td>FABER, Laurentius</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>541</td>
        <td>FABER, Petrus, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>542</td>
        <td>FABRI, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>543</td>
        <td>FABRITIUS, Matthias, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>544</td>
        <td>FALCKENSTEIN, Ludwig, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>545</td>
        <td>FAULHABER, Johann Adam</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>546</td>
        <td>FAUST, Franz Philipp</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>547</td>
        <td>FAUST, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>548</td>
        <td>FAUST, Reinhardus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>549</td>
        <td>FECHEMER, Gerhardus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>550</td>
        <td>FEIERABENT, Joannes, SJ</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>551</td>
        <td>FEYERTAG, Johann Magister</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>552</td>
        <td>FIBIG, Johann</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>553</td>
        <td>FICHARD, Johann Karl</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>554</td>
        <td>FIMBERGER, Nikolaus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>555</td>
        <td>FINAEUS, Jacobus, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>556</td>
        <td>FINCK, Ignatius, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>557</td>
        <td>FINCK, Nikolaus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>558</td>
        <td>FINK, Konrad</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>559</td>
        <td>FISCHER, Johann Gotthelf</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>560</td>
        <td>FISCHER, Johann Nikolaus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>561</td>
        <td>FISCHER, Karl Franz</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>562</td>
        <td>FISCHER, Nicolaus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>563</td>
        <td>FLACHSWEILER, Dietrich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>564</td>
        <td>FLACHSWEILER, Petrus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>565</td>
        <td>FLACHSWEILER, Theodor</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>566</td>
        <td>FLUCKE, Joseph, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>567</td>
        <td>FLUCKE, Lorenz, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>568</td>
        <td>FORESII, Michael</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>569</td>
        <td>FORTUNA, Jodocus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>570</td>
        <td>FRANCK, Franciscus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>571</td>
        <td>FRANCK, Georg Friedrich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>572</td>
        <td>FRANCK, Johannes Philippus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>573</td>
        <td>FRANK, Franz Philipp</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>574</td>
        <td>FRANK, Peter Anton Freiherr von</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>575</td>
        <td>FREISBACH, Johann Adam</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>576</td>
        <td>FREYSLEBEN, Johann Georg</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>577</td>
        <td>FRIDERICH, Philipp, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>578</td>
        <td>FRIDWALD, Richard</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>579</td>
        <td>FRIED, Johann Peter</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>580</td>
        <td>FRIES, Ignatius, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>581</td>
        <td>FRIES, Christophorus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>582</td>
        <td>FRITZ, Bernhard, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>583</td>
        <td>FRÖHLING, Michael, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>584</td>
        <td>FUCHS, Joseph</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>585</td>
        <td>FUCHSIUS, Johannes, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>586</td>
        <td>FUGGER von Kirchheim, Philipp Karl, Graf</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>587</td>
        <td>FULLERUS, Joannes, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>588</td>
        <td>FÜRDERER, Johannes</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>589</td>
        <td>GAAR, Johann Georg, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>590</td>
        <td>GALLADE, Peter, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>591</td>
        <td>GÄRTLER, Johannes Adamus</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>592</td>
        <td>GASSEL, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>593</td>
        <td>GEFFT, Nikolaus, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>594</td>
        <td>GEIER, Balthasar</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>595</td>
        <td>GEIGER, Friedrich, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>596</td>
        <td>GEIGER, Joseph, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>597</td>
        <td>GEISELBRUN, Joseph, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>598</td>
        <td>GELDROPIUS, Erasmus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>599</td>
        <td>GEMER, Nicolaus, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>600</td>
        <td>GEMMING, Johann Peter Joseph</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>601</td>
        <td>GERAU, Johannes von</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>602</td>
        <td>GERBEL, Nikolaus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>603</td>
        <td>GERBER, Johannes, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>604</td>
        <td>GERGENS, Johann Franz</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>605</td>
        <td>GERGENS, Peter</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>606</td>
        <td>GERMERSHAUSEN, Lorenz</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>607</td>
        <td>GERRESHEIM, Gerhard</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>608</td>
        <td>GERSENIUS, Philipp, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>609</td>
        <td>GEYER, Adam</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>610</td>
        <td>GNADT, Hermann, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>611</td>
        <td>GÖBEL, Johannes Gregorius \(Georg\)</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>612</td>
        <td>GOEHAUSEN, Samuel, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>613</td>
        <td>GOETZ, Johann Adam</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>614</td>
        <td>GOETZ, Michael, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>615</td>
        <td>GOLDHAGEN, Hermann, SJ</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>616</td>
        <td>GÖPFERT, Georg, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>617</td>
        <td>GÖPFFERT, Wilderich Christoph</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>618</td>
        <td>GOTHELP, Bertold</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>619</td>
        <td>GOTLIP, Adam</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>620</td>
        <td>GOY, Jakob</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>621</td>
        <td>GRAMBERT, Adam, SJ</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>622</td>
        <td>GREBER, Bruno, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>623</td>
        <td>GRESEMUND, Dietrich d\.Ä\.</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>624</td>
        <td>GRESEMUND, Dietrich der Jüngere</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>625</td>
        <td>GRIES, Johann Emmerich</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>626</td>
        <td>GRUTER, Lambert</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>627</td>
        <td>GUDENUS, Johann Christoph</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>628</td>
        <td>GUDENUS, Johann Christoph von</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>629</td>
        <td>GUDENUS, Urban Ferdinand</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>630</td>
        <td>GÜNTHER, Franz, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>631</td>
        <td>HAABER, Johann Friedrich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>632</td>
        <td>HAAN, Georg, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>633</td>
        <td>HAAN, Wilhelm, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>634</td>
        <td>HACK, Franz, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>635</td>
        <td>HAGEN, Matthias Joseph</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>636</td>
        <td>HAGEN, Edmund von</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>637</td>
        <td>HAGEN, Paulus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>638</td>
        <td>HAGER, Johannes Balthasar, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>639</td>
        <td>HAHN, Johann Philipp</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>640</td>
        <td>HALENIUS, Georg, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>641</td>
        <td>HALVER, Christian, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>642</td>
        <td>HANDEL, Ignaz, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>643</td>
        <td>HARDMANN, Jacobus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>644</td>
        <td>HARDY, Franz \(Theodor\), SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>645</td>
        <td>HAREN, Franz Rüdiger von</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>646</td>
        <td>HARINGS, Paul, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>647</td>
        <td>HARLASS, Georg, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>648</td>
        <td>HARTLEBEN, Franz Joseph</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>649</td>
        <td>HARTLEBEN, Theodor Konrad</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>650</td>
        <td>HARTLIEB, Justus Jodocus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>651</td>
        <td>HARTMAN, Christian, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>652</td>
        <td>HARTMANN, Johann Kaspar Anton</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>653</td>
        <td>HARTMANN, Johannes, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>654</td>
        <td>HARTUNG, Johannes, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>655</td>
        <td>HAUBENREISSER, Peter</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>656</td>
        <td>HAUCK, Christoph, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>657</td>
        <td>HAUCK, Leonhard, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>658</td>
        <td>HAUNOLD, Johann Maximilian von</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>659</td>
        <td>HAUPT, Peter</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>660</td>
        <td>HAUSEN, Conrad</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>661</td>
        <td>HAUSER, Antonius</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>662</td>
        <td>HAYL, Philipp, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>663</td>
        <td>HAYSDORFF, Adam, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>664</td>
        <td>HEBELIN von Helmbach, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>665</td>
        <td>HECK, Paul Xaveri van</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>666</td>
        <td>HECKMANN, Johann Baptist \(Wendel\), SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>667</td>
        <td>HEDIO, Caspar</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>668</td>
        <td>HEGER, Wilhelm</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>669</td>
        <td>HEIDEL, Johann Philipp, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>670</td>
        <td>HEIDEL, Wolfgang Ernst</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>671</td>
        <td>HEIDER, Balthasar, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>672</td>
        <td>HEILMANN, Georg Karl</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>673</td>
        <td>HEIM, Hugo, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>674</td>
        <td>HELDING, Michael</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>675</td>
        <td>HELFERICUS de Bobenhausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>676</td>
        <td>HELLING, Godefridus, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>677</td>
        <td>HELSINGER, Adam</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>678</td>
        <td>HENNER, Blasius, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>679</td>
        <td>HENNER, Georg, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>680</td>
        <td>HENSEL, Konrad</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>681</td>
        <td>HERDT, Alexander, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>682</td>
        <td>HERMANN, Gottfried, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>683</td>
        <td>HERNSSHEIMER, Peter</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>684</td>
        <td>HEROLD, Heinrich</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>685</td>
        <td>HERTLING, Nikolaus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>686</td>
        <td>HESSENHOVER, Johann Heinrich</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>687</td>
        <td>HETTERSDORF, Johann Michael</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>688</td>
        <td>HETTISCH, Lubentius</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>689</td>
        <td>HEUN, Quirinus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>690</td>
        <td>HEUSSER, Nikolaus Karl</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>691</td>
        <td>HEYDT, Adam, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>692</td>
        <td>HEYL, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>693</td>
        <td>HEYSESHEIM, Stephan</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>694</td>
        <td>HIEGELL, Johann Kraffto</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>695</td>
        <td>HILLMANN, Heinrich, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>696</td>
        <td>HIMJOBEN, Jacobus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>697</td>
        <td>HOBER, Hermann Joseph</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>698</td>
        <td>HOEGEL, Johann Joseph</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>699</td>
        <td>HOEMANS, Joannes \(Domelang\)</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>700</td>
        <td>HOEPFFNER, Franz Michael</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>701</td>
        <td>HOFFER, Gottfried, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>702</td>
        <td>HOFFMANN, Estherus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>703</td>
        <td>HOFFMANN, Anton</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>704</td>
        <td>HOFFMANN, Cornelius Erwin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>705</td>
        <td>HOFFMANN, Georg, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>706</td>
        <td>HOFFMANN, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>707</td>
        <td>HOFMANN, Andreas Joseph</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>708</td>
        <td>HÖGLEIN, Ambrosius, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>709</td>
        <td>HÖGLEIN, Johannes</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>710</td>
        <td>HÖGLEIN, Johannes Ambrosius</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>711</td>
        <td>HÖGLEIN, Kaspar, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>712</td>
        <td>HÖGLEIN, Valentin, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>713</td>
        <td>HOHENSTATT, Johann Martin</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>714</td>
        <td>HOHENSTATT, Martin</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>715</td>
        <td>HÖHN, Nikolaus, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>716</td>
        <td>HOLTHOF, Franz</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>717</td>
        <td>HOLTMANN, Gerhard</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>718</td>
        <td>HOLTMANN, Nikolaus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>719</td>
        <td>HOLTMANN, Wilhelm</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>720</td>
        <td>HOLTZGREVEN, Heinrich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>721</td>
        <td>HOLTZKLAU, Thomas, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>722</td>
        <td>HOLTZMANN, Friedrich, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>723</td>
        <td>HOLTZWEILER, Florentin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>724</td>
        <td>HOLZERUS, Leonhard, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>725</td>
        <td>HOLZHEUSER, Joannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>726</td>
        <td>HONCAMP, Georg Ferdinand</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>727</td>
        <td>HÖNICKE, Mathias, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>728</td>
        <td>HOOF, Johann Georg \(August\)</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>729</td>
        <td>HOPFF, Kaspar, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>730</td>
        <td>HORBELT, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>731</td>
        <td>HORCHER, Philipp</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>732</td>
        <td>HORION, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>733</td>
        <td>HORIX, Johann Baptist</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>734</td>
        <td>HORNIG, Joseph, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>735</td>
        <td>HÖRNIGK, Ludwig von</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>736</td>
        <td>HORODAM, Sebastian Franz</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>737</td>
        <td>HUBEN, Franz, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>738</td>
        <td>HUFFNAGEL, Theodor, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>739</td>
        <td>HUTTICH, Johannes</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>740</td>
        <td>INDANUS, Gordianus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>741</td>
        <td>INGENHEIMER, Georg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>742</td>
        <td>INTZ, Nicolaus, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>743</td>
        <td>ISENBIEL, Lorenz</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>744</td>
        <td>ISING, Gerhard</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>745</td>
        <td>ISING, Gerhard d\.J\.</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>746</td>
        <td>ISING, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>747</td>
        <td>ITTNER, Franz Georg Ignaz</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>748</td>
        <td>ITTSTEIN, Anton Franz</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>749</td>
        <td>ITTSTEIN, Christian Franz</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>750</td>
        <td>ITZSTEIN, Franz Erwin Sebastian</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>751</td>
        <td>ITZSTEIN, Anton Franz</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>752</td>
        <td>ITZSTEIN, Faustinus, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>753</td>
        <td>ITZSTEIN, Wilhelm, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>754</td>
        <td>JACOBI, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>755</td>
        <td>JAEGER, Daniel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>756</td>
        <td>JAEGER, Johann Christoph</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>757</td>
        <td>JAEGER, Johann Philipp Franz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>758</td>
        <td>JÄGER, Johann Valentin</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>759</td>
        <td>JÄGER, Johann Wilhelm Heinrich</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>760</td>
        <td>JANSON, Johannes Daniel</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>761</td>
        <td>JENNI, Franz, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>762</td>
        <td>JODOCUS von Gelnhausen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>763</td>
        <td>JORDAN, Ambrosius</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>764</td>
        <td>JOSS, Andreas von</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>765</td>
        <td>Judden, Johann von</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>766</td>
        <td>JUNG, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>767</td>
        <td>JUNG, Johannes, SJ</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>768</td>
        <td>JUNG, Simon</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>769</td>
        <td>KARBACH, Nikolaus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>770</td>
        <td>KAUFF, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>771</td>
        <td>KAUFF, Dietrich</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>772</td>
        <td>KAUPERS, Heinrich Matthias</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>773</td>
        <td>KAUTH, Adam Franz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>774</td>
        <td>KEIM, Jakob</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>775</td>
        <td>KELLER, Johann Christoph Chrysostomus von</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>776</td>
        <td>KENNICKEN, Konrad</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>777</td>
        <td>KENNIKEN, Wigand</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>778</td>
        <td>KERBECKIUS, Antonius</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>779</td>
        <td>KESSE, Heinrich</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>780</td>
        <td>KILBER, Heinrich, SJ</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>781</td>
        <td>KIRCHNER, Melchior, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>782</td>
        <td>KIRN, Christoph, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>783</td>
        <td>KIRSINGER, Wilhelm, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>784</td>
        <td>KISELIUS, Philipp, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>785</td>
        <td>KLEINER, Joseph, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>786</td>
        <td>KLUNCKHART, Anton</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>787</td>
        <td>KNAUD, Johann Valentin</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>788</td>
        <td>KNAUER, Anton</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>789</td>
        <td>KNODT, Heinrich</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>790</td>
        <td>KOCH, Jakob</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>791</td>
        <td>KOCH, Johann Daniel</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>792</td>
        <td>KOCH, Johann Friedrich</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>793</td>
        <td>KOCKANSKI, Adam, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>794</td>
        <td>KOELER, Johann Martin Franz</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>795</td>
        <td>KOELER, Georg Ludwig</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>796</td>
        <td>KOELSCH, Karl Joseph</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>797</td>
        <td>KÖHLER, Andreas</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>798</td>
        <td>KÖHLER, Anton Philipp Thomas</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>799</td>
        <td>KÖHLER, Johann Stephan \(Gregorius\)</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>800</td>
        <td>KOLB, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>801</td>
        <td>KOLER, Jakob</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>802</td>
        <td>KOLLIGS, Johann Philipp</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>803</td>
        <td>KOLTZ, Philipp</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>804</td>
        <td>KÖNIG, Philipp Ludwig</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>805</td>
        <td>KONRAD, Peter</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>806</td>
        <td>KRANEBIETER, Johann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>807</td>
        <td>KRAPFF, Johann Wolfgang</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>808</td>
        <td>KRAUSS, Johann Konrad</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>809</td>
        <td>KREBS, Heinrich, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>810</td>
        <td>KREBS, Johann Adam</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>811</td>
        <td>KREICH, Lorenz</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>812</td>
        <td>KRESS, Michael, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>813</td>
        <td>KREUSSLER, Johann Martin Ignaz, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>814</td>
        <td>KRICK, Johann Baptist</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>815</td>
        <td>KUHN, Kaspar</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>816</td>
        <td>KUHN, Andreas, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>817</td>
        <td>KÜHORN, Jakob Walther V</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>818</td>
        <td>KÜHORN, Bernhard</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>819</td>
        <td>KÜHORN, Johannes d\.Ä\.</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>820</td>
        <td>KÜHORN, Johannes d\.J\.</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>821</td>
        <td>KÜHORN, Johannes, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>822</td>
        <td>KÜLSHEIMER, Johann Christoph</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>823</td>
        <td>KUMMET, Caspar, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>824</td>
        <td>KUNCKEL, Quirinus</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>825</td>
        <td>KUNIGSTEIN, Johann von</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>826</td>
        <td>KÜNNEN, Heinrich</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>827</td>
        <td>KUPPEL, Martin</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>828</td>
        <td>KYSLER, Heinrich</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>829</td>
        <td>LACK, Damian</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>830</td>
        <td>LADRONE, Konrad</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>831</td>
        <td>LAMBERTI, Gerhard</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>832</td>
        <td>LANDVOGT, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>833</td>
        <td>LANGEN, Friedrich Lorenz Theodor</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>834</td>
        <td>LANGEN, Johannes Wilhelm</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>835</td>
        <td>LANGMESSER, Cuno, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>836</td>
        <td>LANKLOTZ, Heinrich</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>837</td>
        <td>LAPICIDA, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>838</td>
        <td>LARES, Nicolaus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>839</td>
        <td>LASSER, Johann Friedrich von</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>840</td>
        <td>LASSER, Johannes Jacobus von</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>841</td>
        <td>LATOMUS, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>842</td>
        <td>LAUTENBACH, \(Johannes\) Christophorus</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>843</td>
        <td>LAUTERBACH, Ambrosius</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>844</td>
        <td>LEBERG, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>845</td>
        <td>LEIMGRÜBER, Georg, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>846</td>
        <td>LEISS, Heinrich, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>847</td>
        <td>LENNEP, Adolph, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>848</td>
        <td>LENNEP, Johannes Theodor, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>849</td>
        <td>LEO, Johannes, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>850</td>
        <td>LEYDIG, Peter Joseph</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>851</td>
        <td>LIEB, Anselm Franz d\.J\.</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>852</td>
        <td>LIEB, Anselm Franz, d\.Ä\.</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>853</td>
        <td>LIEB, Gottfried Christian</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>854</td>
        <td>LIEBRECHT, Christian, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>855</td>
        <td>LIMMER, Christoph, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>856</td>
        <td>LINCKENHELD, \(Franz\) Kaspar</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>857</td>
        <td>LINDE, Albert Wilhelm</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>858</td>
        <td>LINDLA, Christoph \(Christian\)</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>859</td>
        <td>LINN, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>860</td>
        <td>LINTZ, Valentin, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>861</td>
        <td>LIPP, Johann Jakob</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>862</td>
        <td>LISIGNOLO, Nikolaus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>863</td>
        <td>LOBBETIUS, Lambertus, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>864</td>
        <td>LÖFFLER, Johann Friedrich</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>865</td>
        <td>LOHNMÜLLER, Andreas, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>866</td>
        <td>LÖHR, Johann Adam</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>867</td>
        <td>LOOS, Cornelius \(Callidius\)</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>868</td>
        <td>LOPPER, Peter, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>869</td>
        <td>LOSSMANN, Georg, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>870</td>
        <td>LOTH, Sebastian</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>871</td>
        <td>LUCA, Carl Joseph</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>872</td>
        <td>LUCIENBERGIUS, Johann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>873</td>
        <td>LUDOLPH, Hieronymus \(von\)</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>874</td>
        <td>LUDWIG, Andreas</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>875</td>
        <td>LUDWIG, Martin, SJ</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>876</td>
        <td>LUERS, Valentin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>877</td>
        <td>LUTZ, Adam</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>878</td>
        <td>LUTZ, Bartholomaeus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>879</td>
        <td>LUTZ, Nicolaus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>880</td>
        <td>MAHS, Konrad</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>881</td>
        <td>MAIER, Andreas</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>882</td>
        <td>MANDEL, Bernhard Gottfried</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>883</td>
        <td>MANDT, Damianus, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>884</td>
        <td>MANGOLT, Josef, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>885</td>
        <td>MANTZ, Joseph Thomas</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>886</td>
        <td>MARCELLI, Henricus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>887</td>
        <td>MARCHAND, Anton Maria</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>888</td>
        <td>MARTINI, Augustinus</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>889</td>
        <td>MASION, Tossanus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>890</td>
        <td>MASSET, Konrad, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>891</td>
        <td>MAURER, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>892</td>
        <td>MAYER, Martin Simplicius</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>893</td>
        <td>MEDER, Hieronymus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>894</td>
        <td>MEDICUS, Georg Friedrich</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>895</td>
        <td>MEGELE, Franz Ulrich</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>896</td>
        <td>MENSHENGEN, Heinrich, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>897</td>
        <td>MENSHENGEN, Johannes Petrus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>898</td>
        <td>MENZINGER, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>899</td>
        <td>MERCURIANUS, Johannes, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>900</td>
        <td>MERGENTHEIM, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>901</td>
        <td>MERGET, Georg Adam</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>902</td>
        <td>MERSTETTER, Jakob</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>903</td>
        <td>MERTZ, Quirinus von</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>904</td>
        <td>METTERNICH, Anton Franz</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>905</td>
        <td>METTERNICH, Mathias</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>906</td>
        <td>MICHAEL, Johann Friedrich</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>907</td>
        <td>MICHAEL, Petrus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>908</td>
        <td>MILETUS, Vitus</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>909</td>
        <td>MINSINGEN, Albert von</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>910</td>
        <td>MINTZENTHALER \(Münzenthaler\), Gabriel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>911</td>
        <td>MOCKEL, Ignatz, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>912</td>
        <td>MOECKEL, Peter Paul</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>913</td>
        <td>MOELLER, Johann Conrad</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>914</td>
        <td>MOEREN, Johann Theodor</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>915</td>
        <td>MOERZER, Johann Reinhard</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>916</td>
        <td>MOERZER, Emanuel</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>917</td>
        <td>MOHR, Etherius</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>918</td>
        <td>MOHR, Philipp</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>919</td>
        <td>MOLITOR, Bartholomaeus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>920</td>
        <td>MOLITOR, Kaspar, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>921</td>
        <td>MOLITOR, Martin, SJ</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>922</td>
        <td>MOLITOR, Nikolaus Karl</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>923</td>
        <td>MOLITOR, Valentin Friedrich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>924</td>
        <td>MOLITORIS, Tobias Robert</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>925</td>
        <td>MOLL, Friedrich Rudolf</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>926</td>
        <td>MOLL, Georg Wilhelm</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>927</td>
        <td>MOLL, Justus Philipp</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>928</td>
        <td>MOLSTETTER, Johann Peter</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>929</td>
        <td>MONBROT, Henricus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>930</td>
        <td>MONTFORT, Cornelius</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>931</td>
        <td>MÖRING, Johannes</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>932</td>
        <td>MÖRZER d\.J\., Johann Reinhard</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>933</td>
        <td>MOSER, Joseph Nikolaus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>934</td>
        <td>MOYNHARDT, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>935</td>
        <td>SPITZNAES, Johannes, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>936</td>
        <td>MÜLLENKAMPF, Franz Damian Friedrich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>937</td>
        <td>MÜLLER, Johann Caspar</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>938</td>
        <td>MÜLLER, Johann Heinrich</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>939</td>
        <td>MÜLLER, Johann Kaspar</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>940</td>
        <td>MUNCK, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>941</td>
        <td>MURMAN, Gerhard, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>942</td>
        <td>MUSERUS, Petrus, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>943</td>
        <td>NAU, Bernhard Sebastian</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>944</td>
        <td>NAUHEIMER, Johann Jakob</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>945</td>
        <td>NAUHEIMER, Kilian, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>946</td>
        <td>NAUMANN, Georg</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>947</td>
        <td>GRAU, Friedrich</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>948</td>
        <td>NEBEL, Anton, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>949</td>
        <td>NEBEL, Christoph</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>950</td>
        <td>NEBEL, Constantin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>951</td>
        <td>TODT, Konrad</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>952</td>
        <td>NEEB, Johannes</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>953</td>
        <td>NELLING, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>954</td>
        <td>NEUF, Franz, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>955</td>
        <td>NEUREUTHER, Johann Georg</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>956</td>
        <td>NEUSESSER, Johann Ernst</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>957</td>
        <td>NEW, Rudolf, SJ</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>958</td>
        <td>NEW, Richard</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>959</td>
        <td>NICKENICH, Martin</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>960</td>
        <td>NICOLEOS, Melchior, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>961</td>
        <td>NIMIS, Johann Georg \(Norbert\)</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>962</td>
        <td>NIMIS, Leonhard</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>963</td>
        <td>NÖTHIG, Nikolaus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>964</td>
        <td>NYDAENUS, Adam, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>965</td>
        <td>OFFENDAL, Peter</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>966</td>
        <td>OLONIUS, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>967</td>
        <td>OPFERMANN, Paul, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>968</td>
        <td>OPFFERMANN, Lukas, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>969</td>
        <td>OPPENHEIMER, Johann Jakob</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>970</td>
        <td>ORTLIEB, Hermann</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>971</td>
        <td>OSTERMANN, Peter</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>972</td>
        <td>OSTERROD, Wilhelm</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>973</td>
        <td>OTTENDAL, Johann Christian von</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>974</td>
        <td>OTTONIS, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>975</td>
        <td>PAULI, Nikolaus Theodor</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>976</td>
        <td>PEETZ, Raymund</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>977</td>
        <td>PEEZ, Raymundus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>978</td>
        <td>PEMPELFURT, Adolf von</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>979</td>
        <td>PESTEL, Georg Philipp Adam</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>980</td>
        <td>PETTMESSER, Ignaz \(Franz\), SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>981</td>
        <td>PFAFF, Johannes</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>982</td>
        <td>PFEFFER, Heinrich, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>983</td>
        <td>PFEFFER, Johann Adam</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>984</td>
        <td>PFEIFFER, Johann Friedrich von</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>985</td>
        <td>PFINGSTHORN, Lubentius</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>986</td>
        <td>PFRIEMB, Joseph, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>987</td>
        <td>PIERRE, Jean Claude</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>988</td>
        <td>PISTORIUS, Henricus de Stollberg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>989</td>
        <td>PISTORIUS, Philipp Anton</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>990</td>
        <td>PLEST, Sebastianus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>991</td>
        <td>PLETZ, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>992</td>
        <td>PLONIUS, Johann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>993</td>
        <td>PORTIUS, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>994</td>
        <td>POTH, Georg, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>995</td>
        <td>POTTU, Nikolaus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>996</td>
        <td>PREIS, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>997</td>
        <td>PREUSS, Peter</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>998</td>
        <td>PÜCHLER, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>999</td>
        <td>PUTZ, Albert vom</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1000</td>
        <td>QUATTERMART, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1001</td>
        <td>QUIRINI, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1002</td>
        <td>RAK, Johannes</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>1003</td>
        <td>RANG, Kaspar, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1004</td>
        <td>RAPEDIUS, Franz, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1005</td>
        <td>RAPP, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1006</td>
        <td>RATH, Martin</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1007</td>
        <td>RATH, Franciscus, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1008</td>
        <td>RATZEN, Johann Michael Ignaz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1009</td>
        <td>RAUCH, Petrus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1010</td>
        <td>RAVENNAS, Petrus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1011</td>
        <td>REDLINGIUS, Johannes, SJ</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1012</td>
        <td>REFFEY, Henricus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1013</td>
        <td>REICHARD, Kaspar, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1014</td>
        <td>REIDER, Bernhard Gottfried</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1015</td>
        <td>REIDER, Georg Adam</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1016</td>
        <td>REINECK, Johann Georg Wilhelm</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1017</td>
        <td>REINHARD, Konstantin</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1018</td>
        <td>REINHARD, Johann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1019</td>
        <td>REIS, Jodocus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1020</td>
        <td>REITZ, Nikolaus, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1021</td>
        <td>REMIGIUS</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1022</td>
        <td>RENARD, Johannes Claudius</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1023</td>
        <td>REUSS, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1024</td>
        <td>REUTER, Jakob</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1025</td>
        <td>RHODIUS, Franz Anton</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1026</td>
        <td>RICHARDUS, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1027</td>
        <td>RICHER</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1028</td>
        <td>RICHTER, Johann Christoph</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1029</td>
        <td>RICHTERGIN, Lambert</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1030</td>
        <td>RICKER, Gerhard</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1031</td>
        <td>RIEDESEL, Johann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1032</td>
        <td>RIEDNER, Johann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1033</td>
        <td>RIES, Johann Daniel Christoph, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1034</td>
        <td>RIMAEUS, Nicolaus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1035</td>
        <td>RISSE, Johannes, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1036</td>
        <td>RITTER, Michael</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1037</td>
        <td>ROBERT, Urban, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1038</td>
        <td>ROBERTI, Jacobus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1039</td>
        <td>ROBERTI, Johann, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1040</td>
        <td>RODE, Nikolaus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1041</td>
        <td>ROEDER, Bartholomäus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1042</td>
        <td>ROESTIUS, Petrus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1043</td>
        <td>ROLANDI, Johannes</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1044</td>
        <td>ROOS, Godefridus, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1045</td>
        <td>ROSENCRANTZ, Georg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1046</td>
        <td>ROSMANN, Joseph Matthias</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1047</td>
        <td>ROTH, Johann Richard von</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1048</td>
        <td>ROTH, Johann Wendelin</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1049</td>
        <td>ROTH, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1050</td>
        <td>ROTH, Joseph Leopold</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1051</td>
        <td>ROTHENHAN, Marquard, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1052</td>
        <td>RUCKER, Nikolaus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1053</td>
        <td>RÜDEL, Andreas, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1054</td>
        <td>RÜDING, Friedrich Wilhelm</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1055</td>
        <td>RUF, Wendelinus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1056</td>
        <td>RUFFERT, Michael, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1057</td>
        <td>RUFSTEIN, Melchior</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1058</td>
        <td>RÜGER, Georg, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1059</td>
        <td>RUIDIUS, Stephanus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1060</td>
        <td>RUSCHER, Thomas</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1061</td>
        <td>RUTH, Philipp Anton Ignaz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1062</td>
        <td>SAMHABER, Alexander</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1063</td>
        <td>SANDÄUS, Maximilian, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1064</td>
        <td>SANDHOLZER, Friedrich</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1065</td>
        <td>SARTORIUS, Georg Jakob</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1066</td>
        <td>SARTORIUS, Eucharius, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1067</td>
        <td>SARTORIUS, Konrad, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1068</td>
        <td>SARTORIUS, Valerandus, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1069</td>
        <td>SATOR, Georg Friedrich</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1070</td>
        <td>SATTELBERGER, Heinrich, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1071</td>
        <td>SATTLER, Wilhelm</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1072</td>
        <td>SAUR, Georg, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1073</td>
        <td>SCH‚TZ, Jakob, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1074</td>
        <td>SCHAAB, Karl Anton</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1075</td>
        <td>SCHADE, Sebastian</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1076</td>
        <td>SCHÄFER, Johann Nepomuk, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1077</td>
        <td>SCHALCK, Adamus, SJ</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1078</td>
        <td>SCHALL, Friedrich Franz</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1079</td>
        <td>SCHATZ, Johannes, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1080</td>
        <td>SCHEIDEL, Franz Christoph</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1081</td>
        <td>SCHELL, Amandus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1082</td>
        <td>SCHERER, Heinrich, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1083</td>
        <td>SCHEUBEL, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1084</td>
        <td>SCHEUICHAVIUS, Gisbert, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1085</td>
        <td>SCHIFFELER, Petrus, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1086</td>
        <td>SCHILLING, Johannes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1087</td>
        <td>SCHILLINGIUS, Michael, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1088</td>
        <td>SCHLARP, Johann</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1089</td>
        <td>SCHLAUN, Eucharius Dr\. jur\.</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1090</td>
        <td>SCHLAUN, Johann Franz</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1091</td>
        <td>SCHLEENSTEIN, Georg Adam</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1092</td>
        <td>SCHLEICHEL, Johannes, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1093</td>
        <td>SCHLEIFFERT, Michael</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1094</td>
        <td>SCHLÖR, Georg</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1095</td>
        <td>SCHLOSSBERG, Gottfried, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1096</td>
        <td>SCHLOSSER, Petrus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1097</td>
        <td>SCHMELTZING, Georg, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1098</td>
        <td>SCHMIDT \(Schmitt\), Johann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1099</td>
        <td>SCHMIDT, Christoph, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1100</td>
        <td>SCHMIDT, Friedrich Anton</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1101</td>
        <td>SCHMIDT, Georg Christoph</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1102</td>
        <td>SCHMIDT, Maximilian, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1103</td>
        <td>SCHMITT, Georg Konrad</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1104</td>
        <td>SCHMITT, Franz Jakob</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1105</td>
        <td>SCHMITT, Johannes</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1106</td>
        <td>SCHMITT, Philipp</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1107</td>
        <td>SCHÖFFERLIN, Bernhard</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1108</td>
        <td>SCHOLL, Bernhard</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1109</td>
        <td>SCHOMATZ, Peter, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1110</td>
        <td>SCHÖNHUBER, Johann Josef</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1111</td>
        <td>SCHÖNMAN, Markus, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1112</td>
        <td>SCHÖRLY, Johann Leonhard</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1113</td>
        <td>SCHRAUB, Georg</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1114</td>
        <td>SCHULTHEISS, Philipp Adam</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1115</td>
        <td>SCHULTHEISS, Johannes Benedikt</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1116</td>
        <td>SCHUNCK, Johann Peter</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>1117</td>
        <td>SCHUSTER, Friedrich, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1118</td>
        <td>SCHWAAN, Peter, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1119</td>
        <td>SCHWALBACH, Peter</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1120</td>
        <td>SCHWALBACH, Philippus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1121</td>
        <td>SCHWAN, Wolfgang, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1122</td>
        <td>SCHWARTZMANN, Johannes</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1123</td>
        <td>SCHWARZ, Franz, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1124</td>
        <td>SCHWEICKARD, Johann Gottfried</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1125</td>
        <td>SCHWEICKARDT, Kaspar</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1126</td>
        <td>SCHWIND, Christian</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1127</td>
        <td>SCHWIND, Jakob Anton</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1128</td>
        <td>SCRIPTORIS, Johannes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1129</td>
        <td>SEIBAEUS, Ambrosius</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1130</td>
        <td>SEIDEL, Veit, Benediktiner</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1131</td>
        <td>SEILER, Georg</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1132</td>
        <td>SEITZ, Ignaz, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1133</td>
        <td>SELBACH, Jodocus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1134</td>
        <td>SERARIUS, Nikolaus, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1135</td>
        <td>SERARIUS, Petrus, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1136</td>
        <td>SEUBERT, Joseph \(Anton\)</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1137</td>
        <td>SINZEL, Johann Nikolaus</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1138</td>
        <td>SOEHNCHEN, Peter</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1139</td>
        <td>SOMMER, Conrad</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1140</td>
        <td>SÖMMERING, Samuel Thomas</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>1141</td>
        <td>SORBILLO, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1142</td>
        <td>SPECHT, Georg, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1143</td>
        <td>SPEHR, Peter</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1144</td>
        <td>SPETH, Wolfgang, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1145</td>
        <td>SPIES, Valentin</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1146</td>
        <td>SPOOR, Franz Karl</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1147</td>
        <td>SPRINGINCLEE, Peter</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1148</td>
        <td>STARCK, Matthias</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1149</td>
        <td>STEGMANN, Sebastian</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1150</td>
        <td>STEICK \(Streick\), Stephan</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1151</td>
        <td>STEINBACH, Johannes, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1152</td>
        <td>STEINHAUSER, Johannes Michael</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1153</td>
        <td>STEINHÄUSER, Joseph, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1154</td>
        <td>STEINMETZ, Johann Jakob</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1155</td>
        <td>STEPECK, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1156</td>
        <td>STEPHANI, Philipp, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1157</td>
        <td>STODTBROICH, Bernardus, SJ</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1158</td>
        <td>STOLTZ, Heinrich</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1159</td>
        <td>STRACK, Karl</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1160</td>
        <td>STRAUB, Franz Peter</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1161</td>
        <td>STRAUB, Georg, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1162</td>
        <td>STRAUSS, Johann Valentin</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1163</td>
        <td>STRAUSS, Georg Adam, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1164</td>
        <td>STREUN, Johannes, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1165</td>
        <td>STREVESDORFF von, Walther Heinrich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1166</td>
        <td>STROBEL, Peter, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1167</td>
        <td>STUMPF, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1168</td>
        <td>STUMPFF, Anselm Kasimir</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1169</td>
        <td>STURATH, Johannes, SJ</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1170</td>
        <td>SULZER, Heinrich</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1171</td>
        <td>SUSSMANN, Adam, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1172</td>
        <td>SYLVIUS, Theobald</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1173</td>
        <td>SYLVIUS, van den Bossche, Petrus, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1174</td>
        <td>THAMER, Theobald</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1175</td>
        <td>THEIN, Johann Georg</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1176</td>
        <td>THEVERN, Johannes</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1177</td>
        <td>THORWESTEN, Joseph, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1178</td>
        <td>THOSSANUS, Johannes, SJ</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1179</td>
        <td>THYRAEUS, Hermann, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1180</td>
        <td>THYRAEUS, Petrus, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1181</td>
        <td>THYRI, Friedrich Franz</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1182</td>
        <td>TINCTORIS, Rolinus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1183</td>
        <td>TRAUPEL, Johannes</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1184</td>
        <td>TRAVELMANN, Johann Friedrich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1185</td>
        <td>TRENTEL, Franz, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1186</td>
        <td>TURNICH, Heinrich</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1187</td>
        <td>UGELHEIMER, Johannes</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1188</td>
        <td>ULSENIUS, Dietrich \(Theoderich\)</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1189</td>
        <td>ULTSCH, Karl, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1190</td>
        <td>UNCKEL, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1191</td>
        <td>UNGLEICH, Gottlieb</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1192</td>
        <td>UNKRAUT, Petrus Nikolaus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1193</td>
        <td>VAETH, Georg, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1194</td>
        <td>VAGTZ, Johannes</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1195</td>
        <td>VECTORIS, Diether</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1196</td>
        <td>VIERSEN, Peter</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1197</td>
        <td>VILHAUER, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1198</td>
        <td>VINCK, Antonius, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1199</td>
        <td>VINCKE, Friedrich, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1200</td>
        <td>VOGEL, Ignatius, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1201</td>
        <td>VOGELMANN, Heinrich</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1202</td>
        <td>VOGELMANN, Johannes</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>1203</td>
        <td>VOGELMANN, Johannes Christoph</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1204</td>
        <td>VOGELMANN, Melchior Adolph</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1205</td>
        <td>VOGT, Anton, SJ</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>1206</td>
        <td>VOGT, Franz</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1207</td>
        <td>VOGT, Johann Heinrich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1208</td>
        <td>VOGT, Josef Theobald</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1209</td>
        <td>VOGT, Konrad</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1210</td>
        <td>VOGT, Nikolaus \(Niklas\)</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1211</td>
        <td>VOIT, Edmund, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1212</td>
        <td>VÖLCKER, Johann Jacob</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1213</td>
        <td>VOLMAR, Paul</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1214</td>
        <td>VOLMARUS, Heinrich</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1215</td>
        <td>VOLTZ, Anton \(Johannes\)</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1216</td>
        <td>VOLUSIUS, Adolf Gottfried</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1217</td>
        <td>VOMELIUS, Cyprian</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1218</td>
        <td>VONHOFF, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1219</td>
        <td>VOSBACH, Jacob</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1220</td>
        <td>VOSS, Heinrich</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1221</td>
        <td>VOSS, Michael</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1222</td>
        <td>WACKER, Johann</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1223</td>
        <td>WAGENHAUSEN, Johannes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1224</td>
        <td>WAGNER, Georg Joseph</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1225</td>
        <td>WAGNER, Pancratius</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1226</td>
        <td>WAHINGER, Johannes</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1227</td>
        <td>WALDMANN, Andreas</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1228</td>
        <td>WALDMANN, Philipp</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1229</td>
        <td>WALLENDORF, Johannes Joseph</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1230</td>
        <td>WALLRAFF, Arnoldus, SJ</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1231</td>
        <td>WANZOUL, Remigius, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1232</td>
        <td>WASMUTH, Johann Wendlin</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1233</td>
        <td>WASMUTH, Johann Heinrich</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1234</td>
        <td>WEBER, Christoph</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1235</td>
        <td>WEBER, Stephan</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>1236</td>
        <td>WEBER, Theodor, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1237</td>
        <td>WEDEKIND, Georg Christian Gottlieb Theophil</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1238</td>
        <td>WEDEKIND, Liborius, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1239</td>
        <td>WEIDMANN, Conrad</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1240</td>
        <td>WEIDMANN, Johann Diether</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1241</td>
        <td>WEIDMANN, Johann Peter</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>1242</td>
        <td>WEIDNER, Karl Veit</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1243</td>
        <td>WEIL, Bertulph</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1244</td>
        <td>WEILER, Heinrich, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1245</td>
        <td>WEINZ‚RL, Franz Gottfried</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1246</td>
        <td>WEISS, Adam</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1247</td>
        <td>WELDEN, Ludwig Konstantin</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1248</td>
        <td>WELDER, Jakob</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1249</td>
        <td>WENZEL, Josef Franz</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1250</td>
        <td>WENZEL, Josef Franz Ignaz Aloys</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1251</td>
        <td>WENZEL, Karl August</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1252</td>
        <td>WERLEIN, Wilhelm, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1253</td>
        <td>WERNER, Joseph, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1254</td>
        <td>WERREN, Johann Hermann Joseph</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1255</td>
        <td>WESTENBERGER, Heinrich, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1256</td>
        <td>WESTHAUSEN, Kaspar von</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1257</td>
        <td>WESTHOFEN, Georg Joseph</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1258</td>
        <td>WESTHOFEN, Karl Joseph</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1259</td>
        <td>WICK, Conradus, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1260</td>
        <td>WIDT, Johann Hugo</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1261</td>
        <td>WIEDENBRUCK, Wilhelm Theodor</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1262</td>
        <td>WIESE, Christoph Ignaz</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1263</td>
        <td>WIGAND, Andreas, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1264</td>
        <td>WILD, Augustinus, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1265</td>
        <td>WILL, Johann Rudolf</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1266</td>
        <td>WILL, Johannes, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1267</td>
        <td>WILTHELM, Lorenz</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1268</td>
        <td>WILTHELM, Mercurius</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1269</td>
        <td>WINAEUS, Petrus, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1270</td>
        <td>WINDISCHMANN, Karl Joseph Hieronymus</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1271</td>
        <td>WINK, Johann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1272</td>
        <td>WITTICH, Ivo</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>1273</td>
        <td>WITTMANN, Franz Joseph</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1274</td>
        <td>WITTMANN, Johannes Leonhard</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1275</td>
        <td>WOGER, Franz Valentin</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1276</td>
        <td>WOLF von Rosenbach, Philipp</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1277</td>
        <td>WOLFF, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1278</td>
        <td>WOLFF, Adam, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1279</td>
        <td>WOLFF, Balthasar, SJ</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1280</td>
        <td>WOLFF, Franz Philipp</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1281</td>
        <td>WOLLENBERGER, Christophorus, SJ</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1282</td>
        <td>WONECKER, Johannes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1283</td>
        <td>WUNDERLICH, Friedrich, SJ</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1284</td>
        <td>WUNDERLICH, Johann Michael</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1285</td>
        <td>WÜRDTWEIN, Maximilian</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1286</td>
        <td>WÜSTEFLED, Johann Friedrich</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1287</td>
        <td>ZEDER, Georg, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1288</td>
        <td>ZEHENDER, Bartholomäus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1289</td>
        <td>ZENZEN, Thomas</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1290</td>
        <td>ZIEGLER, Johannes Reinhard, SJ</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1291</td>
        <td>ZIEGLER, Jakob</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1292</td>
        <td>ZILLIG, Nikolaus, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1293</td>
        <td>ZIMMERMANN, Philipp</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1294</td>
        <td>ZINCK, Ignaz, SJ</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>1295</td>
        <td>ZINCK, Ludwig, SJ</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1296</td>
        <td>ZINCK, Wilderich, SJ</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1297</td>
        <td>ZINNER, Philipp, SJ</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1298</td>
        <td>ZIRCK, Michael, SJ</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1299</td>
        <td>ZOLLER, Georg, SJ</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1300</td>
        <td>ZULEHNER, \(Johannes\) Anton</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1301</td>
        <td>ZWEIFFEL, \(Johannes\) Jakob, SJ</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1302</td>
        <td>Johann Franz Aegidius \(Egid\) \(von\) BEAURIEUX \(zu SCHÖNBACH\)</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>1303</td>
        <td>Johann Georg NEUREUTER</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1304</td>
        <td>Johann Christoph SPITZ</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>1305</td>
        <td>Franz Wilhelm LOSKAND</td>
        <td>23</td>
    </tr>
    <tr class="hidden-row">
        <td>1306</td>
        <td>Ignaz Friedrich Maria Joseph Anton Apollinaris Canutus \(Freiherr von\) GRUBEN</td>
        <td>53</td>
    </tr>
    <tr class="hidden-row">
        <td>1307</td>
        <td>Franz Joseph Ignaz \(Freiherr von\) LINDEN</td>
        <td>53</td>
    </tr>
    <tr class="hidden-row">
        <td>1308</td>
        <td>Karl Friedrich August Philipp Freiherr von DALWIGK zu LICHTENFELS</td>
        <td>31</td>
    </tr>
    <tr class="hidden-row">
        <td>1309</td>
        <td>Johann Christoph Veit \(Edler von\) TÖNNEANN</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1310</td>
        <td>Johann Hermann Joseph Franz PAPIUS \(Freiherr von PAPE gen\. PAPIUS\)</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1311</td>
        <td>Philipp Karl \(von\) DEEL \(Edler zu DEELSBURG\) \(später: Freiherr DEEL von DEELSBURG\)</td>
        <td>37</td>
    </tr>
    <tr class="hidden-row">
        <td>1312</td>
        <td>Valentin Ferdinand \(Freiherr\) von GUDENUS</td>
        <td>32</td>
    </tr>
    <tr class="hidden-row">
        <td>1313</td>
        <td>Franz Joseph \(Freiherr von\) Albini</td>
        <td>70</td>
    </tr>
    <tr class="hidden-row">
        <td>1314</td>
        <td>Johann Christoph Joseph \(von\) SCHMITZ</td>
        <td>41</td>
    </tr>
    <tr class="hidden-row">
        <td>1315</td>
        <td>Ferdinand Heinrich \(Freiherr von\) DÜNWALDT \(Dünnwaldt, Dünwald, Dün\(n\)ewald\)</td>
        <td>32</td>
    </tr>
    <tr class="hidden-row">
        <td>1316</td>
        <td>Joseph Philipp \(Philipp Karl Joseph\) Graf zu SPAUR und FLAVON</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>1317</td>
        <td>Johann Franz Valentin \(von\) EMMERICH</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1318</td>
        <td>Kaspar Anton \(Freiherr von\) Albini</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>1319</td>
        <td>Friedrich Joseph Anton \(Freiherr\) von SCHMITZ \(zu GROLLENBURG\)</td>
        <td>33</td>
    </tr>
    <tr class="hidden-row">
        <td>1320</td>
        <td>Andreas \(Freiherr von\) STEIGENTESCH</td>
        <td>73</td>
    </tr>
    <tr class="hidden-row">
        <td>1321</td>
        <td>Johann Matthias \(Edler von\) COLL</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>1322</td>
        <td>Johann Hugo Heinrich Franz von GAERZ \(Gaertz\)</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1323</td>
        <td>Johann Georg Jakob \(Freiherr von\) BORIÉ \(Beaurieux\) \(zu SCHÖNBACH\)</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>1324</td>
        <td>Johann Franz Rudolf Nikolaus DEGEN</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1325</td>
        <td>Adolf Friedrich Rudolf Joseph \(Freiherr\) von TROTT zu SOLZ</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1326</td>
        <td>Johann Joachim Georg \(Freiherr\) von MÜNCH \(von/zu BELLINGHAUSEN\)</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1327</td>
        <td>Johann Ludwig Vollrath \(von\) FROHN</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1328</td>
        <td>Peter Joseph Melchior \(von\) HOMMER</td>
        <td>26</td>
    </tr>
    <tr class="hidden-row">
        <td>1329</td>
        <td>Johann Melchior CRAMER von CLAUSBRUCH</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>1330</td>
        <td>Gerhard Georg Wilhelm Franz Xaver \(Freiherr von\) VOGELIUS</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>1331</td>
        <td>Johann Arnold Heinrich Joseph CRAMER von CLAUSBRUCH</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1332</td>
        <td>Christian Franz \[von, S\.J\.\] WEIDENFELD</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>1333</td>
        <td>Johann Stephan \(Edler von\) SPECKMANN</td>
        <td>42</td>
    </tr>
    <tr class="hidden-row">
        <td>1334</td>
        <td>Franz Georg \(Freiherr von\) LEYKAM</td>
        <td>35</td>
    </tr>
    <tr class="hidden-row">
        <td>1335</td>
        <td>Hermann Franz \(Edler von, des Heiligen Römischen Reichs Ritter\) SONBORN</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1336</td>
        <td>Aegidius \(Egid\) Valentin Felix \(Freiherr von\) BORIÉ \(Beaurieux\) \(zu SCHÖNBACH\)</td>
        <td>40</td>
    </tr>
    <tr class="hidden-row">
        <td>1337</td>
        <td>Philipp Heinrich \(Freiherr von\) REUSS \(Reuß\) \(genannt HABERKORN\)</td>
        <td>33</td>
    </tr>
    <tr class="hidden-row">
        <td>1338</td>
        <td>Johann Daniel Clemens \(von\) HUEBER \(von der WILTAU\) \(Wildau\)</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>1339</td>
        <td>Theodor Karl Joseph Johann \(Edler\) de/von L&#39;EAU</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>1340</td>
        <td>Aloys Joseph Dominik Johann Franz \(Freiherr\) MAURER von KRONEGG zu Ungarshofen</td>
        <td>26</td>
    </tr>
    <tr class="hidden-row">
        <td>1341</td>
        <td>Karl Heinrich \(Edler\) von JODOCI</td>
        <td>29</td>
    </tr>
    <tr class="hidden-row">
        <td>1342</td>
        <td>Johann Peter \(von\) ORTMANN</td>
        <td>34</td>
    </tr>
    <tr class="hidden-row">
        <td>1343</td>
        <td>Heinrich Ludwig Karl \(von\) GEBLER, \(des Heiligen Römischen Reichs Ritter\)</td>
        <td>28</td>
    </tr>
    <tr class="hidden-row">
        <td>1344</td>
        <td>Maximilian Joseph Anton Joseph Nepomuk \(Freiherr von\) MARTINI</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1345</td>
        <td>Franz Valerius \(Edler von\) HAUER</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>1346</td>
        <td>Aegidius Joseph Valentin Felix genannt Egid Joseph Karl von FAHNENBERG</td>
        <td>37</td>
    </tr>
    <tr class="hidden-row">
        <td>1347</td>
        <td>Gottfried Emanuel Friedrich Freiherr von ANDRIAN-WERBURG</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>1348</td>
        <td>Franz Bernhard Joseph Freiherr von STEIN zu LAUSNITZ</td>
        <td>44</td>
    </tr>
    <tr class="hidden-row">
        <td>1349</td>
        <td>Karl Wilhelm Friedrich \(Freiherr\) von KÜNSBERG</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>1350</td>
        <td>Joachim Leonhard SCHÜLL</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1351</td>
        <td>Leopold Philipp Albert Adolf Erhard Graf und Freiherr GALLER zu Schwanberg, Lannach und Waldschach</td>
        <td>32</td>
    </tr>
    <tr class="hidden-row">
        <td>1352</td>
        <td>Joachim Albert Johann Zacharias \(Freiherr von\) HESS</td>
        <td>28</td>
    </tr>
    <tr class="hidden-row">
        <td>1353</td>
        <td>Philipp Ernst \(Freiherr von\) REUSS \(genannt HABERKORN\)</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1354</td>
        <td>Joseph ULLHEIMER</td>
        <td>31</td>
    </tr>
    <tr class="hidden-row">
        <td>1355</td>
        <td>Johann Adam \(Freiherr von\) SCHROFF</td>
        <td>41</td>
    </tr>
    <tr class="hidden-row">
        <td>1356</td>
        <td>Johann Sebastian Nikolaus Tolentinus Erasmus Judas Thaddäus \(Freiherr\) von ZILLERBERG</td>
        <td>29</td>
    </tr>
    <tr class="hidden-row">
        <td>1357</td>
        <td>Johann Joseph Edler von WEINBACH</td>
        <td>25</td>
    </tr>
    <tr class="hidden-row">
        <td>1358</td>
        <td>Karl Ludwig \(Freiherr von\) BRANCA</td>
        <td>38</td>
    </tr>
    <tr class="hidden-row">
        <td>1359</td>
        <td>Adolf Karl Alexander Lothar \(Freiherr\) von ZEHMEN</td>
        <td>25</td>
    </tr>
    <tr class="hidden-row">
        <td>1360</td>
        <td>Johann Christian Joseph Freiherr von WALDENFELS</td>
        <td>34</td>
    </tr>
    <tr class="hidden-row">
        <td>1361</td>
        <td>Franz Christoph Heinrich Aloys \(Graf\) von Reigersberg</td>
        <td>62</td>
    </tr>
    <tr class="hidden-row">
        <td>1362</td>
        <td>Kaspar Philipp Joseph Franz \(Graf\) von SPIEGEL zum DIESENBERG\(-HANXLEDEN\)</td>
        <td>41</td>
    </tr>
    <tr class="hidden-row">
        <td>1363</td>
        <td>Paul Theodor \(von\) ANTHONI</td>
        <td>31</td>
    </tr>
    <tr class="hidden-row">
        <td>1364</td>
        <td>Johann Daniel Marianus FRANK</td>
        <td>29</td>
    </tr>
    <tr class="hidden-row">
        <td>1365</td>
        <td>Maria Joseph Graf FUGGER von DIETENHEIM</td>
        <td>28</td>
    </tr>
    <tr class="hidden-row">
        <td>1366</td>
        <td>Karl Kaspar \(Freiherr von\) HERTWICH</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>1367</td>
        <td>Theodor Wilhelm Franz zum PÜTZ</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>1368</td>
        <td>Johann Friedrich Joseph Anton CRAMER von CLAUSBRUCH</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1369</td>
        <td>Franz Arnold \(Freiherr\) von der BECKE</td>
        <td>28</td>
    </tr>
    <tr class="hidden-row">
        <td>1370</td>
        <td>Otto Heinrich \(Freiherr\) von GEMMINGEN-HORNBERG-Hoffenheim</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>1371</td>
        <td>Johann Jacob Billstein</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1372</td>
        <td>Anselm Franz Molitoris</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1373</td>
        <td>Johann Arnold Schütz</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1374</td>
        <td>Johann Philipp Streit</td>
        <td>92</td>
    </tr>
    <tr class="hidden-row">
        <td>1375</td>
        <td>Johann Jacob Lincker</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1376</td>
        <td>Georg Melchior Klemens</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1377</td>
        <td>Johann Rudolph Cöler</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>1378</td>
        <td>Johann Heinrich Demar</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1379</td>
        <td>\[Johann Michael\] Spönla</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1380</td>
        <td>Sigismund Gerstenberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1381</td>
        <td>Valentin Riehßen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1382</td>
        <td>Daniel Mauritius von Gudenus</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1383</td>
        <td>\[Johann Arnold\] Schütz</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1384</td>
        <td>Johann Jakob Lincker von Lützenwick</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1385</td>
        <td>Christoph Ignaz Streit</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1386</td>
        <td>Wilhelm Heinrich Wincop</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1387</td>
        <td>Johann Daniel Streit</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1388</td>
        <td>Philipp Franz von Bellmont</td>
        <td>36</td>
    </tr>
    <tr class="hidden-row">
        <td>1389</td>
        <td>Johann Michael Rotermund</td>
        <td>48</td>
    </tr>
    <tr class="hidden-row">
        <td>1390</td>
        <td>Johann Michael Bockhlet</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1391</td>
        <td>Georg Melchior Gereon Molitoris</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1392</td>
        <td>Georg Melchior Clemens</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1393</td>
        <td>Melchior Ludolph Lilien</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1394</td>
        <td>Ernst Tentzel</td>
        <td>81</td>
    </tr>
    <tr class="hidden-row">
        <td>1395</td>
        <td>Konrad Wilhelm Strecker</td>
        <td>241</td>
    </tr>
    <tr class="hidden-row">
        <td>1396</td>
        <td>Gabriel Heinrich Lilien</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1397</td>
        <td>Ernst Immanuel Tentzel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1398</td>
        <td>Johann Heinrich Meyer</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>1399</td>
        <td>Christoph Ignaz von Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1400</td>
        <td>\[Johann Philipp\] Streit</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1401</td>
        <td>\[Johann Daniel Richard\] Spönla</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1402</td>
        <td>\[Andreas Ignaz\] Meyer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1403</td>
        <td>Johann Daniel Richard Spönla</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1404</td>
        <td>Andreas Ignaz Meyer</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1405</td>
        <td>Ernst Dominik Rhiesen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1406</td>
        <td>Franz Emmerich Kaspar von Bilstein</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1407</td>
        <td>Anselm Franz Friedrich von Ingelheim</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1408</td>
        <td>Gereon Molitoris</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1409</td>
        <td>Johann Gerhard Bresano \[?\]</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1410</td>
        <td>Valentin Riehsen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1411</td>
        <td>\[Elias\] Meltzer</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1412</td>
        <td>Hieronymo Schorchen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1413</td>
        <td>Johann Georg Cöler</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1414</td>
        <td>Sigmund Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1415</td>
        <td>Mauritius Gudenus</td>
        <td>23</td>
    </tr>
    <tr class="hidden-row">
        <td>1416</td>
        <td>Johann Mauritius Gudenus</td>
        <td>56</td>
    </tr>
    <tr class="hidden-row">
        <td>1417</td>
        <td>Johann Jakob von Gudenus</td>
        <td>37</td>
    </tr>
    <tr class="hidden-row">
        <td>1418</td>
        <td>Karl Joseph Adolph Lukas Freiherr Schenk Schmidburg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1419</td>
        <td>Karl Theodor Anton Maria Kämmerer von Worms Freiherr von Dalberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1420</td>
        <td>Franz Damian Linden</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1421</td>
        <td>Adolph Freiherr von Bellmont</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1422</td>
        <td>Anselm Franz Ernst Freiherr von Warsberg</td>
        <td>37</td>
    </tr>
    <tr class="hidden-row">
        <td>1423</td>
        <td>Johann Daniel Christoph Freiherr Lincker von Lützenwick</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1424</td>
        <td>Ernst Wilhelm Strecker</td>
        <td>34</td>
    </tr>
    <tr class="hidden-row">
        <td>1425</td>
        <td>Peter Heinrich Heiland</td>
        <td>43</td>
    </tr>
    <tr class="hidden-row">
        <td>1426</td>
        <td>Johann Arnold von Bellmont</td>
        <td>54</td>
    </tr>
    <tr class="hidden-row">
        <td>1427</td>
        <td>Johann Arnold Freiherr von Bellmont</td>
        <td>47</td>
    </tr>
    <tr class="hidden-row">
        <td>1428</td>
        <td>Johann Georg Brückmann</td>
        <td>95</td>
    </tr>
    <tr class="hidden-row">
        <td>1429</td>
        <td>Daniel Moritz von Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1430</td>
        <td>Friedrich Wilhelm Mosel von Alenstein</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1431</td>
        <td>Johann Christoph Spitz</td>
        <td>68</td>
    </tr>
    <tr class="hidden-row">
        <td>1432</td>
        <td>Alexander Bernhard Strecker</td>
        <td>38</td>
    </tr>
    <tr class="hidden-row">
        <td>1433</td>
        <td>Karl Wilhelm Joseph Adam Freiherr von Breidbach zu Bürresheim</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1434</td>
        <td>Johann Heinrich Genau</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1435</td>
        <td>Georg Mansuet Ignaz Ruding</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1436</td>
        <td>Georg von Klemens zu Millwitz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1437</td>
        <td>Daniel Veit von Pipper</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1438</td>
        <td>Mauritius Bachmann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1439</td>
        <td>Gustav Adolph Graberg</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1440</td>
        <td>Ernst Ludwig Wilhelm Freiherr von Dachröden</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1441</td>
        <td>Christian Joseph Freiherr von Benzel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1442</td>
        <td>Friedrich Ludwig Döring</td>
        <td>81</td>
    </tr>
    <tr class="hidden-row">
        <td>1443</td>
        <td>Johann Adam Schmitt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1444</td>
        <td>Georg Melchior von Klemens</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1445</td>
        <td>Elias Friedrich Heitmann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1446</td>
        <td>Johann Adolph Weltz</td>
        <td>32</td>
    </tr>
    <tr class="hidden-row">
        <td>1447</td>
        <td>Georg Andreas Reinhard</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1448</td>
        <td>Johann Bernhard Müller</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1449</td>
        <td>Gottfried Spönla</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1450</td>
        <td>Matthias Joseph Anton Franz Matthes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1451</td>
        <td>Anton Koch</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1452</td>
        <td>Siegfried Wilhelm Bollmann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1453</td>
        <td>Joseph von Sänger</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1454</td>
        <td>Christoph Kerl</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1455</td>
        <td>Adam Friedrich Christian Reinhard</td>
        <td>73</td>
    </tr>
    <tr class="hidden-row">
        <td>1456</td>
        <td>Johann Joseph Appel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1457</td>
        <td>Herrmann Pfingsten</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1458</td>
        <td>Franz Anton Resch</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1459</td>
        <td>Johann Nepomuk Christoph Hucke</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1460</td>
        <td>Franz Trömer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1461</td>
        <td>Georg Friedrich Trott</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1462</td>
        <td>Eberhard Sigmund Wincop</td>
        <td>342</td>
    </tr>
    <tr class="hidden-row">
        <td>1463</td>
        <td>\[N\.N\.\] Fuxius</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1464</td>
        <td>Johannes Matthias Wincop</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1465</td>
        <td>Johann Veit Stumpelius</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1466</td>
        <td>Tobias Lagus \[?\]</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1467</td>
        <td>Johann Heinrich Daniel von Ritter zu Grünstein</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1468</td>
        <td>\[Johann Moritz\] Gudenus \[?\]</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1469</td>
        <td>Johann Michael Spohnla \[?\]</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1470</td>
        <td>Daniel Mauritius Gudenus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1471</td>
        <td>Franz Hugo Hunoldt</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1472</td>
        <td>\[Adolph Freiherr\] von Bellmont</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1473</td>
        <td>\[Johann Jacob\] Lincker von Lützenwick</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1474</td>
        <td>Johann Arnoldt von Bellmont</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1475</td>
        <td>Mauritius von Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1476</td>
        <td>Johann Moritz Gudenus</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1477</td>
        <td>Maria Magdalena Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1478</td>
        <td>Casparus Junck</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1479</td>
        <td>Johann Heinrich Benedict Meier</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1480</td>
        <td>Johann Andreas Meyer</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1481</td>
        <td>Joachim Andreas Meyer</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1482</td>
        <td>Anselm Franz von Molitoris</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1483</td>
        <td>Karl Friedrich Strecker</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1484</td>
        <td>Wilhelm Moritz Strecker</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1485</td>
        <td>Josepha Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1486</td>
        <td>Karl Strecker</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1487</td>
        <td>Karl Wilhelm Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1488</td>
        <td>Johann Philipp Streidt</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1489</td>
        <td>Georg Heinrich von Ziegler</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1490</td>
        <td>Jacob Paul Heinrich Ziegler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1491</td>
        <td>Georg Heinrich \(von\) Ziegler</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1492</td>
        <td>n/a</td>
        <td>6541</td>
    </tr>
    <tr class="hidden-row">
        <td>1493</td>
        <td>\[N\.N\.\] Papius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1494</td>
        <td>Johann Hallenhorst</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1495</td>
        <td>Jacob Berger</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>1496</td>
        <td>Georg Heinrich Ludolf</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>1497</td>
        <td>Elias Melzer</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1498</td>
        <td>Hieronymus Schorch</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1499</td>
        <td>Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1500</td>
        <td>Benjamin Schüz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1501</td>
        <td>Johann Jacob von Bilstein</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1502</td>
        <td>Johann Pleikard Heinrich</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1503</td>
        <td>\[Anselm Franz\] Molitoris</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1504</td>
        <td>\[Johann Rudolph\] Cöler</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1505</td>
        <td>N\.N\. Mueß</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1506</td>
        <td>Dresanus</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>1507</td>
        <td>\[Georg Marx\] Hahn von Königsburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1508</td>
        <td>\[Valentin\] Rhieß</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1509</td>
        <td>\[Hieronymus\] Schorch</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1510</td>
        <td>\[Sigmund\] Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1511</td>
        <td>\[Christoph Ignaz\] Streit</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1512</td>
        <td>Matthiae</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1513</td>
        <td>Valentin Rhieß</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1514</td>
        <td>\[Friedrich Wilhelm\] Mosel von Alenstein</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1515</td>
        <td>\[Wilhelm Heinrich\] Wincop</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1516</td>
        <td>Johann Jacob von Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1517</td>
        <td>Erhard Dresanus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1518</td>
        <td>Georg Marx Hahn</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1519</td>
        <td>\[Johann Georg\] Cöler</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1520</td>
        <td>\[Johann Michael\] Booklet</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1521</td>
        <td>\[Georg Melchior Gereon\] Molitoris</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1522</td>
        <td>\[Georg Melchior\] Clemens</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1523</td>
        <td>Johann Philipp Demar</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1524</td>
        <td>Georg Friedrich von Creutz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1525</td>
        <td>Georg Friedrich von Kreutz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1526</td>
        <td>Johann Gerald Dresanus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1527</td>
        <td>Valentin Rieß</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1528</td>
        <td>Maximilian Wagner</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1529</td>
        <td>Johann Daniel Lincker</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1530</td>
        <td>\[Johann Pleikard\] Heinrich</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1531</td>
        <td>Matthia</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1532</td>
        <td>\[Georg Marx\] Hahn</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1533</td>
        <td>Johann Michael Bockleth</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1534</td>
        <td>Siegfriedt Wilhelm Bollmann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1535</td>
        <td>George Melchior Clemens</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1536</td>
        <td>Johann Rudolph Cöhler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1537</td>
        <td>Hugo Frantz Hunoldt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1538</td>
        <td>Johann Daniel von Lincker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1539</td>
        <td>Elias Meltzer</td>
        <td>26</td>
    </tr>
    <tr class="hidden-row">
        <td>1540</td>
        <td>Philipp Georg Jerion Molitoris</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1541</td>
        <td>Adam Christian Reinhardt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1542</td>
        <td>Jacob Ernestus Dominicus Riese</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1543</td>
        <td>Johann Ernst Dominicus Riese</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1544</td>
        <td>\[Conrad Wilhelm\] Streckerth</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1545</td>
        <td>Justus Christophorus Weltz</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1546</td>
        <td>Johann Ernst Fratzscher</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1547</td>
        <td>Christian Heinrich Weltz</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1548</td>
        <td>Christoph Reichhart</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1549</td>
        <td>Friedrich Wilhelm Stallforth</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1550</td>
        <td>Eberhardus Sigismundus Winkopp</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1551</td>
        <td>Hieronymus Friedrich Schorch</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1552</td>
        <td>Christian Wilhelm Schorch</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1553</td>
        <td>Johann David Schorch</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1554</td>
        <td>Johann Wilhelm Schorch</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1555</td>
        <td>Friedrich Christian Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1556</td>
        <td>Frantz Adam Bocklett</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1557</td>
        <td>Jacobus Franciscus Bocklet</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1558</td>
        <td>Ernestus Cöler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1559</td>
        <td>Johann Adolph Cöler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1560</td>
        <td>Johann Christian Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1561</td>
        <td>Carl Friedrich Molitoris</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1562</td>
        <td>Johann Anton Pipper</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1563</td>
        <td>Jacobus Berger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1564</td>
        <td>M\. Jacob Berger</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1565</td>
        <td>Maria Berger</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1566</td>
        <td>Agneta Weidmann</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1567</td>
        <td>Martha Berger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1568</td>
        <td>Johann Jacobus Franciscus Spoenla</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1569</td>
        <td>Christoph Ignatius von Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1570</td>
        <td>Christina Sophia Tentzel</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1571</td>
        <td>Carl Dresanus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1572</td>
        <td>N\. Molitoris</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1573</td>
        <td>Anna Regina Cöler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1574</td>
        <td>Philipp Johann Jacobi</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1575</td>
        <td>Martha Regina Gerstenberg</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1576</td>
        <td>Johann Joachim Gerstenberg</td>
        <td>35</td>
    </tr>
    <tr class="hidden-row">
        <td>1577</td>
        <td>Martha Sabina Cöler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1578</td>
        <td>Georg Heinrich von Ziegler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1579</td>
        <td>Philippina von Fensterer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1580</td>
        <td>Catharina N\.N\.</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1581</td>
        <td>Theresia Rotermund</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1582</td>
        <td>Barbara N\.N\.</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1583</td>
        <td>Johann Wolfgang Jungk</td>
        <td>39</td>
    </tr>
    <tr class="hidden-row">
        <td>1584</td>
        <td>Clara Catharina Bader</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1585</td>
        <td>Martha Sophie Schmidt</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1586</td>
        <td>Johann Jacob Schmidt</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1587</td>
        <td>Martha Sophia Menius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1588</td>
        <td>Justina Margaretha Schmidt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1589</td>
        <td>Anna Christina Möltzer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1590</td>
        <td>Johannes Stechanius</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1591</td>
        <td>Regina Magdalena Langguth</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1592</td>
        <td>Eva Maria Breitenbach</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1593</td>
        <td>Hieronymus Friedrich Breitenbach</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1594</td>
        <td>Anna Veronica Schwengfeld</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1595</td>
        <td>Maria Anna von Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1596</td>
        <td>Moritz von Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1597</td>
        <td>Martha Catharina Böning</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1598</td>
        <td>Anna Maria von Zwehl</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1599</td>
        <td>Johann Nicolaus Reinhardt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1600</td>
        <td>Dorothea Wilhelmina Birnstiel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1601</td>
        <td>Georg Heinrich Birnstiel</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>1602</td>
        <td>Maria Josepha Rotermund</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1603</td>
        <td>Anna Philippina Meinong</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1604</td>
        <td>Magdalena Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1605</td>
        <td>Sophia Josepha Rotermund</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1606</td>
        <td>Francisca Stahl</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1607</td>
        <td>Johann Adam Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1608</td>
        <td>Martha Adami</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1609</td>
        <td>Adelgunda Elisabeth Streit</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1610</td>
        <td>Johannes Laurentius Welsch</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1611</td>
        <td>Rosina Sophia Perthes</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1612</td>
        <td>Johann Justus Perthes</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1613</td>
        <td>Johanna Regina Hesse</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1614</td>
        <td>Heinrich Christian Weltz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1615</td>
        <td>Eleonore Sophie Friese</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1616</td>
        <td>Rosina Catharina Ulle</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1617</td>
        <td>Georg Ulle</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1618</td>
        <td>Johannes Matthias Wincop</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1619</td>
        <td>Christina Schröder</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1620</td>
        <td>Michael Schröder</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1621</td>
        <td>Heinrich Enoch Ziegler</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1622</td>
        <td>Anna Regina von Brettin</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1623</td>
        <td>Heinrich Langguth</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>1624</td>
        <td>Sophie Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1625</td>
        <td>Jost Brochhausen</td>
        <td>35</td>
    </tr>
    <tr class="hidden-row">
        <td>1626</td>
        <td>Johanne Christiane Kießling</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1627</td>
        <td>Johann Kießling</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1628</td>
        <td>Marie Dorothee Büchner</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1629</td>
        <td>Johann Christoph Büchner</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1630</td>
        <td>Catharina Dorothea Fischer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1631</td>
        <td>Balthasar Fischer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1632</td>
        <td>Johannes Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1633</td>
        <td>David Georg Ernemann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1634</td>
        <td>Catharina Maria Vogel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1635</td>
        <td>Christina Juditha Schorch</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1636</td>
        <td>Volckmar Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1637</td>
        <td>Juditha Dorothea Stiede</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1638</td>
        <td>Martha Rosina Beyer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1639</td>
        <td>Johann Heinrich Rudolphi</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1640</td>
        <td>Martha Magdalena Fabritius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1641</td>
        <td>Friederike Eleonore Weltz</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1642</td>
        <td>Susanna Christina Weltz</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1643</td>
        <td>Johann Valentin Friese</td>
        <td>39</td>
    </tr>
    <tr class="hidden-row">
        <td>1644</td>
        <td>Martha Sophia Schmatz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1645</td>
        <td>Johann Carl Welz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1646</td>
        <td>Johann Gottfried Spönla</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1647</td>
        <td>Johann Christoph Kerl</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1648</td>
        <td>Mathias Josephus Antonius Frantz Madhes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1649</td>
        <td>\[Johann Bernhard\] Müller</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1650</td>
        <td>\[Gottfried?\] Spönla</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1651</td>
        <td>Emmerich Ernst Joseph Fuxius</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1652</td>
        <td>Melchior Gereon Molitoris</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1653</td>
        <td>\[Johann Adolph\] Cöler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1654</td>
        <td>\[Sigismund\] Gerstenberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1655</td>
        <td>Wolff Christoph von Ziegler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1656</td>
        <td>Antonetta Wilhelmina Ziegler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1657</td>
        <td>M\. Jacobus Berger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1658</td>
        <td>M\. Melchior Weidmann</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1659</td>
        <td>Anna Voigt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1660</td>
        <td>Anna Berger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1661</td>
        <td>Magdalena Berger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1662</td>
        <td>Anna Mohr</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1663</td>
        <td>Johann Rehefeld</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1664</td>
        <td>Johann Melchior Förster</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1665</td>
        <td>Christoph Avianus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1666</td>
        <td>Maria Salome Müller</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1667</td>
        <td>\[Philipp Franz\] von Bellmont</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1668</td>
        <td>\[Johann Michael\] Bocklet</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1669</td>
        <td>\[Johann Michael\] Bockleth</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1670</td>
        <td>\[Johann Philipp\] Dehmar</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1671</td>
        <td>\[Sigmund\] Gerstenberg</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1672</td>
        <td>\[Franz Hugo\] Hunold</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1673</td>
        <td>Johann Jacob Lincker \[von Lützenwick\]</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1674</td>
        <td>\[Johann Jacob\] von Lincker</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1675</td>
        <td>\[Gereon\] Molitor</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1676</td>
        <td>Johann Ernst Dominicus Riehs</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1677</td>
        <td>\[Johann Ernst Dominik\] Rhieß</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1678</td>
        <td>Valentin Riehse</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1679</td>
        <td>\[Valentin\] Riehse</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1680</td>
        <td>\[Valentin\] Rhies</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1681</td>
        <td>\[Valentin\] Rhiß</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1682</td>
        <td>\[Johann Michael\] Rotermund</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1683</td>
        <td>\[Johann Arnold\] Schüz</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1684</td>
        <td>\[Georg Marx\] Hahn \[von Königsburg\]</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1685</td>
        <td>\[Georg Freidrich\] von Kreuz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1686</td>
        <td>\[Johann\] Hallenhorst</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1687</td>
        <td>\[Jacob\] Berger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1688</td>
        <td>\[Georg Heinrich\] Ludolf</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1689</td>
        <td>Elias Andreas Stechan</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1690</td>
        <td>Sabina Magdalena Melzer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1691</td>
        <td>Burckhardt Lincker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1692</td>
        <td>Sibille Lincker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1693</td>
        <td>\[N\.N\.\] Meinong</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1694</td>
        <td>\[N\.N\] Everts</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1695</td>
        <td>Johann Arnold von Bellmont</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>1696</td>
        <td>Johann Daniel Christoph Freiherr Lyncker von Lützenwick</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1697</td>
        <td>Johann Arnold Freiherr von Bellmont</td>
        <td>37</td>
    </tr>
    <tr class="hidden-row">
        <td>1698</td>
        <td>Johann Daniel Heyland</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1699</td>
        <td>Johann Michael Rotermundt</td>
        <td>59</td>
    </tr>
    <tr class="hidden-row">
        <td>1700</td>
        <td>Johann Heinrich Rotermundt</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1701</td>
        <td>Johann Adam Strecker</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1702</td>
        <td>Johann Daniel Freiherr Lyncker von Lützenwick</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1703</td>
        <td>Johann Bartholomäus Brückmann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1704</td>
        <td>Philipp Wilhelm von Boineburg</td>
        <td>85</td>
    </tr>
    <tr class="hidden-row">
        <td>1705</td>
        <td>Johann Christian von Boineburg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1706</td>
        <td>Dieter Guillielmus Matthiae</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1707</td>
        <td>Anna Christina Schütz von Holzhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1708</td>
        <td>Carl Wilhelm Joseph Adam Fraiherr von Breidbach zu Bürresheim</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1709</td>
        <td>Carl Anselm Freiherr von Breidbach zu Bürresheim</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1710</td>
        <td>Sophia Eleonora von Rothenhahn</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1711</td>
        <td>Joachim Andreas von Brettin</td>
        <td>31</td>
    </tr>
    <tr class="hidden-row">
        <td>1712</td>
        <td>Regina Dorothea von Seltzer</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1713</td>
        <td>Dorothea Sophia von Ziegler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1714</td>
        <td>Heinrich Enoch von Ziegler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1715</td>
        <td>Johann Heinrich M\. Riedel</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1716</td>
        <td>Martha Regina Gerstenberger</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1717</td>
        <td>Johann Rudolph Coeler</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1718</td>
        <td>Anna Regina Ilgen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1719</td>
        <td>Sabine Magdalene Cöler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1720</td>
        <td>Johann Joachim Gerstenberger</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1721</td>
        <td>Johann Georg Coeler</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1722</td>
        <td>Susanne Sabine Coeler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1723</td>
        <td>Sigismund Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1724</td>
        <td>J\[ohann\] V\[alentin\] Friese</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1725</td>
        <td>Eleonora Sophia Friese</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1726</td>
        <td>Caspar Friedrich Lentin</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1727</td>
        <td>M\. Johann Ludwig Döring</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1728</td>
        <td>Friederica Sophia Magdalena Döring</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1729</td>
        <td>Christiana Sibylla Weltz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1730</td>
        <td>Henrietta Maria Weltz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1731</td>
        <td>Martha Sophia Schmaltz</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1732</td>
        <td>Johann Jacob Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1733</td>
        <td>Dorothea Regina Gerstenberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1734</td>
        <td>Joachim Gerstenberger</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1735</td>
        <td>Veronica Martini</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1736</td>
        <td>Johann Martini</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1737</td>
        <td>Marcus Gerstenberg</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1738</td>
        <td>Marcus Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1739</td>
        <td>Justina Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1740</td>
        <td>Johann Christoph Dehmar</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1741</td>
        <td>Regina Gerstenberger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1742</td>
        <td>Heinrich Langut</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1743</td>
        <td>Dorothea Gerstenberger</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1744</td>
        <td>Johann Scheffer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1745</td>
        <td>Veronica Gerstenberger</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1746</td>
        <td>Georg de Ahna</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1747</td>
        <td>Dorothea Hentrich</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1748</td>
        <td>Martha Catharina von der Sachsen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1749</td>
        <td>Jacob von der Sachsen</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>1750</td>
        <td>Jacobus Gerstenberger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1751</td>
        <td>Martha Gerstenberger</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1752</td>
        <td>Hieronymus Gerstenberger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1753</td>
        <td>Johann Heinrich Menius</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1754</td>
        <td>Catharina von Bodewitz</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1755</td>
        <td>Henrich Gerstenberg</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1756</td>
        <td>Henrich Rudolph Gerstenberger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1757</td>
        <td>Johann Heinrich von Gerstenberg</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1758</td>
        <td>Sibylla Veronica Gerstenberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1759</td>
        <td>Anna Salome von Ehrenkron</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1760</td>
        <td>Hartmann Jacob von Ehrenkron</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1761</td>
        <td>Anna Salome de Lasser</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1762</td>
        <td>Daniel Mauritius de Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1763</td>
        <td>Johannes Leopold von Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1764</td>
        <td>Wilhelm Streit</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1765</td>
        <td>Henrich Adam Streit</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1766</td>
        <td>Urbanus Josephus Streit</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1767</td>
        <td>Georg Henrich Streit</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1768</td>
        <td>Johannes Mauritius Gudenus</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1769</td>
        <td>Johannes Hallenhorst</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>1770</td>
        <td>Antonius Hallenhorst</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1771</td>
        <td>Anna Hövel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1772</td>
        <td>Johannes Brandis</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1773</td>
        <td>Maria Brand</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1774</td>
        <td>Hieronymus Anthon Hallenhorst</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1775</td>
        <td>Heinrich Adam Hallenhorst</td>
        <td>35</td>
    </tr>
    <tr class="hidden-row">
        <td>1776</td>
        <td>Heinrich Brand</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1777</td>
        <td>Barbara Richthäuser</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1778</td>
        <td>Anne Sabine Ziegler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1779</td>
        <td>Regina Sabina Hallenhorst</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1780</td>
        <td>Juditha Sophia Hallenhorst</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1781</td>
        <td>Johann Christoph Frikkinger</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1782</td>
        <td>Franz Leopold Hunold</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1783</td>
        <td>George Sigismund Hunold</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1784</td>
        <td>Caspar Jungk</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1785</td>
        <td>Justina Magdalena Schmidt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1786</td>
        <td>Valentin Bader</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1787</td>
        <td>Catharina Herr</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1788</td>
        <td>Friderica Sophia Louise Jungk</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1789</td>
        <td>Johann Caspar Jungk</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1790</td>
        <td>Paulus Jungk</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1791</td>
        <td>Elisabeth Gärtner</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1792</td>
        <td>Friederike Sophie Louise Schmidt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1793</td>
        <td>Christian Ferdinand von Zedtwitz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1794</td>
        <td>Johanna Louise Schmidt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1795</td>
        <td>Jacob Samuel Schmidt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1796</td>
        <td>Tobias Lagus</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1797</td>
        <td>Catharina Margaretha Rennemann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1798</td>
        <td>Dorothea Magdalena Brießmann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1799</td>
        <td>Georg Heinrich Ludolph</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1800</td>
        <td>Georg Melchior von Ludolph</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1801</td>
        <td>Martha Benigna Schmidt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1802</td>
        <td>Juditha Margaretha von Seltzer</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1803</td>
        <td>Jeremias Herbord von Seltzer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1804</td>
        <td>Dorothea von Utzberg</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1805</td>
        <td>Melchior Schmidt</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>1806</td>
        <td>Dietrich Wilhelm Matthaei</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1807</td>
        <td>Anna Regina Kniphoff</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1808</td>
        <td>Johann Melchior Kniphoff</td>
        <td>25</td>
    </tr>
    <tr class="hidden-row">
        <td>1809</td>
        <td>Dietrich Wilhelm Matthiae</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1810</td>
        <td>Johann Matthiae</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1811</td>
        <td>Magdalena Müller</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1812</td>
        <td>Cyriacus Müller</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1813</td>
        <td>Martha Ilgen</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1814</td>
        <td>Heinrich Ilgen der Jüngere</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1815</td>
        <td>Martha Mohr</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1816</td>
        <td>Anna Christina Meltzer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1817</td>
        <td>Johann Stechanius</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1818</td>
        <td>Sabina Magdalena Wolff</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1819</td>
        <td>Henning von der Marthen</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>1820</td>
        <td>Peter Cristian Frantz Pape</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1821</td>
        <td>\[N\.N\.\] Pape</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1822</td>
        <td>Johannes Christophorus Spitz</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1823</td>
        <td>Anselm Franz Ernst von Warsberg</td>
        <td>42</td>
    </tr>
    <tr class="hidden-row">
        <td>1824</td>
        <td>Johann Carl Weltz</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1825</td>
        <td>Martha Christina Sophie Brückner</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1826</td>
        <td>Hieronymus Friedrich Brückner</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1827</td>
        <td>Christoph Reichardt</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1828</td>
        <td>Johannes Weltz</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>1829</td>
        <td>N\.N\.</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1830</td>
        <td>Catharina von Ryssel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1831</td>
        <td>Johann Ludwig Döring</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1832</td>
        <td>Johann Heinrich Meier</td>
        <td>26</td>
    </tr>
    <tr class="hidden-row">
        <td>1833</td>
        <td>Johann Henrich Meier</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1834</td>
        <td>Eduard Brochhausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1835</td>
        <td>Lucia Biermann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1836</td>
        <td>Judith Ludolff</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1837</td>
        <td>Hiob Ludolff</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1838</td>
        <td>Andreas Heinrich Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1839</td>
        <td>Johann Joachim Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1840</td>
        <td>Christina Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1841</td>
        <td>Johann Wilhelm Sömmering</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1842</td>
        <td>Regine Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1843</td>
        <td>Johann Ernst Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1844</td>
        <td>Jost Heinrich Brochhausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1845</td>
        <td>Johan Jacob Brochhausen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1846</td>
        <td>Angela Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1847</td>
        <td>Tobias Emanuel Adami</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>1848</td>
        <td>Anna Magdalena Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1849</td>
        <td>Johann Georg Evander</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1850</td>
        <td>Johann Jacob Waldbott von Bassenheim</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1851</td>
        <td>Barbara Brandt</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1852</td>
        <td>Heinrich Jacob Brandt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1853</td>
        <td>David Brandt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1854</td>
        <td>Martha Brandt</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1855</td>
        <td>Tobias Emmanuel Adami</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1856</td>
        <td>Balthasar Rudolph Brandt</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1857</td>
        <td>Hieronymus Brandt</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1858</td>
        <td>Conrad Theodoricus Brandt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1859</td>
        <td>Christina Brandt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1860</td>
        <td>Johann Melchior Brandt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1861</td>
        <td>Maria Brandt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1862</td>
        <td>Heinrich II Brandt</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>1863</td>
        <td>Johann Jakob von Bielstein</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1864</td>
        <td>Agatha von Bingen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1865</td>
        <td>Anna Maria Barbara von Bielstein</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1866</td>
        <td>Daniel Moritz Gudenus</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>1867</td>
        <td>Johannes Michael Spoenla</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1868</td>
        <td>Beate Franziska Gudenus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1869</td>
        <td>Maria Anna Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1870</td>
        <td>Johann Gottfried von Spoenla</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1871</td>
        <td>Maria Josefa Salome Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1872</td>
        <td>Hiob Ludolf</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1873</td>
        <td>Judith Brandt</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1874</td>
        <td>Maria Katharina Böning</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1875</td>
        <td>Adelgunde Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1876</td>
        <td>Maria Theresia Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1877</td>
        <td>Carl Josef Dresanus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1878</td>
        <td>Christoph Ignatius Gudenus</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1879</td>
        <td>Johann Leopold Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1880</td>
        <td>Jacob Moritz Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1881</td>
        <td>Franziska Beata Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1882</td>
        <td>Johann Adam von Eck</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1883</td>
        <td>Friedrich Wilhelm Gudenus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1884</td>
        <td>Anna Elisabeth Maria Emilia von Tattenberg und Rheinstein</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1885</td>
        <td>Johann Daniel Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1886</td>
        <td>Johann Jakob Gudenus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1887</td>
        <td>Franz Christoph Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1888</td>
        <td>Maria Katharina Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1889</td>
        <td>Beata Stein</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1890</td>
        <td>Hans Stein</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1891</td>
        <td>Elisabeth Ziegenhorn</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1892</td>
        <td>Johann Daniel Gudenus</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>1893</td>
        <td>Anna Katharina Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1894</td>
        <td>N\.N\. Wedelmann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1895</td>
        <td>Anna Beate Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1896</td>
        <td>Anna Christiana Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1897</td>
        <td>Johann Dietrich Theodor Heiland</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1898</td>
        <td>Johann Christoph Gudenus</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1899</td>
        <td>Maria Clara Thavonath</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1900</td>
        <td>Urban Ferdinand Gudenus</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>1901</td>
        <td>Lotharia Mechtildis von Birkig</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1902</td>
        <td>Georg Friedrich Gudenus</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1903</td>
        <td>Johanna Franziska von Birkig</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1904</td>
        <td>Dorothea Sibylla von der Weser</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1905</td>
        <td>Magdalene Franziska Isselbach</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1906</td>
        <td>Johanna Klara Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1907</td>
        <td>Christoffel Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1908</td>
        <td>Ursula vom Hoffe</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1909</td>
        <td>Johannes d\.Ä\. Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1910</td>
        <td>Margaretha Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1911</td>
        <td>Johannes d\.J\. Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1912</td>
        <td>Anna Salome Jacobi von Ehrencron</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1913</td>
        <td>Maria Josefa Felizitas Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1914</td>
        <td>Johann Georg Mauritius Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1915</td>
        <td>Maria Franziska Theresia Josefa Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1916</td>
        <td>Maria Katharina Barbara Anastasia Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1917</td>
        <td>Philipp Wilhelm Meinong</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1918</td>
        <td>Friedrich Wilhelm Moritz Bernhard Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1919</td>
        <td>Johann Jakob Josef Franz Gudenus</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1920</td>
        <td>Eva Sabina Straub</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1921</td>
        <td>F\. L\. Löber</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1922</td>
        <td>Benedikt von Döttinchem</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1923</td>
        <td>Christoph Ignatz Alois Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1924</td>
        <td>Maria Philippina Theresia Rotermund</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1925</td>
        <td>Philippina von Bellmont</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1926</td>
        <td>Ursula Loscant</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1927</td>
        <td>Anselm Friedrich Adolf Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1928</td>
        <td>Johann Adolf Damian Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1929</td>
        <td>Mauritius Ferdinand Anton Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1930</td>
        <td>Maria Magdalena Sidonia Gabriela Theresia Gudenus</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1931</td>
        <td>Hans Hugold Strecker</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1932</td>
        <td>Anna Maria Sältzer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1933</td>
        <td>Maria Agnes Jordan</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1934</td>
        <td>Maria Katharina Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1935</td>
        <td>Johann Valtin Kaltwasser</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1936</td>
        <td>Philipp Kaspar Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1937</td>
        <td>Johann Christoph Strecker</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1938</td>
        <td>Elise Ständer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1939</td>
        <td>Johann Hugo Strecker</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1940</td>
        <td>Elisabeth Wolf</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1941</td>
        <td>Johann Franz Strecker</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>1942</td>
        <td>Apollonia Elise Marie Simon</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1943</td>
        <td>Maria Anna Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1944</td>
        <td>Dorothea Elisabeth Strecker</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1945</td>
        <td>Hans Georg Hentrich</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1946</td>
        <td>Georg Heinrich Gottlieb Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1947</td>
        <td>Maria Anna Wagner</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1948</td>
        <td>Maria Maximilia Christina Antonetta Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1949</td>
        <td>Anna Catharina Wilhelmina Josepha Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1950</td>
        <td>Francisca Renata Elisabeth Stahl</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1951</td>
        <td>Ivo Johannes Stahl</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1952</td>
        <td>Catharina Molitoris</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1953</td>
        <td>Alexander Johann Strecker</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1954</td>
        <td>Maria Susanna von Zwehl</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1955</td>
        <td>Johann Herwig von Zwehl</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1956</td>
        <td>Maria Anna Francisca Renata Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1957</td>
        <td>Maria Wilhelmina Josepha Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1958</td>
        <td>Karl Wilhelm Anton Strecker</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1959</td>
        <td>Johann Bernhard Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1960</td>
        <td>Ernst Friedrich Hugo Strecker</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1961</td>
        <td>Alexander Bernhard Johann Nepomuk Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1962</td>
        <td>Maria Anna Josepha Thecla Strecker</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1963</td>
        <td>N\.N\. Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1964</td>
        <td>Adam Ignatz Turin</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>1965</td>
        <td>Maria Anna Francisca Wagner</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1966</td>
        <td>Agnes Turin</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1967</td>
        <td>Maria Francisca Renate Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1968</td>
        <td>Friedrich Christian August Strecker</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1969</td>
        <td>Franciscus Jacobus Johannes Nepomuk Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1970</td>
        <td>Josepha Rotermund</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1971</td>
        <td>Sophia Katharina Josepha Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1972</td>
        <td>Karl Friedrich Wunderlich</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1973</td>
        <td>Susanna Josepha Strecker</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1974</td>
        <td>Johann Jakob Dominicus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1975</td>
        <td>Henricus Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1976</td>
        <td>Maria Apollonia Wilhelmina Susanna Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1977</td>
        <td>Ernst III Tentzel</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>1978</td>
        <td>Regina Elisabeth Tentzel</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>1979</td>
        <td>Friedrich Heinrich Jakob</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1980</td>
        <td>Christine Elisabeth Tentzel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1981</td>
        <td>Hieronymus Gottlieb Tentzel</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1982</td>
        <td>Johann Friedrich Tentzel</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>1983</td>
        <td>Ernst Emanuel Tentzel</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>1984</td>
        <td>Salome Sophia Tentzel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1985</td>
        <td>Christian Friedrich Schelhas</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1986</td>
        <td>Ernst I Tentzel</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>1987</td>
        <td>Barbara Happe</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1988</td>
        <td>Ernst II Tentzel</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1989</td>
        <td>Elisabeth Bonner</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1990</td>
        <td>Johann Gottlieb Adami</td>
        <td>23</td>
    </tr>
    <tr class="hidden-row">
        <td>1991</td>
        <td>Regina Brückner</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>1992</td>
        <td>Regina Adami</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1993</td>
        <td>Rudolph Adami</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>1994</td>
        <td>Johann Christian Tentzel</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1995</td>
        <td>Stephan Bonner</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1996</td>
        <td>Anna Siebold</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1997</td>
        <td>Friedrich Heinrich Jacobs</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>1998</td>
        <td>Heinrich Adam Streit</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>1999</td>
        <td>Juditha Margaretha Döring</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2000</td>
        <td>Hiob Ludolph</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>2001</td>
        <td>Sabine Magdalene von Eberbach</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2002</td>
        <td>Benigna von der Sachsen</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2003</td>
        <td>Adam Ignatius Turin</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>2004</td>
        <td>Tobias Adami</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>2005</td>
        <td>Johann Mauritz Bodo Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2006</td>
        <td>Christian Wilhelm von Brettin</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2007</td>
        <td>Henricus Langut</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2008</td>
        <td>Dorothea von der Sachsen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2009</td>
        <td>Johannes Martini</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2010</td>
        <td>Veronica Kronenberger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2011</td>
        <td>Henning Rennemann</td>
        <td>119</td>
    </tr>
    <tr class="hidden-row">
        <td>2012</td>
        <td>Margaretha Sprocovius</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2013</td>
        <td>Lydia Rothart</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2014</td>
        <td>Maria Northausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2015</td>
        <td>Justus Josias Rennemann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2016</td>
        <td>Helmoldevigus Rennemann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2017</td>
        <td>Franz Mauritius Bachmann</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2018</td>
        <td>Franz Moritz Bachmann</td>
        <td>47</td>
    </tr>
    <tr class="hidden-row">
        <td>2019</td>
        <td>Franz Moriz Bachmann</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2020</td>
        <td>Philipp Frantz von Bellmont</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2021</td>
        <td>Philipp Franciscus von Bellmont</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2022</td>
        <td>Karl Christian von Benzel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2023</td>
        <td>K\[arl\] C\[hristian\] Graf von Benzel-Sternau</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2024</td>
        <td>K\[arl\] Ch\[ristian\] Graf von Benzel-Sternau</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2025</td>
        <td>Carl Christian E\. Graf Benzel-Sternau</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2026</td>
        <td>Karl Christian Ernst Graf von Benzel-Sternau</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>2027</td>
        <td>Karl Christian Graf von Benzel-Sternau</td>
        <td>23</td>
    </tr>
    <tr class="hidden-row">
        <td>2028</td>
        <td>Christian Ernst Karl Graf von Bentzel-Sternau</td>
        <td>43</td>
    </tr>
    <tr class="hidden-row">
        <td>2029</td>
        <td>Gottfried von Benzel-Sternau</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2030</td>
        <td>Carl Christian Graf von Benzel-Sternau</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>2031</td>
        <td>Christian Ernst Graf von Bentzel-Sternau</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>2032</td>
        <td>Karl Graf von Bentzel-Sternau</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>2033</td>
        <td>Johann Jakob Bentzell</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2034</td>
        <td>Anselm Franz von Bentzel-Sternau</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2035</td>
        <td>Karl Christian Ernst Graf von Bentzel-Sternau</td>
        <td>59</td>
    </tr>
    <tr class="hidden-row">
        <td>2036</td>
        <td>Philipp Wilhelm Freiher von Boyneburg</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2037</td>
        <td>Johann Christian Freiherr von Boineburg</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2038</td>
        <td>Philipp Wilhelm Reichsgraf von Boineburg</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>2039</td>
        <td>Philipp Wilhelm Graf von Boyneburg</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>2040</td>
        <td>Hugo Franz Hunold</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2041</td>
        <td>Anselm von Ingelheim</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>2042</td>
        <td>Anselm Franz von Ingelheim</td>
        <td>35</td>
    </tr>
    <tr class="hidden-row">
        <td>2043</td>
        <td>Hans von Ingelheim</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2044</td>
        <td>Georg von Clemens-Millwitz</td>
        <td>26</td>
    </tr>
    <tr class="hidden-row">
        <td>2045</td>
        <td>N\.N\. von Clemens-Millwitz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2046</td>
        <td>Andreas Reinhard</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2047</td>
        <td>Adam Christian Friedrich Reinhard</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2048</td>
        <td>Franz A\[nton\] R\[esch\]</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2049</td>
        <td>Franz Anton? von Resch</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>2050</td>
        <td>Franz Anton von Resch</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2051</td>
        <td>N\.N\. von Ruding</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2052</td>
        <td>Georg Samuel Friedrich Trott</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2053</td>
        <td>Johann Christian von Boineburg</td>
        <td>34</td>
    </tr>
    <tr class="hidden-row">
        <td>2054</td>
        <td>N\.N\. von Boineburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2055</td>
        <td>Melchior Friedrich zu Schönborn</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2056</td>
        <td>Anna Sophia von Boineburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2057</td>
        <td>Johann Christian Baron von Boineburg</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2058</td>
        <td>Johann Christian von Boyneburg</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>2059</td>
        <td>N\.N\. von Boyneburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2060</td>
        <td>Johann Christian Freiherr von Boyneburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2061</td>
        <td>Barbara von Buttlar</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2062</td>
        <td>Berthold Boineburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2063</td>
        <td>Friedrich Ludwig Doering</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2064</td>
        <td>N\.N\. Meier</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2065</td>
        <td>Moritz Gudenus</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>2066</td>
        <td>Christoph Gudenus</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2067</td>
        <td>Beate Stein</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2068</td>
        <td>Ivo Johann Stahl</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2069</td>
        <td>Joachim Gerstenberg</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>2070</td>
        <td>N\.N\. Menius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2071</td>
        <td>Melchior Weidmann</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2072</td>
        <td>Christoph Ignaz Freiherr von Gudenus</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>2073</td>
        <td>Anselm Friedrich von Gudenus</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>2074</td>
        <td>Johann Philipp Jacobi</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2075</td>
        <td>Friedrich Leonhard Löber</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2076</td>
        <td>Georg Melchior von Ludolff</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2077</td>
        <td>George Melchior von Ludolf</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>2078</td>
        <td>Georg Melchior von Ludolf</td>
        <td>45</td>
    </tr>
    <tr class="hidden-row">
        <td>2079</td>
        <td>Martha Benigna Schmidt\]</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2080</td>
        <td>Sophia Dorothea Faligken</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2081</td>
        <td>Christian Friedrich Schellhas</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>2082</td>
        <td>Adam Ignaz Turin</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2083</td>
        <td>Tobias Adami</td>
        <td>22</td>
    </tr>
    <tr class="hidden-row">
        <td>2084</td>
        <td>Georg Melchior von Clemens</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>2085</td>
        <td>Maria Josepha Theresia Molitoris</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2086</td>
        <td>Anna Josepha Wallburgis von Clemens</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2087</td>
        <td>Robert Balthasar von Clemens</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2088</td>
        <td>Maria Margaretha von Clemens</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2089</td>
        <td>Anna Josepha von Clemens</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2090</td>
        <td>Susanna Theresia Fritz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2091</td>
        <td>N\.N\. Fritz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2092</td>
        <td>Catharina Höglein</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2093</td>
        <td>M\. E\. L\. \[?\] von Gerstenberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2094</td>
        <td>N\.N\. von Sommerlatte</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2095</td>
        <td>Charlotte von Bellmont</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2096</td>
        <td>N\.N\. Reinhard</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2097</td>
        <td>Siegfried Willhelm Bollmann</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2098</td>
        <td>Gottfried Spoenla</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2099</td>
        <td>Alexander Bernhard\] Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2100</td>
        <td>Siegfried Wilhelm\] Bollmann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2101</td>
        <td>Franz Madhes</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2102</td>
        <td>Johann Heinrich\] Genau</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2103</td>
        <td>Tobias Emanuel Adami</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2104</td>
        <td>Maria Angelica Bendleb</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2105</td>
        <td>M\. Joh\. Ludwig Döring</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2106</td>
        <td>Gustavus Adolphus Graberg</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2107</td>
        <td>Christian Samuel Graberg</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2108</td>
        <td>Eva Eleonora Schmidt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2109</td>
        <td>Rosina Chrisitna Fratzscher</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2110</td>
        <td>Peter Heinrich Jacob Heylandt</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2111</td>
        <td>Johann Jakob Josef Benzel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2112</td>
        <td>Franz Anselm Freiherr von Benzel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2113</td>
        <td>Anselm Franz Freiherr von Benzel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2114</td>
        <td>Joseph Matthias Frantz Matthes</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2115</td>
        <td>Justus Christoph Weltz</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2116</td>
        <td>Christoph Wilhelm Immanuel Reichart</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2117</td>
        <td>Johann Jacob Frantz Spoenla</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2118</td>
        <td>Carl Wilhelm Strecker</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2119</td>
        <td>Moritz Bachmann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2120</td>
        <td>Arnold von Bellmont</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2121</td>
        <td>Karl von Benzel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2122</td>
        <td>Johann Jakob Josef Franz von Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2123</td>
        <td>Christoph Ignaz Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2124</td>
        <td>Hieronymus Anton Hallenhorst</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2125</td>
        <td>Christoph Ignaz Aloys von Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2126</td>
        <td>Johannes Moritz Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2127</td>
        <td>Johannes Leopold Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2128</td>
        <td>Friedrich Wilhelm Moritz Bernhard von Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2129</td>
        <td>Adolf Johann Sigismund von Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2130</td>
        <td>Moritz Ferdinand von Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2131</td>
        <td>Johann Jakob Berger</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2132</td>
        <td>Jakob Franz Bocklet</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2133</td>
        <td>Jost Heinrich Brockhausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2134</td>
        <td>Johann Ernst Brockhausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2135</td>
        <td>Robert Balthasar Adam Clemens</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2136</td>
        <td>Robert Clemens</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2137</td>
        <td>Ernst Ludwig Wilhelm Freiherr von Dacheröden</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>2138</td>
        <td>Jakob Dominicus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2139</td>
        <td>Karl Josef Dresanus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2140</td>
        <td>Adam Ignaz Durino</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2141</td>
        <td>Johann Georg Evenius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2142</td>
        <td>Johann Christoph Evander</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2143</td>
        <td>Arnold Gottfried Events</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2144</td>
        <td>Gerhard Evers</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2145</td>
        <td>Franz Arnold Evers</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2146</td>
        <td>Johannes Valentin Frisius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2147</td>
        <td>Johann Valentin Frisius</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2148</td>
        <td>Gustav Adolf Graberg</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>2149</td>
        <td>Peter Heinrich Jakob Heiland</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2150</td>
        <td>Adolf Johann Pleichard Heinrici</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2151</td>
        <td>Johann Kaspar Jungk</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2152</td>
        <td>Kaspar Jungk</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2153</td>
        <td>Johann Melchior Kniephoff</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2154</td>
        <td>Johannes Georg Köhler</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2155</td>
        <td>Johann Georg Köhler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2156</td>
        <td>Johannes Rudolf Köhler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2157</td>
        <td>Johann Tobias Lagus Junior</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2158</td>
        <td>Jakob Heinrich Langguth</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2159</td>
        <td>Kaspar Friedrich Lentin</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2160</td>
        <td>Johann Daniel Christoph Lincker Ritter und Edler von Lützenwick</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2161</td>
        <td>Johann Jakob Lincker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2162</td>
        <td>Leonhard Löber</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2163</td>
        <td>Georg Melchior Ludolf</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>2164</td>
        <td>Dietrich Wilhelm von Matthiae</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2165</td>
        <td>Dietrich Matthiae</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2166</td>
        <td>Johann Heinrich Mayer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2167</td>
        <td>Joachim Andreas Meier</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2168</td>
        <td>Johannes Heinrich Meyer</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2169</td>
        <td>Robert Balthasar von Milwitz</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2170</td>
        <td>Johann Bernhard Molitoris</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2171</td>
        <td>Peter Christian Franz Papius</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2172</td>
        <td>Johann Hermann Pfingsten</td>
        <td>115</td>
    </tr>
    <tr class="hidden-row">
        <td>2173</td>
        <td>Vitus Daniel von Piper</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2174</td>
        <td>Christoph Wilhelm Emanuel Reichardt</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2175</td>
        <td>Johann Rese</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2176</td>
        <td>Johann Riese</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2177</td>
        <td>Johannes Ernst Dominik Riese</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2178</td>
        <td>Johann Josef Senger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2179</td>
        <td>Johannes Adam Schmidt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2180</td>
        <td>Johann Jakob Schmidt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2181</td>
        <td>Bernhard von Sommerlattae</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2182</td>
        <td>Otto Arnold von Sommerlattae</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2183</td>
        <td>Johann Jakob Franz Spoenla</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2184</td>
        <td>Johann Gottfried Spoenla</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2185</td>
        <td>Ivo Stahl</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2186</td>
        <td>Alexander Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2187</td>
        <td>Johannes Philipp Streit</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2188</td>
        <td>Ernst Christian Immanuel Tentzel</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2189</td>
        <td>Georg Ulle</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2190</td>
        <td>Johann Karl Weltz</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2191</td>
        <td>Jakob Paul Heinrich von Ziegler</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2192</td>
        <td>Jacob M\. Berger</td>
        <td>19</td>
    </tr>
    <tr class="hidden-row">
        <td>2193</td>
        <td>M\. Georg Berger</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2194</td>
        <td>Jacobus M\. Berger</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2195</td>
        <td>Heinrich II\. Brand</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2196</td>
        <td>Barbara Richthauser</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2197</td>
        <td>Maria Brand</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2198</td>
        <td>Christina Brochhausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2199</td>
        <td>Judith Brochhausen</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2200</td>
        <td>Jost Christoph Reinhardt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2201</td>
        <td>Johann Gerhard Dresanus</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>2202</td>
        <td>Anna Sabina Ziegler</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2203</td>
        <td>David Hamilton</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2204</td>
        <td>Christoph Frickinger</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2205</td>
        <td>Laurentius Heinrici</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2206</td>
        <td>Franz Hugo Hunold</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2207</td>
        <td>Heinrich Ilgen junior</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>2208</td>
        <td>Justina Magdalena Schmidt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2209</td>
        <td>Cyriax Müller</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2210</td>
        <td>Barbara Regina Magdalena Langguth</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2211</td>
        <td>Johann Daniel Lincker Ritter und Edler von Lützenwick</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2212</td>
        <td>Johann Jacob Lincker von Lützenwick</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>2213</td>
        <td>Burckhardt Lincker von Lützenwick</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2214</td>
        <td>Johann Daniel Lincker von Lützenwick</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2215</td>
        <td>Heinrich Wilhelm Ludolf</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2216</td>
        <td>Martha Benigna Ludolf</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2217</td>
        <td>Caspar Friedrich Heidenreich</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2218</td>
        <td>Hiob Ludolf</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2219</td>
        <td>Hans Ludolf</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2220</td>
        <td>Anna Gebhard</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2221</td>
        <td>Hiob I\. Ludolph</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>2222</td>
        <td>Conrad Brand</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2223</td>
        <td>Christina Gebhard</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2224</td>
        <td>Judith Ludolph</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2225</td>
        <td>Sabina Magdalena von der Marthen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2226</td>
        <td>Martha Catharina von Utzberg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2227</td>
        <td>Jonas Meltzer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2228</td>
        <td>Johannes Stechanius</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2229</td>
        <td>Maria Northausen</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2230</td>
        <td>Lydia Rothardt</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2231</td>
        <td>Catharina Margaretha Rennemann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2232</td>
        <td>Jeremias Schorch</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2233</td>
        <td>Martha Birnstiel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2234</td>
        <td>Jeremias Birnstiel</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2235</td>
        <td>Elisabeth Elsner</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2236</td>
        <td>Bartholomaeus Elsner</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2237</td>
        <td>Regina Frischmann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2238</td>
        <td>Bartholomaeus Elßner</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2239</td>
        <td>Ursula Wagner</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2240</td>
        <td>Johannes Wagner</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>2241</td>
        <td>Anna Maria Schorch</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2242</td>
        <td>Heinrich Friedemann</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2243</td>
        <td>Maria Magdalena Schorch</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2244</td>
        <td>Franz Schiller</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2245</td>
        <td>Johann Schorch</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>2246</td>
        <td>Heinrich Bartholomaeus Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2247</td>
        <td>Martha Elisabeth Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2248</td>
        <td>M\. Johann Wilhelm Andreae</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2249</td>
        <td>Johannes Schorch</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2250</td>
        <td>Anna Funcke</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2251</td>
        <td>Martha Nacke</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2252</td>
        <td>Hartmann Nacke</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2253</td>
        <td>Anna Benigna Gerstenberg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2254</td>
        <td>Marie Christine von Brettin</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2255</td>
        <td>Jeremias Herbord Seltzer</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2256</td>
        <td>Judith Margarethe Seltzer</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2257</td>
        <td>Cordula Maximiliana von der Weser</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2258</td>
        <td>Wolf Balthasar von der Weser</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2259</td>
        <td>Hedwig Müller</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2260</td>
        <td>Georg Heinrich Ziegler</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2261</td>
        <td>Jacob Heinrich Ziegler</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2262</td>
        <td>Elisabeth Stichling</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2263</td>
        <td>Martha Vasold</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2264</td>
        <td>Ursula Förster</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2265</td>
        <td>Catharina Herr</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2266</td>
        <td>Johann Rudolph Koehler</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2267</td>
        <td>Jakob Berger</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2268</td>
        <td>Johannes Bartholomaeus Elsnerus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2269</td>
        <td>Heinrich Wilhelm Friedemann</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2270</td>
        <td>Franz Heinrich Schiller</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2271</td>
        <td>Johann Heinrich Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2272</td>
        <td>Heinrich Bartholomäus Schorch</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2273</td>
        <td>Johann Wilhelm Andreae</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2274</td>
        <td>Martha Elisabeth Andreae</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2275</td>
        <td>Andreas Joachim von Brettin</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2276</td>
        <td>N\.N\. Hahn von Königsburg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2277</td>
        <td>Anthonius Hallenhorst</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2278</td>
        <td>Anton Hallenhorst</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2279</td>
        <td>M\. Friedrich Heinrich Jacobs</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2280</td>
        <td>Johann Jungk</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2281</td>
        <td>Johann Melchior der Jüngere Kniphoff</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2282</td>
        <td>Georg Ulla</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2283</td>
        <td>Karl Franz Adolf Schenk Schmiedburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2284</td>
        <td>Philipp Ludwig von Reiffenberg</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>2285</td>
        <td>Friedrich von Greiffenclau zu Vollraths</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2286</td>
        <td>Johann Heinrich Daniel Freiherr von Ritter zu Grünstein</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>2287</td>
        <td>Johann Jacob Walpoth von Bassenheim</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2288</td>
        <td>Gottlieb Philipp Joseph Faust von Stromberg</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2289</td>
        <td>Friedrich Wilhelm Freiherr von Bicken</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2290</td>
        <td>Anselm Franz Freiherr von Warsberg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2291</td>
        <td>Karl Joseph Adolph lukas Freiherr Schenk von Schmidtburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2292</td>
        <td>Karl Theodor Anton Maria von Dalberg</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>2293</td>
        <td>Johann Jacob Bilstein</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2294</td>
        <td>N\.N\. Dehmer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2295</td>
        <td>N\.N\. Molitoris</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2296</td>
        <td>N\.N\. Bocklett</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2297</td>
        <td>Ioannes Gerardus Dresanus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2298</td>
        <td>Ioannes Hallenhorst</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2299</td>
        <td>Johann Daniel Christoph Lincker von Lützenwick</td>
        <td>17</td>
    </tr>
    <tr class="hidden-row">
        <td>2300</td>
        <td>N\.N\. Heyland</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2301</td>
        <td>Carl Joseph Freiherr Schenck von Schmidtburg</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2302</td>
        <td>Karl Wilhelm Freiherr von Breidbach-Bürresheim</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2303</td>
        <td>Karl Theodor von Dalberg</td>
        <td>72</td>
    </tr>
    <tr class="hidden-row">
        <td>2304</td>
        <td>Friedrich Greiffenclau zu Vollrats</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2305</td>
        <td>Karl Joseph Adolph Lukas Freiherr Schenk von Schmidtburg</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2306</td>
        <td>Karl Wilhelm Joseph Adolph von Breidbach zu Bürresheim</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2307</td>
        <td>Johannes Dresanus</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>2308</td>
        <td>N\.N\. Genau</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2309</td>
        <td>Dieter Wilhelm Matthiae</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>2310</td>
        <td>N\.N\. von Lincker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2311</td>
        <td>N\.N\. Papius</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2312</td>
        <td>Peter Christian Papius</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2313</td>
        <td>Philipp von Reiffenberg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2314</td>
        <td>Philipp Ludwig Freiherr von Reiffenberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2315</td>
        <td>Adam F\. Reinhardt</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2316</td>
        <td>Johann Michael Rothermund</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2317</td>
        <td>Johann Christian Spitz</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2318</td>
        <td>N\.N\. Spitz</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2319</td>
        <td>Philipp Ludwig Ritter von Reiffenberg</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>2320</td>
        <td>Johann Jacob von Walpott</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2321</td>
        <td>Johann Jacob Waldbott</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2322</td>
        <td>Friedrich Wilhelm von Bicken</td>
        <td>26</td>
    </tr>
    <tr class="hidden-row">
        <td>2323</td>
        <td>Philipp Wilhelm Graf und edler Herr von Boineburg</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2324</td>
        <td>Carl Wilhelm Joseph Adam von Breidbach zu Bürresheim</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2325</td>
        <td>Ernst Ludwig Wilhelm von Dacheröden</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2326</td>
        <td>Carl Theodor Freiherr von Dalberg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2327</td>
        <td>Carl Theodor Anton Maria von Dalberg</td>
        <td>38</td>
    </tr>
    <tr class="hidden-row">
        <td>2328</td>
        <td>Carl Theodor Cämmerer von Worms Freiherr von und zu Dalberg</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2329</td>
        <td>Joachim Dietrich Evers</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2330</td>
        <td>Sebastian Evert</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2331</td>
        <td>Johann Mauritz Bodo von Gudenus</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2332</td>
        <td>Johann Jakob Freiherr Lincker von Lützenwick</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2333</td>
        <td>Johann Daniel Freiherr Lincker von Lützenwick</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2334</td>
        <td>Damian Freiherr von Linden</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2335</td>
        <td>Ernst Tentzl</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>2336</td>
        <td>Philipp Wilhelm Freiherr von Boineburg</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2337</td>
        <td>Anselmus Franciscus Molitoris</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2338</td>
        <td>Johann Arnold Schütze</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2339</td>
        <td>Johann Jacob Lyncker von Lützenwiyck</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2340</td>
        <td>Nicolaus Meinong</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2341</td>
        <td>Johann Heinrich Dehmer</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2342</td>
        <td>Hugo Franciscus Hunold</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2343</td>
        <td>Johann Ernst Dominicus Rieße</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2344</td>
        <td>Johann Daniel Lyncker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2345</td>
        <td>Ernest Tenzel</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2346</td>
        <td>Franciscus Hugo Hunold</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2347</td>
        <td>Philippus Franciscus a Bellmont</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2348</td>
        <td>Ernest Tentzel</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>2349</td>
        <td>Johann Arnold de Bellmont</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>2350</td>
        <td>Johann Heinrich Daniel Freiherr von Ritter zu Groenesteyn</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>2351</td>
        <td>Johann Michael Spoenla</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2352</td>
        <td>Petrus Christianus Josephus Papius</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2353</td>
        <td>Jacobus de Billstein</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2354</td>
        <td>Johannes Mauritius de Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2355</td>
        <td>Johann Jakob Bielstein</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2356</td>
        <td>Goeorg Marx Hahn von Königsburg</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2357</td>
        <td>Franz Damian Freiherr von Linden</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2358</td>
        <td>Georg Ignaz Mansuet Rüding</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2359</td>
        <td>Friedrich von Greiffenclau</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2360</td>
        <td>Johann Jakob von Waldbott-Olbrueck</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2361</td>
        <td>Gottfried Philipp Faust von Stromberg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2362</td>
        <td>Karl Wilhelm Joseph von Breidbach-Buerresheim</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2363</td>
        <td>Karl Joseph Adolf Schenk von Schmidburg</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2364</td>
        <td>Karl Theodor Anton von Dalberg</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2365</td>
        <td>Karl Theodor Freiherr von Dalberg</td>
        <td>29</td>
    </tr>
    <tr class="hidden-row">
        <td>2366</td>
        <td>Johann Werner von Vorstern</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2367</td>
        <td>Johann Werner von Vorster</td>
        <td>276</td>
    </tr>
    <tr class="hidden-row">
        <td>2368</td>
        <td>Johann Werner Freiherr von Vorster</td>
        <td>179</td>
    </tr>
    <tr class="hidden-row">
        <td>2369</td>
        <td>Philipp Moritz Gedult von Jungenfeld</td>
        <td>164</td>
    </tr>
    <tr class="hidden-row">
        <td>2370</td>
        <td>Friedrich Freiherr von Dalberg</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>2371</td>
        <td>Friedrich Anton Christoph Kämmerer von Worms Freiherr von und zu Dalberg</td>
        <td>342</td>
    </tr>
    <tr class="hidden-row">
        <td>2372</td>
        <td>Christoph Hartmann Freiherr von Fechenbach zu Laudenbach</td>
        <td>152</td>
    </tr>
    <tr class="hidden-row">
        <td>2373</td>
        <td>Christoph Hartmann Freiherr von Fechenbach zu Lautenbach</td>
        <td>350</td>
    </tr>
    <tr class="hidden-row">
        <td>2374</td>
        <td>Christophel Hartmann Freiherr von Fechenbach</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2375</td>
        <td>Karl Friedrich Freiherr von Frankenstein zu Ockstadt</td>
        <td>128</td>
    </tr>
    <tr class="hidden-row">
        <td>2376</td>
        <td>Karl Friedrich Freiherr von Frankenstein</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2377</td>
        <td>Karl von Hagen</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2378</td>
        <td>Karl Freiherr von Hagen</td>
        <td>54</td>
    </tr>
    <tr class="hidden-row">
        <td>2379</td>
        <td>Karl Wilhelm \[sic\!\] Freiherr von Hagen</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2380</td>
        <td>Karl Wilhelm Freiherr von Hagen</td>
        <td>486</td>
    </tr>
    <tr class="hidden-row">
        <td>2381</td>
        <td>Karl Wilhelm von Hagen</td>
        <td>33</td>
    </tr>
    <tr class="hidden-row">
        <td>2382</td>
        <td>Gottfried von Lammertz</td>
        <td>202</td>
    </tr>
    <tr class="hidden-row">
        <td>2383</td>
        <td>Gottfried von Lammerz</td>
        <td>123</td>
    </tr>
    <tr class="hidden-row">
        <td>2384</td>
        <td>Johann Christoph Joseph Schlehlein</td>
        <td>106</td>
    </tr>
    <tr class="hidden-row">
        <td>2385</td>
        <td>Christoph Joseph Schlehlein</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2386</td>
        <td>Johann Chrisoph Joseph Schlehlein</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>2387</td>
        <td>Johann Christoph Schlehlein</td>
        <td>57</td>
    </tr>
    <tr class="hidden-row">
        <td>2388</td>
        <td>Georg von Nitschke</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>2389</td>
        <td>Johann Georg von Nitschke</td>
        <td>82</td>
    </tr>
    <tr class="hidden-row">
        <td>2390</td>
        <td>Johann Friedrich Stubenrauch</td>
        <td>48</td>
    </tr>
    <tr class="hidden-row">
        <td>2391</td>
        <td>Johann Friedrich Edler von Stubenrauch</td>
        <td>72</td>
    </tr>
    <tr class="hidden-row">
        <td>2392</td>
        <td>Johann Ferdinand Andreas von Lammertz</td>
        <td>522</td>
    </tr>
    <tr class="hidden-row">
        <td>2393</td>
        <td>Johann Ferdinand Andreas von Lammerz</td>
        <td>15</td>
    </tr>
    <tr class="hidden-row">
        <td>2394</td>
        <td>Ferdinand Andreas von Lammertz</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2395</td>
        <td>Georg Friedrich von Lasser</td>
        <td>112</td>
    </tr>
    <tr class="hidden-row">
        <td>2396</td>
        <td>Johann Jakob  Stubenrauch</td>
        <td>78</td>
    </tr>
    <tr class="hidden-row">
        <td>2397</td>
        <td>Johann Jakob Edler von Stubenrauch</td>
        <td>292</td>
    </tr>
    <tr class="hidden-row">
        <td>2398</td>
        <td>Jakob Stubenrauch</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2399</td>
        <td>Heinrich Schweickart Hellmandel</td>
        <td>14</td>
    </tr>
    <tr class="hidden-row">
        <td>2400</td>
        <td>Heinrich Schweickart Oswald Hellmandel</td>
        <td>94</td>
    </tr>
    <tr class="hidden-row">
        <td>2401</td>
        <td>Johann Erhard Franz von Löhr</td>
        <td>57</td>
    </tr>
    <tr class="hidden-row">
        <td>2402</td>
        <td>Johann Eberhard \[sic\!\] Franz von Löhr</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2403</td>
        <td>Johann Eberhard Franz von Löhr</td>
        <td>88</td>
    </tr>
    <tr class="hidden-row">
        <td>2404</td>
        <td>Franz Bertram von Scheben, Edler von Kronfeld</td>
        <td>380</td>
    </tr>
    <tr class="hidden-row">
        <td>2405</td>
        <td>Franz Bertram Freiherr \[sic\!\] von Scheben</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2406</td>
        <td>Franz Bertram Freiherr von Scheben</td>
        <td>151</td>
    </tr>
    <tr class="hidden-row">
        <td>2407</td>
        <td>Veit Christoph Molitor</td>
        <td>414</td>
    </tr>
    <tr class="hidden-row">
        <td>2408</td>
        <td>Anselm Franz Serger</td>
        <td>412</td>
    </tr>
    <tr class="hidden-row">
        <td>2409</td>
        <td>Anselm Franz Särger</td>
        <td>69</td>
    </tr>
    <tr class="hidden-row">
        <td>2410</td>
        <td>Aeneas Anton Fleischmann</td>
        <td>99</td>
    </tr>
    <tr class="hidden-row">
        <td>2411</td>
        <td>Aeneas Anton von \[sic\!\] Fleischmann</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2412</td>
        <td>Aeneas Anton von Fleischmann</td>
        <td>53</td>
    </tr>
    <tr class="hidden-row">
        <td>2413</td>
        <td>Andreas \(sic\!\) Anton Fleischmann</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>2414</td>
        <td>Johann Philipp Freiherr von Bettendorf</td>
        <td>191</td>
    </tr>
    <tr class="hidden-row">
        <td>2415</td>
        <td>Johann Philipp Freiherr von Bettendorff</td>
        <td>183</td>
    </tr>
    <tr class="hidden-row">
        <td>2416</td>
        <td>Johann Philipp Graf von Stadion</td>
        <td>398</td>
    </tr>
    <tr class="hidden-row">
        <td>2417</td>
        <td>Johann Philipp Graf von Stadion-Thannhausen und Warthausen</td>
        <td>43</td>
    </tr>
    <tr class="hidden-row">
        <td>2418</td>
        <td>Hugo \[sic\!\] Johann Philipp Graf von Stadion-Thannhausen und Warthausen</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2419</td>
        <td>Hugo Johann Philipp Graf von Stadion-Thannhausen und Warthausen</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2420</td>
        <td>Hugo Johann Philipp Reichsgraf von Stadion-Thannhausen und Warthausen</td>
        <td>149</td>
    </tr>
    <tr class="hidden-row">
        <td>2421</td>
        <td>Hugo Johann Philipp Graf von Stadion und Tannhausen</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>2422</td>
        <td>Johann Philipp Graf von Stadion-Warthausen und Tannhausen</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2423</td>
        <td>Hugo Johann Philipp Graf von Stadion</td>
        <td>324</td>
    </tr>
    <tr class="hidden-row">
        <td>2424</td>
        <td>Hugo Johann Philipp Graf von Stadion</td>
        <td>105</td>
    </tr>
    <tr class="hidden-row">
        <td>2425</td>
        <td>Lothar Franz Michael Freiherr von Erthal</td>
        <td>680</td>
    </tr>
    <tr class="hidden-row">
        <td>2426</td>
        <td>Lothar Franz Michael Freiherr von und zu Erthal</td>
        <td>153</td>
    </tr>
    <tr class="hidden-row">
        <td>2427</td>
        <td>Lothar Franz Freiherr von und zu Erthal</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2428</td>
        <td>Bernhard Gottfried Reider</td>
        <td>403</td>
    </tr>
    <tr class="hidden-row">
        <td>2429</td>
        <td>Bernhard Gottfried von \[sic\!\] Reider</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2430</td>
        <td>Bernhard Gottfried von Reider</td>
        <td>889</td>
    </tr>
    <tr class="hidden-row">
        <td>2431</td>
        <td>Gottfried von Reider</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2432</td>
        <td>Johann Melchior Birckenstock</td>
        <td>206</td>
    </tr>
    <tr class="hidden-row">
        <td>2433</td>
        <td>Johann Melchior von Birckenstock</td>
        <td>90</td>
    </tr>
    <tr class="hidden-row">
        <td>2434</td>
        <td>Rupert Klemens</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2435</td>
        <td>Robert Balthasar von Klemens</td>
        <td>169</td>
    </tr>
    <tr class="hidden-row">
        <td>2436</td>
        <td>Karl Friedrich Wilhelm Freiherr von Erthal</td>
        <td>439</td>
    </tr>
    <tr class="hidden-row">
        <td>2437</td>
        <td>Friedrich Wilhelm Freiherr von Erthal</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2438</td>
        <td>Karl Kaspar Freiherr von Breidbach zu Bürresheim</td>
        <td>40</td>
    </tr>
    <tr class="hidden-row">
        <td>2439</td>
        <td>Karl Franz \[sic\!\] Freiherr von Breidbach zu Bürresheim</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2440</td>
        <td>Karl Franz Freiherr von Breidbach zu Bürresheim</td>
        <td>119</td>
    </tr>
    <tr class="hidden-row">
        <td>2441</td>
        <td>Karl Emerich Franz Freiherr von Breidbach zu Bürresheim</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>2442</td>
        <td>Johann Albert Freiherr von Gudenus</td>
        <td>104</td>
    </tr>
    <tr class="hidden-row">
        <td>2443</td>
        <td>Johann Albert von Gudenus</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2444</td>
        <td>Friedrich Reichsgraf von und zu Stadion-Thannhausen und Warthausen</td>
        <td>147</td>
    </tr>
    <tr class="hidden-row">
        <td>2445</td>
        <td>Friederich Graf von Stadion</td>
        <td>217</td>
    </tr>
    <tr class="hidden-row">
        <td>2446</td>
        <td>Franz Eberhard Freiherr von Ebersberg genannt von Weyers und Leyen</td>
        <td>63</td>
    </tr>
    <tr class="hidden-row">
        <td>2447</td>
        <td>Franz Eberhard Freiherr von Ebersberg genannt von Weyers und Layen</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>2448</td>
        <td>Franz Eberhard Freiherr von Ebersberg genannt von Wayers und Layen</td>
        <td>84</td>
    </tr>
    <tr class="hidden-row">
        <td>2449</td>
        <td>Franz Eberhard Freiherr von Ebersheim genannt von Meyers und Leyen</td>
        <td>8</td>
    </tr>
    <tr class="hidden-row">
        <td>2450</td>
        <td>Franz Eberhard Freiherr von Meyers und Leyen</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>2451</td>
        <td>Eberhard Sigismund Wincop</td>
        <td>53</td>
    </tr>
    <tr class="hidden-row">
        <td>2452</td>
        <td>Joseph Franz Graf von Schönborn Buchheim</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2453</td>
        <td>Joseph Franz Graf von Schönborn-Buchheim</td>
        <td>222</td>
    </tr>
    <tr class="hidden-row">
        <td>2454</td>
        <td>Franz Graf von Spaur</td>
        <td>83</td>
    </tr>
    <tr class="hidden-row">
        <td>2455</td>
        <td>Franz Reichsgraf von Spauer</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2456</td>
        <td>Franz Graf von Spauer zu Pflaum und Valeur</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2457</td>
        <td>Franz Graf von Spauer</td>
        <td>83</td>
    </tr>
    <tr class="hidden-row">
        <td>2458</td>
        <td>Franz Reichsgraf von Spauer zu Pflaum und Valeur</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2459</td>
        <td>Karl Peter Rüssel</td>
        <td>615</td>
    </tr>
    <tr class="hidden-row">
        <td>2460</td>
        <td>Karl Peter Rüßel</td>
        <td>24</td>
    </tr>
    <tr class="hidden-row">
        <td>2461</td>
        <td>Augustin Franz Kunibert</td>
        <td>99</td>
    </tr>
    <tr class="hidden-row">
        <td>2462</td>
        <td>Augustin Franz von \[sic\!\] Kunibert</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2463</td>
        <td>Augustin Franz von Kunibert</td>
        <td>84</td>
    </tr>
    <tr class="hidden-row">
        <td>2464</td>
        <td>Franz Philipp Ernst Freiherr von Hettersdorff</td>
        <td>63</td>
    </tr>
    <tr class="hidden-row">
        <td>2465</td>
        <td>Franz Philipp Ernst Freiherr von Hettersdorf</td>
        <td>218</td>
    </tr>
    <tr class="hidden-row">
        <td>2466</td>
        <td>Franz Philipp Ernest Freiherr von Hettersdorf</td>
        <td>234</td>
    </tr>
    <tr class="hidden-row">
        <td>2467</td>
        <td>Franz Philipp Ernst Freiherr von Heddesdorf</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2468</td>
        <td>Franz Philipp Ernst Freiherr von Hedersdorf</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>2469</td>
        <td>Johann Georg Neureuter</td>
        <td>224</td>
    </tr>
    <tr class="hidden-row">
        <td>2470</td>
        <td>Johann Georg Reurether</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2471</td>
        <td>Christian Ottenthal</td>
        <td>204</td>
    </tr>
    <tr class="hidden-row">
        <td>2472</td>
        <td>Christian von \[sic\!\] Ottenthal</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2473</td>
        <td>Christian von Ottenthal</td>
        <td>458</td>
    </tr>
    <tr class="hidden-row">
        <td>2474</td>
        <td>Emmerich Joseph Freiherr von Breidbach zu Bürresheim</td>
        <td>716</td>
    </tr>
    <tr class="hidden-row">
        <td>2475</td>
        <td>Anselm Freiherr Groß von und zu Trockau</td>
        <td>141</td>
    </tr>
    <tr class="hidden-row">
        <td>2476</td>
        <td>Anselm Baron von Groß zu Trockau</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>2477</td>
        <td>Johann Maria Rudolph Reichsgraf von Waldbott von Bassenheim</td>
        <td>184</td>
    </tr>
    <tr class="hidden-row">
        <td>2478</td>
        <td>Johann Maria Rudolph Reichsgraf von Waldbott in Bassenheim</td>
        <td>7</td>
    </tr>
    <tr class="hidden-row">
        <td>2479</td>
        <td>Johann Maria Rudolph Graf von Waldbott zu Bassenheim</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>2480</td>
        <td>Johann Maria Rudolph Graf von Waldbott in Bassenheim</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2481</td>
        <td>Joseph Anton Leonard Hartmann</td>
        <td>341</td>
    </tr>
    <tr class="hidden-row">
        <td>2482</td>
        <td>Johann Anton Leonard Hartmann</td>
        <td>23</td>
    </tr>
    <tr class="hidden-row">
        <td>2483</td>
        <td>Karl Adolph Freiherr von Ritter zu Grünstein</td>
        <td>1301</td>
    </tr>
    <tr class="hidden-row">
        <td>2484</td>
        <td>Karl Adolph Freiherr von Ritter zu Grünestein</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2485</td>
        <td>Karl Adolph Baron von Ritter</td>
        <td>16</td>
    </tr>
    <tr class="hidden-row">
        <td>2486</td>
        <td>Johann Georg Mansuet von Bentzel</td>
        <td>147</td>
    </tr>
    <tr class="hidden-row">
        <td>2487</td>
        <td>Johann Georg Mansuet Freiherr \[sic\!\] von Bentzel</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2488</td>
        <td>Johann Georg Mansuet Freiherr von Bentzel</td>
        <td>683</td>
    </tr>
    <tr class="hidden-row">
        <td>2489</td>
        <td>Johann Georg Mansuet Freiherr von Benzel</td>
        <td>52</td>
    </tr>
    <tr class="hidden-row">
        <td>2490</td>
        <td>Georg Mansuet Freiherr von Bentzel</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2491</td>
        <td>Joseph Graf von Fugger zu Kirchheim</td>
        <td>68</td>
    </tr>
    <tr class="hidden-row">
        <td>2492</td>
        <td>Joseph Graf von Fugger</td>
        <td>169</td>
    </tr>
    <tr class="hidden-row">
        <td>2493</td>
        <td>Adolph Freiherr von Greiffenclau zu Vollrads</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2494</td>
        <td>Adolph Wilhelm Franz \[sic\!\] Freiherr von Greiffenclau zu Vollrads</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2495</td>
        <td>Adolph Wilhelm Franz Freiherr von Greiffenclau zu Vollrads</td>
        <td>81</td>
    </tr>
    <tr class="hidden-row">
        <td>2496</td>
        <td>Adolph Freiherr von Greiffenclau</td>
        <td>20</td>
    </tr>
    <tr class="hidden-row">
        <td>2497</td>
        <td>Friedrich Karl Freiherr von Groschlag zu Dieburg</td>
        <td>285</td>
    </tr>
    <tr class="hidden-row">
        <td>2498</td>
        <td>Friedrich Karl Freiherr von Großschlag zu Dieburg</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2499</td>
        <td>Friedrich Karl Freiherr von Groschlag</td>
        <td>301</td>
    </tr>
    <tr class="hidden-row">
        <td>2500</td>
        <td>Philipp Franz Freiherr Knebel von Katzenelnbogen</td>
        <td>261</td>
    </tr>
    <tr class="hidden-row">
        <td>2501</td>
        <td>Philipp Franz Freiherr von \[sic\!\] Knebel zu \[sic\!\] Katzenelnbogen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2502</td>
        <td>Philipp Franz Freiherr von Knebel zu Katzenelnbogen</td>
        <td>93</td>
    </tr>
    <tr class="hidden-row">
        <td>2503</td>
        <td>Philipp Franz Karl Freiherr von Wambold</td>
        <td>44</td>
    </tr>
    <tr class="hidden-row">
        <td>2504</td>
        <td>Philipp Franz Karl Freiherr von Wambold zu Umstadt</td>
        <td>189</td>
    </tr>
    <tr class="hidden-row">
        <td>2505</td>
        <td>Philipp Franz Freiherr von Wambold</td>
        <td>279</td>
    </tr>
    <tr class="hidden-row">
        <td>2506</td>
        <td>Karl Anton von Vorster</td>
        <td>42</td>
    </tr>
    <tr class="hidden-row">
        <td>2507</td>
        <td>Karl Anton Freiherr \[sic\!\] von Vorster</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2508</td>
        <td>Karl Anton Freiherr von Vorster</td>
        <td>72</td>
    </tr>
    <tr class="hidden-row">
        <td>2509</td>
        <td>Hartmann Andreas Faber</td>
        <td>135</td>
    </tr>
    <tr class="hidden-row">
        <td>2510</td>
        <td>Hartmann Andreas von \[sic\!\] Faber</td>
        <td>12</td>
    </tr>
    <tr class="hidden-row">
        <td>2511</td>
        <td>Hartmann Andreas von Faber</td>
        <td>279</td>
    </tr>
    <tr class="hidden-row">
        <td>2512</td>
        <td>Karl Christian Susanne</td>
        <td>18</td>
    </tr>
    <tr class="hidden-row">
        <td>2513</td>
        <td>Damian Friedrich von Strauß</td>
        <td>226</td>
    </tr>
    <tr class="hidden-row">
        <td>2514</td>
        <td>Damian Friedrich Strauß</td>
        <td>59</td>
    </tr>
    <tr class="hidden-row">
        <td>2515</td>
        <td>Lothar Karl Freiherr von Bettendorf</td>
        <td>31</td>
    </tr>
    <tr class="hidden-row">
        <td>2516</td>
        <td>Johann Michael Rottermund</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2517</td>
        <td>Johann Michael Rodermund</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2518</td>
        <td>Joannes Michael Rotermund</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2519</td>
        <td>Johann Michel Rottermund</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2520</td>
        <td>Johann Daniel Christoph Freiherr von Lincker</td>
        <td>11</td>
    </tr>
    <tr class="hidden-row">
        <td>2521</td>
        <td>Johann Daniel Christoph Linckert von Lützewick</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2522</td>
        <td>Johann Daniel Christoph Freiherr \[sic\!\] Lincker von Lützenwick</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2523</td>
        <td>Johann Daniel Christoph Freiherr Linker von Lützenwick</td>
        <td>6</td>
    </tr>
    <tr class="hidden-row">
        <td>2524</td>
        <td>Ernst \[sic\!\] Wilhelm Strecker</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2525</td>
        <td>Ernest Wilhelm Strecker</td>
        <td>5</td>
    </tr>
    <tr class="hidden-row">
        <td>2526</td>
        <td>Peter Heinrich Heyland</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2527</td>
        <td>Joannes Arnold von Bellmont</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2528</td>
        <td>Joannes Jakobus von Gudenus</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2529</td>
        <td>Joann Georg Brückmann</td>
        <td>13</td>
    </tr>
    <tr class="hidden-row">
        <td>2530</td>
        <td>Hugo Franz Karl Reichsgraf von und zu Eltz-Kempenich</td>
        <td>819</td>
    </tr>
    <tr class="hidden-row">
        <td>2531</td>
        <td>Johann Kaspar von Hagen</td>
        <td>310</td>
    </tr>
    <tr class="hidden-row">
        <td>2532</td>
        <td>Karl Wilhelm von Hagen \[sic\!\]</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2533</td>
        <td>Franz Wenzel Kaysenberg</td>
        <td>55</td>
    </tr>
    <tr class="hidden-row">
        <td>2534</td>
        <td>Adam Philipp Teitzel</td>
        <td>190</td>
    </tr>
    <tr class="hidden-row">
        <td>2535</td>
        <td>Anselm Gerhard Schott</td>
        <td>49</td>
    </tr>
    <tr class="hidden-row">
        <td>2536</td>
        <td>Johann Michael Strecker</td>
        <td>235</td>
    </tr>
    <tr class="hidden-row">
        <td>2537</td>
        <td>Lothar von Horn</td>
        <td>73</td>
    </tr>
    <tr class="hidden-row">
        <td>2538</td>
        <td>Jakob von Gudenus</td>
        <td>9</td>
    </tr>
    <tr class="hidden-row">
        <td>2539</td>
        <td>Johann Christian Jakob Gudenus</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2540</td>
        <td>Eberhard Siegmund Wincop</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2541</td>
        <td>Christoph Ignaz Ludwig von Bellmont</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2542</td>
        <td>Christian Jakob Gudenus</td>
        <td>27</td>
    </tr>
    <tr class="hidden-row">
        <td>2543</td>
        <td>Johann Michael Rotermunt</td>
        <td>1</td>
    </tr>
    <tr class="hidden-row">
        <td>2544</td>
        <td>Bernhard Alexander Strecker</td>
        <td>30</td>
    </tr>
    <tr class="hidden-row">
        <td>2545</td>
        <td>Johann Alexander Bernhard Strecker</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2546</td>
        <td>Franz Wenzel von Kaysenberg</td>
        <td>60</td>
    </tr>
    <tr class="hidden-row">
        <td>2547</td>
        <td>Hugo Franz Karl Graf von und zu Eltz</td>
        <td>36</td>
    </tr>
    <tr class="hidden-row">
        <td>2548</td>
        <td>Anselm Schott</td>
        <td>36</td>
    </tr>
    <tr class="hidden-row">
        <td>2549</td>
        <td>Anselm Gerhard Schott</td>
        <td>166</td>
    </tr>
    <tr class="hidden-row">
        <td>2550</td>
        <td>Franz Anselm Keisenberg</td>
        <td>180</td>
    </tr>
    <tr class="hidden-row">
        <td>2551</td>
        <td>Franz Anselm Kaysenberg</td>
        <td>21</td>
    </tr>
    <tr class="hidden-row">
        <td>2552</td>
        <td>Franz Anselm von Keisenberg</td>
        <td>66</td>
    </tr>
    <tr class="hidden-row">
        <td>2553</td>
        <td>Karl Wilhelm Frei- und Kammerherr von Hagen</td>
        <td>3</td>
    </tr>
    <tr class="hidden-row">
        <td>2554</td>
        <td>Carl Wilhelm von Hagen</td>
        <td>498</td>
    </tr>
    <tr class="hidden-row">
        <td>2555</td>
        <td>Johann Jakob Stubenrauch</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2556</td>
        <td>Friederich Reichsgraf von Stadion</td>
        <td>4</td>
    </tr>
    <tr class="hidden-row">
        <td>2557</td>
        <td>Bernhard Gottfried Reuter</td>
        <td>2</td>
    </tr>
    <tr class="hidden-row">
        <td>2558</td>
        <td>Friedrich Wilhelm Freiherr von Ehrthal</td>
        <td>10</td>
    </tr>
    <tr class="hidden-row">
        <td>2559</td>
        <td>Friedrich Anton Christoph Freiherr von und zu Dalberg</td>
        <td>191</td>
    </tr>
    <tr class="hidden-row">
        <td>2560</td>
        <td>Karl Kaspar Franz Freiherr von Breidbach zu Bürresheim</td>
        <td>54</td>
    </tr>
    <tr class="hidden-row">
        <td>2561</td>
        <td>Anton Heinrich Friedrich Graf von Stadion</td>
        <td>153</td>
    </tr>
    <tr class="hidden-row">
        <td>2562</td>
        <td>Franz Eberhard Freiherr von Ebersberg</td>
        <td>52</td>
    </tr>
    <tr class="hidden-row">
        <td>2563</td>
        <td>Joseph Franz Graf von Schönborn</td>
        <td>118</td>
    </tr>
    <tr class="hidden-row">
        <td>2564</td>
        <td>Johann Maria Rudolph Graf Waldbott von Bassenheim</td>
        <td>86</td>
    </tr>
    <tr class="hidden-row">
        <td>2565</td>
        <td>Hugo Franz Karl Graf von und zu Eltz-Kempenich</td>
        <td>352</td>
    </tr>
    <tr class="hidden-row">
        <td>2566</td>
        <td>Franz Wenzel von Keisenberg</td>
        <td>94</td>
    </tr>
    <!-- Add more rows as needed -->
  </tbody>
</table>

<p><a href="javascript:void(0);" id="read-more-link">Read More</a></p>

<script>
  const readMoreLink = document.getElementById("read-more-link");
  const hiddenRows = document.querySelectorAll(".hidden-row");

  let isExpanded = false;

  readMoreLink.addEventListener("click", function() {
    if (!isExpanded) {
      hiddenRows.forEach((row) => {
        row.style.display = "table-row";
      });
      readMoreLink.textContent = "Read Less";
    } else {
      hiddenRows.forEach((row) => {
        row.style.display = "none";
      });
      readMoreLink.textContent = "Read More";
    }

    isExpanded = !isExpanded;
  });
</script>
