expenses = []

def show_menu():
    print("===================")
    print("  EXPENSE TRACKER  ")
    print("===================")
    print("1. Add Expense")
    print("2. View expenses")
    print("3. View Total")
    print("4. Quit")

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: $"))
    category = input("Enter category (Food/Transport/Shopping/Other): ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense Added! ✅")

def view_expenses():
    for expense in expenses:
        print(f"{expense['name']} - ${expense['amount']} - {expense['category']}")

def view_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ${total:.2f}")

while True:
    show_menu()
    select = input("Pick a number from 1-4: ")
    if select not in ["1","2","3","4"]:
        print("Wrong number! Pick a number between 1-4!")
    elif select == "1":
        add_expense()
    elif select == "2":
        view_expenses()
    elif select == "3":
        view_total()
    elif select == "4":
        print("Goodbye! 👋")
        break


     
   
