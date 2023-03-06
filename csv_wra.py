import csv


def erstellen():
    file = open("Datenbank.csv", "w", encoding="UTF-8") #erstellen der csv Datei
    file.close()                                        #schließen der Datei


# Daten der Datei hinzufügen
def teschreiben():
    name = input("Name: ")

    tel = input("Telefonnummer: ")

    eintrag = [name, tel]

    file = open("telefon.csv", "a", encoding="utf-8")

    writerobj = csv.writer(file, delimiter=";", lineterminator="\n") # delimiter heißt wie die Zeichentrennung aussehensoll
    # lineterminator sorgt dafür das beim einfügen einer neuen Datei eine neue Zeile benutzt wird

    writerobj.writerow(eintrag) # beschreibt eine Reihe

    file.close()

    print(eintrag)

    print("Eintrag erfolgreich eingefügt.")

# Aus der Datei auslesen
def telesen():
    fileobj = open("telefon.csv", "r", encoding="utf-8")

    readerobj = csv.reader(fileobj, delimiter=";")

    telefonliste=[]

    for z in readerobj:
        telefonliste.append(z)

    fileobj.close()

    header = ["Name", "Telefon"]
    Ueberschrift = f"|{header[0]:20}|{header[1]:15}|"
    print(Ueberschrift)
    print("-"*len(Ueberschrift))

    for z in telefonliste:
        print(f"|{z[0]:20}|{z[1]:15}|")





