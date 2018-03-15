try:
    name = str(input("Enter your Name:"))
except TypeError:
    print("Invalid Name")
print("Finished")

import os
print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
 print(item)