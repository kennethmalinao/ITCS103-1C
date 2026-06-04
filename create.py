import openpyxl as op

wbk= op.Workbook()
sheet = wbk.active

sheet ['A1'] = "ID"
sheet ['B1'] = "Guest Name"
sheet ['C1'] = "Room Number"
sheet ['D1'] = "Room type"
sheet ['E1'] = "Check-in"
sheet ['F1'] = "Check-Out"
sheet ['G1'] = "Down Payment"
sheet ['H1'] = "Days Reserved"

wbk.save("Malinao_Database.xlsx")