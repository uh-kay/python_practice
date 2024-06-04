'''5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)'''

# # Success version
# alien_color = 'green'
# if alien_color == 'green':
#     print("You earned 5 points!")

# Failed version
# alien_color = 'red'
# if alien_color == 'green':
#     print("You earned 5 points!")

'''5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
and write an if-else chain.
• If the alien's color is green, print a statement that the player just earned 5
points for shooting the alien.
• If the alien's color isn't green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.'''

# alien_color = 'red'
# if alien_color == 'green':
#     print("You earned 5 points!")
# else:
#     print("You earned 10 points!")

# alien_color = 'green'
# if alien_color == 'green':
#     print("You earned 5 points!")
# else:
#     print("You earned 10 points!")

'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.'''

# alien_color = 'green'
# if alien_color == 'green':
#     print("You earned 5 points!")
# elif alien_color == 'yellow':
#     print("You earned 10 points!")
# else:
#     print("You earned 15 points!")

# alien_color = 'yellow'
# if alien_color == 'green':
#     print("You earned 5 points!")
# elif alien_color == 'yellow':
#     print("You earned 10 points!")
# else:
#     print("You earned 15 points!")

# alien_color = 'red'
# if alien_color == 'green':
#     print("You earned 5 points!")
# elif alien_color == 'yellow':
#     print("You earned 10 points!")
# else:
#     print("You earned 15 points!")

'''5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage
of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that the
person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.'''

# age = 25
# if age < 2:
#     print("You're a baby")
# elif (age >= 2) and (age < 4):
#     print("You are a toddler")
# elif (age >= 4) and (age < 13):
#     print("You are a kid")
# elif (age >= 13) and (age < 20):
#     print("YOu are a teenager")
# elif (age >= 20) and (age < 65):
#     print("You are an adult")
# else:
#     print("You are an elder")

'''5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.'''

# usernames = ['rio', 'adam', 'jane', 'linda', 'admin']

# for name in usernames:
#     if name == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {name}, thank you for logging in again.")

'''5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct mes-
sage is printed.'''

# usernames = ['rio', 'adam', 'jane', 'linda', 'admin']
usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")
