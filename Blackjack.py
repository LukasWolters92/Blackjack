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
        self.Einsatz = 0
        self.SplitEinsatz = 0


    def leerehand(self):
        self.Hand = []
        self.SplitHand = []
        self.Handwert = 0
        self.Einsatz = 0
        self.SplitEinsatz = 0

    def handwert(self):
        a = 0
        b = 0

        for i in range(0,len(self.Hand)):
            if self.Hand[i].returnkartenname() != "♥ Ass" or  "♣ Ass" or "♦ Ass" or "♠ Ass":
                a += self.Hand[i].returnkartenwert()
                b += self.Hand[i].returnkartenwert()
            else:
                a += 11
                b += 1

        if a <= 21:
            self.Handwert = a
        else:
            self.Handwert = b

    def printHand(self):
        for i in range(0,len(self.Hand)):
            print(self.Hand[i].returnkartenname())

    def wetten(self, Wette):

        if self.Spielerguthaben >= Wette:
            self.Spielerguthaben -= Wette
            self.Einsatz = Wette
            return True
        else:
            return False



#a = Deck(1)
#a.deckausgabe()
#a.mischen()

#b = a.karteziehen()
#c = a.karteziehen()
#print(b.returnkartenname())


#print(lukas.Spielerguthaben)
#lukas = Spieler("Lukas", 300)

#lukas.Hand.append(b)
#lukas.Hand.append(c)


#lukas.printHand()
#lukas.handwert()
#print(lukas.Handwert)

#Spiel

spieldeck = Deck(5)
spieldeck.mischen()

dealer = Spieler("Dealer", 1000000)
Teilnehmer = []
Teilnehmer.append(dealer)

while True:

    Name = input("Geben Sie Ihren Namen ein. Wenn sich alle Spieler eingetragen haben geben Sie x ein ")
    if Name != "x":
        Guthaben = input("Wie hoch ist Ihr Guthaben? ")
        Teilnehmer.append(Spieler(Name, Guthaben))
    else:
        break

AlleSpieler = Teilnehmer

while spieldeck.anzahlkarten() > 52:
    Teilnehmer
    for i in range(1, len(Teilnehmer)):
        a = 0                                                                                                           # a ist eine Hilfsvariable
        while True:

            a = input(Teilnehmer[i].Spielername + ", Was ist Ihr Einsatz? Ihr Guthaben beträgt" + str(Teilnehmer[i].Spielerguthaben))
            b = False
            b = Teilnehmer[i].wetten(a)
            if b:
                break
            else:
                print("Sie haben nicht genug Guthaben.")

    print("Die ersten Karten werden gezogen")

    for i in range(0, len(Teilnehmer)):
        Teilnehmer[i].Hand.append(spieldeck.karteziehen())

    print(Teilnehmer[0].Spielername + "s Hand:")
    Teilnehmer[0].printHand()

    for i in range(0, len(Teilnehmer)):
        Teilnehmer[i].Hand.append(spieldeck.karteziehen())

    print(Teilnehmer[0].Spielername + "s Hand:")
    Teilnehmer[0].printHand()

    for i in range(1, len(Teilnehmer)):
        print(Teilnehmer[i].Spielername + "s Hand:")
        Teilnehmer[i].printHand()


    for i in range(1, len(Teilnehmer)):
        Teilnehmer[i].handwert()
        if Teilnehmer[i].Handwert == 21:
            Teilnehmer[i].Spielerguthaben += 2 * Teilnehmer[i].Einsatz
            print("Sie haben gewonnen! Ihr Guthaben beträgt" + str(Teilnehmer[i].Spielerguthaben))
            continue

        karte1 = Teilnehmer[i].Hand[0].returnkartenname()
        karte2 = Teilnehmer[i].Hand[1].returnkartenname()

        zeichen1 = karte1.split()
        zeichen2 = karte2.split()

        print(Teilnehmer[i].Spielername + " ist an der Reihe.")

        if zeichen1[1] == zeichen2[1] and Teilnehmer[i].Spielerguthaben >= Teilnehmer[i].Einsatz:

            while True:
                wahl = ""
                wahl = input("Wollen Sie splitten? (Y/N)")
                if wahl == "Y" or wahl == "N"
                    break
                else:
                    print("Ungültige Eingabe!")

            if wahl == "Y" :






    #for i in range(1, len(Teilnehmer)):



