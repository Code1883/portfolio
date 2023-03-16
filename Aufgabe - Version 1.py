while True:
  try:
    number = input("Bitte eine Zahl von 0 bis 999 eingeben: ")
    if number.isdigit():
       number=int(number)
    else:   
       raise ValueError()
    if 0 <= number <= 999:
        break
    raise ValueError()
  except ValueError:
    print("Bitte geben Sie eine Zahl zwischen 0 und 999 ein.")


if number == 1:
    print("Eins")
if number == 15:
    print("Fünfzehn")
if number == 224:
    print("Zweihundertvierundzwanzig")
if number == 6:
    print("Sechs")
if number == 7:
    print("Sieben")
if number == 8:
    print("Acht")

