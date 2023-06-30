from openpyxl.reader.excel import load_workbook
import datetime
import numpy as np
import matplotlib.pyplot as plt

wb = load_workbook("test.xlsx")
ws = wb.active


def dodaj():
    kwota = input("Podaj kwote: ")
    data = input("Data: ")
    kategoria = input("Kategoria: ")
    opis = input("Opis: ")

    ws["A" + str(3 + int(ws["D1"].value))] = int(kwota)
    ws["B" + str(3 + int(ws["D1"].value))] = str(data)
    ws["C" + str(3 + int(ws["D1"].value))] = str(kategoria)
    ws["D" + str(3 + int(ws["D1"].value))] = str(opis)

    ws["D1"] = int(ws["D1"].value) + 1
    ws["B1"] = int(ws["B1"].value) + int(kwota)
    wb.save("test.xlsx")


def wyswietl(x):
    print(str(ws["A" + str(x)].value) + ",\t" + str(ws["B" + str(x)].value) + ",\t" +
          str(ws["C" + str(x)].value) + ",\t\t" + str(ws["D" + str(x)].value))


def wyczysc_wszystko():
    for x in range(3, 3 + int(ws["D1"].value)):
        ws.delete_rows(3)

    ws["D1"] = 0
    ws["B1"] = 0
    wb.save("test.xlsx")


def szukaj_data():
    dzien = input("Dzień: ")
    miesiac = input("Miesiąc: ")
    rok = input("Rok: ")
    print(str(ws["A2"].value) + "\t" + str(ws["B2"].value) + "\t\t" + str(ws["C2"].value) + "\t" + str(ws["D2"].value))
    for x in range(3, 3 + int(ws["D1"].value)):
        if dzien == "" and miesiac == "" and rok == str(ws["B" + str(x)].value)[6:10]:
            wyswietl(x)
        elif dzien == "" and miesiac == str(ws["B" + str(x)].value)[3:5] and rok == str(ws["B" + str(x)].value)[6:10]:
            wyswietl(x)
        elif dzien == str(ws["B" + str(x)].value)[0:2] and miesiac == str(ws["B" + str(x)].value)[3:5] and rok == str(
                ws["B" + str(x)].value)[6:10]:
            wyswietl(x)


def okres():
    dzien_p = int(input("Dzień początkowy: "))
    miesiac_p = int(input("Miesiąc początkowy: "))
    rok_p = int(input("Rok początkowy: "))
    data_p = datetime.date(rok_p, miesiac_p, dzien_p)

    dzien_k = int(input("Dzień końcowy: "))
    miesiac_k = int(input("Miesiąc końcowy: "))
    rok_k = int(input("Rok końcowy: "))
    data_k = datetime.date(rok_k, miesiac_k, dzien_k)

    print(str(ws["A2"].value) + "\t" + str(ws["B2"].value) + "\t\t" + str(ws["C2"].value) + "\t" + str(ws["D2"].value))
    for x in range(3, 3 + int(ws["D1"].value)):
        data_x = datetime.date(int(str(ws["B" + str(x)].value)[6:10]), int(str(ws["B" + str(x)].value)[3:5]),
                               int(str(ws["B" + str(x)].value)[0:2]))
        if data_p <= data_x <= data_k:
            wyswietl(x)


def szukaj_kategoria():
    kategoria = input("Karegoria: ")
    print(str(ws["A2"].value) + "\t" + str(ws["B2"].value) + "\t\t" + str(ws["C2"].value) + "\t" + str(ws["D2"].value))
    for x in range(3, 3 + int(ws["D1"].value)):
        if kategoria == str(ws["C" + str(x)].value):
            wyswietl(x)


def wykres():
    x = []
    y = []

    wyk = input("Wykres ma być:\n"
                "1. Liniowy\n"
                "2. Słupkowy\n"
                "(Dowolna wartość) Powrót\n")
    if wyk != "1" and wyk != "2":
        return

    dzien_p = int(input("Dzień początkowy: "))
    miesiac_p = int(input("Miesiąc początkowy: "))
    rok_p = int(input("Rok początkowy: "))
    data_p = datetime.date(rok_p, miesiac_p, dzien_p)

    dzien_k = int(input("Dzień końcowy: "))
    miesiac_k = int(input("Miesiąc końcowy: "))
    rok_k = int(input("Rok końcowy: "))
    data_k = datetime.date(rok_k, miesiac_k, dzien_k)

    for n in range(3, 3 + int(ws["D1"].value)):
        data_x = datetime.date(int(str(ws["B" + str(n)].value)[6:10]), int(str(ws["B" + str(n)].value)[3:5]),
                               int(str(ws["B" + str(n)].value)[0:2]))
        if data_p <= data_x <= data_k:
            x.append(str(ws["B" + str(n)].value))
            y.append(str(ws["A" + str(n)].value))
    if wyk == "1":
        plt.plot(x, y)
    elif wyk =="2":
        plt.bar(x,y)
    plt.xlabel("Data")
    plt.ylabel("Kwota")
    plt.show()


if __name__ == '__main__':
    while True:
        n = input("\nCo chcesz zrobić?\n"
                  "1. Dodaj wydatek\n"
                  "2. Wyświetl wszystkie wydatki\n"
                  "3. Szukaj\n"
                  "4. Wykres \n"
                  "9. Wyczyść cały kalkulator\n"
                  "0. Zakończ program\n")
        if n == "1":
            dodaj()
        elif n == "2":
            print(str(ws["A2"].value) + "\t" + str(ws["B2"].value) + "\t\t" +
                  str(ws["C2"].value) + "\t" + str(ws["D2"].value))
            for x in range(3, 3 + int(ws["D1"].value)):
                wyswietl(x)
        elif n == "3":
            print("Chcę szukać po:")
            s = input("1. Dacie\n"
                      "2. Okresie\n"
                      "3. Kategorii\n"
                      "(Dowolna wartość) Wróć\n")
            if s == "1":
                szukaj_data()
            elif s == "2":
                okres()
            elif s == "3":
                szukaj_kategoria()
            else:
                continue

        elif n == "4":
            wykres()
        elif n == "9":
            print("Na pewno chcesz wyczyścić całą historię? Sracisz w ten sposób wszyskie dane")
            w = input("(Dowolna wartość) Nie! Nie chcę stracić moich cennych danych\n"
                      "9. Tak, chcę wyczyścić całą historię i zacząć od zera\n")
            if w == "9":
                wyczysc_wszystko()
            else:
                continue

        elif n == "0":
            print("\nPaPa...\n")
            exit()

        else:
            print("Podano złą wartość!\n")
    wb.save("test.xlsx")
