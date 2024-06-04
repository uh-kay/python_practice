# 3-4

guests = ['Robert', 'Lea', 'Andre', 'Josh', 'Anne']

# print(f'{guests[0]}, you are invited to my dinner party!')
# print(f'{guests[1]}, you are invited to my dinner party!')
# print(f'{guests[2]}, you are invited to my dinner party!')
# print(f'{guests[3]}, you are invited to my dinner party!')
# print(f'{guests[4]}, you are invited to my dinner party!')

# 3-5

# print("Unfortunately, Lea and Josh can't make it to the dinner party.")
guests[1], guests[3] = 'Sarah', "John"

# print(f'{guests[0]}, you are invited to my dinner party!')
# print(f'{guests[1]}, you are invited to my dinner party!')
# print(f'{guests[2]}, you are invited to my dinner party!')
# print(f'{guests[3]}, you are invited to my dinner party!')
# print(f'{guests[4]}, you are invited to my dinner party!')

# 3-6

# print("Greetings everyone, I found a bigger table so we're inviting more"
#     "guests!")
guests.insert(0, 'Peter')
guests.insert(3, 'Lex')
guests.append('Noa')

# print(f'{guests[0]}, you are invited to my dinner party!')
# print(f'{guests[1]}, you are invited to my dinner party!')
# print(f'{guests[2]}, you are invited to my dinner party!')
# print(f'{guests[3]}, you are invited to my dinner party!')
# print(f'{guests[4]}, you are invited to my dinner party!')
# print(f'{guests[5]}, you are invited to my dinner party!')
# print(f'{guests[6]}, you are invited to my dinner party!')
# print(f'{guests[7]}, you are invited to my dinner party!')

# 3-7

print("Sorry everyone, it seems like the new dinner table won't arrive in" 
    "time, so I only have space for two guests.")
print(f"Sorry {guests.pop()}, I can't invite you to the dinner party")
print(f"Sorry {guests.pop()}, I can't invite you to the dinner party")
print(f"Sorry {guests.pop()}, I can't invite you to the dinner party")
print(f"Sorry {guests.pop()}, I can't invite you to the dinner party")
print(f"Sorry {guests.pop()}, I can't invite you to the dinner party")
print(f"Sorry {guests.pop()}, I can't invite you to the dinner party")
print(f'{guests[0]}, you are still invited to my dinner party!')
print(f'{guests[1]}, you are still invited to my dinner party!')
del guests[1]
del guests[0]
print(guests)

