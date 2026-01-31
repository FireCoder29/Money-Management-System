class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_info(self):
        print(f"Name: {self.name}, Role: {self.role}")
    

class Parent(Person):
    def __init__(self, name, salary):
        super().__init__(name, role="Parent")
        self.salary = salary
        self.expenses = {}
        self.remaining_balance = salary

    def add_expense(self, category, amount):
        if amount <= 0:
            print("Invalid Amount! Expense amount must be greater than zero.")
            return
        
        if amount > self.remaining_balance:
            print("Not enough balance")
            return
        
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

        self.remaining_balance -= amount
        print(f"Expense added: {category} - {amount} Taka")

    def give_pocket_money(self, child, amount):
        if amount <= 0:
            print("Invalid Amount! Pocket money must be greater than zero.")
            return
        
        if amount > self.remaining_balance:
            print("Not enough balance to give pocket money")
            return
        
        self.add_expense("Pocket Money", amount)
        child.receive_pocket_money(amount)

    def show_balance(self):
        print(f"Father's Total Salary: {self.salary} Taka")
        print("Expense Details:")
        if not self.expenses:
            print(" - No expenses recorded.")
        else:
            for category, amount in self.expenses.items():
                print(f" - {category}: {amount} Taka")
        print(f"Remaining Balance: {self.remaining_balance} Taka")

    
    class Child(Person):
        def __init__(self, name):
            super().__init__(name, role="Child")
            self.pocket_money = 0
            self.spent = 0
            self.total_received = 0

        def receive_money(self, amount):
            if amount <= 0:
                print("Invalid Amount! Received amount must be greater than zero.")
                return
            
            self.pocket_money += amount
            self.total_received += amount
            print(f"{self.name} received {amount} Taka as pocket money.")

        def receive_extra_income(self, amount):
            if amount <= 0:
                print("Invalid Amount! Extra income must be greater than zero.")
                return

            self.pocket_money += amount
            self.total_received += amount
            print(f"{self.name} received {amount} Taka as extra income.")

        def spend_money(self, amount):
            if amount <= 0:
                print("Invalid Amount! Spend amount must be greater than zero.")
                return

            if amount > self.pocket_money:
                print("Not enough pocket money to spend")
            else:
                self.pocket_money -= amount
                self.spent += amount
                print(f"{self.name} spent {amount} Taka.")

        def show_balance(self):
            print(f"{self.name}'s Pocket Money Details:")
            print(f" - Total Received: {self.total_received} Taka")
            print(f" - Total Spent: {self.spent} Taka")
            print(f" - Remaining Pocket Money: {self.pocket_money} Taka")

parent = Parent("Parent", 50000)
child = Child("Child")

while True:
    print("\n--- Family Money Management System ---")
    print("1. Add Parent's Expenses")
    print("2. Show Parent's Current Balance")
    print("3. Give Pocket Money to Child")
    print("4. Child Spends Money")
    print("5. Child Receives Extra Income")
    print("6. Show Child's Current Balance")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        category = input("Enter expense category (e.g., Food, Transport): ")

        if not category:
            print("Expense category cannot be empty.")
            continue

        if any (char.isdigit() for char in category):
            print("Expense category cannot contain numbers.")
            continue

        try:
            amount = float(input("Enter expense amount (Taka): "))
            parent.add_expense(category, amount)
        except ValueError:
            print("Invalid input! Please enter a numeric value for amount.")
        
    elif choice == "2":
        parent.show_balance()

    elif choice == "3":
        try:
            amount = float(input("Enter pocket money amount to give (Taka): "))
            parent.give_pocket_money(child, amount)
        except ValueError:
            print("Invalid input! Please enter a numeric value for amount.")

    elif choice == "4":
        try:
            amount = float(input("Enter amount for child to spend (Taka): "))
            child.spend_money(amount)
        except ValueError:
            print("Invalid input! Please enter a numeric value for amount.")

    elif choice == "5":
        try:
            amount = float(input("Enter extra income amount for child (Taka): "))
            child.receive_extra_income(amount)
        except ValueError:
            print("Invalid input! Please enter a numeric value for amount.")

    elif choice == "6":
        child.show_balance()

    elif choice == "7":
        print("Exiting the Family Money Management System. Goodbye!")
        break

    else:
        print("Invalid! Please try again.")