import os
import taxi

print("Flight Sim Calculator v 0.0.1")

print("What aircraft would you like to use?")
print("1. A20N")
print("2. CRJ7")
print("3. Other")
sel = int(input("Make your choice: "))

if sel == 1:
    acSel = "A20N"
elif sel == 2: 
    acSel = "CRJ7"
else: 
    acSel = "Other"

with open('settings.txt', 'w') as setFile:
    setFile.writelines('Aircraft Choice: %s, \n' % acSel)
setFile.close()

taxi.fuel(acSel)
