import json

A20N = "4850"
CRJ7 = "3000"

def fuel(acSel):
    dist = float(input("What is the distance of the taxi for departure? "))

    if acSel == 1:
        fb = int(A20N)
    elif acSel == 2:
        fb = int(CRJ7)
    else:
        fb = int(input("What is the fuel burn of your aircraft? "))
        data = {"fuelBurn": fb}
        jsonObj = json.dumps(data, indent = 4)
        with open("settings.json", "a") as setFile:
            setFile.write(jsonObj)
            setFile.write("\n]\n}")
        
    gs = 20

    ete = (dist/gs)
    fuel = round(ete * fb, 2)
    fuel = str(fuel)
    if ete < 9:
        ete = ete * 60
        ete = round(ete, 1)
        unit = "minutes"
    else:
        unit = "hours"

    ete = str(ete)

    print("Your estimated taxi time for departure is " + ete + " " + unit)
    print("You need " + fuel + " pounds of fuel to taxi for departure.")

    with open("fuel.json", "w") as fuelFile:
        fuelFile.write('{"taxiOut": %s, \n' % fuel)
    fuelFile.close()
