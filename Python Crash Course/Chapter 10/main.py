# 10-1
from pathlib import Path


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

try:
    first_number = input("Please enter the first number: ")
    first_number = int(first_number)

    second_number = input("Now enter the second number: ")
    second_number = int(second_number)
except ValueError:
    print("Please enter only number.")
else:
    answer = first_number + second_number
    print(f"The sum of {first_number} and {second_number} is: {answer}.\n")