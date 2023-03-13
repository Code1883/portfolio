friends = [

    {"name": "Elvin", "Alter": "22", "Ort": "Bad Cannstatt"},
    {"name": "Enzo", "Alter": "22", "Ort": "Münster"},
    {"name": "Christos", "Alter": "22", "Ort": "Botnang"},
    {"name": "Marco", "Alter": "24", "Ort": "Reutlingen"}
]

for _ in friends:
    print(_["name"], _["Alter"], _["Ort"], sep=" = ")
