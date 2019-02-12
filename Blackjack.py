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






