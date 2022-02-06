import taxiOut
import enroute
import json

with open("settings.json", "w") as setFile:
    setFile.write('{\n "settings": [\n')

print("Flight Sim Calculator v 0.0.1")

print("What aircraft would you like to use?")
print("1. A20N")
print("2. CRJ7")
print("3. Other")
sel = int(input("Make your choice: "))

if sel == 1:
    sel == "A20N"
elif sel == 2:
    sel == "CRJ7"
else:
    sel == "Other"

data = {"aircraft": sel}
jsonObj = json.dumps(data, indent = 4)
with open("settings.json", "a") as setFile:
    setFile.write(jsonObj)
    setFile.write(", \n")

taxiOut.fuel(sel)
enroute.fuel(sel)