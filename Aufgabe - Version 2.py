arr = ['Eins', 'Fünfzehn', 'Zweihundertvierundzwanzig', 'Sechs', 'Sieben', 'Acht']

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

if number in arr:
        if number == 0:
            print(arr[0])
        if number == 15:
            print(arr[1])
        if number == 224:
            print(arr[2])
        if number == 6:
            print(arr[3])
        if number == 7:
            print(arr[4])
        if number == 8:
            print(arr[5])