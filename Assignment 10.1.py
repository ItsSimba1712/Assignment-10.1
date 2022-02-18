import os
import json

createDirectory = input("Please select where you would like to save your file! ")

os.makedirs(createDirectory)

os.chdir(createDirectory)
print(os.getcwd())

filePath = input("Please specify what you want to call your file! ")

with open(filePath, "w+") as f:
    f.write
    x = {
    "name" : input("Enter name "),
    "address" : input("Enter address "),
    "phonenumber" : input("Enter phone number ")
    }
    json.dump(x, f)