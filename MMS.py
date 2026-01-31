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