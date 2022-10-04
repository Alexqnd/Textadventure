import json
from LaptopConsole import *

class Spieler():
	def __init__(self):
		self.name = None
		self.standort = None
		self.laptopC = LaptopConsole()
	
	def umschauen(self):
		print(self.standort.beschreibung)
	
	def checkstandort(self):
		if self.standort.name == "R49":
			self.laptopC.start()
		else:
			print("Der Unterricht fängt an! Du musst zuerst in den Klassenraum.")
	
	def bewege_nach_n(self):
		self.gehen(0, "Norden")
	
	def bewege_nach_o(self):
		self.gehen(1, "Osten")

	def bewege_nach_s(self):
		self.gehen(2, "Süden")
	
	def bewege_nach_w(self):
		self.gehen(3, "Westen")

	def gehen(self, ausgang, richtung):
		if self.standort.ausgaenge[ausgang] != None:
			self.standort = self.standort.ausgaenge[ausgang]
			print(f"{self.name} geht nach {richtung}.")
		else:
			print(f"Keine Tür im {richtung}!")


class Raum():
	def __init__(self, pname, pbeschreibung):
		self.name = pname
		self.beschreibung = pbeschreibung
		self.ausgaenge = [None] * 4

befehlsregister_t = []


class BefehlTConsole():
	def __init__(self, pname, pbeschreibung, pfunktion):
		self.name = pname
		self.beschreibung =  pbeschreibung
		self.funktion = pfunktion
		befehlsregister_t.append(self)

	def print_beschreibung(self):
		print(self.name + ":")
		print(self.beschreibung)
		print()


class TextadventureConsole():
	def __init__(self):
		self.weiter = True
		self.load_text()
		self.raeume_erstellen()
		self.raeume_verbinden()
		self.spieler_erstellen()
		self.befehle_zuweisen()

	def load_text(self):
		with open('text.json') as f:
			self.text = json.load(f)

	def read(self, name):
		return self.text[0][name]


	def spieler_erstellen(self):
		self.spieler = Spieler()
		self.spieler.standort = self.cafeteria		

	def raeume_erstellen(self):
		self.r49 = Raum("R49", "Die Klassenkameraden sitzen schon")
		self.cafeteria = Raum("Cafeteria", "Die Cafeteria ist  halb voll")
		self.flur = Raum("Flur", "Der Flur ist leer")
		self.lehrerzimmer = Raum("Lehrerzimmer", "Lehrerzimmer fast leer")

	def raeume_verbinden(self):
		self.r49.ausgaenge[1] = self.flur
		self.flur.ausgaenge[3] = self.r49
		self.flur.ausgaenge[0] = self.cafeteria
		self.flur.ausgaenge[1] = self.lehrerzimmer
		self.lehrerzimmer.ausgaenge[3] = self.flur
		self.cafeteria.ausgaenge[2] = self.flur

	def befehle_zuweisen(self):
		self.n = BefehlTConsole("n", "Lässt den Spieler nach Norden gehen.", self.spieler.bewege_nach_n)
		self.o = BefehlTConsole("o", "Lässt den Spieler nach Osten gehen.", self.spieler.bewege_nach_o)
		self.s = BefehlTConsole("s", "Lässt den Spieler nach Süden gehen.", self.spieler.bewege_nach_s)
		self.w = BefehlTConsole("w", "Lässt den Spieler nach Westen gehen.", self.spieler.bewege_nach_w)
		self.ls = BefehlTConsole("ls", "Schauen, was dort los ist", self.spieler.umschauen)
		self.laptop = BefehlTConsole("laptop", "Den Laptop benutzen. Er kann aber erst im Klasenraum verwendet werden, weil der Unterricht schon anfängt.", self.spieler.checkstandort)
		self.hilfe = BefehlTConsole("hilfe", "Zeigt alle Befehle an, die der Spieler verwenden kann.", self.hilfe_anzeigen)
		self.q = BefehlTConsole("q", "Verlassen des Spiels. Der Fortschritt wird NICHT gespeichert!", self.spielverlassen)

	def befehl_ausfueren(self, eingabe):
		#try:
		befehl_attr = getattr(self, eingabe) 
		befehl_attr.funktion() 
		#except AttributeError:
		#print(eingabe + ": Befehl unbekannt! Gib \"hilfe\" ein.")

	def hilfe_anzeigen(self):
		for item in befehlsregister_t:
			item.print_beschreibung()

	def spielverlassen(self):
		self.weiter = False

	def run(self):
		text = Text()
		self.spieler.name = input(self.read("name"))
		self.introduction()
		while self.weiter == True and self.spieler.laptopC.ziel_erreicht == False:
			eingabe = input(self.spieler.name.lower() + "@" + self.spieler.name.lower() + "-terminal:" + self.spieler.standort.name + " $ ")
			eingabe = eingabe.lower()
			self.befehl_ausfueren(eingabe)
		if self.spieler.laptopC.ziel_erreicht == True:
			self.congratulations()

	def introduction(self):
		print(self.spieler.name +  self.read("softwareaufgabe"))
		print("Der fleißige " +  self.spieler.name +  " hat das auch recht schnell hinbekommen.")
		print("Leider hat " + self.spieler.name + " einen großen Fehler in seinem Programm gemacht und kann auf")
		print("die Außenwelt nur noch über die Konsole zugreifen.")
		print("Um alle Befehle zu sehen, die " +  self.spieler.name +  " verwenden kann, gibt man \"hilfe\" ein.")

	def congratulations(self):
		print("Das fehlerhafte Programm wurde gelöscht. Nun kann " + self.spieler.name + " wieder") 
		print("ganz normal mit der Außenwelt interagieren.")
		print()
		print("Vielen Dank fürs Spielen!")
		print("Ein Spiel von Alexander Quindt")



