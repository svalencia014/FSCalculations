#Import packages
import json

#Define Fuel Burn Vars
a20n = 4850
crj7 = 3000

a20nCruise = 425
crj7Cruise = 400
customCruise = 0

print("Flight simulator fuel calculator v 0.1")
print("1. A20N")
print("2. CRJ7")
print("3. Other")
print("What plane are you using?")

acSel = int(input("Choose one: "))

if acSel == 1:
    fb = a20n
elif acSel ==2:
    fb = crj7
elif acSel == 3:
    fb = int(input("What is the fuel burn of your Aircraft? "))
    customCruise = int(input("What is the cruise speed of your aircraft? "))

#--------------Taxi Out --------------
dist = float(input("What is the distance to taxi to the runway? "))
gs = 20

ete = (dist/gs)
fuel = round(ete * fb, 2)

if ete < 1:
    ete = (ete * 60)
    unit = "minutes"
else:
    unit = "hours"

ete = str(ete)
fuel = str(fuel)

print(f'It will take {ete} {unit} to taxi to the runway.')
print(f'It will take {fuel} pounds of fuel to taxi to the runway')
outFuel = fuel
#-------------------------------------
#------------Enroute------------------
dist = int(input("What is the distance of your route? "))
if acSel == 1:
    gs = a20nCruise
elif acSel == 2:
    gs = crj7Cruise
elif acSel == 3:
    gs = customCruise

ete = (dist/gs)
fuel = round(ete * fb, 2)

if ete < 1:
    ete = (ete * 60)
    unit = "minutes"
else:
    unit = "hours"

ete = str(ete)
fuel = str(fuel)

print(f'It will take {ete} {unit} to fly your route.')
print(f'It will take {fuel} pounds of fuel to fly your route.')
enrouteFuel = fuel
#-------------------------------------
#-----------Taxi In-------------------
dist = float(input("What is the distance to taxi to the ramp? "))
gs = 20

ete = (dist/gs)
fuel = round(ete * fb, 2)

if ete < 1:
    ete = (ete * 60)
    unit = "minutes"
else:
    unit = "hours"

print(f'It will take {ete} {unit} to taxi to the ramp.')
print(f'It will take {fuel} pounds to taxi to the ramp')
inFuel = fuel
#-------------------------------------
#-----------Emergency Fuel------------
ete = int(input("How many minutes of extra fuel do you need? "))
extra = int(input("Any extra? "))

ete = (ete / 60)
fuel = round(ete * fb, 2)
fuel = fuel + extra
fuel = str(fuel)
print(f'Add {fuel} pounds of fuel.')
emergencyFuel = fuel

#-------------------------------------
#--------Calculate Total Fuel---------
totalFuel = float(outFuel) + float(enrouteFuel) + float(inFuel) + float(emergencyFuel)
print(f'You need {str(totalFuel)} pounds of fuel for this flight')