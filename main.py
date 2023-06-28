from openpyxl.reader.excel import load_workbook

wb = load_workbook("test.xlsx")
ws = wb.active
petla = True
def dodaj():
    print("\nProgramistyczna dupa\n")

def wyswietl_wszystko():
    for x in range(3, 3+int(ws["D1"].value)):
        print(str(ws["A" + str(x)].value))



if __name__ == '__main__':
    while petla:
        print("Saldo:" + str(ws["A2"].value))
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