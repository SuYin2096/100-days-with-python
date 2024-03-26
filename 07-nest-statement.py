print("Fake Fan Finder")
print("---------------")
favAnime = input("What's your favourite Anime?")

if favAnime == "One piece":
  print("Oh really?! Name me any of the characters?")
  favCharacter = input("What's your favourite character?")
  if favCharacter == "Nami":
     job = input("You got that by pure chance. Okay then, what is her job on the ship?")
     if job == "Navigator":
      bounty = input("Hmph! What was her first bounty then?")
      if bounty == "Ummm...":
        print("See! FAKE One piece fan!")
else:
  print("Oh! You are not the Anime fan!")