# 4-1

pizzas = ['meat lover', 'cheese galore', 'pepperoni']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print(f"I like {pizzas[0]} pizza.")
print(f"I like {pizzas[1]} pizza.")
print(f"I like {pizzas[2]} pizza.")
print("I really love pizza!")

# 4-2

pets = ["dog", "cat", "hamster", "parrot"]
for animal in pets:
    print(f"A {animal} would make a great pet!")

print("Any of these animals would make a great pet!")

# 4-3

for number in range(1, 21):
    print(number)

# 4-4

numbers = list(range(1, 1000001))

for number in numbers:
    print(number)

# 4-5

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6

odd_numbers = list(range(1, 20, 2))

for num in odd_numbers:
    print(num)

# 4-7

threes = list(range(3, 31, 3))

for num in threes:
    print(num)

# 4-8

cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)

for num in cubes:
    print(num)

# 4-9

cubes = [value**3 for value in range(1, 11)]
for num in cubes:
    print(num)

# 4-10

print("The first three items in the list are:")
for num in cubes[:3]:
    print(num)

print("Three items from the middle of the list are:")
for num in cubes[4:7]:
    print(num)

print("The last three items in the list are:")
for num in cubes[7:]:
    print(num)

# 4-11

pizzas = ['meat lover', 'cheese galore', 'pepperoni']
friend_pizzas = pizzas[:]

pizzas.append('american favorite')
friend_pizzas.append('tuna melt')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

# 4-12

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's foods are:")
for food in friend_foods:
    print(f"- {food}")

# 4-13

menu = ('fried rice', 'burger', 'fried chicken', 'chicken soup', 'porridge')
print("Our menu:")
for food in menu:
    print(f"- {food}")

menu[0] = 'sushi'  # tuple can't be modified

menu = ('curry udon', 'burger', 'fried chicken', 'beef stew', 'porridge')
print("Our new menu:")
for food in menu:
    print(f"- {food}")
