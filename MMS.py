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