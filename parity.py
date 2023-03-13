def main():
    # Getting the Input of the User + number available's
    x = int(input("What's x? "))
    # Printing Even or Odd 
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    


def is_even(n):
    # Creating Function to see if the input of the user is even or false
    if n % 2 == 0:
        return True
    else:
        return False 

main()
