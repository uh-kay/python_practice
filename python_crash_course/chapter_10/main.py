# 10-1
from pathlib import Path
import json

# path = Path('Python Crash Course/Chapter 10/learning_python.txt')
# contents = path.read_text()
# lines = contents.splitlines()

# print(contents)

# line_list = []
# for line in lines:
#     line_list.append(line)

# for line in line_list:
#     print(line)

# 10-2

# line_list = []
# for line in lines:
#     line = line.replace('Python', 'Rust')
#     line_list.append(line)

# for line in line_list:
#     print(line)

# 10-3

# path = Path('Python Crash Course/Chapter 10/pi_digits.txt')

# contents = path.read_text()

# for line in contents.splitlines():
#     print(line)

# path = Path('Python Crash Course/Chapter 10/pi_digits.txt')
# contents = path.read_text()
# pi_string = ''

# for line in contents.splitlines():
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

# path = Path('Python Crash Course/Chapter 10/pi_million_digits.txt')
# contents = path.read_text()

# pi_string = ''

# for line in contents.splitlines():
#     pi_string += line.lstrip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# birthday = input("Enter your birthday, in the form ddmmyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# 10-4

# name = input("Please enter your name: ")
# path = Path('Python Crash Course/Chapter 10/guest.txt')
# path.write_text(f"Guest name: {name}")

# 10-5

# path = Path('Python Crash Course/Chapter 10/guest_book.txt')
# guest_list = 'Guest name: \n'
# prompt = "Please enter your name"
# prompt += "\n(type 'quit' to quit): "
# count = 1

# while True:
#     name = input(prompt)
#     if name == 'quit':
#         break
#     guest_list += f"{count}. {name}\n"
#     count += 1

# path.write_text(guest_list)

# 10-6

# try:
#     first_number = input("Please enter the first number: ")
#     first_number = int(first_number)

#     second_number = input("Now enter the second number: ")
#     second_number = int(second_number)
# except ValueError:
#     print("Please enter only number.")
# else:
#     answer = first_number + second_number
#     print(f"The sum of {first_number} and {second_number} is: {answer}.\n")

# 10-7

# while True:
#     try:
#         first_number = input("Please enter the first number: ")
#         first_number = int(first_number)

#         second_number = input("Now enter the second number: ")
#         second_number = int(second_number)
#     except ValueError:
#         print("Please enter only number.")
#         continue
#     else:
#         answer = first_number + second_number
#         print(f"The sum of {first_number} and {second_number}"
#         f"is: {answer}.\n")
#         break

# 10-8

# try:
#     dogs_path = Path('Python Crash Course/Chapter 10/dogs.txt')
#     cats_path = Path('Python Crash Course/Chapter 10/cats.txt')

#     print(dogs_path.read_text())
#     print(cats_path.read_text())
# except FileNotFoundError:
#     print(f"Sorry, {cats_path} is missing.")

# 10-9

# try:
#     dogs_path = Path('Python Crash Course/Chapter 10/dogs.txt')
#     cats_path = Path('Python Crash Course/Chapter 10/cats.txt')

#     print(dogs_path.read_text())
#     print(cats_path.read_text())
# except FileNotFoundError:
#     pass

# 10-10

# try:
#     path = Path('Python Crash Course/Chapter 10/oliver twist.txt')
#     contents = path.read_text(encoding='utf-8')
#     word_count = 0

#     for line in contents.splitlines():
#         word_count += line.lower().count('the ')

#     print(word_count)
# except FileNotFoundError:
#     pass

# 10-11

path = Path('Python Crash Course/Chapter 10/favorite_number.json')

fav_num = input("Enter your favorite number: ")

# Write user's favorite number into favorite_number.json
contents = json.dumps(fav_num)
path.write_text(contents)

# Print favorite_number.json
contents = path.read_text()
fav_num = json.loads(contents)
print(f"I know your favorite number! It's {fav_num}.")
