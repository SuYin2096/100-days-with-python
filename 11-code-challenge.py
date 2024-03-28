numOfSecondsInADay = 60 * 60 * 24

numOfDaysInAYear = 120 + 217 + 28;

leapYear = input("Is it a leap year?")

if leapYear == "yes":
  numOfDaysInAYear = numOfDaysInAYear +1;
else:
  numOfDaysINAYear = numOfDaysInAYear;

numOfSecondsInAYear = numOfSecondsInADay * numOfDaysInAYear;

print("Total seconds in a year: ", numOfSecondsInAYear)