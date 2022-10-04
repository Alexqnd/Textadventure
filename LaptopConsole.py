class Text():
    def __init__(self) -> None:
        pass
    

class Laptop():
    def __init__(self):
        self.standort = None

    def bewege_nach_n(self):
        if self.standort.ausgangN != None:
            self.standort = self.standort.ausgangN
        else:
            print("Keine Tür im Norden!")
    def bewege_nach_o(self):
        if self.standort.ausgangO != None:
            self.standort = self.standort.ausgangO
        else:
            print("Keine Tür im Osten!")

    def bewege_nach_s(self):
        if self.standort.ausgangS != None:
            self.standort = self.standort.ausgangS
        else:
            print("Keine Tür im Süden!")

    def bewege_nach_w(self):
        if self.standort.ausgangW != None:
            self.standort = self.standort.ausgangW
        else:
            print("Keine Tür im Westen!")


class Ordner():
    def __init__(self, pbeschreibung):
        self.beschreibung = pbeschreibung
        self.ausgangN = None
        self.ausgangO = None
        self.ausgangS = None
        self.ausgangW = None
befehlsregister_l = []


class BefehlLConsole():
    def __init__(self, pname, pbeschreibung, pfunktion):
        self.name = pname
        self.beschreibung =  pbeschreibung
        self.funktion = pfunktion
        befehlsregister_l.append(self)

    def print_beschreibung(self):
        print(self.name + ":")
        print(self.beschreibung)
        print()


class LaptopConsole():
    def __init__(self):
        self.weiter = True
        self.ziel_erreicht = False
        self.jahr2022 = Ordner("jahr2022.py")
        self.cafeteria = Ordner("Cafeteria")
        self.flur = Ordner("Flur")
        self.lehrerzimmer = Ordner("Lehrerzimmer")
        self.jahr2022.ausgangO = self.flur
        self.flur.ausgangW = self.jahr2022
        self.flur.ausgangN = self.cafeteria
        self.flur.ausgangO = self.lehrerzimmer
        self.lehrerzimmer.ausgangW = self.flur
        self.cafeteria.ausgangS = self.flur
        self.laptop= Laptop()
        self.laptop.standort = self.cafeteria
        self.norden = BefehlLConsole("norden", "Der Laptop wird ausgeschaltet", self.laptop.bewege_nach_n)
        self.osten = BefehlLConsole("osten", "Der Laptop wird ausgeschaltet", self.laptop.bewege_nach_o)
        self.süden = BefehlLConsole("süden", "Der Laptop wird ausgeschaltet", self.laptop.bewege_nach_s)
        self.westen = BefehlLConsole("westen", "Der Laptop wird ausgeschaltet", self.laptop.bewege_nach_w)
        self.hilfe = BefehlLConsole("hilfe", "Der Laptop wird ausgeschaltet", self.hilfe_anzeigen)
        self.q = BefehlLConsole("q", "Der Laptop wird ausgeschaltet", self.laptop_ausschalten)

    def start(self):
        print("Mit dem Laptop scheint heute auch irgendetwas komisch zu sein.")
        print("Um alle Befehle zu sehen, die der Laptop kann, gibt man \"hilfe\" ein.")
        while self.weiter:
            if self.laptop.standort.beschreibung == "jahr2022.py":
                print("Du hast die Datei zum Zeitreisen gefunden. Du kannst sie entweder mit \"p\" ausführen")
                print("oder sie mit \"r\" löschen.")
                self.p = BefehlLConsole("p", "Der Laptop wird ausgeschaltet", self.ausfuehren)
                self.r = BefehlLConsole("r", "Der Laptop wird ausgeschaltet", self.loeschen)
            eingabe = input("laptop@terminal:" + self.laptop.standort.beschreibung +" $ ")
            eingabe = eingabe.lower()
            self.befehl_ausfueren(eingabe)

    def befehl_ausfueren(self, eingabe):
        try:
            befehl_attr = getattr(self, eingabe)
            befehl_attr.funktion() 
        except AttributeError:
            print(eingabe + ": Befehl unbekannt! Gib \"hilfe\" ein")

    def hilfe_anzeigen(self):
        for item in befehlsregister_l:
            item.print_beschreibung()

    def laptop_ausschalten(self):
        self.weiter = False

    def ausfuehren(self):
        self.laptop.standort = self.cafeteria

    def loeschen(self):
        self.ziel_erreicht = True
        self.laptop_ausschalten()
