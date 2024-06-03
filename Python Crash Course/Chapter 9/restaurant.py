class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Tells everyone that the restaurant is open"""
        print(f"{self.restaurant_name} restaurant is now open!")

    def set_number_served(self, num):
        """Set the number of customers that have been served."""
        self.number_served = num

    def increment_number_served(self, num):
        """Increments the number of customers that have been served."""
        self.number_served += num

class IceCreamStand(Restaurant):
    """An attempt to model an ice cream stand based on restaurant class."""
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        """
        Initializes attributes of the parent class.
        Then initializes attributes specific to ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = flavors
        
        
    def display_flavors(self):
        print(f"Selected flavors: {self.flavors}")

