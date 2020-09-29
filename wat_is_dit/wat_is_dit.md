#### 1)Lees het bestand. Kan ik het bestand raadplegen? Hoe doe ik dat efficiënt?
###### 1.Wat is de gedachte achter je aanpak?

Het bestand per lijn inladen. Zodat ik het bestand neit in een keer moet inladen. 
per lijn kijk is welke attribuut het is (seq_id, seq, +, quality). Op het moment dat die vier
zijn ingeladen ga ik er mee aan de slag voor dat ik een volgende inlaad.

###### 2.Welketechniekengebruik?

Er wordt gebruikt gemaakt van `open(...)`, `if elif else` en twee counters.

###### 3.Welke hardware gebruik je?

Het programma draait op een laptop.

###### 4.Hoe lang duren je procedures in tijd, en vind je jouw procedures snel?


De functie kan zo'n 11 miljoen regels inladen en scores berekenen per minuut.
Dat zijn zo'n 2.750.000 seq per minuut. Met een O(n)

###### 5.Waardoor denk je dat je uitvoering snel / langzaam is?

Ik denk dat hij niet snel genoeg is omdat hij maar op 1 thread draait en niks parallel doet.

###### 6.Hoe test je of het verkregen resultaat klopt bij je uitvoering?

Dit zou je kunnen doen door een kleine test sample voor unittest om te kijken of de functies correct zijn.
In dit geval zou het fout kunnen gaan als de file niet geheel de zelfde format heeft.

###### 7.Welke verandering in aanpak laat je werking/algoritme versnellen?

Meer threads gebruiken. 

#### 2)Retourneer een sequentie op basis van een sequentie ID. 

###### 1.Wat is de gedachte achter je aanpak?

Mijn is om eerst een basis op te stellen. De makkelijkste aanpak is om door de lijst 
heen te lopen en telkens kijken of je een match hebt.

###### 2.Welketechniekengebruik?

Er is gemaakt van string splicing `string[1:5]`, `with open(...)` en andere basis

###### 3.Welke hardware gebruik je?

Het programma draait op een laptop.

###### 4.Hoe lang duren je procedures in tijd, en vind je jouw procedures snel?

Dit hang af van waar in de lijst de seq zich bevind. Met een O(n)

###### 5.Waardoor denk je dat je uitvoering snel / langzaam is?

Ik weet dat mijn uitvoering langzaam is omdat de file niet gesorteerd is.
Als dit van te voren gebeurdt kan je met een ander sneller algoritme zoeken.

###### 6.Hoe test je of het verkregen resultaat klopt bij je uitvoering?

Dit zou je kunnen doen door een kleine test sample voor unittest om te kijken of de functies correct zijn.
In dit geval kun je vantevoren de sequencies al weten bv. en dan de twee sequencies vergelijken

###### 7.Welke verandering in aanpak laat je werking/algoritme versnellen?

ander algoritme + sorteren

#### 3)Bereken de Phredscore voor iedere Read (gebruik het gemiddelde in alle vragen). 
###### 1.Wat is de gedachte achter je aanpak?

Mijn gedachte was om de unicode te gebruiken als score. 

###### 2.Welketechniekengebruik?

De technieken die ik gebruik zijn `numpy.mean()` en ik maak gebruik van list comprehensions.

###### 3.Welke hardware gebruik je?

Het programma draait op een laptop.

###### 4.Hoe lang duren je procedures in tijd, en vind je jouw procedures snel?

De functie kan zo'n 11 miljoen regels inladen en scores berekenen per minuut.
Dat zijn zo'n 2.750.000 seq per minuut. O(n)

###### 5.Waardoor denk je dat je uitvoering snel / langzaam is?

Ik denk dat hij niet snel genoeg is omdat hij maar op 1 thread draait en niks parallel doet.

###### 6.Hoe test je of het verkregen resultaat klopt bij je uitvoering?

Dit zou je kunnen doen door een kleine test sample voor unittest om te kijken of de functies correct zijn.
In dit geval zou het fout kunnen gaan als de file niet geheel de zelfde format heeft.

###### 7.Welke verandering in aanpak laat je werking/algoritme versnellen?

Meer threads gebruiken. 


#### 4)Retourneer de sequentie met hoogste / laagste PhredScore.
###### 1.Wat is de gedachte achter je aanpak?

Mijn gedachte was om tijdens het berekenen meteen te checken 
of het getal de hoogste of de laagste was en die opslaan in een var 

###### 2.Welketechniekengebruik?

ik maak gebruik van inline if statements

###### 3.Welke hardware gebruik je?

Het programma draait op een laptop.

###### 4.Hoe lang duren je procedures in tijd, en vind je jouw procedures snel?

Het wordt meteen berekent tijdens het inladen dus na het inladen kost het 
alleen het lezen van twee losse vars.
Het inladen kost alleen wel veel tijd.

###### 5.Waardoor denk je dat je uitvoering snel / langzaam is?

Mijn uitvoering maakt het inladen/score_berekening langzamer, maar
zorgt er wel voor dat het opvragen van min/max instant is na de tijd.

###### 6.Hoe test je of het verkregen resultaat klopt bij je uitvoering?

Dit zou je kunnen doen door een kleine test sample voor unittest om te kijken of de functies correct zijn.
Ook zou je dit nog met de hand kunnen doen als je dat fijn vind.

###### 7.Welke verandering in aanpak laat je werking/algoritme versnellen?
 
Na het inladen kan het niet sneller.

#### 5)Filter het bestand op basis van een PhredScore (Threshold>9, of hoger).
TODO
#### 6)Sorteer het bestand op basis van PhredScore.
TODO
#### 7)Plotdedistributie van alle gevonden PhredScores in een histogram.
###### 1.Wat is de gedachte achter je aanpak?

De gedachte was om `matplotlib` te gebruiken.
Erna kwam ik erachter dat veel scores hoog waren en maar weinig lage scores.
Hierdoor heb ik er ook voor gekozen om een logaritmische y as te gebruiken.

###### 2.Welketechniekengebruik?

`matplotlib`

###### 3.Welke hardware gebruik je?

Het programma draait op een laptop.

###### 4.Hoe lang duren je procedures in tijd, en vind je jouw procedures snel?

Niet gemeten. maar nadat alles is ingeladen/berekent was het voor mij gevoel heel vlot.

###### 5.Waardoor denk je dat je uitvoering snel / langzaam is?

maak gebruik van een library, geen idee hoe dat er van de achterkant uit ziet.
Dus zou hier ook geen ordeel over kunnen geven

###### 6.Hoe test je of het verkregen resultaat klopt bij je uitvoering?

Dit zou je kunnen doen door een kleine test sample voor unittest om te kijken of de functies correct zijn.
Ook zou je dit nog met de hand kunnen doen als je dat fijn vind.

###### 7.Welke verandering in aanpak laat je werking/algoritme versnellen?
 
Mogelijk een andere library of het zelf doen maar dit kan het ook erg verslomen.