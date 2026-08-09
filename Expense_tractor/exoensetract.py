import csv
import os
from datetime import datetime

FILE_NAME = "expense.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Note"])

def add_expense():
    amount = input("Enter the amount: ")
    category = input("Enter the category (like food, travelling, bills...): ")
    note = input("Enter the note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("Expense added successfully")

def view_expense():
    if not os.path.exists(FILE_NAME):
        print("No expense found")
        return
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_spent():
    if not os.path.exists(FILE_NAME):
        print("No expense found")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[1])
    print("Total spent:", total)

def main():
    create_file()
    while True:
        print("------------ Expense Tracker --------------")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Spent")
        print("4. Exit")
        print("-------------------------------------------")

        c = input("Enter your choice (1-4): ")
        if c == "1":
            add_expense()
        elif c == "2":
            view_expense()
        elif c == "3":
            total_spent()
        elif c == "4":
            print("Bye")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()


# import csv
# import os
# from datetime import datetime

# FILE_NAME = "expense.csv"

# def create_file():
#     if not os.path.exists(FILE_NAME):
#         with open(FILE_NAME, "w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(["Date", "Amount", "Category", "Note"])

# # create_file()
# # print("done")

# def add_expense():
#     amount=input("Enter the amount:")
#     category=input("enter the category (like foor, travelling, ebills....)")
#     note=input("enter the note(optional)")
#     date=datetime.now().strftime("%y-%m-%d")

#     with open("expense.csv","a",newline="") as file:
#         writer=csv.writer(file)
#         writer.writerow([date,amount,category,note])
#         print("Expense added successfully")

#     # add_expense()
# def view_expense():
#     if not os.path.exists("expense.csv"):
#         print("no expense found")
#         return
#     with open("expense.csv","r") as file:
#         reader=csv.reader(file)
#         for row in reader:
#             print(row)
# #  view_expense()

# def total_spent():
#     if not os.path.exists("expense.csv"):
#         print("no expense found")
#         return

#     total=0
#     with open("expense.csv","r") as file:
#         reader=csv.reader(file)
#         next(reader)
#         for row in reader:
#             total=total+float(row[1])

#             print("total spent : ",total)

# def main():
#     create_file()
#     while True:
#         print("------------Expense tractor--------------")
#         print("\n 1. Add Expense")
#         print("\n 2. View Expense")
#         print("\n 3. Total Spent")
#         print("\n 4. Exit")
#         print("------------------------------------------")

#         c=input("enter your choice (1-4)")
#         if c=="1":
#             add_expense()
#         elif c=="2":
#             view_expense()
#         elif c=="3":
#             total_spent()
#           elif c=="4":
#             print("Bye")
#             break
#         else:
#             print("Invalid")

