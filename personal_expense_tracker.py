
import os
from datetime import datetime
FILE_NAME = "expense.csv"
def add_expense():
    item = input("Where Did You Spend It: ")
    try:
        price = float(input("How Much Money Did You Spend It: "))
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("expense.csv", "a") as file:
            file.write(f"{now},{item},{price}\n")
        print("Expense Added Successfully!")
    except ValueError:
        print("Error: Please Enter Price In Numbers Only!")

def show_total():
    total = 0
    if os.path.exists("expense.csv"):
        with open("expense.csv", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 3:
                    total += float(data[2])
                elif len(data) == 2:
                    total += float(data[1])
        print(f"\n Total Money Spent: {total} PKR")
    else:
        print("No Records Found!")

def search_expense():
    query = input("Enter Item Name To Search: ").lower()
    found = False
    if os.path.exists("expense.csv"):
        with open("expense.csv", "r") as file:
            print(f"\n--- Search Results For '{query}. ---")
            for line in file:
                if query in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("No Matching Records Found.")
    else:
        print("No Data File Found.")

def delete_expense():
    if os.path.exists("expense.csv"):
        with open("expense.csv", "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")
            
        try:
            no = int(input("Which Number To Delete?: "))
            if 1 <= no <= len(lines):
                lines.pop(no - 1) 
                with open("expense.csv", "w") as f:
                    f.writelines(lines) 
                print ("Deleted!")
        except:
            print("Error: Please Try Again!")

def main():
    while True:
        print("\n" + "="*10 + " PRO EXPENSE TRACKER " + "="*10)
        print("1. Add Expense")
        print("2. Show Total Expense")
        print("3. View All Records")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nEnter An Option(1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_total()
        elif choice == "3":
            if os.path.exists("expense.csv"):
                with open("expense.csv", "r") as file:
                    print("\n--- All Records ---\n", file.read())
            else:
                print("File Not Found!")
        elif choice == "4":
            search_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("GOOD BYE! HAPPY CODING.")
            break
        else:
            print("Invalid Option, Try Again.")
if __name__ == "__main__":
    main()
                  




    
                


