print("Custom Affirmation Generator")
print("----------------------------")

name = input("what is your name?")

if name == "Su" or name == "su":
  print("Hi Su!")

  favouriteThing = input("what is your favourite thing?")

  currentDay = input("what is your currentday of the week?")

  if currentDay == "monday" or currentDay == "Monday":
     print("Hey", name, "you are going to have a great day today")

  elif currentDay == "tuesday" or currentDay == "Tuesday":
     print(name, ", you will have a lucky day today")

  elif currentDay == "wednesday" or currentDay == "Wednesday":
     print("Hello!! ", name, " are you ready for your special day?")

  elif currentDay == "thursday" or currentDay == "Thursday":
     print(name, " what is your plan today?")

  elif currentDay == "friday" or currentDay == "Friday":
     print("Hey", name, " its firday, lets go party!!")

  elif currentDay == "saturday" or currentDay == "Saturday":
     print("Hi!! ", name, " today is holiday, you can do whatever you want")

  elif currentDay == "sunday" or currentDay == "Sunday":
     print("Hello!!! ", name, " its sunday, lets go to church")
  
  else:
     print(name, " are you kidding me?!!!")
else:
   print("Opps!! I don't know you.")