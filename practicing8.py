while True:
    n = input("Number: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
    else:
        print("Must be a number.")

print(f"Your Number is {n}")


