import random

#Definiere Karte
class Karte:

    def __init__(self, Name : str, Wert: int):
        self.Kartenname = Name
        self.Kartenwert = Wert

    def ausgabe(self):
        print(self.Kartenname + " " + str(self.Kartenwert))

    def returnkartenname(self):
        return self.Kartenname

    def returnkartenwert(self):
        return self.Kartenwert


class Deck:
    deck = []
    def __init__(self, anzahl: int):

        for i in range(1,anzahl+1):
            for Farbe in ["♥", "♣", "♦", "♠"]:
                for Zahl in range(2,11):
                    self.deck.append(Karte(Farbe + " " + str(Zahl), Zahl))
                for Bild in ["Bube", "Dame", "König"]:
                    self.deck.append(Karte(Farbe + " " + Bild, 10))
                self.deck.append(Karte(Farbe + " Ass", -1))

    def deckausgabe(self):
        herz = []
        kreuz = []
        karo = []
        pik = []
        for a in self.deck:
            kartenname = a.returnkartenname()
            parts = kartenname.split(" ")

            if parts[0] == "♥":
                herz.append(kartenname)

            elif parts[0] == "♣":
                kreuz.append(kartenname)

            elif parts[0] == "♦":
                karo.append(kartenname)

            else:
                pik.append(kartenname)

        print(herz)
        print(kreuz)
        print(karo)
        print(pik)

    def karteziehen(self):
        karte = self.deck[0]
        self.deck.remove(self.deck[0])
        return karte

    def mischen(self):
        for i in range(1,1001):
            a = random.randint(0,len(self.deck)-1)
            self.deck.append(self.deck[a])
            self.deck.remove(self.deck[a])

    def anzahlkarten(self):
        a = len(self.deck)
        return a


class Spieler:

    def __init__(self, Name : str, Guthaben: int):
        self.Spielerguthaben = Guthaben
        self.Spielername = Name
        self.Hand = []
        self.SplitHand = []
        self.Handwert = 0
        self.SplitHandwert = 0
        self.Einsatz = 0
        self.SplitEinsatz = 0


    def leerehand(self):
        self.Hand = []
        self.SplitHand = []
        self.Handwert = 0
        self.Einsatz = 0
        self.SplitEinsatz = 0

    def handwert(self):
        handwert_1 = 0
        handwert_2 = 0

        for i in range(0, len(self.Hand)):

            if self.Hand[i].returnkartenwert() != -1:
                handwert_1 += self.Hand[i].returnkartenwert()
                handwert_2 += self.Hand[i].returnkartenwert()
            else:
                handwert_1 += 11
                handwert_2 += 1

        if handwert_1 <= 21:
            self.Handwert = handwert_1
        else:
            self.Handwert = handwert_2


    def splithandwert(self):
        splithandwert_1 = 0
        splithandwert_2 = 0

        for i in range(0, len(self.SplitHand)):
            if self.SplitHand[i].returnkartenname() != "♥ Ass" or self.SplitHand[i].returnkartenname() != "♣ Ass" or self.SplitHand[i].returnkartenname() != "♦ Ass" or self.SplitHand[i].returnkartenname() != "♠ Ass":
                splithandwert_1 += self.SplitHand[i].returnkartenwert()
                splithandwert_2 += self.SplitHand[i].returnkartenwert()
            else:
                splithandwert_1 += 11
                splithandwert_2 += 1

        if splithandwert_1 <= 21:
            self.SplitHandwert = splithandwert_1
        else:
            self.SplitHandwert = splithandwert_2

    def printHand(self):
        for i in range(0, len(self.Hand)):
            print(self.Hand[i].returnkartenname())
        self.handwert()
        print(self.Handwert)

    def printSplitHand(self):
        for i in range(0, len(self.SplitHand)):
            print(self.SplitHand[i].returnkartenname())

    def wetten(self, wette):

        if self.Spielerguthaben >= wette:
            self.Spielerguthaben -= wette
            self.Einsatz = wette
            return True
        else:
            return False


def doubledown(Teilnehmer):

    wahl = ""
    if Teilnehmer.Handwert <= 11 and len(Teilnehmer.Hand) == 2 and Teilnehmer.Spielerguthaben > Teilnehmer.Einsatz:
        while True:

            try:
                wahl = str(input("Double Down? (Y/N)"))
                if wahl == "Y":
                    Teilnehmer.Spielerguthaben -= Teilnehmer.Einsatz
                    Teilnehmer.Einsatz = 2 * Teilnehmer.Einsatz
                    Teilnehmer.Hand.append(spieldeck.karteziehen())
                    Teilnehmer.printHand()
                    raise Exception
                elif wahl == "N":
                    break
                else:
                    continue


            except ValueError:
                print("Ungültige Eingabe!")


def doubledownsplit(Teilnehmer):

    wahl = ""
    if Teilnehmer.SplitHandwert <= 11 and len(Teilnehmer.SplitHand) == 2 and Teilnehmer.Spielerguthaben > Teilnehmer.SplitEinsatz:
        while True:

            try:
                wahl = str(input("Double Down? (Y/N)"))
                if wahl == "Y":
                    Teilnehmer.Spielerguthaben -= Teilnehmer.SplitEinsatz
                    Teilnehmer.SplitEinsatz = 2 * Teilnehmer.SplitEinsatz
                    Teilnehmer.SplitHand.append(spieldeck.karteziehen())
                    Teilnehmer.printSplitHand()
                    raise Exception
                elif wahl == "N":
                    break
                else:
                    continue


            except ValueError:
                print("Ungültige Eingabe!")




#######   Spiel   #######

spieldeck = Deck(5)
spieldeck.mischen()

dealer = Spieler("Dealer", 1000000)
Teilnehmer = []
Teilnehmer.append(dealer)

while True:

    Name = input("Geben Sie Ihren Namen ein. Wenn sich alle Spieler eingetragen haben geben Sie x ein ")
    if Name != "x":
        try:
            Guthaben = int(input("Wie hoch ist Ihr Guthaben? "))
            Teilnehmer.append(Spieler(Name, Guthaben))
        except ValueError:
            print("Sie müssen einen Integer eingeben!")
    else:
        break


while spieldeck.anzahlkarten() > 52:

    for i in range(0, len(Teilnehmer)):
        Teilnehmer[i].leerehand()


    for i in range(1, len(Teilnehmer)):
        a = 0                                                                                                           # a ist eine Hilfsvariable
        while True:

            ### Test Codeänderung
            try:
                a = int(input(Teilnehmer[i].Spielername + ", Was ist Ihr Einsatz? Ihr Guthaben beträgt " + str(Teilnehmer[i].Spielerguthaben) + " "))
                b = False
                b = Teilnehmer[i].wetten(a)
                if b:
                    print(Teilnehmer[i].Einsatz)
                    break
                else:
                    print("Sie haben nicht genug Guthaben.")
            except ValueError:
                print("Sie müssen einen Integer eingeben!")

    print("Die ersten Karten werden gezogen")

    for i in range(0, len(Teilnehmer)):

        Teilnehmer[i].Hand.append(spieldeck.karteziehen())

    print(Teilnehmer[0].Spielername + "s Hand:")
    Teilnehmer[0].printHand()

    for i in range(0, len(Teilnehmer)):
        Teilnehmer[i].Hand.append(spieldeck.karteziehen())


    for i in range(1, len(Teilnehmer)):
        print(Teilnehmer[i].Spielername + "s Hand:")
        Teilnehmer[i].printHand()


    for i in range(1, len(Teilnehmer)):

        #Test Split

        #Teilnehmer[i].leerehand()
        #Teilnehmer[i].Hand.append(Karte("♥ 2", 2))
        #Teilnehmer[i].Hand.append(Karte("♣ 2", 2))
        #Teilnehmer[i].printHand()

        #TestEnde Split

        print(Teilnehmer[i].Spielername + " ist an der Reihe.")

        Teilnehmer[i].handwert()
        if Teilnehmer[i].Handwert == 21:
        #    Teilnehmer[i].Spielerguthaben += 2 * Teilnehmer[i].Einsatz
            print("Sie haben Blackjack!")
            continue

        karte1 = Teilnehmer[i].Hand[0].returnkartenname()
        karte2 = Teilnehmer[i].Hand[1].returnkartenname()

        zeichen1 = karte1.split()
        zeichen2 = karte2.split()


        if zeichen1[1] == zeichen2[1] and Teilnehmer[i].Spielerguthaben >= Teilnehmer[i].Einsatz:

            while True:
                wahl = ""
                try:
                    wahl = str(input("Wollen Sie splitten? (Y/N)"))
                    if wahl == "Y":
                        Teilnehmer[i].SplitEinsatz = Teilnehmer[i].Einsatz
                        Teilnehmer[i].Spielerguthaben -= Teilnehmer[i].SplitEinsatz
                        Teilnehmer[i].SplitHand.append(Teilnehmer[i].Hand[1])
                        del Teilnehmer[i].Hand[1]

                        Teilnehmer[i].Hand.append(spieldeck.karteziehen())
                        Teilnehmer[i].SplitHand.append(spieldeck.karteziehen())

                        print(Teilnehmer[i].Spielername + "s 1.Hand:")
                        Teilnehmer[i].printHand()
                        print(Teilnehmer[i].Spielername + "s 2.Hand:")
                        Teilnehmer[i].printSplitHand()


                        print("1.Hand")



                        while True:

                            Teilnehmer[i].handwert()

                            if Teilnehmer[i].Handwert > 21:

                                break

                            try:
                                doubledown(Teilnehmer[i])
                            except Exception:
                                break
                            else:
                                pass


                            wahl = ""
                            try:
                                wahl = str(input("Hit? (Y/N)"))
                                if wahl == "Y":
                                    Teilnehmer[i].Hand.append(spieldeck.karteziehen())
                                    Teilnehmer[i].printHand()
                                    continue
                                else:
                                    break

                            except ValueError:
                                print("Ungültige Eingabe!")

                        print("2.Hand")

                        while True:
                            Teilnehmer[i].splithandwert()

                            if Teilnehmer[i].SplitHandwert > 21:

                                break

                            try:
                                doubledownsplit(Teilnehmer[i])
                            except Exception:
                                break
                            else:
                                pass

                            wahl = ""

                            try:
                                wahl = str(input("Hit? (Y/N)"))
                                if wahl == "Y":
                                    Teilnehmer[i].SplitHand.append(spieldeck.karteziehen())
                                    Teilnehmer[i].printSplitHand()
                                    continue
                                else:
                                    break

                            except ValueError:
                                print("Ungültige Eingabe!")


                    elif wahl == "N":
                        break
                    else:
                        print("Ungültige Eingabe!")

                except ValueError:
                    print("Ungültige Eingabe")

            break

        else:
            while True:

                Teilnehmer[i].handwert()

                if Teilnehmer[i].Handwert > 21:

                    break

                try:
                    doubledown(Teilnehmer[i])
                except Exception:
                    break
                else:
                    pass

                wahl = ""
                try:
                    wahl = str(input("Hit? (Y/N)"))
                    if wahl == "Y":
                        Teilnehmer[i].Hand.append(spieldeck.karteziehen())
                        Teilnehmer[i].printHand()
                        continue
                    else:
                        break

                except ValueError:
                    print("Ungültige Eingabe!")

    Teilnehmer[0].handwert()

    if Teilnehmer[0].Handwert < 17:
        Teilnehmer[0].Hand.append(spieldeck.karteziehen())
        print(Teilnehmer[0].Spielername + "s Hand:")
        Teilnehmer[0].printHand()
    else:
        print(Teilnehmer[0].Spielername + "s Hand:")
        Teilnehmer[0].printHand()

    Teilnehmer[0].handwert()


    for i in range(1, len(Teilnehmer)):

        Teilnehmer[i].handwert()
        Teilnehmer[i].splithandwert()

        if Teilnehmer[i].Handwert > 21:
            Teilnehmer[i].Handwert = 0

        else:
            pass

        if Teilnehmer[i].SplitHandwert > 21:
            Teilnehmer[i].SplitHandwert = 0
        else:
            pass

        if Teilnehmer[0].Handwert == 21 and len(Teilnehmer[0].Hand) == 2:


            if Teilnehmer[i].Handwert == 21 and len(Teilnehmer[i].Hand) == 2 and len(Teilnehmer[i].SplitHand) == 0:

                print("Unentschieden! " + Teilnehmer[i].Spielername + " und Dealer haben Blackjack")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + Teilnehmer[i].Einsatz

            else:

                print(Teilnehmer[i].Spielername + " hat verloren")

        elif Teilnehmer[i].Handwert == 21 and len(Teilnehmer[i].Hand) == 2 and len(Teilnehmer[i].SplitHand) == 0:

            print(Teilnehmer[i].Spielername + " hat mit Blackjack gewonnen")

            Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 3 * Teilnehmer[i].Einsatz

        elif Teilnehmer[0].Handwert > 21:

            if Teilnehmer[i].Handwert > 21:

                print(Teilnehmer[i].Spielername + "s 1.Hand hat verloren")

            else:

                print("Dealer ist Bust! " + Teilnehmer[i].Spielername + "s 1.Hand hat gewonnen")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 2 * Teilnehmer[i].Einsatz

            if Teilnehmer[i].SplitHandwert > 21 and len(Teilnehmer[i].SplitHand) > 0:

                print(Teilnehmer[i].Spielername + "s 2.Hand hat verloren")

            elif len(Teilnehmer[i].SplitHand) > 0:

                print("Dealer ist Bust! " + Teilnehmer[i].Spielername + "s 2.Hand hat gewonnen")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 2 * Teilnehmer[i].SplitEinsatz
            else:
                pass

        elif Teilnehmer[0].Handwert <= 21:

            if Teilnehmer[i].Handwert > Teilnehmer[0].Handwert:
                print(Teilnehmer[i].Spielername + "s 1.Hand hat gewonnen")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 2 * Teilnehmer[i].Einsatz

            elif Teilnehmer[i].Handwert == Teilnehmer[0].Handwert:
                print(Teilnehmer[i].Spielername + "s 1.Hand ist unentschieden")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 1 * Teilnehmer[i].Einsatz

            elif Teilnehmer[i].Handwert < Teilnehmer[0].Handwert:
                print(Teilnehmer[i].Spielername + "s 1.Hand hat verloren")

            else:
                pass

            if Teilnehmer[i].SplitHandwert > Teilnehmer[0].Handwert and len(Teilnehmer[i].SplitHand) > 0:
                print(Teilnehmer[i].Spielername + "s 2.Hand hat gewonnen")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 2 * Teilnehmer[i].SplitEinsatz

            elif Teilnehmer[i].SplitHandwert == Teilnehmer[0].Handwert and len(Teilnehmer[i].SplitHand) > 0:
                print(Teilnehmer[i].Spielername + "s 2.Hand ist unentschieden")

                Teilnehmer[i].Spielerguthaben = Teilnehmer[i].Spielerguthaben + 1 * Teilnehmer[i].SplitEinsatz

            elif Teilnehmer[i].SplitHandwert < Teilnehmer[0].Handwert and len(Teilnehmer[i].SplitHand) > 0:
                print(Teilnehmer[i].Spielername + "s 2.Hand hat verloren")

            else:
                pass

        else:
            print("etwas ist flasch gelaufen")

        print(Teilnehmer[i].Einsatz)


        print(Teilnehmer[i].Spielerguthaben)
    print("Runde vorbei!")










        #Testen ob der Spieler gewonnen hat durch Blackjack usw
        # Geld verteilen

    ##### GIT hochladen #####





<!doctype html>
<html>
	<head>
		<title>Hello World</title>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
	
		<section class = "section section-top">
			<input type = "text" id = "dateInputDate" placeholder = "dd.mm.jjjj"></input>
			<input type = "text" id = "dateInputTime" placeholder = "hh:mm:ss"></input>
			<button type = "button" onclick = "triggerInterval()">Calculate!</button>
			<p id = demo class = "size-four"></p>
		</section>
		
		<section class="section section-left">
			<ul class="inline-list">
				<li class="ulist">
					<div class="num-one">
						<a href="#" id="farbe_one" onclick="changeColor('#9c4f65')" >Seite 1</a>
					</div>
						<ul>	
							<li>
								<div class= "lilist num-one">
									<a href="#" id="farbe_two" onclick="changeColor('#11526c')" >Seite 1.1</a>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<a href="#" id="farbe_three" onclick="changeColor('#d08e1f')" >Seite 1.2</a>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<a href="#" id="farbe_four" onclick="changeColor('#115b58')" >Seite 1.3</a>
								</div>
								
							</li>
						</ul>	
				</li>
				
								<li class="ulist">
					<div class="num-one">
						<a href="#" id="farbe_five" onclick="changeColor('#e3d5d0')" >Seite 2</a>
					</div>
						<ul>	
							<li>
								<div class= "lilist num-one">
									<a href="#" id="six" onclick="changeColor('#ae7893')" >Seite 2.1</a>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<a href="#" id="seven" onclick="changeColor('#8286a3')" >Seite 2.2</a>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<a href="#" id="eight" onclick="changeColor('#751a4a')" >Seite 2.3</a>
								</div>
								
							</li>
						</ul>	
				</li>
				
								<li class="ulist">
					<div class="num-one">
						<a href="#" id="farbe_nine" onclick="colorRandom()" >Seite 3</a>
					</div>
						<ul>	
							<li>
								<div class= "lilist num-one">
									<a href="#" id="farbe_ten" onclick="changeColor('#b33044')" >Seite 3.1</a>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<a href="#" id="farbe_eleven" onclick="changeColor('#ffaf00')" >Seite 3.2</a>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<a href="#" id="farbe_twelve" onclick="changeColor('#d08e1f')" >Seite 3.3</a>
								</div>
								
							</li>
						</ul>	
				</li>

			</ul>
		</section>
		
		<section class="section section-right">
			<h1 class="box-right">
				Meine erste Aufgabe
			</h1>
			<figure class=size-two>
				<p class="size-three">
					<img src="screen.png" class="size">
					<figcaption class="size">
						Meine erste Aufgabe
					</figcaption>
				</p>
			</figure>
			<p class="box-right">
				CSS wurde entworfen, um Darstellungsvorgaben weitgehend von den Inhalten zu trennen.
				Wenn diese Trennung konsequent vollzogen wird, werden nur noch die inhaltliche Gliederung
				eines Dokumentes und die Bedeutung seiner Teile in HTML oder XML beschrieben, während mit
				CSS gesondert davon, vorzugsweise in separaten CSS-Dateien, die Darstellung der Inhalte festgelegt wird
				(z. B. Layout, Farben und Typografie). Gab es anfangs nur einfache Darstellungsanweisungen, so wurden im
				Verlauf komplexere Module hinzugefügt, mit denen z. B. Animationen und für verschiedene Ausgabemedien 
				verschiedene Darstellungen definiert werden können.
				Elemente eines Dokumentes können aufgrund verschiedener Eigenschaften identifiziert werden. Dazu zählen neben dem Elementnamen 
				(z. B. a für alle Hyperlinks), ihrer ID und ihrer Position innerhalb des Dokumentes (z. B. alle Bildelemente innerhalb von Linkelementen)
				auch Details wie Attribute (z. B. alle Linkelemente, deren href-Attribut mit www.example.com beginnen) oder die Position in einer Menge 
				von Elementen (z. B. das siebte Element einer Liste). Mit CSS-Anweisungen können für jede solcher Elementegruppen Vorgaben für die 
				Darstellung festgelegt werden. Diese Festlegungen können zentral erfolgen, auch in separaten Dateien, so dass sie leichter für andere 
				Dokumente wiederverwendet werden können. Außerdem enthält CSS ein Vererbungsmodell für Auszeichnungsattribute, das die Anzahl 
				erforderlicher Definitionen vermindert.
				Mit CSS können für verschiedene Ausgabemedien (Bildschirm, Papier, Projektion, Sprache) unterschiedliche Darstellungen vorgegeben werden. 
				Das ist nützlich, um z. B. die Verweisadressen von Hyperlinks beim Drucken aufzuführen, und um für Geräte wie PDAs und Mobiltelefone, die 
				kleine Displays oder eine geringe Bildauflösung haben, Darstellungen anzubieten, die schmal genug und nicht zu hoch sind, um auf solchen Geräten 
				lesbar zu bleiben.
				CSS ist die Standard-Stylesheet-Sprache im World Wide Web. Früher übliche, darstellungsorientierte HTML-Elemente wie font oder
				center gelten als „veraltet“ (englisch obsolete), das heißt, sie sollen in Zukunft aus dem HTML-Standard entfernt werden.[1]
				So gelten diese u. a. seit HTML 4 (1997) als „unerwünscht“ und mit HTML5 als missbilligt (englisch deprecated).[2]
			</p>
			<a href="#" id="openCloseSitemap" onclick="somFunction()" >Schließen</a>
			
			
			<ul class="inline-list" id="open-close">
				<li class="ulist">
					<div class="num-one">
					<span>Seite 1</span>
					</div>
						<ul>	
							<li>
								<div class= "lilist num-one">
									<span>Seite 1.1</span>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<span>Seite 1.2</span>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<span>Seite 1.3</span>
								</div>
								
							</li>
						</ul>	
				</li>
				
								<li class="ulist">
					<div class="num-one">
					<span>Seite 2</span>
					</div>
						<ul>	
							<li>
								<div class= "lilist num-one">
									<span>Seite 2.1</span>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<span>Seite 2.2</span>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<span>Seite 2.3</span>
								</div>
								
							</li>
						</ul>	
				</li>
				
								<li class="ulist">
					<div class="num-one">
					<span>Seite 3</span>
					</div>
						<ul>	
							<li>
								<div class= "lilist num-one">
									<span>Seite 3.1</span>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<span>Seite 3.2</span>
								</div>
								
							</li>
							<li>
								<div class= "lilist num-one">
									<span>Seite 3.3</span>
								</div>
								
							</li>
						</ul>	
				</li>

			</ul>
		</section>
			
		<script type="text/javascript" src="script.js"></script>
		
		
	</body>
</html>


function somFunction() {
	
	var x = document.getElementById("openCloseSitemap").textContent;
	
	if (x == "Schließen"){
	
		closeFunction();
		
		} else {
		
		openFunction();
		
		}
										

}
	
	
	
function closeFunction() {
	document.getElementById("open-close").style.display = "none";
	document.getElementById("openCloseSitemap").innerHTML = "Öffnen";
}
	

	
	
function openFunction() {
	document.getElementById("open-close").style.display = "block";
	document.getElementById("openCloseSitemap").innerHTML = "Schließen";
}

function changeColor(colorHex){
	var y = document.getElementsByClassName("section-right");
	var i;
	for (i = 0; i < y.length; i++) {
		y[i].style.backgroundColor = colorHex;
	}

}

function colorRandom(){

	
	var z = ["a","b","c","d","e","f","1","2","3","4","5","6","7","8","9","0"];
	
	var a = "#";
	
	var j = 0;
	
	for (j ; j < 6; j++){
		var x = Math.round(Math.random()*16);
		a = a + z[x];
	}
	
	
	var y = document.getElementsByClassName("section-right");
	var i;
	for (i = 0; i < y.length; i++) {
		y[i].style.backgroundColor = a;
	}

}

function XmasCounter(then){
	var now = new Date();
	//var thenDate = document.getElementById("dateInputDate").value;
	//var thenTime = document.getElementById("dateInputTime").value;
	//var then = thenDate + "T" + thenTime;
	//console.log(new Date(then));
	//then = Date.parse(then);
	var dif = then - now;
	var weeks = Math.floor(dif / (1000 * 60 * 60 * 24 * 7)); 
	dif = dif % (1000 * 60 * 60 * 24 * 7);
	var days = Math.floor(dif / (1000 * 60 * 60 * 24));
	dif = dif % (1000 * 60 * 60 * 24);
	var hours = Math.floor(dif / (1000 * 60 * 60));
	dif = dif % (1000 * 60 * 60);
	var minutes = Math.floor(dif / (1000 * 60));
	dif = dif % (1000 * 60);
	var seconds = Math.floor(dif / (1000));
	
	var timeString = weeks + "w " + days + "d " + hours + "h " + minutes +  "m " + seconds + "s";
	
	document.getElementById("demo").innerHTML = timeString;
	
}

var countdown;

function triggerInterval(){
	clearInterval(countdown);
	document.getElementById("demo").innerHTML = "";
	var gerdate = document.getElementById("dateInputDate").value;
	var arraydate = gerdate.split(".");
	var check1 = arraydate[2] + "-" + arraydate[1] + "-" + arraydate[0];
	console.log(check1);
	var check2 = document.getElementById("dateInputTime").value;
	var check = check1 + "T" + check2;
	check = new Date(check);
	console.log(check.getTime());
	
	if(check instanceof Date && !isNaN(check.getTime())){
		countdown = setInterval(function() {
			XmasCounter(check);
		}, 1000)
	} else {
		alert("Bitte Datum und Zeit eingeben!");
	}
}

html{ 
	background: linear-gradient(#3535cd, #f2f2fc) no-repeat;
	height:100%;
	font-family: Helvetica;
	font-size: 18px;
	line-height: 1.4;
}

.section{
	overflow: auto;
	background: #ffffff;
	border: 10px solid blue;
	top: 100px;
	position:absolute;
	
}

.section-right{
	width: 1200px;
	height: 600px;
	left: 550px;
	position: absolute;
	background-color: #FFFFFF;
	overflow: -moz-scrollbars-vertical; 
    overflow-y: scroll;
}

.section-right .inline-list > li{
    display:inline-block;
}

.section-left{
	width: 400px;
	height: 600px;
	left: 100px;
	position: absolute; 
}

.section-top{
	width: 1650px;
	height: 65px;
	top: 10px;
	left: 100px;
	position: absolute;
	text-align: center;
	font-size: 20px;
	font-weight: bold;
	color: white;
	text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
	background-image: url("gin-geschenke.jpg");
	
}

.num-one{
	width: 315px;
	height: 75px;
	background-color: #00AFFF;
	position: relative;
	margin-left: auto;
	margin-right: auto;
	margin-top: 20px;
	margin-bottom: 20px;
	text-align: center;
	font-size: 20px;
	display: flex;
	flex-direction: column;
	justify-content: center;
}

.box-left{	
	text-align: center;
	margin: 0%;
	
}

.box-right{
	margin-left: 1%;
	margin-right: 1%;
	text-align: justify;
}

.size-two{
	margin: 10px;
	width: 20%;
	height: 32%;
	float: left;
}
.size-three{
	margin-top: 0px;
	margin-bottom: 0px;
}

.size-four{
	margin-top: 0px;
	margin-bottom: 0px;
}

img{
}
.size{
	width: 98%;
	padding: 1%;
	text-align: center;
	font-size: 16px;
	
}

.ulist{
	padding: 0px;
	
	
}

.lilist{
	width: 285px;
	height: 30px;
}





