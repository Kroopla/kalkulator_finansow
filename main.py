from openpyxl.reader.excel import load_workbook

wb = load_workbook("test.xlsx")
ws = wb.active
petla = True
def dodaj():
    print("\nProgramistyczna dupa\n")
    kwota = input("Podaj kwote: ")
    data = input("Data: ")
    ws["A" + str(3+int(ws["D1"].value))] = int(kwota)
    ws["B" + str(3+int(ws["D1"].value))] = str(data)
    ws["D1"] = int(ws["D1"].value) + 1
    ws["B1"] = int(ws["B1"].value) + int(kwota)
    wb.save("test.xlsx")

def wyswietl_wszystko():
    for x in range(3, 3+int(ws["D1"].value)):
        print(str(ws["A" + str(x)].value) + ", " + str(ws["B" + str(x)].value))



if __name__ == '__main__':
    while petla:
        print("\nSaldo:" + str(ws["B1"].value))
        n = int(input("Co chcesz zrobić?\n"
                    "1. Dodaj wydatek lub przychód\n"
                    "2. Wyświetl wszystkie wydatki\n"
                    "0. Zakończ program\n"))
        if n == 1:
            dodaj()
        elif n == 2:
            wyswietl_wszystko()
        elif n == 0:
            print("PaPa...\n")
            exit()
    wb.save("test.xlsx")