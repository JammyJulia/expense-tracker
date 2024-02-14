#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

import json


with open("expenses.json",'r') as file:
    expenses = json.load(file)

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

def save():
    with open("expenses.json", "w") as otherfile:
        json.dump(expenses, otherfile)

def sort(expense):
    return int(expense["sum"])

while True:
    command = input('''\nChoose command 
1 - Add new expense
2 - View all expenses
3 - View 10 biggest expenses
4 - View 10 smallest expenses
5 - Avarage expense sum
e - Exit
Select: ''')
    if command == "1":
        name = input('Name: ')
        while True:
            try:
                sum = round(float(input('Sum: ')), 2)
                break
            except:
                print("Not a number!")
        category = input('Category: ')
        newexpense = {"name" : name, "sum" : sum, "category" : category}
        try:
            expenses.append(newexpense)
        except AttributeError:
            expenses = []
            expenses.append(newexpense)
        print(expenses)
        save()
    if command == "2":
        for i in expenses:
            print("-------------------")
            print("Name:", i["name"])
            print("Sum:", i["sum"])
            print("Category:", i["category"])
    if command == "3":
        expenses.sort(key = sort, reverse=True)
        for i in range(10):
            try:
                print("-------------------")
                print("Name:", expenses[i]["name"])
                print("Sum:", expenses[i]["sum"])
                print("Category:", expenses[i]["category"])
            except:
                break
    if command == "4":
        expenses.sort(key = sort)
        for i in range(10):
            try:
                print("-------------------")
                print("Name:", expenses[i]["name"])
                print("Sum:", expenses[i]["sum"])
                print("Category:", expenses[i]["category"])
            except:
                break
    if command == "5":
        summa = 0
        for i in expenses:
            summa += i['sum']
        avarage = summa/len(expenses)
        print("Avarage", round(avarage, 2))
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

