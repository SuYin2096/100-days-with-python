print("Tip Calculator")

spentAmount = float(input("How much did you spend?:"))

tipPercent = int(input("What percentage do you want to tip?:"))

numberOfPeople = int(input("How many people in your group?:"))

totalBill = spentAmount * (1+tipPercent/100)

amountPerPerson = round(totalBill/numberOfPeople, 2)

print("You eacyh owe $", amountPerPerson)