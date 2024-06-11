class Employee:
    """An attempt to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initializes employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Adds $5,000 to an employee annual salary."""
        self.amount = amount
        self.annual_salary += amount
