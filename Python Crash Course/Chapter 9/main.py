from restaurant import Restaurant, IceCreamStand
from user import User
from admin import Admin
from electric_car import Car, ElectricCar, Battery
from die import Die

# 9-1
# restaurant = Restaurant('Shangrila', 'Chinese')

# print(f"The new restaurant is called {restaurant.restaurant_name}.")
# print(f"It serves {restaurant.cuisine_type} food.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9-2
# restaurant_1 = Restaurant('Shangrila', 'Chinese')
# restaurant_2 = Restaurant('KFC', 'American')
# restaurant_3 = Restaurant('Pizza Hut', 'Italian')

# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()

# 9-3
# user_john = User('John', 'Doe', 50, 'US')
# user_john.describe_user()
# user_john.greet_user()

# user_sarah = User('Sarah', 'Blake', 24, 'UK')
# user_sarah.describe_user()
# user_sarah.greet_user()

# 9-4
# restaurant = Restaurant('Shangrila', 'Chinese')

# print(f"The new restaurant is called {restaurant.restaurant_name}.")
# print(f"It serves {restaurant.cuisine_type} food.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.set_number_served(4)
# restaurant.increment_number_served(2)

# print(f"The restaurant has served {restaurant.number_served} customers.")

# 9-5
# user_john = User('John', 'Doe', 50, 'US')
# user_john.describe_user()
# user_john.greet_user()
# user_john.increment_login_attempts()
# user_john.increment_login_attempts()
# user_john.increment_login_attempts()
# print(f"Login attempts: {user_john.login_attempts}")
# user_john.reset_login_attempts()
# print(f"Login attempts: {user_john.login_attempts}")

# 9-6
# woodie = IceCreamStand('Woodie', 'dessert', 'chocolate')
# woodie.describe_restaurant()
# woodie.display_flavors()

# 9-7
# bob = Admin('Bob', 'Powell', 19, 'Ireland', ['can add post', 'can delete post',
#  'can ban user'])
# bob.show_privileges()

# 9-8
# alice = Admin('Alice', 'Steward', 26, 'Japan', ['can add post', 'can delete post',
#  'can ban user'])
# alice.priveleges.show_privileges()

# 9-9
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
# my_leaf.battery.upgrade_battery()
# my_leaf.battery.get_range()

# 9-13
# new_die = Die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()
# new_die.roll_die()

# ten_sided_die = Die(10)
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()

# twenty_sided_die = Die(20)
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()

# 9-14 and 9-15
from random import choice

char_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 
    'd', 'e')
my_ticket = '5b2c'
winning_ticket = ''
count = 0

while True:
    for i in range(4):
        winning_ticket += choice(char_list)
    if winning_ticket == my_ticket:
        break
    winning_ticket = ''
    count += 1

print(f"The winner of the lottery is: {winning_ticket}")
print(f"It took {count} tries to win.")