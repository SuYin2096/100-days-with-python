print("Generation Identifier")

bornYear = int(input("Which year were you born?"))
if bornYear <= 1900 and bornYear >= 1883:
    print("Lost Generation")

elif bornYear <=1927 and bornYear >= 1901:
    print("Greatest Generation")

elif bornYear <= 1945 and bornYear >= 1928:
    print("Silent Generation")

elif bornYear <=1964  and bornYear >= 1946:
    print("Baby Boomers")

elif bornYear <= 1980 and bornYear >= 1965:
    print("Generation X")

elif bornYear <= 1996 and bornYear >= 1981:
    print("Millennials")

elif bornYear <= 2012  and bornYear >=1997:
    print("Generation Z")

elif bornYear <=2024  and bornYear >= 2013:
    print("Generation Alpha")