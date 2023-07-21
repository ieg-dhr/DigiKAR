**Process of person identification and disambiguation**

The challenges of working with (German and Latinised) person names in DigiKAR has been described in one of my blog post.
In the process, we first experimented with a Python script that did the following:

1) Read all names from PersonList into memory
2) Ask the user to enter a name
3) Search for the name in PersonList
4) Ask for confirmation
5) On confirmation, match all variants of the name with EventList persons
6) Show complete matches with all event info
7) Search for similar names on user request

To search for similarities, we calculated the name strings' Cosine Similarity, and specified, for example, that they must be at least 80% to consider a match. But if only 1st name and surname and once 10 first names of the person are given, the Similarity is far below that. If we assume that at least one last name is always present, and that it must be the last word in an n-gram, then one could match only the last names and introduce a spelling tolerance of 0.8?  Based on this, one can make a person ambiguation script that can put life events into relation.

If father and son have the same name and the year of birth is known for both, then we can assess whether a study period in the year YYYY concerns the father or the son. But here I still have the question of whether we can assign unique norm names or whether we can only work with the IDs. In the latter case, they must also be included in the factoid list..... In the first case, we could simply normalise the factoid list regularly and work only with the names.

**Preliminary overview of persons in the data and number of (initial) events associated with them**

So far, we have collected **48497 rows of events** (excluding reconstructed information). These events relate to **2566 person names** (prior to normalisation, disambiguation and ID-assignment). The majority of persons have less than 10 recorded biographic events. For some individuals, we have more than 100 entries (resulting from repeated mentions in annual lists of office holders).

|index|pers\_name|frequency|
|---|---|---|
|0|Wendelin Wendelin  Dietes|3|
|1|Matthäus Anton Chrysostomus  Eberwein|2|
|2|Johann Friedrich  Wüstefeld|7|
|3|Bertold Georg  Gothelp|6|
|4|Johann Franz  Asmut|8|
|5|Alexander Günther  Samhaber|5|
|6|Friedrich Franz  Thyri|8|
|7|Amandus Clemens  Schell|7|
|8|Samuel Thomas  Sömmering|13|
|9|Johannes Jacobus  von Lasser|9|
|10|Damian Friedrich  Boost|7|
|11|Heinrich Ignaz Joseph  Vogelmann|5|
|12|Johann Heinrich  Hessenhover|7|
|13|Johann Philipp  Fibig|7|
|14|Petrus Nikolaus  Unkraut|7|
|15|Wendelin Wilhelm Josef  Braunschiedel|5|
|16|Franz Valentin  Woger|6|
|17|Johann Rudolf  Will|9|
|18|Heinrich Ernst  Herold|5|
|19|Johannes Friedrich  Unckel|6|
|20|Petrus Michael Ignaz  Ravennas|8|
|21|Matthias Joseph  Hagen|8|
|22|Johannes Claudius  Renard|6|
|23|Georg Christian Gottlieb Theophil  Wedekind|11|
|24|Peter Joseph  Leydig|7|
|25|Johannes Jochem Hans  Höglein|5|
|26|Christoph Ignaz  Wiese|6|
|27|Johann Gottfried  Schweickard|8|
|28|Johann Kaspar Anton  Hartmann|7|
|29|Josef Theobald  Vogt|7|
|30|Jakob Franz Xaver  Koch|6|
|31|Johann Heinrich  Faber|6|
|32|Johann Philipp  Hahn|7|
|33|Johannes Wilhelm  Beusser|2|
|34|Lambert Christoph  Richtergin|6|
|35|Raymund Theodor  Peetz|7|
|36|Valentin Amandus  Bleidenstatt|6|
|37|Albert Friedrich  von Minsingen|6|
|38|Johann Baptist  von Horix|12|
|39|Franz Ulrich  Megele|7|
|40|Johann Stephan Valentin  Burckard|8|
|41|Johann Richard  von Roth|10|
|42|Peter Nikolaus  Söhnchen|8|
|43|Peter Anton  Freiherr von Frank|8|
|44|Gerhard Anton  Gerresheim|6|
|45|Philipp Karl  von Fugger|6|
|46|Christoph Siegfried  Faber|5|
|47|Cyprian Kardinal  Vomelius|8|
|48|Johannes Rudolf Dubslaff  Eler|3|
|49|Hieronymus Maria Joseph Alexander  von Ludolph|9|
|50|Franz Erwin Sebastian  Itzstein|6|
|51|Johann Adam  Krebs|7|
|52|Johann Anton  Antzmann|5|
|53|Johann Josef  Schönhuber|2|
|54|Johann Wendelin  Dictes|5|
|55|Anselm Franz Joseph  Ernst|7|
|56|Franz Phillipp  Frank|8|
|57|Peter Jakob  Ostermann|6|
|58|Johann Philipp  Dirolf|3|
|59|Jakob Fidelis  Ackermann|12|
|60|Johann Christoph  Freiherr von Gudenus|8|
|61|Carolus Siegfried  Faber|4|
|62|Dionysius Hans Fritz Philipp  Campius|5|
|63|Johannes Adolf  Mergentheim|3|
|64|Ludwig Konstantin  Reichsfreiherr von Welden|7|
|65|Johann Ernst  Neusesser gen\. Leibelbacher|5|
|66|Franz Ignaz Joseph  Bodmann|9|
|67|Joseph Nikolaus  Moser|6|
|68|Jakob Walther  Kühorn|5|
|69|Johann Kraffto  Hiegell|9|
|70|Adam Anton Chrysostomus  Ebersheim|6|
|71|Georg Joseph  Westhofen|5|
|72|Johann Babtist Joseph  Dilenius|9|
|73|Nikolaus Karl  Molitor|8|
|74|Franz Joseph  Wittmann|6|
|75|Franz Philipp  Beusser|4|
|76|Ludwig Philipp  Behlen|9|
|77|Bernhard Baptist  Kühorn von Feuerfeld|6|
|78|Georg Friedrich  Franck|5|
|79|Karl Joseph Hieronymus  Windischmann|9|
|80|Joseph William Mulvany  Seubert|5|
|81|Johann Friedrich  Michael|8|
|82|Johann Wendelin  Wasmuth|7|
|83|Philipp Friedrich  Waldmann|8|
|84|Heinrich Otto  Holtzgreven|5|
|85|Friedrich Rudolf  Moll|5|
|86|Joseph Thomas  Mantz|7|
|87|Franz Anton Chrysostomus  Dürr|8|
|88|Antonius Quirinus Hans Fritz Philipp  Campius|5|
|89|Jakob Heinrich  Reuter|5|
|90|Karl Joseph  Koelsch|6|
|91|Dietrich Joachim  Kauff|7|
|92|Philipp Paul  Koltz|5|
|93|Bernhard Max  Schöfferlin|5|
|94|Philipp Franz  Dünwald|9|
|95|Anton Franz  Metternich|9|
|96|Theodor Konrad  Hartleben|10|
|97|Johann Valentin  Strauss|7|
|98|Johann Joachim  Becher|9|
|99|Lorenz Rudolf  Wilthelm|6|
|100|Johannes Wilhelm  Langen|4|
|101|Andreas Rudolf Dubslaff  Eler|6|
|102|Michael Kardinal  Voss|8|
|103|Jacob Kardinal  Vosbach|5|
|104|Johannes Ambrosius  Höglein|7|
|105|Kaspar Gottfried  Schweickardt|6|
|106|Anton Jochem Hans  Hoffmann|7|
|107|Johannes Petrus  Menshengen|7|
|108|Johann Conrad  Moeller|4|
|109|Kaspar Hermann Joseph  von Westhausen|6|
|110|Ludwig Baptist  von Hörnigk|10|
|111|Markus Karl Klaus  Bausmann|7|
|112|Georg Leonhard  Schraub|6|
|113|Laurentius Heinrich  Faber|6|
|114|Cornelius Peter  Montfort|7|
|115|Friedrich Lorenz Theodor  Langen|7|
|116|Jakob Georg  Goy|5|
|117|Franz Peter  Straub|5|
|118|Johannes Georg  Thevern|6|
|119|Johann Kaspar Ignatz Anton  Creve|6|
|120|Jakob Adolf  Merstetter|6|
|121|Johann Christoph  Richter|6|
|122|Franz Joseph  Hartleben|8|
|123|Simon Heinrich  Bagen|6|
|124|Anton Philipp Thomas  Köhler|7|
|125|Nikolaus Otto  Rücker|5|
|126|Nikolaus Otto  Rucker|6|
|127|Johannes Fritz Konrad  Wahinger|5|
|128|Martin Simplicius  Mayer|7|
|129|Johann Jakob  Oppenheimer|8|
|130|Johann Georg Wilhelm  Reineck|5|
|131|Heinrich Franz Xaver  Knodt|7|
|132|Karl Dieter  Strack|8|
|133|Johann Jakob  Nauheimer|8|
|134|Georg Joseph  Wagner|7|
|135|Lubentius Friedrich  Pfingsthorn|7|
|136|Georg William Mulvany  Seiler|7|
|137|Johann Hermann Joseph  Werren|7|
|138|Friedrich Anton  Schmidt|4|
|139|Johann Valentin  Jäger|4|
|140|Georg Wilhelm  Moll|6|
|141|Philipp Anton Ignaz  Ruth|5|
|142|Emanuel Theodor  Moerzer|6|
|143|Johannes Bartholomaeus  Appelius|8|
|144|Joseph Matthias  Rosmann|7|
|145|Johann Peter  Bentzel|5|
|146|Franz Georg Ignaz  Ittner|8|
|147|Bernhard Gottfried  Reider|6|
|148|Johannes Ignaz Joseph  Vogelmann|7|
|149|Quirinus Adolf  von Mertz|8|
|150|Josef Franz  Wenzel|9|
|151|Johann Christian  von Ottendal|7|
|152|Lubertus Martin  Erbenius|3|
|153|Georg Karl  Heilmann|4|
|154|Johann Leonhard  Schörly|8|
|155|Karl Veit  Weidner|5|
|156|Jodocus Georg Wilhelm  Reis|7|
|157|Peter Joseph  Daniels|8|
|158|Friedrich Wilhelm  Rüding|6|
|159|Dietrich Franz  Flachsweiler|5|
|160|Gerhard Anton Chrysostomus  Ebersheim|4|
|161|Kaspar Baptist  Kuhn|6|
|162|Johann Karl  Fichard|5|
|163|Georg Ferdinand  Honcamp|6|
|164|Johann Friedrich  von Pfeiffer|4|
|165|Johannes Otto  Fürderer \(genannt Kühorn\)|6|
|166|Gottfried Ferdinand  von Buckisch und Löwenfels|8|
|167|Georg Ludwig  Koeler|6|
|168|Sebastian Maria Joseph Alexander  Loth|7|
|169|Franz Philipp  von Faust|6|
|170|Franz Anton  Rhodius|8|
|171|Justus Jodocus  Hartlieb|7|
|172|Johannes Otto Constantin  Berneburger|4|
|173|Johannes Peter  Möring|6|
|174|Johann Jakob  Lipp|4|
|175|Gottfried Christian  Lieb|6|
|176|Karl Anton  Schaab|8|
|177|Anton Franz  Ittstein|8|
|178|Johann Peter  Fried|6|
|179|Philipp Theodor  Mohr|4|
|180|Dietrich Heinz Walter Hans Ludwig  Gresemund d\. Ä\.|6|
|181|Dietrich F\.  Gresemund d\. J\.|8|
|182|Anselm Franz  Lieb d\. Ä\.|6|
|183|Peter Ernst  Hernssheimer|5|
|184|Johann Michael  Dahm|7|
|185|Peter Christoph  Brahm|8|
|186|Leonhard Otto Constantin  Nimis|7|
|187|Johann Peter  Molstetter|7|
|188|Lukas Otto  Arabier|3|
|189|Johann Christoph  Riedesel von Camberg zu Nassau|5|
|190|Georg Anna  Schlör|8|
|191|Philipp Adam  Schultheiss|7|
|192|Rolinus Günther  Tinctoris|5|
|193|Adolf Georg Hugo Samuel  von Pempelfurt|6|
|194|Adam Georg  Gotlip|3|
|195|Albert Wilhelm  Linde|3|
|196|Eucharius Alexander  Schlaun|3|
|197|Franz Adolph  Vogt|6|
|198|Georg Friedrich  Hornung|3|
|199|Johann Christoph  Jaeger|2|
|200|Johann Joseph Hieronymus  Wink|6|
|201|Joseph Leopold  Roth|2|
|202|Mercurius Rudolf  Wilthelm|6|
|203|Paul Kardinal  Volmar|5|
|204|Johann Diether  Weidmann|6|
|205|Andreas Karl  von Joss|6|
|206|Anselm Franz  Lieb d\. J\.|6|
|207|Ivo Walter Wilhelm  Wittich|7|
|208|Johann Wilhelm  Delvaux|7|
|209|Jakob Christoph  Bourdon|7|
|210|Damian Hartard  Dünwald|6|
|211|Jakob Kaspar Ignatz Anton  Curio|7|
|212|Peter Nikolaus  Viersen|5|
|213|Nikolaus Karl Anton  Heusser|5|
|214|Johann Franz  Gergens|4|
|215|Johann Wilhelm Heinrich  Jäger|5|
|216|Johannes Walther  Kühorn d\. J\.|6|
|217|Andreas Franz  Birnbeck|5|
|218|Jakob Hans Fritz Philipp  Campius|4|
|219|Nikolaus Philipp  Lisignolo|7|
|220|Johann Martin Franz  Koeler|5|
|221|Johannes Christoph  Vogelmann|7|
|222|Johannes Friedrich  Bertram|7|
|223|Johann Franz  Schlaun|6|
|224|Josef Franz Ignaz Aloys  Wenzel|6|
|225|Nikolaus Gerhard  Finck|4|
|226|Johann Siegfried  Faber|4|
|227|Urban Ferdinand  Gudenus|7|
|228|Johann Anton  Caprano|6|
|229|Jodocus William Mulvany  Selbach|4|
|230|Melchior Adolph  Vogelmann|6|
|231|Johann Hugo  Widt|6|
|232|Jakob Philipp Thomas  Koler|3|
|233|Bernhard Max  Scholl|6|
|234|Johann Christoph  von Gudenus|6|
|235|Johann Kaspar  Müller|7|
|236|Quirinus E\.  Kunckel|7|
|237|Nikolaus Friedrich Michael  Capito|3|
|238|Johann Adam  Freisbach|4|
|239|Balthasar Heinrich  Geier|4|
|240|Nikolaus Theodor  Pauli|6|
|241|Dietrich Friedrich  Ulsenius|4|
|242|Michael Anna  Schleiffert|4|
|243|Daniel Erwin Sebastian  Jaeger|3|
|244|Karl Maria Anton  Andre|7|
|245|Philipp Lambert  Wolf von Rosenbach|4|
|246|Anton Erwin Sebastian  Bayer|2|
|247|Heinrich Siegfried  Faber|4|
|248|Johannes Wendelin  Diel|6|
|249|Johann Friedrich Michael  Capitel|4|
|250|Justus Philipp Wilhelm  Moll|6|
|251|Gottlieb Friedrich  Ungleich|5|
|252|Kilian Rudolf Dubslaff  Eler|4|
|253|Franz Gottfried  Weinzürl|6|
|254|Johann Baptist  Krick|6|
|255|Jakob Konstantin  Welder|10|
|256|Johannes Walther  Kühorn d\. Ä\.|3|
|257|Karl August  Wenzel|5|
|258|Johann Georg  Neureuther|6|
|259|Wigand Christoph Chrysostomus  Kenniken|5|
|260|Johannes Franz Joseph  Eseler|5|
|261|Johann Peter  Weidmann|8|
|262|Johann Philipp Franz  Jaeger|7|
|263|Johannes Wolfgang  Munck|5|
|264|Christian Franz  Ittstein|6|
|265|Johann Christoph  Külsheimer|6|
|266|Karl Franz  Fischer|5|
|267|Johann Martin  Engelhardt|7|
|268|Bernhard Gottfried  Mandel|7|
|269|Valentin Friedrich  Molitor|5|
|270|Ferdinand Heinrich  von Dünwald|5|
|271|Philipp Ludwig  König|3|
|272|Friedrich Kaspar Ignatz Anton  Cronberg|6|
|273|Johann Martin  Hohenstatt|5|
|274|Johannes Magnus  Baimer|4|
|275|Johann Michael Ignaz  Ratzen|6|
|276|Philipp Wilhelm Karl  Horcher|5|
|277|Thomas Karl  Zenzen|5|
|278|Anton Kardinal  Voltz|1|
|279|Anton Maria  Marchand|3|
|280|Bartholomaeus Franz Joseph  von Ethen|1|
|281|Franz Michael  Hoepffner|3|
|282|Franz Otto  Holthof|7|
|283|Franz Peter  Dürr|4|
|284|Franz Rüdiger  von Haren|3|
|285|Georg Friedrich  Medicus|4|
|286|Johann Theodor  Moeren|1|
|287|Johannes Ernst Alexander  Schwartzman|5|
|288|Johannes Friedrich  Püchler|3|
|289|Johannes Veit  Bondius|1|
|290|Philipp Wilhelm  Bucheimer|2|
|291|Philippus Friedrich  von Schwalbach|5|
|292|Philippus Willi Otto  Beckardus|5|
|293|Wendelinus Wilhelm  Ruf|5|
|294|Wilhelm Jakob  Sattler|4|
|295|Lothar Clemens Joseph Emil  Dulog|2|
|296|Stephan Felix  Steick|3|
|297|Florentin Otto  Holtzweiler|6|
|298|Augustinus Peter  Berchem|6|
|299|Georg Konrad  Breuel|5|
|300|Sebastianus Friedrich  Plest|5|
|301|Georg Nikolaijewitsch  Blum|6|
|302|Martin Martin  Hohenstatt|5|
|303|Johann Emmerich  Gries|3|
|304|Edmund Georg Ferdinand Hans  von Hagen|7|
|305|Johannes Heinrich  Fabri|5|
|306|Conrad Peter  Weidmann|6|
|307|Gabriel Friedrich  Mintzenthaler|4|
|308|Johannes Karl  Jung|3|
|309|Johann Wolfgang  Krapff|5|
|310|Johann Georg  Thein|5|
|311|Johann Valentin  Knaud|5|
|312|Anton Valentin  Knauer|3|
|313|Michael Karl Max  Foresii|3|
|314|Johannes Thomas  Sorbillo|4|
|315|Christian Maria Joseph Alexander  Beinhauer|1|
|316|Johannes Anton  Carben|2|
|317|Wilhelm Jakob  Osterrod|2|
|318|Johannes Georg  Wonecker|1|
|319|Johannes Alexander  Schilling|3|
|320|Johann Maria Hugo  Kranebieter|3|
|321|Johannes Walther  Kühorn|1|
|322|Martin Karl  Bechel|1|
|323|Balthasar Philipp  Distelhusen|3|
|324|Leonhard Albertinus  de Alten|2|
|325|Hermann Franz Dionys  Kämmerer|1|
|326| ACKER, Philipp|9|
|327| ACKERMANN, Jakob Fidelis|10|
|328| ADEL\(T\), Peter|6|
|329| AGRICOLA, Christian|8|
|330| ALICH, Werner|6|
|331| ALTEN, Leonhard Albertinus de|1|
|332| ALTENBERG, Johann Georg|6|
|333| AMBACH, Melchior|5|
|334| AMELON, Heinrich|3|
|335| ANDLAU, Johann Ulrich von|8|
|336| ANDRE, Karl Maria Anton|8|
|337| ANTONI, Friedrich|1|
|338| ANTZ, Johann Wolfgang|13|
|339| ANTZMANN, Johann|8|
|340| APPEL, Christian, SJ|15|
|341| APPELIUS, Johannes Bartholomaeus|11|
|342| ARABIER, Lukas|4|
|343| ARAND, Karl Melchior|17|
|344| ARETZ, Jakob|6|
|345| ARNOLDI, Nicolaus, SJ|11|
|346| ARTOPOEUS, Georg|9|
|347| ARTOPOEUS, Johannes|2|
|348| ASMUT, Johann Franz|14|
|349| AUER, Lambert, SJ|8|
|350| BACHERELIUS , Ludwig, SJ|5|
|351| BADERUS, Georg, SJ|8|
|352| BAGEN, Simon|12|
|353| BAIMER, Johannes Magnus|1|
|354| BAIUMVILLE, Wilhelm, SJ|6|
|355| BALISTA, Lorenz|1|
|356| BANNIZA, Johann Peter Joseph, SJ|8|
|357| BAUR, Philipp, SJ|7|
|358| BAUSMANN, Markus|5|
|359| BAYER, Anton|4|
|360| BAYER, Jakob, SJ|15|
|361| BECANUS, Martin, SJ|12|
|362| BECHEL, Martin|2|
|363| BECHER, Johann Joachim|18|
|364| BECKARDUS, Philippus|3|
|365| BECKER, \(Joh\.\) Leonhard|13|
|366| BECKER, Johannes Aloysius|8|
|367| BEERSCHMITT, Georg, SJ|5|
|368| BEGER, Peter \(Petrus\)|3|
|369| BEHEIM, Georg|11|
|370| BEHLEN, Ludwig Philipp|24|
|371| BEHRS, Philipp, SJ|8|
|372| BEINHAUER, Christian|1|
|373| BENCKESER, Martin, SJ|3|
|374| BENTZEL, Balthasar, SJ|6|
|375| BENTZEL, Franz Kuno|10|
|376| BENTZEL, Ignaz von, SJ|13|
|377| BENTZEL, Johann Baptist Karl Fortunat von|10|
|378| BENTZEL, Johann Peter \(von\)|12|
|379| BERCHEM, Augustinus|3|
|380| BERGMANN, Joseph|12|
|381| BERINGER, Sigismund|10|
|382| BERNEBURGER, Johannes|7|
|383| BERTRAM, Johannes|11|
|384| BETTINGEN, Johannes, SJ|10|
|385| BEUSSER, Johannes|3|
|386| BEUSSER, Caspar|10|
|387| BEUSSER, Franz Philipp|7|
|388| BEUSSER, Johann Heinrich|7|
|389| BIBER, Nithardus, SJ|11|
|390| BIBER, Wolfgang, SJ|7|
|391| BIBERUS, Johannes|1|
|392| BIEGEISEN, Johannes, SJ|7|
|393| BIRNBECK, Andreas|10|
|394| BLAU, Felix Anton|21|
|395| BLEIDENSTADT, Johannes|10|
|396| BLEY, Johannes Jodocus|9|
|397| BLÖCHINGER, Johann Bernhard|9|
|398| BLUM, Georg|2|
|399| BODMANN, Franz Ignaz Joseph|17|
|400| BONDIUS, Johannes|1|
|401| BOOST, Damian Friedrich|10|
|402| BORG, Heinrich|3|
|403| BORLER, Augustin, SJ|8|
|404| BOSENDORFF, Hermann, SJ|7|
|405| BOURDON, Jakob Christoph|6|
|406| BRAHM, Peter|14|
|407| BRAUN, Quirinus Lorenz|10|
|408| BRAUNSCHIEDEL, Wendelin|8|
|409| BREITHARDT, Johannes|3|
|410| BRENEISEN, Johannes, SJ|6|
|411| BRENTANO, Joseph, SJ|6|
|412| BREUEL, Georg|3|
|413| BREUNIG, Conradus, SJ|10|
|414| BROCKAEUS, Guilielmus, SJ|8|
|415| BROCKARD, Aloysius, SJ|8|
|416| BROICH, Heinrich|7|
|417| BRORBELL, Jeremias|1|
|418| BROWERUS, Eberhard, SJ|8|
|419| BRUCH, Kaspar, SJ|6|
|420| BRUDER, Johann|8|
|421| BRUNHEIMER, Stephan Dominikus|9|
|422| BUCHEIMER, Philipp \(Jodocus\)|3|
|423| BÜCHELMANN, Melchior, SJ|1|
|424| BUCKISCH und Löwenfels, Gottfried Ferdinand von|12|
|425| BURANUS, Leonhard |5|
|426| BURCKARD, Johann Stephan Valentin|8|
|427| BURGER, Johannes|5|
|428| BUSAEUS, Johannes, SJ|9|
|429| BUSZLER Urbanus, Johann|1|
|430| CAMPIUS, Dionysius|8|
|431| CAMPIUS, Jakob|9|
|432| CAMPIUS, Antonius Quirinus|6|
|433| CAPITEL, Johann Friedrich Michael|3|
|434| CAPITO, Nikolaus|2|
|435| CAPRANO, Johann Anton|5|
|436| CARBEN, Johannes|4|
|437| CELLARIUS, Johannes|5|
|438| CETTI, Joseph, SJ|6|
|439| CHYLENUS, Martinus, SJ|5|
|440| COCI, Kaspar|3|
|441| COLBINUS, Philipp|7|
|442| COLONIA, Johannes |7|
|443| CONRADI, Adam|4|
|444| CONTZEN, Adam, SJ|8|
|445| CORNAEUS, Melchior, SJ|11|
|446| CORSMICH, Heinrich, SJ|6|
|447| CORVINUS, Arnold|6|
|448| COSTER, Franciscus, SJ|6|
|449| CRAFFTO, Michael, SJ|7|
|450| CRATZ, Johann Baptist \(Peter\)|7|
|451| CREMERIUS, Johannes, SJ|7|
|452| CREUTZNACH, Johannes|4|
|453| CREVE, Johann Kaspar Ignatz Anton|7|
|454| CROEFF, Johannes, SJ|4|
|455| CRONBERG, Friedrich|9|
|456| CRONENBURG, Johannes|1|
|457| CURIO, Jakob|6|
|458| DABUTZ, Florinus, SJ|9|
|459| DAHL, Thomas|3|
|460| DAHM, Jacob, SJ|8|
|461| DAHM, Johann Michael|15|
|462| DANIELS, Peter \(Philipp\) Joseph|5|
|463| DAUDE, Adrianus, SJ|7|
|464| DAUDE, Joseph, SJ|7|
|465| DECIUS, Franz Peter|3|
|466| DECIUS, Johann Rudolph Heinrich|10|
|467| DEGENHARDT, Georg, SJ|9|
|468| DELVAUX, Johann Wilhelm|11|
|469| DICHTEL, Franz Christoph|15|
|470| DICHTELBACH, Tilmann|6|
|471| DICTES, Johann \(Franz\) Wendelin|3|
|472| DIEL, Conrad|4|
|473| DIEL, Florentin|8|
|474| DIEL, Johannes|5|
|475| DIEMER, Johann Kaspar \(Konrad\)|7|
|476| DIETENBERGER, Johannes|9|
|477| DIETES, Wendelin|3|
|478| DIETRICH, Alexander|13|
|479| DIETZ, Andreas|8|
|480| DIETZ, Johann Valentin|4|
|481| DIEZE, Andreas|5|
|482| DILENIUS, Johann Baptist Joseph|9|
|483| DIPPERT, Joseph, SJ|5|
|484| DIROLF, Johann Philipp|4|
|485| DISTELHUSEN, Balthasar|3|
|486| DITTLER, Wilhelm|7|
|487| DONUNG, Stephan, SJ|9|
|488| DÖPPELIUS, Wilhelm|4|
|489| DORN, Franz, SJ|4|
|490| DORN, Ignaz, SJ|6|
|491| DORN, Petrus|7|
|492| DORSCH, Anton Joseph|27|
|493| DRAPP, Anton|5|
|494| DREIS, Wilhelm, SJ|7|
|495| DRIEL, Gottfried von|8|
|496| DÜCKER, Heinrich, SJ|11|
|497| DUDEN, Jakob|3|
|498| DÜNWALD, Damian Hartard|7|
|499| DÜNWALD, Philipp Franz|10|
|500| DÜNWALD, Ferdinand Heinrich von|9|
|501| DÜRKHEIMER, Nikolaus|11|
|502| DÜRR, Franz Anton Chrysostomus|21|
|503| EBEL, Anton \(Franz\)|6|
|504| EBERSHEIM, Ludwig|5|
|505| EBERSHEIM, Wilhelm|5|
|506| EBERSHEIM, Adam|9|
|507| EBERSHEIM, Gerhard|6|
|508| EBERWEIN, Matthäus|2|
|509| ECKARDT, Georg \[auch Johannes Georg\), SJ|7|
|510| ECKART, Johann Georg Joseph von|15|
|511| EGEL, Ambrosius, SJ|8|
|512| EHMICH, Matthias|5|
|513| EICKEMEYER, Johann Heinrich Rudolf|19|
|514| EIMER, Jodocus, SJ|13|
|515| EIMER, Ludwig, SJ|11|
|516| ELER, Andreas|11|
|517| ELER, Johannes|8|
|518| ELER, Kilian|5|
|519| EMUNTS, Johannes Thomas|13|
|520| ENGEL, Johann Michael \[Melchior\)|7|
|521| ENGELHARDT, Johann Martin|12|
|522| ENGELMOHR, \(Georg\) Joseph, SJ|11|
|523| ERBENIUS, Lubertus|4|
|524| ERBERMANN, Vitus, SJ|10|
|525| ERBIUS, Peter, SJ|7|
|526| ERNFELDERUS, Jacobus, SJ|7|
|527| ERNST, Anselm Franz Joseph|9|
|528| ESELER, Johannes|5|
|529| ETHEN, Bartholomaeus|2|
|530| ETTINGSHAUSEN, Fridericus|9|
|531| ETTINGSHAUSEN, Georg|3|
|532| ETZELIUS, Balthasar, SJ|6|
|533| EULER, Johannes Philipp|5|
|534| FABER, Carolus|5|
|535| FABER, Christoph|6|
|536| FABER, Heinrich|6|
|537| FABER, Johann \(Jonas\)|9|
|538| FABER, Johann Heinrich|7|
|539| FABER, Johannes|5|
|540| FABER, Laurentius|7|
|541| FABER, Petrus, SJ|3|
|542| FABRI, Johannes|1|
|543| FABRITIUS, Matthias, SJ|6|
|544| FALCKENSTEIN, Ludwig, SJ|5|
|545| FAULHABER, Johann Adam|13|
|546| FAUST, Franz Philipp|9|
|547| FAUST, Johannes|6|
|548| FAUST, Reinhardus, SJ|8|
|549| FECHEMER, Gerhardus|2|
|550| FEIERABENT, Joannes, SJ|2|
|551| FEYERTAG, Johann Magister|2|
|552| FIBIG, Johann|9|
|553| FICHARD, Johann Karl|7|
|554| FIMBERGER, Nikolaus, SJ|8|
|555| FINAEUS, Jacobus, SJ|4|
|556| FINCK, Ignatius, SJ|1|
|557| FINCK, Nikolaus|5|
|558| FINK, Konrad|6|
|559| FISCHER, Johann Gotthelf|9|
|560| FISCHER, Johann Nikolaus|3|
|561| FISCHER, Karl Franz|5|
|562| FISCHER, Nicolaus, SJ|8|
|563| FLACHSWEILER, Dietrich|5|
|564| FLACHSWEILER, Petrus|7|
|565| FLACHSWEILER, Theodor|3|
|566| FLUCKE, Joseph, SJ|4|
|567| FLUCKE, Lorenz, SJ|9|
|568| FORESII, Michael|1|
|569| FORTUNA, Jodocus|4|
|570| FRANCK, Franciscus|4|
|571| FRANCK, Georg Friedrich|5|
|572| FRANCK, Johannes Philippus|7|
|573| FRANK, Franz Philipp|11|
|574| FRANK, Peter Anton Freiherr von|16|
|575| FREISBACH, Johann Adam|10|
|576| FREYSLEBEN, Johann Georg|8|
|577| FRIDERICH, Philipp, SJ|8|
|578| FRIDWALD, Richard|4|
|579| FRIED, Johann Peter|9|
|580| FRIES, Ignatius, SJ|6|
|581| FRIES, Christophorus, SJ|9|
|582| FRITZ, Bernhard, SJ|9|
|583| FRÖHLING, Michael, SJ|10|
|584| FUCHS, Joseph|8|
|585| FUCHSIUS, Johannes, SJ|5|
|586| FUGGER von Kirchheim, Philipp Karl, Graf|5|
|587| FULLERUS, Joannes, SJ|1|
|588| FÜRDERER, Johannes|12|
|589| GAAR, Johann Georg, SJ|9|
|590| GALLADE, Peter, SJ|10|
|591| GÄRTLER, Johannes Adamus|14|
|592| GASSEL, Johannes|3|
|593| GEFFT, Nikolaus, SJ|7|
|594| GEIER, Balthasar|11|
|595| GEIGER, Friedrich, SJ|7|
|596| GEIGER, Joseph, SJ|4|
|597| GEISELBRUN, Joseph, SJ|4|
|598| GELDROPIUS, Erasmus, SJ|8|
|599| GEMER, Nicolaus, SJ|5|
|600| GEMMING, Johann Peter Joseph|7|
|601| GERAU, Johannes von|2|
|602| GERBEL, Nikolaus|9|
|603| GERBER, Johannes, SJ|7|
|604| GERGENS, Johann Franz|4|
|605| GERGENS, Peter|4|
|606| GERMERSHAUSEN, Lorenz|14|
|607| GERRESHEIM, Gerhard|5|
|608| GERSENIUS, Philipp, SJ|11|
|609| GEYER, Adam|1|
|610| GNADT, Hermann, SJ|8|
|611| GÖBEL, Johannes Gregorius \(Georg\)|9|
|612| GOEHAUSEN, Samuel, SJ|4|
|613| GOETZ, Johann Adam|7|
|614| GOETZ, Michael, SJ|6|
|615| GOLDHAGEN, Hermann, SJ|16|
|616| GÖPFERT, Georg, SJ|8|
|617| GÖPFFERT, Wilderich Christoph|7|
|618| GOTHELP, Bertold|3|
|619| GOTLIP, Adam|3|
|620| GOY, Jakob|3|
|621| GRAMBERT, Adam, SJ|13|
|622| GREBER, Bruno, SJ|11|
|623| GRESEMUND, Dietrich d\.Ä\.|15|
|624| GRESEMUND, Dietrich der Jüngere|21|
|625| GRIES, Johann Emmerich|2|
|626| GRUTER, Lambert|4|
|627| GUDENUS, Johann Christoph|14|
|628| GUDENUS, Johann Christoph von|7|
|629| GUDENUS, Urban Ferdinand|13|
|630| GÜNTHER, Franz, SJ|9|
|631| HAABER, Johann Friedrich|9|
|632| HAAN, Georg, SJ|10|
|633| HAAN, Wilhelm, SJ|5|
|634| HACK, Franz, SJ|6|
|635| HAGEN, Matthias Joseph|7|
|636| HAGEN, Edmund von|4|
|637| HAGEN, Paulus|1|
|638| HAGER, Johannes Balthasar, SJ|10|
|639| HAHN, Johann Philipp|13|
|640| HALENIUS, Georg, SJ|6|
|641| HALVER, Christian, SJ|4|
|642| HANDEL, Ignaz, SJ|6|
|643| HARDMANN, Jacobus, SJ|6|
|644| HARDY, Franz \(Theodor\), SJ|5|
|645| HAREN, Franz Rüdiger von|8|
|646| HARINGS, Paul, SJ|11|
|647| HARLASS, Georg, SJ|6|
|648| HARTLEBEN, Franz Joseph|15|
|649| HARTLEBEN, Theodor Konrad|14|
|650| HARTLIEB, Justus Jodocus|9|
|651| HARTMAN, Christian, SJ|7|
|652| HARTMANN, Johann Kaspar Anton|7|
|653| HARTMANN, Johannes, SJ|4|
|654| HARTUNG, Johannes, SJ|9|
|655| HAUBENREISSER, Peter|4|
|656| HAUCK, Christoph, SJ|10|
|657| HAUCK, Leonhard, SJ|8|
|658| HAUNOLD, Johann Maximilian von|7|
|659| HAUPT, Peter|8|
|660| HAUSEN, Conrad|1|
|661| HAUSER, Antonius|3|
|662| HAYL, Philipp, SJ|10|
|663| HAYSDORFF, Adam, SJ|7|
|664| HEBELIN von Helmbach, Johannes|3|
|665| HECK, Paul Xaveri van|2|
|666| HECKMANN, Johann Baptist \(Wendel\), SJ|12|
|667| HEDIO, Caspar|13|
|668| HEGER, Wilhelm|15|
|669| HEIDEL, Johann Philipp, SJ|8|
|670| HEIDEL, Wolfgang Ernst|8|
|671| HEIDER, Balthasar, SJ|8|
|672| HEILMANN, Georg Karl|6|
|673| HEIM, Hugo, SJ|10|
|674| HELDING, Michael|10|
|675| HELFERICUS de Bobenhausen|2|
|676| HELLING, Godefridus, SJ|4|
|677| HELSINGER, Adam|7|
|678| HENNER, Blasius, SJ|6|
|679| HENNER, Georg, SJ|7|
|680| HENSEL, Konrad|8|
|681| HERDT, Alexander, SJ|9|
|682| HERMANN, Gottfried, SJ|8|
|683| HERNSSHEIMER, Peter|3|
|684| HEROLD, Heinrich|2|
|685| HERTLING, Nikolaus, SJ|9|
|686| HESSENHOVER, Johann Heinrich|8|
|687| HETTERSDORF, Johann Michael|20|
|688| HETTISCH, Lubentius|9|
|689| HEUN, Quirinus|6|
|690| HEUSSER, Nikolaus Karl|6|
|691| HEYDT, Adam, SJ|8|
|692| HEYL, Johannes|2|
|693| HEYSESHEIM, Stephan|2|
|694| HIEGELL, Johann Kraffto|17|
|695| HILLMANN, Heinrich, SJ|7|
|696| HIMJOBEN, Jacobus, SJ|6|
|697| HOBER, Hermann Joseph|11|
|698| HOEGEL, Johann Joseph|11|
|699| HOEMANS, Joannes \(Domelang\)|5|
|700| HOEPFFNER, Franz Michael|5|
|701| HOFFER, Gottfried, SJ|5|
|702| HOFFMANN, Estherus|7|
|703| HOFFMANN, Anton|7|
|704| HOFFMANN, Cornelius Erwin|3|
|705| HOFFMANN, Georg, SJ|5|
|706| HOFFMANN, Johannes|6|
|707| HOFMANN, Andreas Joseph|11|
|708| HÖGLEIN, Ambrosius, SJ|11|
|709| HÖGLEIN, Johannes|7|
|710| HÖGLEIN, Johannes Ambrosius|7|
|711| HÖGLEIN, Kaspar, SJ|7|
|712| HÖGLEIN, Valentin, SJ|5|
|713| HOHENSTATT, Johann Martin|8|
|714| HOHENSTATT, Martin|6|
|715| HÖHN, Nikolaus, SJ|10|
|716| HOLTHOF, Franz|10|
|717| HOLTMANN, Gerhard|3|
|718| HOLTMANN, Nikolaus|3|
|719| HOLTMANN, Wilhelm|4|
|720| HOLTZGREVEN, Heinrich|5|
|721| HOLTZKLAU, Thomas, SJ|7|
|722| HOLTZMANN, Friedrich, SJ|5|
|723| HOLTZWEILER, Florentin|3|
|724| HOLZERUS, Leonhard, SJ|5|
|725| HOLZHEUSER, Joannes|2|
|726| HONCAMP, Georg Ferdinand|8|
|727| HÖNICKE, Mathias, SJ|8|
|728| HOOF, Johann Georg \(August\)|11|
|729| HOPFF, Kaspar, SJ|7|
|730| HORBELT, Johannes |6|
|731| HORCHER, Philipp|6|
|732| HORION, Johannes, SJ|8|
|733| HORIX, Johann Baptist|24|
|734| HORNIG, Joseph, SJ|6|
|735| HÖRNIGK, Ludwig von|20|
|736| HORODAM, Sebastian Franz|11|
|737| HUBEN, Franz, SJ|7|
|738| HUFFNAGEL, Theodor, SJ|10|
|739| HUTTICH, Johannes|11|
|740| INDANUS, Gordianus|1|
|741| INGENHEIMER, Georg|2|
|742| INTZ, Nicolaus, SJ|10|
|743| ISENBIEL, Lorenz|11|
|744| ISING, Gerhard|8|
|745| ISING, Gerhard d\.J\.|4|
|746| ISING, Johannes|3|
|747| ITTNER, Franz Georg Ignaz|11|
|748| ITTSTEIN, Anton Franz|9|
|749| ITTSTEIN, Christian Franz|6|
|750| ITZSTEIN, Franz Erwin Sebastian|3|
|751| ITZSTEIN, Anton Franz|9|
|752| ITZSTEIN, Faustinus, SJ|10|
|753| ITZSTEIN, Wilhelm, SJ|5|
|754| JACOBI, Johannes|4|
|755| JAEGER, Daniel|2|
|756| JAEGER, Johann Christoph|1|
|757| JAEGER, Johann Philipp Franz|8|
|758| JÄGER, Johann Valentin|7|
|759| JÄGER, Johann Wilhelm Heinrich|3|
|760| JANSON, Johannes Daniel|5|
|761| JENNI, Franz, SJ|4|
|762| JODOCUS von Gelnhausen|3|
|763| JORDAN, Ambrosius|4|
|764| JOSS, Andreas von|5|
|765| Judden, Johann von|6|
|766| JUNG, Johannes|2|
|767| JUNG, Johannes, SJ|16|
|768| JUNG, Simon|8|
|769| KARBACH, Nikolaus|6|
|770| KAUFF, Johannes|1|
|771| KAUFF, Dietrich|12|
|772| KAUPERS, Heinrich Matthias|8|
|773| KAUTH, Adam Franz|8|
|774| KEIM, Jakob|4|
|775| KELLER, Johann Christoph Chrysostomus von|11|
|776| KENNICKEN, Konrad|6|
|777| KENNIKEN, Wigand|8|
|778| KERBECKIUS, Antonius|7|
|779| KESSE, Heinrich|4|
|780| KILBER, Heinrich, SJ|17|
|781| KIRCHNER, Melchior, SJ|8|
|782| KIRN, Christoph, SJ|11|
|783| KIRSINGER, Wilhelm, SJ|6|
|784| KISELIUS, Philipp, SJ|10|
|785| KLEINER, Joseph, SJ|10|
|786| KLUNCKHART, Anton|7|
|787| KNAUD, Johann Valentin|2|
|788| KNAUER, Anton|4|
|789| KNODT, Heinrich|10|
|790| KOCH, Jakob|9|
|791| KOCH, Johann Daniel|3|
|792| KOCH, Johann Friedrich|13|
|793| KOCKANSKI, Adam, SJ|6|
|794| KOELER, Johann Martin Franz|4|
|795| KOELER, Georg Ludwig|4|
|796| KOELSCH, Karl Joseph|5|
|797| KÖHLER, Andreas|1|
|798| KÖHLER, Anton Philipp Thomas|9|
|799| KÖHLER, Johann Stephan \(Gregorius\)|21|
|800| KOLB, Johannes|1|
|801| KOLER, Jakob|5|
|802| KOLLIGS, Johann Philipp|7|
|803| KOLTZ, Philipp|6|
|804| KÖNIG, Philipp Ludwig|2|
|805| KONRAD, Peter|11|
|806| KRANEBIETER, Johann|2|
|807| KRAPFF, Johann Wolfgang|3|
|808| KRAUSS, Johann Konrad|6|
|809| KREBS, Heinrich, SJ|9|
|810| KREBS, Johann Adam|9|
|811| KREICH, Lorenz|6|
|812| KRESS, Michael, SJ|4|
|813| KREUSSLER, Johann Martin Ignaz, SJ|10|
|814| KRICK, Johann Baptist|15|
|815| KUHN, Kaspar|4|
|816| KUHN, Andreas, SJ|3|
|817| KÜHORN, Jakob Walther V|5|
|818| KÜHORN, Bernhard|5|
|819| KÜHORN, Johannes d\.Ä\.|6|
|820| KÜHORN, Johannes d\.J\. |7|
|821| KÜHORN, Johannes, SJ|10|
|822| KÜLSHEIMER, Johann Christoph|5|
|823| KUMMET, Caspar, SJ|8|
|824| KUNCKEL, Quirinus|18|
|825| KUNIGSTEIN, Johann von|1|
|826| KÜNNEN, Heinrich|3|
|827| KUPPEL, Martin|4|
|828| KYSLER, Heinrich|2|
|829| LACK, Damian|4|
|830| LADRONE, Konrad|16|
|831| LAMBERTI, Gerhard|7|
|832| LANDVOGT, Johannes|6|
|833| LANGEN, Friedrich Lorenz Theodor|10|
|834| LANGEN, Johannes Wilhelm|3|
|835| LANGMESSER, Cuno, SJ|10|
|836| LANKLOTZ, Heinrich|6|
|837| LAPICIDA, Johannes|3|
|838| LARES, Nicolaus, SJ|8|
|839| LASSER, Johann Friedrich von|12|
|840| LASSER, Johannes Jacobus von|10|
|841| LATOMUS, Johannes, SJ|8|
|842| LAUTENBACH, \(Johannes\) Christophorus|12|
|843| LAUTERBACH, Ambrosius|5|
|844| LEBERG, Johannes|3|
|845| LEIMGRÜBER, Georg, SJ|5|
|846| LEISS, Heinrich, SJ|7|
|847| LENNEP, Adolph, SJ|6|
|848| LENNEP, Johannes Theodor, SJ|9|
|849| LEO, Johannes, SJ|7|
|850| LEYDIG, Peter Joseph|9|
|851| LIEB, Anselm Franz d\.J\.|8|
|852| LIEB, Anselm Franz, d\.Ä\.|7|
|853| LIEB, Gottfried Christian|9|
|854| LIEBRECHT, Christian, SJ|10|
|855| LIMMER, Christoph, SJ|8|
|856| LINCKENHELD, \(Franz\) Kaspar|12|
|857| LINDE, Albert Wilhelm|1|
|858| LINDLA, Christoph \(Christian\)|7|
|859| LINN, Johannes, SJ|8|
|860| LINTZ, Valentin, SJ|4|
|861| LIPP, Johann Jakob|4|
|862| LISIGNOLO, Nikolaus|7|
|863| LOBBETIUS, Lambertus, SJ|5|
|864| LÖFFLER, Johann Friedrich|6|
|865| LOHNMÜLLER, Andreas, SJ|10|
|866| LÖHR, Johann Adam|3|
|867| LOOS, Cornelius \(Callidius\)|7|
|868| LOPPER, Peter, SJ|7|
|869| LOSSMANN, Georg, SJ|4|
|870| LOTH, Sebastian|15|
|871| LUCA, Carl Joseph|12|
|872| LUCIENBERGIUS, Johann|3|
|873| LUDOLPH, Hieronymus \(von\)|11|
|874| LUDWIG, Andreas|5|
|875| LUDWIG, Martin, SJ|15|
|876| LUERS, Valentin|3|
|877| LUTZ, Adam|7|
|878| LUTZ, Bartholomaeus, SJ|8|
|879| LUTZ, Nicolaus, SJ|6|
|880| MAHS, Konrad|10|
|881| MAIER, Andreas|4|
|882| MANDEL, Bernhard Gottfried|10|
|883| MANDT, Damianus, SJ|11|
|884| MANGOLT, Josef, SJ|7|
|885| MANTZ, Joseph Thomas|6|
|886| MARCELLI, Henricus, SJ|9|
|887| MARCHAND, Anton Maria|3|
|888| MARTINI, Augustinus|12|
|889| MASION, Tossanus, SJ|9|
|890| MASSET, Konrad, SJ|10|
|891| MAURER, Johannes|5|
|892| MAYER, Martin Simplicius|9|
|893| MEDER, Hieronymus|2|
|894| MEDICUS, Georg Friedrich|6|
|895| MEGELE, Franz Ulrich|7|
|896| MENSHENGEN, Heinrich, SJ|10|
|897| MENSHENGEN, Johannes Petrus|6|
|898| MENZINGER, Johannes|4|
|899| MERCURIANUS, Johannes, SJ|5|
|900| MERGENTHEIM, Johannes|2|
|901| MERGET, Georg Adam|7|
|902| MERSTETTER, Jakob|7|
|903| MERTZ, Quirinus von|9|
|904| METTERNICH, Anton Franz|11|
|905| METTERNICH, Mathias|15|
|906| MICHAEL, Johann Friedrich|8|
|907| MICHAEL, Petrus, SJ|8|
|908| MILETUS, Vitus|11|
|909| MINSINGEN, Albert von |5|
|910| MINTZENTHALER \(Münzenthaler\), Gabriel|2|
|911| MOCKEL, Ignatz, SJ|10|
|912| MOECKEL, Peter Paul|11|
|913| MOELLER, Johann Conrad|6|
|914| MOEREN, Johann Theodor|2|
|915| MOERZER, Johann Reinhard|12|
|916| MOERZER, Emanuel|7|
|917| MOHR, Etherius|6|
|918| MOHR, Philipp|5|
|919| MOLITOR, Bartholomaeus, SJ|8|
|920| MOLITOR, Kaspar, SJ|10|
|921| MOLITOR, Martin, SJ|13|
|922| MOLITOR, Nikolaus Karl|15|
|923| MOLITOR, Valentin Friedrich|9|
|924| MOLITORIS, Tobias Robert|3|
|925| MOLL, Friedrich Rudolf|7|
|926| MOLL, Georg Wilhelm|5|
|927| MOLL, Justus Philipp|7|
|928| MOLSTETTER, Johann Peter|9|
|929| MONBROT, Henricus|2|
|930| MONTFORT, Cornelius|7|
|931| MÖRING, Johannes|7|
|932| MÖRZER d\.J\., Johann Reinhard|10|
|933| MOSER, Joseph Nikolaus|5|
|934| MOYNHARDT, Johannes|3|
|935| SPITZNAES, Johannes, SJ|10|
|936| MÜLLENKAMPF, Franz Damian Friedrich|5|
|937| MÜLLER, Johann Caspar|9|
|938| MÜLLER, Johann Heinrich|11|
|939| MÜLLER, Johann Kaspar|6|
|940| MUNCK, Johannes|5|
|941| MURMAN, Gerhard, SJ|4|
|942| MUSERUS, Petrus, SJ|3|
|943| NAU, Bernhard Sebastian|14|
|944| NAUHEIMER, Johann Jakob|11|
|945| NAUHEIMER, Kilian, SJ|7|
|946| NAUMANN, Georg|5|
|947|GRAU, Friedrich|13|
|948| NEBEL, Anton, SJ|6|
|949| NEBEL, Christoph|19|
|950| NEBEL, Constantin|3|
|951| TODT, Konrad|7|
|952| NEEB, Johannes|10|
|953| NELLING, Johannes|5|
|954| NEUF, Franz, SJ|9|
|955| NEUREUTHER, Johann Georg|9|
|956| NEUSESSER, Johann Ernst|6|
|957| NEW, Rudolf, SJ|13|
|958| NEW, Richard|5|
|959| NICKENICH, Martin|9|
|960| NICOLEOS, Melchior, SJ|5|
|961| NIMIS, Johann Georg \(Norbert\)|19|
|962| NIMIS, Leonhard|12|
|963| NÖTHIG, Nikolaus|9|
|964| NYDAENUS, Adam, SJ|7|
|965| OFFENDAL, Peter|6|
|966| OLONIUS, Johannes|1|
|967| OPFERMANN, Paul, SJ|10|
|968| OPFFERMANN, Lukas, SJ|10|
|969| OPPENHEIMER, Johann Jakob|7|
|970| ORTLIEB, Hermann|4|
|971| OSTERMANN, Peter|2|
|972| OSTERROD, Wilhelm|4|
|973| OTTENDAL, Johann Christian von|8|
|974| OTTONIS, Johannes|2|
|975| PAULI, Nikolaus Theodor|9|
|976| PEETZ, Raymund|10|
|977| PEEZ, Raymundus|5|
|978| PEMPELFURT, Adolf von|11|
|979| PESTEL, Georg Philipp Adam|13|
|980| PETTMESSER, Ignaz \(Franz\), SJ|8|
|981| PFAFF, Johannes|14|
|982| PFEFFER, Heinrich, SJ|12|
|983| PFEFFER, Johann Adam|10|
|984| PFEIFFER, Johann Friedrich von|11|
|985| PFINGSTHORN, Lubentius|9|
|986| PFRIEMB, Joseph, SJ|9|
|987| PIERRE, Jean Claude|4|
|988| PISTORIUS, Henricus de Stollberg|1|
|989| PISTORIUS, Philipp Anton|2|
|990| PLEST, Sebastianus|4|
|991| PLETZ, Johannes, SJ|8|
|992| PLONIUS, Johann|1|
|993| PORTIUS, Johannes|2|
|994| POTH, Georg, SJ|10|
|995| POTTU, Nikolaus, SJ|9|
|996| PREIS, Johannes, SJ|8|
|997| PREUSS, Peter|7|
|998| PÜCHLER, Johannes|4|
|999| PUTZ, Albert vom|9|
|1000| QUATTERMART, Johannes|4|
|1001| QUIRINI, Johannes, SJ|8|
|1002| RAK, Johannes|14|
|1003| RANG, Kaspar, SJ|5|
|1004| RAPEDIUS, Franz, SJ|9|
|1005| RAPP, Johannes|3|
|1006| RATH, Martin|8|
|1007| RATH, Franciscus, SJ|5|
|1008| RATZEN, Johann Michael Ignaz|8|
|1009| RAUCH, Petrus|6|
|1010| RAVENNAS, Petrus|6|
|1011| REDLINGIUS, Johannes, SJ|2|
|1012| REFFEY, Henricus, SJ|8|
|1013| REICHARD, Kaspar, SJ|4|
|1014| REIDER, Bernhard Gottfried|10|
|1015| REIDER, Georg Adam|11|
|1016| REINECK, Johann Georg Wilhelm|8|
|1017| REINHARD, Konstantin|10|
|1018| REINHARD, Johann|2|
|1019| REIS, Jodocus|7|
|1020| REITZ, Nikolaus, SJ|10|
|1021| REMIGIUS|1|
|1022| RENARD, Johannes Claudius|10|
|1023| REUSS, Johannes|3|
|1024| REUTER, Jakob|6|
|1025| RHODIUS, Franz Anton|9|
|1026| RICHARDUS, Johannes |1|
|1027| RICHER|1|
|1028| RICHTER, Johann Christoph|5|
|1029| RICHTERGIN, Lambert|6|
|1030| RICKER, Gerhard|4|
|1031| RIEDESEL, Johann|3|
|1032| RIEDNER, Johann|3|
|1033| RIES, Johann Daniel Christoph, SJ|12|
|1034| RIMAEUS, Nicolaus, SJ|6|
|1035| RISSE, Johannes, SJ|7|
|1036| RITTER, Michael|5|
|1037| ROBERT, Urban, SJ|6|
|1038| ROBERTI, Jacobus, SJ|6|
|1039| ROBERTI, Johann, SJ|9|
|1040| RODE, Nikolaus|2|
|1041| ROEDER, Bartholomäus, SJ|8|
|1042| ROESTIUS, Petrus, SJ|8|
|1043| ROLANDI, Johannes|8|
|1044| ROOS, Godefridus, SJ|4|
|1045| ROSENCRANTZ, Georg|2|
|1046| ROSMANN, Joseph Matthias|8|
|1047| ROTH, Johann Richard von|20|
|1048| ROTH, Johann Wendelin|4|
|1049| ROTH, Johannes, SJ|8|
|1050| ROTH, Joseph Leopold|3|
|1051| ROTHENHAN, Marquard, SJ|8|
|1052| RUCKER, Nikolaus|7|
|1053| RÜDEL, Andreas, SJ|12|
|1054| RÜDING, Friedrich Wilhelm|9|
|1055| RUF, Wendelinus|5|
|1056| RUFFERT, Michael, SJ|6|
|1057| RUFSTEIN, Melchior|6|
|1058| RÜGER, Georg, SJ|6|
|1059| RUIDIUS, Stephanus, SJ|6|
|1060| RUSCHER, Thomas|8|
|1061| RUTH, Philipp Anton Ignaz|8|
|1062| SAMHABER, Alexander|1|
|1063| SANDÄUS, Maximilian, SJ|10|
|1064| SANDHOLZER, Friedrich|3|
|1065| SARTORIUS, Georg Jakob|6|
|1066| SARTORIUS, Eucharius, SJ|7|
|1067| SARTORIUS, Konrad, SJ|5|
|1068| SARTORIUS, Valerandus, SJ|1|
|1069| SATOR, Georg Friedrich|12|
|1070| SATTELBERGER, Heinrich, SJ|9|
|1071| SATTLER, Wilhelm|4|
|1072| SAUR, Georg, SJ|10|
|1073| SCH‚TZ, Jakob, SJ|11|
|1074| SCHAAB, Karl Anton|10|
|1075| SCHADE, Sebastian|5|
|1076| SCHÄFER, Johann Nepomuk, SJ|11|
|1077| SCHALCK, Adamus, SJ|2|
|1078| SCHALL, Friedrich Franz|9|
|1079| SCHATZ, Johannes, SJ|6|
|1080| SCHEIDEL, Franz Christoph|17|
|1081| SCHELL, Amandus|7|
|1082| SCHERER, Heinrich, SJ|5|
|1083| SCHEUBEL, Johannes|5|
|1084| SCHEUICHAVIUS, Gisbert, SJ|8|
|1085| SCHIFFELER, Petrus, SJ|1|
|1086| SCHILLING, Johannes|1|
|1087| SCHILLINGIUS, Michael, SJ|4|
|1088| SCHLARP, Johann|4|
|1089| SCHLAUN, Eucharius Dr\. jur\.|1|
|1090| SCHLAUN, Johann Franz|6|
|1091| SCHLEENSTEIN, Georg Adam|7|
|1092| SCHLEICHEL, Johannes, SJ|3|
|1093| SCHLEIFFERT, Michael|4|
|1094| SCHLÖR, Georg|15|
|1095| SCHLOSSBERG, Gottfried, SJ|7|
|1096| SCHLOSSER, Petrus|5|
|1097| SCHMELTZING, Georg, SJ|7|
|1098| SCHMIDT \(Schmitt\), Johann|3|
|1099| SCHMIDT, Christoph, SJ|7|
|1100| SCHMIDT, Friedrich Anton|7|
|1101| SCHMIDT, Georg Christoph|6|
|1102| SCHMIDT, Maximilian, SJ|5|
|1103| SCHMITT, Georg Konrad|5|
|1104| SCHMITT, Franz Jakob|6|
|1105| SCHMITT, Johannes|9|
|1106| SCHMITT, Philipp|1|
|1107| SCHÖFFERLIN, Bernhard|6|
|1108| SCHOLL, Bernhard|9|
|1109| SCHOMATZ, Peter, SJ|3|
|1110| SCHÖNHUBER, Johann Josef|4|
|1111| SCHÖNMAN, Markus, SJ|11|
|1112| SCHÖRLY, Johann Leonhard|15|
|1113| SCHRAUB, Georg|9|
|1114| SCHULTHEISS, Philipp Adam|16|
|1115| SCHULTHEISS, Johannes Benedikt|9|
|1116| SCHUNCK, Johann Peter|21|
|1117| SCHUSTER, Friedrich, SJ|10|
|1118| SCHWAAN, Peter, SJ|12|
|1119| SCHWALBACH, Peter|4|
|1120| SCHWALBACH, Philippus|2|
|1121| SCHWAN, Wolfgang, SJ|7|
|1122| SCHWARTZMANN, Johannes|9|
|1123| SCHWARZ, Franz, SJ|11|
|1124| SCHWEICKARD, Johann Gottfried|10|
|1125| SCHWEICKARDT, Kaspar|5|
|1126| SCHWIND, Christian|2|
|1127| SCHWIND, Jakob Anton|7|
|1128| SCRIPTORIS, Johannes|3|
|1129| SEIBAEUS, Ambrosius|12|
|1130| SEIDEL, Veit, Benediktiner|13|
|1131| SEILER, Georg|11|
|1132| SEITZ, Ignaz, SJ|5|
|1133| SELBACH, Jodocus|7|
|1134| SERARIUS, Nikolaus, SJ|9|
|1135| SERARIUS, Petrus, SJ|5|
|1136| SEUBERT, Joseph \(Anton\)|6|
|1137| SINZEL, Johann Nikolaus|10|
|1138| SOEHNCHEN, Peter|11|
|1139| SOMMER, Conrad|3|
|1140| SÖMMERING, Samuel Thomas|27|
|1141| SORBILLO, Johannes|4|
|1142| SPECHT, Georg, SJ|9|
|1143| SPEHR, Peter|4|
|1144| SPETH, Wolfgang, SJ|9|
|1145| SPIES, Valentin|6|
|1146| SPOOR, Franz Karl|4|
|1147| SPRINGINCLEE, Peter|5|
|1148| STARCK, Matthias|17|
|1149| STEGMANN, Sebastian|7|
|1150| STEICK \(Streick\), Stephan|1|
|1151| STEINBACH, Johannes, SJ|11|
|1152| STEINHAUSER, Johannes Michael|10|
|1153| STEINHÄUSER, Joseph, SJ|5|
|1154| STEINMETZ, Johann Jakob|4|
|1155| STEPECK, Johannes|5|
|1156| STEPHANI, Philipp, SJ|4|
|1157| STODTBROICH, Bernardus, SJ|2|
|1158| STOLTZ, Heinrich|3|
|1159| STRACK, Karl|12|
|1160| STRAUB, Franz Peter|5|
|1161| STRAUB, Georg, SJ|9|
|1162| STRAUSS, Johann Valentin|13|
|1163| STRAUSS, Georg Adam, SJ|7|
|1164| STREUN, Johannes, SJ|8|
|1165| STREVESDORFF von, Walther Heinrich|9|
|1166| STROBEL, Peter, SJ|8|
|1167| STUMPF, Johannes|6|
|1168| STUMPFF, Anselm Kasimir|4|
|1169| STURATH, Johannes, SJ|3|
|1170| SULZER, Heinrich|11|
|1171| SUSSMANN, Adam, SJ|6|
|1172| SYLVIUS, Theobald|2|
|1173| SYLVIUS, van den Bossche, Petrus, SJ|7|
|1174| THAMER, Theobald|11|
|1175| THEIN, Johann Georg|6|
|1176| THEVERN, Johannes|7|
|1177| THORWESTEN, Joseph, SJ|7|
|1178| THOSSANUS, Johannes, SJ|2|
|1179| THYRAEUS, Hermann, SJ|11|
|1180| THYRAEUS, Petrus, SJ|11|
|1181| THYRI, Friedrich Franz|11|
|1182| TINCTORIS, Rolinus|6|
|1183| TRAUPEL, Johannes|7|
|1184| TRAVELMANN, Johann Friedrich|5|
|1185| TRENTEL, Franz, SJ|9|
|1186| TURNICH, Heinrich|5|
|1187| UGELHEIMER, Johannes|4|
|1188| ULSENIUS, Dietrich \(Theoderich\)|7|
|1189| ULTSCH, Karl, SJ|4|
|1190| UNCKEL, Johannes|5|
|1191| UNGLEICH, Gottlieb|6|
|1192| UNKRAUT, Petrus Nikolaus|6|
|1193| VAETH, Georg, SJ|9|
|1194| VAGTZ, Johannes|8|
|1195| VECTORIS, Diether|5|
|1196| VIERSEN, Peter|6|
|1197| VILHAUER, Johannes|6|
|1198| VINCK, Antonius, SJ|9|
|1199| VINCKE, Friedrich, SJ|10|
|1200| VOGEL, Ignatius, SJ|9|
|1201| VOGELMANN, Heinrich|4|
|1202| VOGELMANN, Johannes|19|
|1203| VOGELMANN, Johannes Christoph|12|
|1204| VOGELMANN, Melchior Adolph|12|
|1205| VOGT, Anton, SJ|14|
|1206| VOGT, Franz|9|
|1207| VOGT, Johann Heinrich|9|
|1208| VOGT, Josef Theobald|5|
|1209| VOGT, Konrad|1|
|1210| VOGT, Nikolaus \(Niklas\)|17|
|1211| VOIT, Edmund, SJ|8|
|1212| VÖLCKER, Johann Jacob|9|
|1213| VOLMAR, Paul|3|
|1214| VOLMARUS, Heinrich|9|
|1215| VOLTZ, Anton \(Johannes\)|4|
|1216| VOLUSIUS, Adolf Gottfried|11|
|1217| VOMELIUS, Cyprian|13|
|1218| VONHOFF, Johannes|6|
|1219| VOSBACH, Jacob|2|
|1220| VOSS, Heinrich|4|
|1221| VOSS, Michael|11|
|1222| WACKER, Johann|8|
|1223| WAGENHAUSEN, Johannes|5|
|1224| WAGNER, Georg Joseph|11|
|1225| WAGNER, Pancratius|9|
|1226| WAHINGER, Johannes|6|
|1227| WALDMANN, Andreas|11|
|1228| WALDMANN, Philipp|9|
|1229| WALLENDORF, Johannes Joseph|6|
|1230| WALLRAFF, Arnoldus, SJ|6|
|1231| WANZOUL, Remigius, SJ|8|
|1232| WASMUTH, Johann Wendlin|8|
|1233| WASMUTH, Johann Heinrich|6|
|1234| WEBER, Christoph|11|
|1235| WEBER, Stephan|19|
|1236| WEBER, Theodor, SJ|9|
|1237| WEDEKIND, Georg Christian Gottlieb Theophil|20|
|1238| WEDEKIND, Liborius, SJ|5|
|1239| WEIDMANN, Conrad|8|
|1240| WEIDMANN, Johann Diether|9|
|1241| WEIDMANN, Johann Peter|14|
|1242| WEIDNER, Karl Veit|4|
|1243| WEIL, Bertulph|10|
|1244| WEILER, Heinrich, SJ|9|
|1245| WEINZ‚RL, Franz Gottfried|8|
|1246| WEISS, Adam|9|
|1247| WELDEN, Ludwig Konstantin|3|
|1248| WELDER, Jakob|17|
|1249| WENZEL, Josef Franz|10|
|1250| WENZEL, Josef Franz Ignaz Aloys|6|
|1251| WENZEL, Karl August|7|
|1252| WERLEIN, Wilhelm, SJ|7|
|1253| WERNER, Joseph, SJ|7|
|1254| WERREN, Johann Hermann Joseph|6|
|1255| WESTENBERGER, Heinrich, SJ|12|
|1256| WESTHAUSEN, Kaspar von|9|
|1257| WESTHOFEN, Georg Joseph|3|
|1258| WESTHOFEN, Karl Joseph|13|
|1259| WICK, Conradus, SJ|1|
|1260| WIDT, Johann Hugo|5|
|1261| WIEDENBRUCK, Wilhelm Theodor|6|
|1262| WIESE, Christoph Ignaz|9|
|1263| WIGAND, Andreas, SJ|8|
|1264| WILD, Augustinus, SJ|4|
|1265| WILL, Johann Rudolf|10|
|1266| WILL, Johannes, SJ|9|
|1267| WILTHELM, Lorenz|6|
|1268| WILTHELM, Mercurius|4|
|1269| WINAEUS, Petrus, SJ|12|
|1270| WINDISCHMANN, Karl Joseph Hieronymus|15|
|1271| WINK, Johann|1|
|1272| WITTICH, Ivo|19|
|1273| WITTMANN, Franz Joseph|6|
|1274| WITTMANN, Johannes Leonhard|10|
|1275| WOGER, Franz Valentin|9|
|1276| WOLF von Rosenbach, Philipp|4|
|1277| WOLFF, Johannes|2|
|1278| WOLFF, Adam, SJ|12|
|1279| WOLFF, Balthasar, SJ|9|
|1280| WOLFF, Franz Philipp|6|
|1281| WOLLENBERGER, Christophorus, SJ|7|
|1282| WONECKER, Johannes|2|
|1283| WUNDERLICH, Friedrich, SJ|12|
|1284| WUNDERLICH, Johann Michael|7|
|1285| WÜRDTWEIN, Maximilian|5|
|1286| WÜSTEFLED, Johann Friedrich|10|
|1287| ZEDER, Georg, SJ|8|
|1288| ZEHENDER, Bartholomäus|4|
|1289| ZENZEN, Thomas|7|
|1290| ZIEGLER, Johannes Reinhard, SJ|11|
|1291| ZIEGLER, Jakob|2|
|1292| ZILLIG, Nikolaus, SJ|8|
|1293| ZIMMERMANN, Philipp|3|
|1294| ZINCK, Ignaz, SJ|14|
|1295| ZINCK, Ludwig, SJ|8|
|1296| ZINCK, Wilderich, SJ|13|
|1297| ZINNER, Philipp, SJ|1|
|1298| ZIRCK, Michael, SJ|5|
|1299| ZOLLER, Georg, SJ|4|
|1300| ZULEHNER, \(Johannes\) Anton|10|
|1301| ZWEIFFEL, \(Johannes\) Jakob, SJ|10|
|1302|Johann Franz Aegidius \(Egid\) \(von\) BEAURIEUX \(zu SCHÖNBACH\)|22|
|1303|Johann Georg NEUREUTER|24|
|1304|Johann Christoph SPITZ|27|
|1305|Franz Wilhelm LOSKAND|23|
|1306|Ignaz Friedrich Maria Joseph Anton Apollinaris Canutus \(Freiherr von\) GRUBEN|53|
|1307|Franz Joseph Ignaz \(Freiherr von\) LINDEN|53|
|1308|Karl Friedrich August Philipp Freiherr von DALWIGK zu LICHTENFELS|31|
|1309|Johann Christoph Veit \(Edler von\) TÖNNEANN|15|
|1310|Johann Hermann Joseph Franz PAPIUS \(Freiherr von PAPE gen\. PAPIUS\)|20|
|1311|Philipp Karl \(von\) DEEL \(Edler zu DEELSBURG\) \(später: Freiherr DEEL von DEELSBURG\)|37|
|1312|Valentin Ferdinand \(Freiherr\) von GUDENUS|32|
|1313|Franz Joseph \(Freiherr von\) Albini|70|
|1314|Johann Christoph Joseph \(von\) SCHMITZ|41|
|1315|Ferdinand Heinrich \(Freiherr von\) DÜNWALDT \(Dünnwaldt, Dünwald, Dün\(n\)ewald\)|32|
|1316|Joseph Philipp \(Philipp Karl Joseph\) Graf zu SPAUR und FLAVON|21|
|1317|Johann Franz Valentin \(von\) EMMERICH|24|
|1318|Kaspar Anton \(Freiherr von\) Albini|30|
|1319|Friedrich Joseph Anton \(Freiherr\) von SCHMITZ \(zu GROLLENBURG\)|33|
|1320|Andreas \(Freiherr von\) STEIGENTESCH|73|
|1321|Johann Matthias \(Edler von\) COLL|30|
|1322|Johann Hugo Heinrich Franz von GAERZ \(Gaertz\)|16|
|1323|Johann Georg Jakob \(Freiherr von\) BORIÉ \(Beaurieux\) \(zu SCHÖNBACH\)|21|
|1324|Johann Franz Rudolf Nikolaus DEGEN|17|
|1325|Adolf Friedrich Rudolf Joseph \(Freiherr\) von TROTT zu SOLZ|24|
|1326|Johann Joachim Georg \(Freiherr\) von MÜNCH \(von/zu BELLINGHAUSEN\)|24|
|1327|Johann Ludwig Vollrath \(von\) FROHN|20|
|1328|Peter Joseph Melchior \(von\) HOMMER|26|
|1329|Johann Melchior CRAMER von CLAUSBRUCH|18|
|1330|Gerhard Georg Wilhelm Franz Xaver \(Freiherr von\) VOGELIUS|30|
|1331|Johann Arnold Heinrich Joseph CRAMER von CLAUSBRUCH|24|
|1332|Christian Franz \[von, S\.J\.\] WEIDENFELD|30|
|1333|Johann Stephan \(Edler von\) SPECKMANN|42|
|1334|Franz Georg \(Freiherr von\) LEYKAM|35|
|1335|Hermann Franz \(Edler von, des Heiligen Römischen Reichs Ritter\) SONBORN|24|
|1336|Aegidius \(Egid\) Valentin Felix \(Freiherr von\) BORIÉ \(Beaurieux\) \(zu SCHÖNBACH\)|40|
|1337|Philipp Heinrich \(Freiherr von\) REUSS \(Reuß\) \(genannt HABERKORN\)|33|
|1338|Johann Daniel Clemens \(von\) HUEBER \(von der WILTAU\) \(Wildau\)|27|
|1339|Theodor Karl Joseph Johann \(Edler\) de/von L'EAU|22|
|1340|Aloys Joseph Dominik Johann Franz \(Freiherr\) MAURER von KRONEGG zu Ungarshofen|26|
|1341|Karl Heinrich \(Edler\) von JODOCI|29|
|1342|Johann Peter \(von\) ORTMANN|34|
|1343|Heinrich Ludwig Karl \(von\) GEBLER, \(des Heiligen Römischen Reichs Ritter\)|28|
|1344|Maximilian Joseph Anton Joseph Nepomuk \(Freiherr von\) MARTINI|20|
|1345|Franz Valerius \(Edler von\) HAUER|27|
|1346|Aegidius Joseph Valentin Felix genannt Egid Joseph Karl von FAHNENBERG|37|
|1347|Gottfried Emanuel Friedrich Freiherr von ANDRIAN-WERBURG|19|
|1348|Franz Bernhard Joseph Freiherr von STEIN zu LAUSNITZ|44|
|1349|Karl Wilhelm Friedrich \(Freiherr\) von KÜNSBERG|21|
|1350|Joachim Leonhard SCHÜLL|24|
|1351|Leopold Philipp Albert Adolf Erhard Graf und Freiherr GALLER zu Schwanberg, Lannach und Waldschach|32|
|1352|Joachim Albert Johann Zacharias \(Freiherr von\) HESS|28|
|1353|Philipp Ernst \(Freiherr von\) REUSS \(genannt HABERKORN\)|16|
|1354|Joseph ULLHEIMER|31|
|1355|Johann Adam \(Freiherr von\) SCHROFF|41|
|1356|Johann Sebastian Nikolaus Tolentinus Erasmus Judas Thaddäus \(Freiherr\) von ZILLERBERG|29|
|1357|Johann Joseph Edler von WEINBACH|25|
|1358|Karl Ludwig \(Freiherr von\) BRANCA|38|
|1359|Adolf Karl Alexander Lothar \(Freiherr\) von ZEHMEN|25|
|1360|Johann Christian Joseph Freiherr von WALDENFELS|34|
|1361|Franz Christoph Heinrich Aloys \(Graf\) von Reigersberg|62|
|1362|Kaspar Philipp Joseph Franz \(Graf\) von SPIEGEL zum DIESENBERG\(-HANXLEDEN\)|41|
|1363|Paul Theodor \(von\) ANTHONI|31|
|1364|Johann Daniel Marianus FRANK|29|
|1365|Maria Joseph Graf FUGGER von DIETENHEIM|28|
|1366|Karl Kaspar \(Freiherr von\) HERTWICH|22|
|1367|Theodor Wilhelm Franz zum PÜTZ|22|
|1368|Johann Friedrich Joseph Anton CRAMER von CLAUSBRUCH|24|
|1369|Franz Arnold \(Freiherr\) von der BECKE|28|
|1370|Otto Heinrich \(Freiherr\) von GEMMINGEN-HORNBERG-Hoffenheim|21|
|1371|Johann Jacob Billstein|9|
|1372|Anselm Franz Molitoris|12|
|1373|Johann Arnold Schütz|6|
|1374|Johann Philipp Streit|92|
|1375|Johann Jacob Lincker|3|
|1376|Georg Melchior Klemens|2|
|1377|Johann Rudolph Cöler|22|
|1378|Johann Heinrich Demar|4|
|1379|\[Johann Michael\] Spönla|4|
|1380|Sigismund Gerstenberg|2|
|1381|Valentin Riehßen|2|
|1382|Daniel Mauritius von Gudenus|8|
|1383|\[Johann Arnold\] Schütz|4|
|1384|Johann Jakob Lincker von Lützenwick|3|
|1385|Christoph Ignaz Streit|4|
|1386|Wilhelm Heinrich Wincop|7|
|1387|Johann Daniel Streit|17|
|1388|Philipp Franz von Bellmont|36|
|1389|Johann Michael Rotermund|48|
|1390|Johann Michael Bockhlet|6|
|1391|Georg Melchior Gereon Molitoris|7|
|1392|Georg Melchior Clemens|10|
|1393|Melchior Ludolph Lilien|2|
|1394|Ernst Tentzel|81|
|1395|Konrad Wilhelm Strecker|241|
|1396|Gabriel Heinrich Lilien|2|
|1397|Ernst Immanuel Tentzel|1|
|1398|Johann Heinrich Meyer|14|
|1399|Christoph Ignaz von Gudenus|4|
|1400|\[Johann Philipp\] Streit|12|
|1401|\[Johann Daniel Richard\] Spönla|1|
|1402|\[Andreas Ignaz\] Meyer|1|
|1403|Johann Daniel Richard Spönla|3|
|1404|Andreas Ignaz Meyer|4|
|1405|Ernst Dominik Rhiesen|1|
|1406|Franz Emmerich Kaspar von Bilstein|2|
|1407|Anselm Franz Friedrich von Ingelheim|12|
|1408|Gereon Molitoris|16|
|1409|Johann Gerhard Bresano \[?\]|2|
|1410|Valentin Riehsen|2|
|1411|\[Elias\] Meltzer|5|
|1412|Hieronymo Schorchen|2|
|1413|Johann Georg Cöler|5|
|1414|Sigmund Gerstenberger|1|
|1415|Mauritius Gudenus|23|
|1416|Johann Mauritius Gudenus|56|
|1417|Johann Jakob von Gudenus|37|
|1418|Karl Joseph Adolph Lukas Freiherr Schenk Schmidburg|2|
|1419|Karl Theodor Anton Maria Kämmerer von Worms Freiherr von Dalberg|2|
|1420|Franz Damian Linden|3|
|1421|Adolph Freiherr von Bellmont|2|
|1422|Anselm Franz Ernst Freiherr von Warsberg|37|
|1423|Johann Daniel Christoph Freiherr Lincker von Lützenwick|17|
|1424|Ernst Wilhelm Strecker|34|
|1425|Peter Heinrich Heiland|43|
|1426|Johann Arnold von Bellmont|54|
|1427|Johann Arnold Freiherr von Bellmont|47|
|1428|Johann Georg Brückmann|95|
|1429|Daniel Moritz von Gudenus|3|
|1430|Friedrich Wilhelm Mosel von Alenstein|1|
|1431|Johann Christoph Spitz|68|
|1432|Alexander Bernhard Strecker|38|
|1433|Karl Wilhelm Joseph Adam Freiherr von Breidbach zu Bürresheim|3|
|1434|Johann Heinrich Genau|9|
|1435|Georg Mansuet Ignaz Ruding|1|
|1436|Georg von Klemens zu Millwitz|1|
|1437|Daniel Veit von Pipper|1|
|1438|Mauritius Bachmann|1|
|1439|Gustav Adolph Graberg|9|
|1440|Ernst Ludwig Wilhelm Freiherr von Dachröden|1|
|1441|Christian Joseph Freiherr von Benzel|1|
|1442|Friedrich Ludwig Döring|81|
|1443|Johann Adam Schmitt|2|
|1444|Georg Melchior von Klemens|1|
|1445|Elias Friedrich Heitmann|2|
|1446|Johann Adolph Weltz|32|
|1447|Georg Andreas Reinhard|4|
|1448|Johann Bernhard Müller|6|
|1449|Gottfried Spönla|1|
|1450|Matthias Joseph Anton Franz Matthes|1|
|1451|Anton Koch|11|
|1452|Siegfried Wilhelm Bollmann|3|
|1453|Joseph von Sänger|3|
|1454|Christoph Kerl|2|
|1455|Adam Friedrich Christian Reinhard|73|
|1456|Johann Joseph Appel|1|
|1457|Herrmann Pfingsten|2|
|1458|Franz Anton Resch|1|
|1459|Johann Nepomuk Christoph Hucke|1|
|1460|Franz Trömer|1|
|1461|Georg Friedrich Trott|1|
|1462|Eberhard Sigmund Wincop|342|
|1463|\[N\.N\.\] Fuxius|5|
|1464|Johannes Matthias Wincop|2|
|1465|Johann Veit Stumpelius|3|
|1466|Tobias Lagus \[?\]|3|
|1467|Johann Heinrich Daniel von Ritter zu Grünstein|2|
|1468|\[Johann Moritz\] Gudenus \[?\]|2|
|1469|Johann Michael Spohnla \[?\]|2|
|1470|Daniel Mauritius Gudenus|6|
|1471|Franz Hugo Hunoldt|5|
|1472|\[Adolph Freiherr\] von Bellmont|1|
|1473|\[Johann Jacob\] Lincker von Lützenwick|2|
|1474|Johann Arnoldt von Bellmont|2|
|1475|Mauritius von Gudenus|1|
|1476|Johann Moritz Gudenus|24|
|1477|Maria Magdalena Gudenus|1|
|1478|Casparus Junck|5|
|1479|Johann Heinrich Benedict Meier|4|
|1480|Johann Andreas Meyer|16|
|1481|Joachim Andreas Meyer|13|
|1482|Anselm Franz von Molitoris|4|
|1483|Karl Friedrich Strecker|16|
|1484|Wilhelm Moritz Strecker|13|
|1485|Josepha Strecker|1|
|1486|Karl Strecker|5|
|1487|Karl Wilhelm Strecker|2|
|1488|Johann Philipp Streidt|5|
|1489|Georg Heinrich von Ziegler|5|
|1490|Jacob Paul Heinrich Ziegler|1|
|1491|Georg Heinrich \(von\) Ziegler|3|
|1492|n/a|6541|
|1493|\[N\.N\.\] Papius|2|
|1494|Johann Hallenhorst|10|
|1495|Jacob Berger|18|
|1496|Georg Heinrich Ludolf|21|
|1497|Elias Melzer|3|
|1498|Hieronymus Schorch|17|
|1499|Gudenus|2|
|1500|Benjamin Schüz|1|
|1501|Johann Jacob von Bilstein|1|
|1502|Johann Pleikard Heinrich|1|
|1503|\[Anselm Franz\] Molitoris|9|
|1504|\[Johann Rudolph\] Cöler|6|
|1505|N\.N\. Mueß|1|
|1506|Dresanus|13|
|1507|\[Georg Marx\] Hahn von Königsburg|1|
|1508|\[Valentin\] Rhieß|1|
|1509|\[Hieronymus\] Schorch|4|
|1510|\[Sigmund\] Gerstenberger|1|
|1511|\[Christoph Ignaz\] Streit|3|
|1512|Matthiae|3|
|1513|Valentin Rhieß|4|
|1514|\[Friedrich Wilhelm\] Mosel von Alenstein|1|
|1515|\[Wilhelm Heinrich\] Wincop|4|
|1516|Johann Jacob von Gudenus|1|
|1517|Erhard Dresanus|1|
|1518|Georg Marx Hahn|1|
|1519|\[Johann Georg\] Cöler|5|
|1520|\[Johann Michael\] Booklet|1|
|1521|\[Georg Melchior Gereon\] Molitoris|3|
|1522|\[Georg Melchior\] Clemens|3|
|1523|Johann Philipp Demar|4|
|1524|Georg Friedrich von Creutz|1|
|1525|Georg Friedrich von Kreutz|1|
|1526|Johann Gerald Dresanus|1|
|1527|Valentin Rieß|1|
|1528|Maximilian Wagner|2|
|1529|Johann Daniel Lincker|6|
|1530|\[Johann Pleikard\] Heinrich|1|
|1531|Matthia|1|
|1532|\[Georg Marx\] Hahn|1|
|1533|Johann Michael Bockleth|2|
|1534|Siegfriedt Wilhelm Bollmann|1|
|1535|George Melchior Clemens|1|
|1536|Johann Rudolph Cöhler|2|
|1537|Hugo Frantz Hunoldt|1|
|1538|Johann Daniel von Lincker|1|
|1539|Elias Meltzer|26|
|1540|Philipp Georg Jerion Molitoris|1|
|1541|Adam Christian Reinhardt|4|
|1542|Jacob Ernestus Dominicus Riese|1|
|1543|Johann Ernst Dominicus Riese|4|
|1544|\[Conrad Wilhelm\] Streckerth|1|
|1545|Justus Christophorus Weltz|2|
|1546|Johann Ernst Fratzscher|4|
|1547|Christian Heinrich Weltz|24|
|1548|Christoph Reichhart|4|
|1549|Friedrich Wilhelm Stallforth|7|
|1550|Eberhardus Sigismundus Winkopp|3|
|1551|Hieronymus Friedrich Schorch|4|
|1552|Christian Wilhelm Schorch|6|
|1553|Johann David Schorch|8|
|1554|Johann Wilhelm Schorch|3|
|1555|Friedrich Christian Schorch|2|
|1556|Frantz Adam Bocklett|1|
|1557|Jacobus Franciscus Bocklet|1|
|1558|Ernestus Cöler|1|
|1559|Johann Adolph Cöler|2|
|1560|Johann Christian Gudenus|4|
|1561|Carl Friedrich Molitoris|1|
|1562|Johann Anton Pipper|1|
|1563|Jacobus Berger|1|
|1564|M\. Jacob Berger|7|
|1565|Maria Berger|5|
|1566|Agneta Weidmann|5|
|1567|Martha Berger|1|
|1568|Johann Jacobus Franciscus Spoenla|1|
|1569|Christoph Ignatius von Gudenus|4|
|1570|Christina Sophia Tentzel|7|
|1571|Carl Dresanus|2|
|1572|N\. Molitoris|3|
|1573|Anna Regina Cöler|1|
|1574|Philipp Johann Jacobi|5|
|1575|Martha Regina Gerstenberg|5|
|1576|Johann Joachim Gerstenberg|35|
|1577|Martha Sabina Cöler |2|
|1578|Georg Heinrich von Ziegler |2|
|1579|Philippina von Fensterer|1|
|1580|Catharina N\.N\.|1|
|1581|Theresia Rotermund|1|
|1582|Barbara N\.N\.|1|
|1583|Johann Wolfgang Jungk|39|
|1584|Clara Catharina Bader|10|
|1585|Martha Sophie Schmidt|7|
|1586|Johann Jacob Schmidt|15|
|1587|Martha Sophia Menius|2|
|1588|Justina Margaretha Schmidt |1|
|1589|Anna Christina Möltzer |1|
|1590|Johannes Stechanius|5|
|1591|Regina Magdalena Langguth|1|
|1592|Eva Maria Breitenbach|1|
|1593|Hieronymus Friedrich Breitenbach|6|
|1594|Anna Veronica Schwengfeld|1|
|1595|Maria Anna von Gudenus|1|
|1596|Moritz von Gudenus|2|
|1597|Martha Catharina Böning|1|
|1598|Anna Maria von Zwehl|1|
|1599|Johann Nicolaus Reinhardt|2|
|1600|Dorothea Wilhelmina Birnstiel|1|
|1601|Georg Heinrich Birnstiel |10|
|1602|Maria Josepha Rotermund|1|
|1603|Anna Philippina Meinong|1|
|1604|Magdalena Gudenus|1|
|1605|Sophia Josepha Rotermund |1|
|1606|Francisca Stahl |1|
|1607|Johann Adam Strecker |1|
|1608|Martha Adami|8|
|1609|Adelgunda Elisabeth Streit|1|
|1610|Johannes Laurentius Welsch|1|
|1611|Rosina Sophia Perthes|2|
|1612|Johann Justus Perthes|5|
|1613|Johanna Regina Hesse|1|
|1614|Heinrich Christian Weltz |8|
|1615|Eleonore Sophie Friese|12|
|1616|Rosina Catharina Ulle |2|
|1617|Georg Ulle |4|
|1618|Johannes Matthias Wincop |2|
|1619|Christina Schröder|1|
|1620|Michael Schröder|1|
|1621|Heinrich Enoch Ziegler|16|
|1622|Anna Regina von Brettin|6|
|1623|Heinrich Langguth|18|
|1624|Sophie Brochhausen|1|
|1625|Jost Brochhausen|35|
|1626|Johanne Christiane Kießling|1|
|1627|Johann Kießling|3|
|1628|Marie Dorothee Büchner|1|
|1629|Johann Christoph Büchner |2|
|1630|Catharina Dorothea Fischer|1|
|1631|Balthasar Fischer |1|
|1632|Johannes Schorch|2|
|1633|David Georg Ernemann|1|
|1634|Catharina Maria Vogel|1|
|1635|Christina Juditha Schorch|1|
|1636|Volckmar Schorch|2|
|1637|Juditha Dorothea Stiede|1|
|1638|Martha Rosina Beyer|1|
|1639|Johann Heinrich Rudolphi |1|
|1640|Martha Magdalena Fabritius|2|
|1641|Friederike Eleonore Weltz |3|
|1642|Susanna Christina Weltz |5|
|1643|Johann Valentin Friese|39|
|1644|Martha Sophia Schmatz|1|
|1645|Johann Carl Welz|1|
|1646|Johann Gottfried Spönla|4|
|1647|Johann Christoph Kerl|7|
|1648|Mathias Josephus Antonius Frantz Madhes|1|
|1649|\[Johann Bernhard\] Müller|1|
|1650|\[Gottfried?\] Spönla|1|
|1651|Emmerich Ernst Joseph Fuxius|1|
|1652|Melchior Gereon Molitoris|1|
|1653|\[Johann Adolph\] Cöler|1|
|1654|\[Sigismund\] Gerstenberg|2|
|1655|Wolff Christoph von Ziegler|1|
|1656|Antonetta Wilhelmina Ziegler|1|
|1657|M\. Jacobus Berger|1|
|1658|M\. Melchior Weidmann|9|
|1659|Anna Voigt|1|
|1660|Anna Berger |1|
|1661|Magdalena Berger|1|
|1662|Anna Mohr |1|
|1663|Johann Rehefeld|5|
|1664|Johann Melchior Förster|9|
|1665|Christoph Avianus|1|
|1666|Maria Salome Müller |1|
|1667|\[Philipp Franz\] von Bellmont|2|
|1668|\[Johann Michael\] Bocklet|4|
|1669|\[Johann Michael\] Bockleth|1|
|1670|\[Johann Philipp\] Dehmar|2|
|1671|\[Sigmund\] Gerstenberg|3|
|1672|\[Franz Hugo\] Hunold|2|
|1673|Johann Jacob Lincker \[von Lützenwick\]|1|
|1674|\[Johann Jacob\] von Lincker|5|
|1675|\[Gereon\] Molitor|1|
|1676|Johann Ernst Dominicus Riehs|1|
|1677|\[Johann Ernst Dominik\] Rhieß|1|
|1678|Valentin Riehse|1|
|1679|\[Valentin\] Riehse|2|
|1680|\[Valentin\] Rhies|1|
|1681|\[Valentin\] Rhiß|1|
|1682|\[Johann Michael\] Rotermund|2|
|1683|\[Johann Arnold\] Schüz|4|
|1684|\[Georg Marx\] Hahn \[von Königsburg\]|1|
|1685|\[Georg Freidrich\] von Kreuz|1|
|1686|\[Johann\] Hallenhorst|1|
|1687|\[Jacob\] Berger|1|
|1688|\[Georg Heinrich\] Ludolf|1|
|1689|Elias Andreas Stechan|1|
|1690|Sabina Magdalena Melzer|1|
|1691|Burckhardt Lincker|1|
|1692|Sibille Lincker|1|
|1693|\[N\.N\.\] Meinong|2|
|1694|\[N\.N\] Everts|1|
|1695|Johann Arnold von Bellmont |30|
|1696|Johann Daniel Christoph Freiherr Lyncker von Lützenwick|3|
|1697|Johann Arnold Freiherr von Bellmont |37|
|1698|Johann Daniel Heyland|1|
|1699|Johann Michael Rotermundt|59|
|1700|Johann Heinrich Rotermundt|6|
|1701|Johann Adam Strecker|16|
|1702|Johann Daniel Freiherr Lyncker von Lützenwick|5|
|1703|Johann Bartholomäus Brückmann|1|
|1704|Philipp Wilhelm von Boineburg|85|
|1705|Johann Christian von Boineburg |2|
|1706|Dieter Guillielmus Matthiae|2|
|1707|Anna Christina Schütz von Holzhausen|1|
|1708|Carl Wilhelm Joseph Adam Fraiherr von Breidbach zu Bürresheim|3|
|1709|Carl Anselm Freiherr von Breidbach zu Bürresheim|4|
|1710|Sophia Eleonora von Rothenhahn|1|
|1711|Joachim Andreas von Brettin|31|
|1712|Regina Dorothea von Seltzer|6|
|1713|Dorothea Sophia von Ziegler|2|
|1714|Heinrich Enoch von Ziegler|2|
|1715|Johann Heinrich M\. Riedel|11|
|1716|Martha Regina Gerstenberger|4|
|1717|Johann Rudolph Coeler|4|
|1718|Anna Regina Ilgen|2|
|1719|Sabine Magdalene Cöler|1|
|1720|Johann Joachim Gerstenberger|12|
|1721|Johann Georg Coeler|6|
|1722|Susanne Sabine Coeler|2|
|1723|Sigismund Gerstenberger|1|
|1724|J\[ohann\] V\[alentin\] Friese|1|
|1725|Eleonora Sophia Friese|1|
|1726|Caspar Friedrich Lentin|16|
|1727|M\. Johann Ludwig Döring|2|
|1728|Friederica Sophia Magdalena Döring|1|
|1729|Christiana Sibylla Weltz|1|
|1730|Henrietta Maria Weltz|1|
|1731|Martha Sophia Schmaltz|4|
|1732|Johann Jacob Gerstenberger|1|
|1733|Dorothea Regina Gerstenberg|2|
|1734|Joachim Gerstenberger|17|
|1735|Veronica Martini|6|
|1736|Johann Martini|4|
|1737|Marcus Gerstenberg|5|
|1738|Marcus Gerstenberger|1|
|1739|Justina Gerstenberger|1|
|1740|Johann Christoph Dehmar|1|
|1741|Regina Gerstenberger|2|
|1742|Heinrich Langut|3|
|1743|Dorothea Gerstenberger|4|
|1744|Johann Scheffer|2|
|1745|Veronica Gerstenberger|4|
|1746|Georg de Ahna|1|
|1747|Dorothea Hentrich|1|
|1748|Martha Catharina von der Sachsen |3|
|1749|Jacob von der Sachsen|14|
|1750|Jacobus Gerstenberger|1|
|1751|Martha Gerstenberger |3|
|1752|Hieronymus Gerstenberger |2|
|1753|Johann Heinrich Menius|9|
|1754|Catharina von Bodewitz|2|
|1755|Henrich Gerstenberg|3|
|1756|Henrich Rudolph Gerstenberger|2|
|1757|Johann Heinrich von Gerstenberg|4|
|1758|Sibylla Veronica Gerstenberg|2|
|1759|Anna Salome von Ehrenkron|2|
|1760|Hartmann Jacob von Ehrenkron|1|
|1761|Anna Salome de Lasser|1|
|1762|Daniel Mauritius de Gudenus|4|
|1763|Johannes Leopold von Gudenus|2|
|1764|Wilhelm Streit|6|
|1765|Henrich Adam Streit|2|
|1766|Urbanus Josephus Streit |1|
|1767|Georg Henrich Streit|2|
|1768|Johannes Mauritius Gudenus|15|
|1769|Johannes Hallenhorst|27|
|1770|Antonius Hallenhorst |2|
|1771|Anna Hövel|1|
|1772|Johannes Brandis |1|
|1773|Maria Brand |6|
|1774|Hieronymus Anthon Hallenhorst|1|
|1775|Heinrich Adam Hallenhorst|35|
|1776|Heinrich Brand|2|
|1777|Barbara Richthäuser |3|
|1778|Anne Sabine Ziegler|2|
|1779|Regina Sabina Hallenhorst|3|
|1780|Juditha Sophia Hallenhorst|3|
|1781|Johann Christoph Frikkinger |4|
|1782|Franz Leopold Hunold|3|
|1783|George Sigismund Hunold|3|
|1784|Caspar Jungk|16|
|1785|Justina Magdalena Schmidt |4|
|1786|Valentin Bader|9|
|1787|Catharina Herr|2|
|1788|Friderica Sophia Louise Jungk|1|
|1789|Johann Caspar Jungk |1|
|1790|Paulus Jungk|5|
|1791|Elisabeth Gärtner|1|
|1792|Friederike Sophie Louise Schmidt|2|
|1793|Christian Ferdinand von Zedtwitz |1|
|1794|Johanna Louise Schmidt|2|
|1795|Jacob Samuel Schmidt|2|
|1796|Tobias Lagus|20|
|1797|Catharina Margaretha Rennemann |3|
|1798|Dorothea Magdalena Brießmann|2|
|1799|Georg Heinrich Ludolph|8|
|1800|Georg Melchior von Ludolph|5|
|1801|Martha Benigna Schmidt|2|
|1802|Juditha Margaretha von Seltzer|3|
|1803|Jeremias Herbord von Seltzer|2|
|1804|Dorothea von Utzberg|3|
|1805|Melchior Schmidt|24|
|1806|Dietrich Wilhelm Matthaei|1|
|1807|Anna Regina Kniphoff|5|
|1808|Johann Melchior Kniphoff|25|
|1809|Dietrich Wilhelm Matthiae|17|
|1810|Johann Matthiae|2|
|1811|Magdalena Müller|1|
|1812|Cyriacus Müller |1|
|1813|Martha Ilgen|4|
|1814|Heinrich Ilgen der Jüngere|1|
|1815|Martha Mohr|2|
|1816|Anna Christina Meltzer|1|
|1817|Johann Stechanius|4|
|1818|Sabina Magdalena Wolff|2|
|1819|Henning von der Marthen|30|
|1820|Peter Cristian Frantz Pape|2|
|1821|\[N\.N\.\] Pape|1|
|1822|Johannes Christophorus Spitz|7|
|1823|Anselm Franz Ernst von Warsberg|42|
|1824|Johann Carl Weltz|3|
|1825|Martha Christina Sophie Brückner|2|
|1826|Hieronymus Friedrich Brückner|3|
|1827|Christoph Reichardt|8|
|1828|Johannes Weltz|18|
|1829|N\.N\.|1|
|1830|Catharina von Ryssel|1|
|1831|Johann Ludwig Döring|3|
|1832|Johann Heinrich Meier|26|
|1833|Johann Henrich Meier|8|
|1834|Eduard Brochhausen|2|
|1835|Lucia Biermann|1|
|1836|Judith Ludolff |1|
|1837|Hiob Ludolff |1|
|1838|Andreas Heinrich Brochhausen|1|
|1839|Johann Joachim Brochhausen|1|
|1840|Christina Brochhausen |1|
|1841|Johann Wilhelm Sömmering|9|
|1842|Regine Brochhausen |1|
|1843|Johann Ernst Brochhausen |1|
|1844|Jost Heinrich Brochhausen|2|
|1845|Johan Jacob Brochhausen|3|
|1846|Angela Brochhausen|1|
|1847|Tobias Emanuel Adami |16|
|1848|Anna Magdalena Brochhausen |1|
|1849|Johann Georg Evander|2|
|1850|Johann Jacob Waldbott von Bassenheim|1|
|1851|Barbara Brandt |3|
|1852|Heinrich Jacob Brandt|4|
|1853|David Brandt |4|
|1854|Martha Brandt |3|
|1855|Tobias Emmanuel Adami |3|
|1856|Balthasar Rudolph Brandt |3|
|1857|Hieronymus Brandt |3|
|1858|Conrad Theodoricus Brandt |2|
|1859|Christina Brandt |4|
|1860|Johann Melchior Brandt|2|
|1861|Maria Brandt |4|
|1862|Heinrich II Brandt|19|
|1863|Johann Jakob von Bielstein|4|
|1864|Agatha von Bingen|2|
|1865|Anna Maria Barbara von Bielstein|2|
|1866|Daniel Moritz Gudenus|17|
|1867|Johannes Michael Spoenla|2|
|1868|Beate Franziska Gudenus|5|
|1869|Maria Anna Gudenus|2|
|1870|Johann Gottfried von Spoenla|2|
|1871|Maria Josefa Salome Gudenus|2|
|1872|Hiob Ludolf |2|
|1873|Judith Brandt|4|
|1874|Maria Katharina Böning|3|
|1875|Adelgunde Gudenus |3|
|1876|Maria Theresia Gudenus |3|
|1877|Carl Josef Dresanus|1|
|1878|Christoph Ignatius Gudenus|8|
|1879|Johann Leopold Gudenus|3|
|1880|Jacob Moritz Gudenus|2|
|1881|Franziska Beata Gudenus|3|
|1882|Johann Adam von Eck|2|
|1883|Friedrich Wilhelm Gudenus|6|
|1884|Anna Elisabeth Maria Emilia von Tattenberg und Rheinstein|2|
|1885|Johann Daniel Gudenus |2|
|1886|Johann Jakob Gudenus|5|
|1887|Franz Christoph Gudenus|2|
|1888|Maria Katharina Gudenus|2|
|1889|Beata Stein|3|
|1890|Hans Stein|1|
|1891|Elisabeth Ziegenhorn|1|
|1892|Johann Daniel Gudenus|12|
|1893|Anna Katharina Gudenus|3|
|1894|N\.N\. Wedelmann|1|
|1895|Anna Beate Gudenus |3|
|1896|Anna Christiana Gudenus|3|
|1897|Johann Dietrich Theodor Heiland|1|
|1898|Johann Christoph Gudenus|11|
|1899|Maria Clara Thavonath|2|
|1900|Urban Ferdinand Gudenus |11|
|1901|Lotharia Mechtildis von Birkig|2|
|1902|Georg Friedrich Gudenus|7|
|1903|Johanna Franziska von Birkig|2|
|1904|Dorothea Sibylla von der Weser|2|
|1905|Magdalene Franziska Isselbach|2|
|1906|Johanna Klara Gudenus|2|
|1907|Christoffel Gudenus|4|
|1908|Ursula vom Hoffe|1|
|1909|Johannes d\.Ä\. Gudenus|2|
|1910|Margaretha Gudenus|2|
|1911|Johannes d\.J\. Gudenus|2|
|1912|Anna Salome Jacobi von Ehrencron|2|
|1913|Maria Josefa Felizitas Gudenus|2|
|1914|Johann Georg Mauritius Gudenus|2|
|1915|Maria Franziska Theresia Josefa Gudenus|2|
|1916|Maria Katharina Barbara Anastasia Gudenus|3|
|1917|Philipp Wilhelm Meinong|3|
|1918|Friedrich Wilhelm Moritz Bernhard Gudenus|3|
|1919|Johann Jakob Josef Franz Gudenus|8|
|1920|Eva Sabina Straub|1|
|1921|F\. L\. Löber|3|
|1922|Benedikt von Döttinchem|1|
|1923|Christoph Ignatz Alois Gudenus|4|
|1924|Maria Philippina Theresia Rotermund|2|
|1925|Philippina von Bellmont|1|
|1926|Ursula Loscant|2|
|1927|Anselm Friedrich Adolf Gudenus|4|
|1928|Johann Adolf Damian Gudenus|3|
|1929|Mauritius Ferdinand Anton Gudenus|3|
|1930|Maria Magdalena Sidonia Gabriela Theresia Gudenus|6|
|1931|Hans Hugold Strecker|6|
|1932|Anna Maria Sältzer|2|
|1933|Maria Agnes Jordan|1|
|1934|Maria Katharina Strecker|2|
|1935|Johann Valtin Kaltwasser|1|
|1936|Philipp Kaspar Strecker|1|
|1937|Johann Christoph Strecker|4|
|1938|Elise Ständer|1|
|1939|Johann Hugo Strecker|3|
|1940|Elisabeth Wolf|1|
|1941|Johann Franz Strecker|4|
|1942|Apollonia Elise Marie Simon|1|
|1943|Maria Anna Strecker|2|
|1944|Dorothea Elisabeth Strecker|3|
|1945|Hans Georg Hentrich|2|
|1946|Georg Heinrich Gottlieb Strecker|2|
|1947|Maria Anna Wagner|1|
|1948|Maria Maximilia Christina Antonetta Strecker|2|
|1949|Anna Catharina Wilhelmina Josepha Strecker|2|
|1950|Francisca Renata Elisabeth Stahl|2|
|1951|Ivo Johannes Stahl|2|
|1952|Catharina Molitoris|1|
|1953|Alexander Johann Strecker|6|
|1954|Maria Susanna von Zwehl|3|
|1955|Johann Herwig von Zwehl|1|
|1956|Maria Anna Francisca Renata Strecker|2|
|1957|Maria Wilhelmina Josepha Strecker|1|
|1958|Karl Wilhelm Anton Strecker|5|
|1959|Johann Bernhard Strecker|1|
|1960|Ernst Friedrich Hugo Strecker|3|
|1961|Alexander Bernhard Johann Nepomuk Strecker|2|
|1962|Maria Anna Josepha Thecla Strecker|3|
|1963|N\.N\. Strecker|1|
|1964|Adam Ignatz Turin|15|
|1965|Maria Anna Francisca Wagner|1|
|1966|Agnes Turin|1|
|1967|Maria Francisca Renate Strecker|1|
|1968|Friedrich Christian August Strecker|6|
|1969|Franciscus Jacobus Johannes Nepomuk Strecker|2|
|1970|Josepha Rotermund|1|
|1971|Sophia Katharina Josepha Strecker|2|
|1972|Karl Friedrich Wunderlich|7|
|1973|Susanna Josepha Strecker|3|
|1974|Johann Jakob Dominicus|5|
|1975|Henricus Strecker|2|
|1976|Maria Apollonia Wilhelmina Susanna Strecker|2|
|1977|Ernst III Tentzel|20|
|1978|Regina Elisabeth Tentzel|3|
|1979|Friedrich Heinrich Jakob|2|
|1980|Christine Elisabeth Tentzel|1|
|1981|Hieronymus Gottlieb Tentzel|6|
|1982|Johann Friedrich Tentzel|6|
|1983|Ernst Emanuel Tentzel|9|
|1984|Salome Sophia Tentzel|2|
|1985|Christian Friedrich Schelhas|2|
|1986|Ernst I Tentzel|8|
|1987|Barbara Happe|1|
|1988|Ernst II Tentzel|7|
|1989|Elisabeth Bonner|5|
|1990|Johann Gottlieb Adami|23|
|1991|Regina Brückner|7|
|1992|Regina Adami|2|
|1993|Rudolph Adami|2|
|1994|Johann Christian Tentzel|5|
|1995|Stephan Bonner|5|
|1996|Anna Siebold|1|
|1997|Friedrich Heinrich Jacobs|5|
|1998|Heinrich Adam Streit|1|
|1999|Juditha Margaretha Döring|2|
|2000|Hiob Ludolph|10|
|2001|Sabine Magdalene von Eberbach|2|
|2002|Benigna von der Sachsen|6|
|2003|Adam Ignatius Turin|10|
|2004|Tobias Adami |13|
|2005|Johann Mauritz Bodo Gudenus|2|
|2006|Christian Wilhelm von Brettin|12|
|2007|Henricus Langut|1|
|2008|Dorothea von der Sachsen|3|
|2009|Johannes Martini|6|
|2010|Veronica Kronenberger|2|
|2011|Henning Rennemann|119|
|2012|Margaretha Sprocovius|3|
|2013|Lydia Rothart |5|
|2014|Maria Northausen |2|
|2015|Justus Josias Rennemann |6|
|2016|Helmoldevigus Rennemann|2|
|2017|Franz Mauritius Bachmann|5|
|2018|Franz Moritz Bachmann|47|
|2019|Franz Moriz Bachmann|6|
|2020|Philipp Frantz von Bellmont|4|
|2021|Philipp Franciscus von Bellmont|12|
|2022|Karl Christian von Benzel|2|
|2023|K\[arl\] C\[hristian\] Graf von Benzel-Sternau|5|
|2024|K\[arl\] Ch\[ristian\] Graf von Benzel-Sternau|3|
|2025|Carl Christian E\. Graf Benzel-Sternau|2|
|2026|Karl Christian Ernst Graf von Benzel-Sternau|16|
|2027|Karl Christian Graf von Benzel-Sternau|23|
|2028|Christian Ernst Karl Graf von Bentzel-Sternau|43|
|2029|Gottfried von Benzel-Sternau|6|
|2030|Carl Christian Graf von Benzel-Sternau|15|
|2031|Christian Ernst Graf von Bentzel-Sternau|22|
|2032|Karl Graf von Bentzel-Sternau|16|
|2033|Johann Jakob Bentzell|2|
|2034|Anselm Franz von Bentzel-Sternau|12|
|2035|Karl Christian Ernst Graf von Bentzel-Sternau|59|
|2036|Philipp Wilhelm Freiher von Boyneburg|7|
|2037|Johann Christian Freiherr von Boineburg|7|
|2038|Philipp Wilhelm Reichsgraf von Boineburg|18|
|2039|Philipp Wilhelm Graf von Boyneburg|15|
|2040|Hugo Franz Hunold|6|
|2041|Anselm von Ingelheim|18|
|2042|Anselm Franz von Ingelheim|35|
|2043|Hans von Ingelheim|1|
|2044|Georg von Clemens-Millwitz|26|
|2045|N\.N\. von Clemens-Millwitz|1|
|2046|Andreas Reinhard|4|
|2047|Adam Christian Friedrich Reinhard|2|
|2048|Franz A\[nton\] R\[esch\]|1|
|2049|Franz Anton? von Resch|11|
|2050|Franz Anton von Resch|6|
|2051|N\.N\. von Ruding|2|
|2052|Georg Samuel Friedrich Trott|7|
|2053|Johann Christian von Boineburg|34|
|2054|N\.N\. von Boineburg|1|
|2055|Melchior Friedrich zu Schönborn|2|
|2056|Anna Sophia von Boineburg|1|
|2057|Johann Christian Baron von Boineburg|12|
|2058|Johann Christian von Boyneburg|27|
|2059|N\.N\. von Boyneburg|1|
|2060|Johann Christian Freiherr von Boyneburg|1|
|2061|Barbara von Buttlar|1|
|2062|Berthold Boineburg|1|
|2063|Friedrich Ludwig Doering|3|
|2064|N\.N\. Meier|1|
|2065|Moritz Gudenus|24|
|2066|Christoph Gudenus|3|
|2067|Beate Stein|1|
|2068|Ivo Johann Stahl|6|
|2069|Joachim Gerstenberg|22|
|2070|N\.N\. Menius|2|
|2071|Melchior Weidmann|5|
|2072|Christoph Ignaz Freiherr von Gudenus|18|
|2073|Anselm Friedrich von Gudenus|14|
|2074|Johann Philipp Jacobi|4|
|2075|Friedrich Leonhard Löber|12|
|2076|Georg Melchior von Ludolff|6|
|2077|George Melchior von Ludolf|14|
|2078|Georg Melchior von Ludolf|45|
|2079|Martha Benigna Schmidt\]|1|
|2080|Sophia Dorothea Faligken|2|
|2081|Christian Friedrich Schellhas|11|
|2082|Adam Ignaz Turin|6|
|2083|Tobias Adami|22|
|2084|Georg Melchior von Clemens|9|
|2085|Maria Josepha Theresia Molitoris|2|
|2086|Anna Josepha Wallburgis von Clemens|1|
|2087|Robert Balthasar von Clemens|4|
|2088|Maria Margaretha von Clemens|2|
|2089|Anna Josepha von Clemens|1|
|2090|Susanna Theresia Fritz|1|
|2091|N\.N\. Fritz|1|
|2092|Catharina Höglein|1|
|2093|M\. E\. L\. \[?\] von Gerstenberg|2|
|2094|N\.N\. von Sommerlatte |2|
|2095|Charlotte von Bellmont|1|
|2096|N\.N\. Reinhard|3|
|2097|Siegfried Willhelm Bollmann|4|
|2098|Gottfried Spoenla|6|
|2099|Alexander Bernhard\] Strecker|2|
|2100|Siegfried Wilhelm\] Bollmann|3|
|2101|Franz Madhes|1|
|2102|Johann Heinrich\] Genau|2|
|2103|Tobias Emanuel Adami|2|
|2104|Maria Angelica Bendleb|1|
|2105|M\. Joh\. Ludwig Döring|1|
|2106|Gustavus Adolphus Graberg|6|
|2107|Christian Samuel Graberg|6|
|2108|Eva Eleonora Schmidt|1|
|2109|Rosina Chrisitna Fratzscher|2|
|2110|Peter Heinrich Jacob Heylandt|3|
|2111|Johann Jakob Josef Benzel|1|
|2112|Franz Anselm Freiherr von Benzel|2|
|2113|Anselm Franz Freiherr von Benzel|1|
|2114|Joseph Matthias Frantz Matthes|3|
|2115|Justus Christoph Weltz|2|
|2116|Christoph Wilhelm Immanuel Reichart|4|
|2117|Johann Jacob Frantz Spoenla|1|
|2118|Carl Wilhelm Strecker|4|
|2119|Moritz Bachmann|2|
|2120|Arnold von Bellmont|3|
|2121|Karl von Benzel|2|
|2122|Johann Jakob Josef Franz von Gudenus|4|
|2123|Christoph Ignaz Gudenus|1|
|2124|Hieronymus Anton Hallenhorst|4|
|2125|Christoph Ignaz Aloys von Gudenus|2|
|2126|Johannes Moritz Gudenus|2|
|2127|Johannes Leopold Gudenus|1|
|2128|Friedrich Wilhelm Moritz Bernhard von Gudenus|2|
|2129|Adolf Johann Sigismund von Gudenus|2|
|2130|Moritz Ferdinand von Gudenus|2|
|2131|Johann Jakob Berger|3|
|2132|Jakob Franz Bocklet|2|
|2133|Jost Heinrich Brockhausen|2|
|2134|Johann Ernst Brockhausen|2|
|2135|Robert Balthasar Adam Clemens|2|
|2136|Robert Clemens|1|
|2137|Ernst Ludwig Wilhelm Freiherr von Dacheröden|15|
|2138|Jakob Dominicus|1|
|2139|Karl Josef Dresanus|2|
|2140|Adam Ignaz Durino|2|
|2141|Johann Georg Evenius|2|
|2142|Johann Christoph Evander|2|
|2143|Arnold Gottfried Events|2|
|2144|Gerhard Evers|2|
|2145|Franz Arnold Evers|2|
|2146|Johannes Valentin Frisius|2|
|2147|Johann Valentin Frisius|1|
|2148|Gustav Adolf Graberg|11|
|2149|Peter Heinrich Jakob Heiland|2|
|2150|Adolf Johann Pleichard Heinrici|2|
|2151|Johann Kaspar Jungk|2|
|2152|Kaspar Jungk|2|
|2153|Johann Melchior Kniephoff|4|
|2154|Johannes Georg Köhler|3|
|2155|Johann Georg Köhler|2|
|2156|Johannes Rudolf Köhler|2|
|2157|Johann Tobias Lagus Junior|2|
|2158|Jakob Heinrich Langguth|2|
|2159|Kaspar Friedrich Lentin|2|
|2160|Johann Daniel Christoph Lincker Ritter und Edler von Lützenwick|1|
|2161|Johann Jakob Lincker|2|
|2162|Leonhard Löber|2|
|2163|Georg Melchior Ludolf|9|
|2164|Dietrich Wilhelm von Matthiae|1|
|2165|Dietrich Matthiae|1|
|2166|Johann Heinrich Mayer|2|
|2167|Joachim Andreas Meier|4|
|2168|Johannes Heinrich Meyer|8|
|2169|Robert Balthasar von Milwitz|2|
|2170|Johann Bernhard Molitoris|2|
|2171|Peter Christian Franz Papius|5|
|2172|Johann Hermann Pfingsten|115|
|2173|Vitus Daniel von Piper|2|
|2174|Christoph Wilhelm Emanuel Reichardt|3|
|2175|Johann Rese|2|
|2176|Johann Riese|4|
|2177|Johannes Ernst Dominik Riese|2|
|2178|Johann Josef Senger|2|
|2179|Johannes Adam Schmidt|2|
|2180|Johann Jakob Schmidt|1|
|2181|Bernhard von Sommerlattae|1|
|2182|Otto Arnold von Sommerlattae|1|
|2183|Johann Jakob Franz Spoenla|2|
|2184|Johann Gottfried Spoenla|7|
|2185|Ivo Stahl|2|
|2186|Alexander Strecker|2|
|2187|Johannes Philipp Streit|2|
|2188|Ernst Christian Immanuel Tentzel|2|
|2189|Georg Ulle|4|
|2190|Johann Karl Weltz|2|
|2191|Jakob Paul Heinrich von Ziegler|2|
|2192|Jacob M\. Berger|19|
|2193|M\. Georg Berger|2|
|2194|Jacobus M\. Berger|12|
|2195|Heinrich II\. Brand|6|
|2196|Barbara Richthauser|2|
|2197|Maria Brand|5|
|2198|Christina Brochhausen|2|
|2199|Judith Brochhausen|1|
|2200|Jost Christoph Reinhardt|1|
|2201|Johann Gerhard Dresanus|13|
|2202|Anna Sabina Ziegler|3|
|2203|David Hamilton|2|
|2204|Christoph Frickinger|1|
|2205|Laurentius Heinrici|4|
|2206|Franz Hugo Hunold|3|
|2207|Heinrich Ilgen junior|11|
|2208|Justina Magdalena Schmidt|2|
|2209|Cyriax Müller |1|
|2210|Barbara Regina Magdalena Langguth|2|
|2211|Johann Daniel Lincker Ritter und Edler von Lützenwick|12|
|2212|Johann Jacob Lincker von Lützenwick|9|
|2213|Burckhardt Lincker von Lützenwick|3|
|2214|Johann Daniel Lincker von Lützenwick|2|
|2215|Heinrich Wilhelm Ludolf|7|
|2216|Martha Benigna Ludolf |1|
|2217|Caspar Friedrich Heidenreich|1|
|2218|Hiob Ludolf|1|
|2219|Hans Ludolf|7|
|2220|Anna Gebhard|1|
|2221|Hiob I\. Ludolph|11|
|2222|Conrad Brand |6|
|2223|Christina Gebhard|2|
|2224|Judith Ludolph|1|
|2225|Sabina Magdalena von der Marthen|2|
|2226|Martha Catharina von Utzberg|1|
|2227|Jonas Meltzer|1|
|2228|Johannes Stechanius |4|
|2229|Maria Northausen|2|
|2230|Lydia Rothardt |2|
|2231|Catharina Margaretha Rennemann|2|
|2232|Jeremias Schorch|8|
|2233|Martha Birnstiel|1|
|2234|Jeremias Birnstiel|1|
|2235|Elisabeth Elsner |2|
|2236|Bartholomaeus Elsner |4|
|2237|Regina Frischmann|1|
|2238|Bartholomaeus Elßner |3|
|2239|Ursula Wagner|5|
|2240|Johannes Wagner|20|
|2241|Anna Maria Schorch|1|
|2242|Heinrich Friedemann|1|
|2243|Maria Magdalena Schorch|1|
|2244|Franz Schiller|4|
|2245|Johann Schorch|15|
|2246|Heinrich Bartholomaeus Schorch|2|
|2247|Martha Elisabeth Schorch |2|
|2248|M\. Johann Wilhelm Andreae|4|
|2249|Johannes Schorch |5|
|2250|Anna Funcke|1|
|2251|Martha Nacke|2|
|2252|Hartmann Nacke |5|
|2253|Anna Benigna Gerstenberg |1|
|2254|Marie Christine von Brettin|1|
|2255|Jeremias Herbord Seltzer|7|
|2256|Judith Margarethe Seltzer|1|
|2257|Cordula Maximiliana von der Weser |1|
|2258|Wolf Balthasar von der Weser|5|
|2259|Hedwig Müller|1|
|2260|Georg Heinrich Ziegler |7|
|2261|Jacob Heinrich Ziegler|4|
|2262|Elisabeth Stichling|1|
|2263|Martha Vasold |2|
|2264|Ursula Förster |1|
|2265|Catharina Herr |1|
|2266|Johann Rudolph Koehler|1|
|2267|Jakob Berger|5|
|2268|Johannes Bartholomaeus Elsnerus|2|
|2269|Heinrich Wilhelm Friedemann|2|
|2270|Franz Heinrich Schiller|3|
|2271|Johann Heinrich Schorch|2|
|2272|Heinrich Bartholomäus Schorch|2|
|2273|Johann Wilhelm Andreae|4|
|2274|Martha Elisabeth Andreae|1|
|2275|Andreas Joachim von Brettin|1|
|2276|N\.N\. Hahn von Königsburg|2|
|2277|Anthonius Hallenhorst |2|
|2278|Anton Hallenhorst |1|
|2279|M\. Friedrich Heinrich Jacobs|2|
|2280|Johann Jungk|2|
|2281|Johann Melchior der Jüngere Kniphoff|1|
|2282|Georg Ulla|4|
|2283|Karl Franz Adolf Schenk Schmiedburg|1|
|2284|Philipp Ludwig von Reiffenberg|21|
|2285|Friedrich von Greiffenclau zu Vollraths|5|
|2286|Johann Heinrich Daniel Freiherr von Ritter zu Grünstein|17|
|2287|Johann Jacob Walpoth von Bassenheim|4|
|2288|Gottlieb Philipp Joseph Faust von Stromberg|5|
|2289|Friedrich Wilhelm Freiherr von Bicken|4|
|2290|Anselm Franz Freiherr von Warsberg|1|
|2291|Karl Joseph Adolph lukas Freiherr Schenk von Schmidtburg|1|
|2292|Karl Theodor Anton Maria von Dalberg|21|
|2293|Johann Jacob Bilstein|3|
|2294|N\.N\. Dehmer|2|
|2295|N\.N\. Molitoris|1|
|2296|N\.N\. Bocklett|1|
|2297|Ioannes Gerardus Dresanus|1|
|2298|Ioannes Hallenhorst|2|
|2299|Johann Daniel Christoph Lincker von Lützenwick|17|
|2300|N\.N\. Heyland|1|
|2301|Carl Joseph Freiherr Schenck von Schmidtburg|4|
|2302|Karl Wilhelm Freiherr von Breidbach-Bürresheim|3|
|2303|Karl Theodor von Dalberg|72|
|2304|Friedrich Greiffenclau zu Vollrats|3|
|2305|Karl Joseph Adolph Lukas Freiherr Schenk von Schmidtburg|3|
|2306|Karl Wilhelm Joseph Adolph von Breidbach zu Bürresheim|4|
|2307|Johannes Dresanus|14|
|2308|N\.N\. Genau|2|
|2309|Dieter Wilhelm Matthiae|24|
|2310|N\.N\. von Lincker|1|
|2311|N\.N\. Papius|3|
|2312|Peter Christian Papius|3|
|2313|Philipp von Reiffenberg|1|
|2314|Philipp Ludwig Freiherr von Reiffenberg|2|
|2315|Adam F\. Reinhardt|5|
|2316|Johann Michael Rothermund|6|
|2317|Johann Christian Spitz|4|
|2318|N\.N\. Spitz|1|
|2319|Philipp Ludwig Ritter von Reiffenberg|13|
|2320|Johann Jacob von Walpott|4|
|2321|Johann Jacob Waldbott|7|
|2322|Friedrich Wilhelm von Bicken|26|
|2323|Philipp Wilhelm Graf und edler Herr von Boineburg|7|
|2324|Carl Wilhelm Joseph Adam von Breidbach zu Bürresheim|2|
|2325|Ernst Ludwig Wilhelm von Dacheröden|5|
|2326|Carl Theodor Freiherr von Dalberg|1|
|2327|Carl Theodor Anton Maria von Dalberg|38|
|2328|Carl Theodor Cämmerer von Worms Freiherr von und zu Dalberg|6|
|2329|Joachim Dietrich Evers|2|
|2330|Sebastian Evert|2|
|2331|Johann Mauritz Bodo von Gudenus|5|
|2332|Johann Jakob Freiherr Lincker von Lützenwick|2|
|2333|Johann Daniel Freiherr Lincker von Lützenwick|2|
|2334|Damian Freiherr von Linden|4|
|2335|Ernst Tentzl|24|
|2336|Philipp Wilhelm Freiherr von Boineburg|8|
|2337|Anselmus Franciscus Molitoris|2|
|2338|Johann Arnold Schütze|1|
|2339|Johann Jacob Lyncker von Lützenwiyck|1|
|2340|Nicolaus Meinong|2|
|2341|Johann Heinrich Dehmer|2|
|2342|Hugo Franciscus Hunold|4|
|2343|Johann Ernst Dominicus Rieße|2|
|2344|Johann Daniel Lyncker|1|
|2345|Ernest Tenzel|4|
|2346|Franciscus Hugo Hunold|1|
|2347|Philippus Franciscus a Bellmont|1|
|2348|Ernest Tentzel|14|
|2349|Johann Arnold de Bellmont|14|
|2350|Johann Heinrich Daniel Freiherr von Ritter zu Groenesteyn|20|
|2351|Johann Michael Spoenla|2|
|2352|Petrus Christianus Josephus Papius|2|
|2353|Jacobus de Billstein|2|
|2354|Johannes Mauritius de Gudenus|2|
|2355|Johann Jakob Bielstein|2|
|2356|Goeorg Marx Hahn von Königsburg|1|
|2357|Franz Damian Freiherr von Linden|6|
|2358|Georg Ignaz Mansuet Rüding|5|
|2359|Friedrich von Greiffenclau|4|
|2360|Johann Jakob von Waldbott-Olbrueck|2|
|2361|Gottfried Philipp Faust von Stromberg|2|
|2362|Karl Wilhelm Joseph von Breidbach-Buerresheim|4|
|2363|Karl Joseph Adolf Schenk von Schmidburg|2|
|2364|Karl Theodor Anton von Dalberg|8|
|2365|Karl Theodor Freiherr von Dalberg|29|
|2366|Johann Werner von Vorstern|12|
|2367|Johann Werner von Vorster|276|
|2368|Johann Werner Freiherr von Vorster|179|
|2369|Philipp Moritz Gedult von Jungenfeld|164|
|2370|Friedrich Freiherr von Dalberg|10|
|2371|Friedrich Anton Christoph Kämmerer von Worms Freiherr von und zu Dalberg|342|
|2372|Christoph Hartmann Freiherr von Fechenbach zu Laudenbach|152|
|2373|Christoph Hartmann Freiherr von Fechenbach zu Lautenbach|350|
|2374|Christophel Hartmann Freiherr von Fechenbach|4|
|2375|Karl Friedrich Freiherr von Frankenstein zu Ockstadt|128|
|2376|Karl Friedrich Freiherr von Frankenstein|8|
|2377|Karl von Hagen|12|
|2378|Karl Freiherr von Hagen|54|
|2379|Karl Wilhelm \[sic\!\] Freiherr von Hagen|6|
|2380|Karl Wilhelm Freiherr von Hagen|486|
|2381|Karl Wilhelm von Hagen|33|
|2382|Gottfried von Lammertz|202|
|2383|Gottfried von Lammerz|123|
|2384|Johann Christoph Joseph Schlehlein|106|
|2385|Christoph Joseph Schlehlein|3|
|2386|Johann Chrisoph Joseph Schlehlein|18|
|2387|Johann Christoph Schlehlein|57|
|2388|Georg von Nitschke|18|
|2389|Johann Georg von Nitschke|82|
|2390|Johann Friedrich Stubenrauch|48|
|2391|Johann Friedrich Edler von Stubenrauch|72|
|2392|Johann Ferdinand Andreas von Lammertz|522|
|2393|Johann Ferdinand Andreas von Lammerz|15|
|2394|Ferdinand Andreas von Lammertz|8|
|2395|Georg Friedrich von Lasser|112|
|2396|Johann Jakob  Stubenrauch|78|
|2397|Johann Jakob Edler von Stubenrauch|292|
|2398|Jakob Stubenrauch|4|
|2399|Heinrich Schweickart Hellmandel|14|
|2400|Heinrich Schweickart Oswald Hellmandel|94|
|2401|Johann Erhard Franz von Löhr|57|
|2402|Johann Eberhard \[sic\!\] Franz von Löhr|3|
|2403|Johann Eberhard Franz von Löhr|88|
|2404|Franz Bertram von Scheben, Edler von Kronfeld|380|
|2405|Franz Bertram Freiherr \[sic\!\] von Scheben|3|
|2406|Franz Bertram Freiherr von Scheben|151|
|2407|Veit Christoph Molitor|414|
|2408|Anselm Franz Serger|412|
|2409|Anselm Franz Särger|69|
|2410|Aeneas Anton Fleischmann|99|
|2411|Aeneas Anton von \[sic\!\] Fleischmann|3|
|2412|Aeneas Anton von Fleischmann|53|
|2413|Andreas \(sic\!\) Anton Fleischmann|9|
|2414|Johann Philipp Freiherr von Bettendorf|191|
|2415|Johann Philipp Freiherr von Bettendorff|183|
|2416|Johann Philipp Graf von Stadion|398|
|2417|Johann Philipp Graf von Stadion-Thannhausen und Warthausen|43|
|2418|Hugo \[sic\!\] Johann Philipp Graf von Stadion-Thannhausen und Warthausen|4|
|2419|Hugo Johann Philipp Graf von Stadion-Thannhausen und Warthausen|4|
|2420|Hugo Johann Philipp Reichsgraf von Stadion-Thannhausen und Warthausen|149|
|2421|Hugo Johann Philipp Graf von Stadion und Tannhausen|13|
|2422|Johann Philipp Graf von Stadion-Warthausen und Tannhausen|12|
|2423|Hugo Johann Philipp Graf von Stadion|324|
|2424|Hugo Johann Philipp Graf von Stadion |105|
|2425|Lothar Franz Michael Freiherr von Erthal|680|
|2426|Lothar Franz Michael Freiherr von und zu Erthal|153|
|2427|Lothar Franz Freiherr von und zu Erthal|3|
|2428|Bernhard Gottfried Reider|403|
|2429|Bernhard Gottfried von \[sic\!\] Reider|3|
|2430|Bernhard Gottfried von Reider|889|
|2431|Gottfried von Reider|6|
|2432|Johann Melchior Birckenstock|206|
|2433|Johann Melchior von Birckenstock|90|
|2434|Rupert Klemens|3|
|2435|Robert Balthasar von Klemens|169|
|2436|Karl Friedrich Wilhelm Freiherr von Erthal|439|
|2437|Friedrich Wilhelm Freiherr von Erthal|8|
|2438|Karl Kaspar Freiherr von Breidbach zu Bürresheim|40|
|2439|Karl Franz \[sic\!\] Freiherr von Breidbach zu Bürresheim|6|
|2440|Karl Franz Freiherr von Breidbach zu Bürresheim|119|
|2441|Karl Emerich Franz Freiherr von Breidbach zu Bürresheim|30|
|2442|Johann Albert Freiherr von Gudenus|104|
|2443|Johann Albert von Gudenus|4|
|2444|Friedrich Reichsgraf von und zu Stadion-Thannhausen und Warthausen|147|
|2445|Friederich Graf von Stadion|217|
|2446|Franz Eberhard Freiherr von Ebersberg genannt von Weyers und Leyen|63|
|2447|Franz Eberhard Freiherr von Ebersberg genannt von Weyers und Layen|9|
|2448|Franz Eberhard Freiherr von Ebersberg genannt von Wayers und Layen|84|
|2449|Franz Eberhard Freiherr von Ebersheim genannt von Meyers und Leyen|8|
|2450|Franz Eberhard Freiherr von Meyers und Leyen|20|
|2451|Eberhard Sigismund Wincop|53|
|2452|Joseph Franz Graf von Schönborn Buchheim|6|
|2453|Joseph Franz Graf von Schönborn-Buchheim|222|
|2454|Franz Graf von Spaur|83|
|2455|Franz Reichsgraf von Spauer|4|
|2456|Franz Graf von Spauer zu Pflaum und Valeur|4|
|2457|Franz Graf von Spauer|83|
|2458|Franz Reichsgraf von Spauer zu Pflaum und Valeur|4|
|2459|Karl Peter Rüssel|615|
|2460|Karl Peter Rüßel|24|
|2461|Augustin Franz Kunibert|99|
|2462|Augustin Franz von \[sic\!\] Kunibert|4|
|2463|Augustin Franz von Kunibert|84|
|2464|Franz Philipp Ernst Freiherr von Hettersdorff|63|
|2465|Franz Philipp Ernst Freiherr von Hettersdorf|218|
|2466|Franz Philipp Ernest Freiherr von Hettersdorf|234|
|2467|Franz Philipp Ernst Freiherr von Heddesdorf|5|
|2468|Franz Philipp Ernst Freiherr von Hedersdorf|20|
|2469|Johann Georg Neureuter|224|
|2470|Johann Georg Reurether|5|
|2471|Christian Ottenthal|204|
|2472|Christian von \[sic\!\] Ottenthal|3|
|2473|Christian von Ottenthal|458|
|2474|Emmerich Joseph Freiherr von Breidbach zu Bürresheim|716|
|2475|Anselm Freiherr Groß von und zu Trockau|141|
|2476|Anselm Baron von Groß zu Trockau|13|
|2477|Johann Maria Rudolph Reichsgraf von Waldbott von Bassenheim|184|
|2478|Johann Maria Rudolph Reichsgraf von Waldbott in Bassenheim|7|
|2479|Johann Maria Rudolph Graf von Waldbott zu Bassenheim|16|
|2480|Johann Maria Rudolph Graf von Waldbott in Bassenheim|12|
|2481|Joseph Anton Leonard Hartmann|341|
|2482|Johann Anton Leonard Hartmann|23|
|2483|Karl Adolph Freiherr von Ritter zu Grünstein|1301|
|2484|Karl Adolph Freiherr von Ritter zu Grünestein|4|
|2485|Karl Adolph Baron von Ritter|16|
|2486|Johann Georg Mansuet von Bentzel|147|
|2487|Johann Georg Mansuet Freiherr \[sic\!\] von Bentzel|5|
|2488|Johann Georg Mansuet Freiherr von Bentzel|683|
|2489|Johann Georg Mansuet Freiherr von Benzel|52|
|2490|Georg Mansuet Freiherr von Bentzel |3|
|2491|Joseph Graf von Fugger zu Kirchheim|68|
|2492|Joseph Graf von Fugger|169|
|2493|Adolph Freiherr von Greiffenclau zu Vollrads|12|
|2494|Adolph Wilhelm Franz \[sic\!\] Freiherr von Greiffenclau zu Vollrads|3|
|2495|Adolph Wilhelm Franz Freiherr von Greiffenclau zu Vollrads|81|
|2496|Adolph Freiherr von Greiffenclau|20|
|2497|Friedrich Karl Freiherr von Groschlag zu Dieburg|285|
|2498|Friedrich Karl Freiherr von Großschlag zu Dieburg|4|
|2499|Friedrich Karl Freiherr von Groschlag |301|
|2500|Philipp Franz Freiherr Knebel von Katzenelnbogen|261|
|2501|Philipp Franz Freiherr von \[sic\!\] Knebel zu \[sic\!\] Katzenelnbogen|3|
|2502|Philipp Franz Freiherr von Knebel zu Katzenelnbogen|93|
|2503|Philipp Franz Karl Freiherr von Wambold|44|
|2504|Philipp Franz Karl Freiherr von Wambold zu Umstadt|189|
|2505|Philipp Franz Freiherr von Wambold|279|
|2506|Karl Anton von Vorster|42|
|2507|Karl Anton Freiherr \[sic\!\] von Vorster|3|
|2508|Karl Anton Freiherr von Vorster|72|
|2509|Hartmann Andreas Faber|135|
|2510|Hartmann Andreas von \[sic\!\] Faber|12|
|2511|Hartmann Andreas von Faber|279|
|2512|Karl Christian Susanne|18|
|2513|Damian Friedrich von Strauß|226|
|2514|Damian Friedrich Strauß|59|
|2515|Lothar Karl Freiherr von Bettendorf|31|
|2516|Johann Michael Rottermund|3|
|2517|Johann Michael Rodermund|4|
|2518|Joannes Michael Rotermund|1|
|2519|Johann Michel Rottermund|1|
|2520|Johann Daniel Christoph Freiherr von Lincker|11|
|2521|Johann Daniel Christoph Linckert von Lützewick|3|
|2522|Johann Daniel Christoph Freiherr \[sic\!\] Lincker von Lützenwick|1|
|2523|Johann Daniel Christoph Freiherr Linker von Lützenwick|6|
|2524|Ernst \[sic\!\] Wilhelm Strecker|1|
|2525|Ernest Wilhelm Strecker|5|
|2526|Peter Heinrich Heyland|1|
|2527|Joannes Arnold von Bellmont|1|
|2528|Joannes Jakobus von Gudenus|1|
|2529|Joann Georg Brückmann|13|
|2530|Hugo Franz Karl Reichsgraf von und zu Eltz-Kempenich|819|
|2531|Johann Kaspar von Hagen|310|
|2532|Karl Wilhelm von Hagen \[sic\!\]|4|
|2533|Franz Wenzel Kaysenberg|55|
|2534|Adam Philipp Teitzel|190|
|2535|Anselm Gerhard Schott|49|
|2536|Johann Michael Strecker|235|
|2537|Lothar von Horn|73|
|2538|Jakob von Gudenus|9|
|2539|Johann Christian Jakob Gudenus|2|
|2540|Eberhard Siegmund Wincop|4|
|2541|Christoph Ignaz Ludwig von Bellmont|1|
|2542|Christian Jakob Gudenus|27|
|2543|Johann Michael Rotermunt|1|
|2544|Bernhard Alexander Strecker|30|
|2545|Johann Alexander Bernhard Strecker|2|
|2546|Franz Wenzel von Kaysenberg|60|
|2547|Hugo Franz Karl Graf von und zu Eltz|36|
|2548|Anselm Schott |36|
|2549|Anselm Gerhard Schott |166|
|2550|Franz Anselm Keisenberg|180|
|2551|Franz Anselm Kaysenberg|21|
|2552|Franz Anselm von Keisenberg|66|
|2553|Karl Wilhelm Frei- und Kammerherr von Hagen|3|
|2554|Carl Wilhelm von Hagen|498|
|2555|Johann Jakob Stubenrauch|4|
|2556|Friederich Reichsgraf von Stadion|4|
|2557|Bernhard Gottfried Reuter|2|
|2558|Friedrich Wilhelm Freiherr von Ehrthal|10|
|2559|Friedrich Anton Christoph Freiherr von und zu Dalberg|191|
|2560|Karl Kaspar Franz Freiherr von Breidbach zu Bürresheim|54|
|2561|Anton Heinrich Friedrich Graf von Stadion|153|
|2562|Franz Eberhard Freiherr von Ebersberg|52|
|2563|Joseph Franz Graf von Schönborn|118|
|2564|Johann Maria Rudolph Graf Waldbott von Bassenheim|86|
|2565|Hugo Franz Karl Graf von und zu Eltz-Kempenich|352|
|2566|Franz Wenzel von Keisenberg|94|
