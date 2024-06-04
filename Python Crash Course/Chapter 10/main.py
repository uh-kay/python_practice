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