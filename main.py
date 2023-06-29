from openpyxl.reader.excel import load_workbook

wb = load_workbook("test.xlsx")
ws = wb.active
petla = True
def dodaj():
    kwota = input("Podaj kwote: ")
    data = input("Data: ")
    kategoria = input("Kategoria: ")
    opis = input("Opis: ")

    ws["A" + str(3+int(ws["D1"].value))] = int(kwota)
    ws["B" + str(3+int(ws["D1"].value))] = str(data)
    ws["C" + str(3+int(ws["D1"].value))] = str(kategoria)
    ws["D" + str(3+int(ws["D1"].value))] = str(opis)

    ws["D1"] = int(ws["D1"].value) + 1
    ws["B1"] = int(ws["B1"].value) + int(kwota)
    wb.save("test.xlsx")

def wyswietl_wszystko():
    print(str(ws["A2"].value) + "\t" + str(ws["B2"].value) + "\t\t" + str(ws["C2"].value) + "\t" + str(ws["D2"].value))
    for x in range(3, 3+int(ws["D1"].value)):
        print(str(ws["A" + str(x)].value) + ",\t" + str(ws["B" + str(x)].value) + ",\t" +
              str(ws["C" + str(x)].value) + ",\t\t" + str(ws["D" + str(x)].value))

def wyczysc_wszystko():
    for x in range(3, 3+int(ws["D1"].value)):
        ws.delete_rows(3)
        ws["D1"] = 0
        ws["B1"] = 0
    wb.save("test.xlsx")

if __name__ == '__main__':
    while petla:
        print("\nSaldo:" + str(ws["B1"].value))
        n = int(input("Co chcesz zrobić?\n"
                    "1. Dodaj wydatek\n"
                    "2. Wyświetl wszystkie wydatki\n"
                    "9. Wyczyść cały kalkulator\n"
                    "0. Zakończ program\n"))
        if n == 1:
            dodaj()
        elif n == 2:
            wyswietl_wszystko()
        elif n == 9:
            print("Na pewno chcesz wyczyścić całą historię? Sracisz w ten sposób wszyskie dane")
            w = int(input("1. Nie! Nie chcę stracić moich cennych danych\n"
                          "9. Tak, chcę wyczyścić całą historię i zacząć od zera\n"))
            if w == 9:
                wyczysc_wszystko()
            elif n == 1:
                continue
        elif n == 0:
            print("PaPa...\n")
            exit()
    wb.save("test.xlsx")