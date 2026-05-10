import openpyxl as op
from datetime import datetime

wbk = op.Workbook()
sheet = wbk.active

sheet['A1'] = "ID"
sheet['B1'] = "First Name"
sheet['C1'] = "Last Name"
sheet['D1'] = "Birth Year"
sheet['E1'] = "Age"

print("\nPerson 1")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth_year = int(input("Birth Year: "))
age = 2026 - birth_year

sheet["A2"] = 1
sheet["B2"] = first_name
sheet["C2"] = last_name
sheet["D2"] = birth_year
sheet["E2"] = age

print("\nPerson 2")
first_name1 = input("First Name: ")
last_name1 = input("Last Name: ")
birth_year1 = int(input("Birth Year: "))
age1 = 2026 - birth_year1

sheet["A3"] = 2
sheet["B3"] = first_name1
sheet["C3"] = last_name1
sheet["D3"] = birth_year1
sheet["E3"] = age1

print("\nPerson 3")
first_name2 = input("First Name: ")
last_name2 = input("Last Name: ")
birth_year2 = int(input("Birth Year: "))
age2 = 2026 - birth_year2

sheet["A4"] = 3
sheet["B4"] = first_name2
sheet["C4"] = last_name2
sheet["D4"] = birth_year2
sheet["E4"] = age2

print("\nFavorite people saved succesfully")

print(("\n===== FAVORITE PEOPLE LIST=====\n"))
print(("ID", "First Name", "Last Name", "Birth Year", "Age"))
print((1, first_name, last_name, birth_year, age))
print((2, first_name1, last_name1, birth_year1, age1))
print((3, first_name2, last_name2, birth_year2, age2))

wbk.save("favorite_people.xlsx")

input("\nPress Enter to exit...")