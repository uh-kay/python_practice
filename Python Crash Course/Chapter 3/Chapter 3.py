'''
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''

guests = ['Robert', 'Lea', 'Andre', 'Josh', 'Anne']

# print(f'{guests[0]}, you are invited to my dinner party!')
# print(f'{guests[1]}, you are invited to my dinner party!')
# print(f'{guests[2]}, you are invited to my dinner party!')
# print(f'{guests[3]}, you are invited to my dinner party!')
# print(f'{guests[4]}, you are invited to my dinner party!')

'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
'''

# print("Unfortunately, Lea and Josh can't make it to the dinner party.")
guests[1], guests[3] = 'Sarah', "John"

# print(f'{guests[0]}, you are invited to my dinner party!')
# print(f'{guests[1]}, you are invited to my dinner party!')
# print(f'{guests[2]}, you are invited to my dinner party!')
# print(f'{guests[3]}, you are invited to my dinner party!')
# print(f'{guests[4]}, you are invited to my dinner party!')

'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

# print("Greetings everyone, I found a bigger table so we're inviting more guests!")
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

'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
'''

print("Sorry everyone, it seems like the new dinner table won't arrive in time, so I only have space for two guests.")
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

