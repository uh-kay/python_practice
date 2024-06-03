# 10-1
from pathlib import Path


path = Path('learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()


# print(contents)

# line_list = []
# for line in lines:
#     line_list.append(line)

# for line in line_list:
#     print(line)

# 10-2

line_list = []
for line in lines:
    line = line.replace('Python', 'Rust')
    line_list.append(line)

for line in line_list:
    print(line)