x, y, z = input("Expression: ").split(" ")

if y == "+":
    solution = float(x) + float(z)
    
elif y == "-":
    solution = float(x) - float(z)

elif y == "*":
    solution = float(x) * float(z)

elif y == "/":
    solution = float(x) / float(z)
    

print(solution)