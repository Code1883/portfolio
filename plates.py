def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while True:
        if s[0:2].isalpha() and 2 <= len(s) <= 6 and s.isalnum():
            for _ in s:
                if _.isdigit():
                    index = s.index(_)
                    if s[index:].isdigit() and int(_) != 0:
                        return True
                    else:
                        return False
            return True
       
main()