''' 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.” '''

print('Albert Einstein once said, "A person who never made a mistake never ' 
'tried anything new."')

'''2-8. File Extensions: Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do. '''

filename = 'python_notes.txt'
filename_without_extension = filename.removesuffix('.txt')
print(filename_without_extension)

import this