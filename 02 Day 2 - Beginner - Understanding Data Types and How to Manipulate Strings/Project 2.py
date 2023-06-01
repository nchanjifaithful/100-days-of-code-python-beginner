print("Welcome to the tip Calculator. \n")
totalBill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = (tip / 100) * bill + bill
bill_per_person = bill_with_tip / people
formatted_bill = "{:.2f}".format(bill_per_person)
print(f"Everyone should pay ${bill_per_person}")