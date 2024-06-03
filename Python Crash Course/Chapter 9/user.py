class User:
    """A simple attempt of modeling a user."""
    def __init__(self, first_name, last_name, age, address, login_attempts=0):
        """Initializes attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.login_attempts = login_attempts

    def describe_user(self):
        """Display the information of a specified user."""
        print("\nUser info:")
        print(f"\nFirst name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

    def greet_user(self):
        """Greets the specified user."""
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts back to 0."""
        self.login_attempts = 0