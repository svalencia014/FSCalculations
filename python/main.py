#Import packages
import json

#Define Fuel Burn Vars
a20n = 4850
crj7 = 3000
fb = 0

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

#----------Taxi Out Fuel--------------
dist = int(input("What is the distance to taxi to the runway? "))
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
#-------------------------------------
#------------Enroute------------------

