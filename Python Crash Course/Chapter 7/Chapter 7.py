'''7-1. Rental Car: Write a program that asks the user what kind of rental car 
they would like. Print a message about that car, such as “Let me see if I can 
find you a Subaru.”'''

# car_type = input("What kind of car would you like to rent? ")
# print(f"Let me see if I can find you a {car_type.title()}.")

'''7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message 
saying they'll have to wait for a table. Otherwise, report that their table is 
ready.'''

# num_of_people = input("How many people are in your dinner group? ")
# num_of_people = int(num_of_people)

# if num_of_people > 8:
#     print("Sorry, you'll have to wait for a table.")
# else:  
#     print("Your table is ready.")

'''7-3. Multiples of Ten: Ask the user for a number, and then report whether 
the number is a multiple of 10 or not.'''

# num = input("Please type a number: ")
# num = int(num)

# if num % 10 == 0:
#     print("Your number is a multiple of 10.")
# else:
#     print("Your number is not a multiple of 10.")


'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you'll add that topping to their pizza.'''

# pizza_topping = ''

# while pizza_topping != 'quit':
#     pizza_topping = input("Enter your desired pizza toppings: ")
#     if pizza_topping == 'quit':
#         break
#     else:
#         print(f"Adding {pizza_topping} to your pizza.")

'''7-5. Movie Tickets: A movie theater charges different ticket prices 
depending on a person's age. If a person is under the age of 3, the ticket is 
free; if they are between 3 and 12, the ticket is $10; and if they are over age
12, the ticket is $15. Write a loop in which you ask users their age, and then 
tell them the cost of their movie ticket.'''

# age = None
# ticket_price = None
# prompt = "\nPlease enter your age:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     age = input(prompt)

#     if age == 'quit':
#         break

#     age = int(age)
#     if age < 3:
#         ticket_price = 0
#     elif (age >= 3) and (age <= 12):
#         ticket_price = 10
#     elif age > 12:
#         ticket_price = 15

#     print(f"Your ticket cost ${ticket_price}")

'''7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' 
value.'''

# Exiting loop using a conditional test
# pizza_topping = ''

# while pizza_topping != 'quit':
#     pizza_topping = input("Enter your desired pizza toppings: ")
#     print(f"Adding {pizza_topping} to your pizza.")

# Exiting loop using an active variable (flag)
# active = True
# pizza_topping = ''

# while active:
#     pizza_topping = input("Enter your desired pizza toppings: ")
#     if pizza_topping == 'quit':
#         active = False
#     else:
#         print(f"Adding {pizza_topping} to your pizza.")

# Exiting loop using a break statement
# pizza_topping = ''

# while pizza_topping != 'quit':
#     pizza_topping = input("Enter your desired pizza toppings: ")
#     if pizza_topping == 'quit':
#         break
#     else:
#         print(f"Adding {pizza_topping} to your pizza.")

'''7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, 
press CTRL-C or close the window displaying the output.)'''

# Warning: infinite loop!
# num = 0

# while True:
#     print(num)
#     num += 1

'''7-8. Deli: Make a list called sandwich_orders and fill it with the names of 
various sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order, such as
I made your tuna sandwich. As each sandwich is made, move it to the list of 
finished sandwiches. After all the sandwiches have been made, print a message 
listing each sandwich that was made.'''

# sandwich_orders = ['grilled cheese', 'french', 'egg', 'chicken', 'falafel']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
    
#     print(f"Making sandwich: {current_sandwich.title()}")
#     finished_sandwiches.append(current_sandwich)

# print("\nSandwiches ready to eat:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich.title()} sandwich")

'''7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.'''

# sandwich_orders = [
#     'grilled cheese', 'pastrami', 'french', 'pastrami', 'egg', 'chicken', 
#     'falafel', 'pastrami']
# finished_sandwiches = []

# print("Sorry, our deli run out of Pastrami sandwich.\n")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
    
#     print(f"Making sandwich: {current_sandwich.title()}")
#     finished_sandwiches.append(current_sandwich)

# print("\nSandwiches ready to eat:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich.title()} sandwich")

'''7-10. Dream Vacation: Write a program that polls users about their dream 
vacation. Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the 
poll.'''

# responses = {}
# polling_active = True

# while polling_active:
#     name = input("What is your name? ")
#     response = input(
#         "If you could visit one place in the world, where would you go? ")
    
#     responses[name] = response

#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to go to {response.title()}.")