print("Exam Grade Calculator")
examName = input("Name of exam:")
maxScore = int(input("Max. Possible Score:"))
yourScore = int(input("Your score:"))

if yourScore >= 90:
  print("You got", yourScore, "%. Which is an A+")
elif yourScore >= 80 and yourScore <= 89:
  print("You got", yourScore, "%. Which is an A-")
elif yourScore >= 70 and yourScore <= 79:
  print("You got", yourScore, "%. Which is a B")
elif yourScore >= 60 and yourScore <= 69:
  print("You got", yourScore, "%. Which is a C")
elif yourScore >= 50 and yourScore <= 59:
  print("You got", yourScore, "%. Which is a D")
elif yourScore >= 40 and yourScore <= 49:
  print("You got", yourScore, "%. Which is an U")