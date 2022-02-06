import json

A20N = "4850"
CRJ7 = "3000"

def fuel(acSel):
    dist = float(input("What is the distance of your route? "))

    if acSel == 1:
        fb = int(A20N)
    elif acSel == 2:
        fb = int(CRJ7)
    else:
        setFile = open("settings.json")
        jsonObj = json.load(setFile)
        data = jsonObj["settings"]
        fb = data["fuelBurn"]
    
    gs = int(input("What is your planned cruise speed? "))

    ete = (dist/gs)
    fuel = round(ete * float(fb), 10)
    print(fuel)
    fuel = str(fuel)
    if ete < 9:
        ete = ete * 60
        ete = round(ete, 1)
        unit = "minutes"
    else:
        unit = "hours"
    
    ete = str(ete)

    print("Your estimated taxi time for departure is " + ete + " " + unit)
    print("You need " + fuel + " pounds of fuel to fly your route.")

    with open("fuel.json", "a") as fuelFile:
       fuelFile.write('"enroute": %s, \n' % fuel)
    fuelFile.close()
