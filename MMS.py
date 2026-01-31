class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_info(self):
        return f"Name: {self.name}, Role: {self.role}"