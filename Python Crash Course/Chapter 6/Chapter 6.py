'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary.'''

# friend = {
#     "first_name": "Steven",
#     "last_name": "Wibowo",
#     "age": 18,
#     "city": "Bogor"
# }

# print(friend["first_name"])
# print(friend["last_name"])
# print(friend["age"])
# print(friend["city"])

'''6-2. Favorite Numbers: Use a dictionary to store people's favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a 
favorite number for each person, and store each as a value in your dictionary. 
Print each person's name and their favorite number. For even more fun, poll a 
few friends and get some actual data for your program.'''

# fav_numbers = {
#     "charles": 69,
#     "kevin": 8,
#     "nanda": 69,
#     "steven": 95,
#     "oscar": 7
# }

# print(f"Charles' favorite number is: {fav_numbers["charles"]}")
# print(f"Kevin' favorite number is: {fav_numbers["kevin"]}")
# print(f"Nanda' favorite number is: {fav_numbers["nanda"]}")
# print(f"Steven' favorite number is: {fav_numbers["steven"]}")
# print(f"Oscar' favorite number is: {fav_numbers["oscar"]}")

'''6-3. Glossary: A Python dictionary can be used to model an actual 
dictionary. However, to avoid confusion, let's call it a glossary.
• Think of five programming words you've learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.'''

# programming_terms = {
#     'print': 'outputs a string on the screen',
#     'variable': 'named storage location that holds data',
#     'list': 'a collection of data',
#     'import': 'function used to call external library',
#     'tuple': 'an immutable collection of data'
# }

# print(f"print: \n\t{programming_terms['print']}")
# print(f"variable: \n\t{programming_terms['variable']}")
# print(f"list: \n\t{programming_terms['list']}")
# print(f"import: \n\t{programming_terms['import']}")
# print(f"tuple: \n\t{programming_terms['tuple']}")

'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary's keys and values. When
you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.'''

# programming_terms = {
#     'print': 'outputs a string on the screen',
#     'variable': 'named storage location that holds data',
#     'list': 'a collection of data',
#     'import': 'function used to call external library',
#     'tuple': 'an immutable collection of data',
#     'range': 'function used to create a range of number',
#     'for': 'a loop that runs finite times according to the specified term',
#     'key': "a variable that's associated to a value",
#     'value': 'the data inside the key',
#     'dictionary': 'a collection of key-value pairs'
# }

# for word, meaning in programming_terms.items():
#     print(f"{word}: \n\t{meaning}")

'''6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.'''

# rivers = {
#     'egypt': 'nile',
#     'united states': 'mississippi',
#     'brazil': 'amazon'
# }

# for country, river in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}")

# for country in rivers.keys():
#     print(country.title())

# for river in rivers.values():
#     print(river.title())

'''6-6. Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.'''

required_respondents = []

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    required_respondents.append(name)

required_respondents.append('alice')
required_respondents.append('bob')

for name in required_respondents:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for participating in the poll.")
    else:
        print(f"{name.title()}, please participate in the poll.")

# Todo
# 6-7 - 6-12
