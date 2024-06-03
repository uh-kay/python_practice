'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.'''

# for number in range(1, 21):
#     print(number)

'''4-4. One Million: Make a list of the numbers from one to one million, and 
then use a for loop to print the numbers. (If the output is taking too long, 
stop it by pressing CTRL-C or by closing the output window.)'''

numbers = list(range(1, 1000001))

# for number in numbers:
#     print(number)

'''4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python 
can add a million numbers.'''

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

'''4-6. Odd Numbers: Use the third argument of the range() function to make a 
list of the odd numbers from 1 to 20. Use a for loop to print each number.'''

odd_numbers = list(range(1, 20, 2))

# for num in odd_numbers:
#     print(num)

'''4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop
to print the numbers in your list.'''

threes = list(range(3, 31, 3))

# for num in threes:
#     print(num)

'''4-8. Cubes: A number raised to the third power is called a cube. For 
example, the cube of 2 is written as 2**3 in Python. Make a list of the first 
10 cubes (that is, the cube of each integer from 1 through 10), and use a for 
loop to print out the value of each cube.'''

# cubes = []
# for num in range(1, 11):
#     cubes.append(num ** 3)

# for num in cubes:
#     print(num)

'''4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.'''

cubes = [value**3 for value in range(1, 11)]
# for num in cubes:
#     print(num)

'''4-10. Slices: Using one of the programs you wrote in this chapter, add
several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program's list.
• Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list.
'''

# print("The first three items in the list are:")
# for num in cubes[:3]:
#     print(num)

# print("Three items from the middle of the list are:")
# for num in cubes[4:7]:
#     print(num)

# print("The last three items in the list are:")
# for num in cubes[7:]:
#     print(num)

'''4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think 
of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.'''

menu = ('fried rice', 'burger', 'fried chicken', 'pizza', 'lasagna')
print("Our menu:")
for food in menu:
    print(f"- {food}")

# foods[0] = 'sushi' #tuple can't be modified

menu = ('curry udon', 'burger', 'fried chicken', 'french fries', 'lasagna')
print("Our new menu:")
for food in menu:
    print(f"- {food}")