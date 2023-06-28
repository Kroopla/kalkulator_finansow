from openpyxl.reader.excel import load_workbook

wb = load_workbook("test.xlsx")
ws = wb.active

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(ws["A1"].value)
