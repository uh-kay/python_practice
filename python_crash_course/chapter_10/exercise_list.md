## 10-1. Learning Python
Open a blank file in your text editor and write a few lines summarizing what 
you’ve learned about Python so far. Start each line with the phrase In Python 
you can. . . . Save the file as learning_python.txt in the same directory as 
your exercises from this chapter. Write a program that reads the file and 
prints what you wrote two times: print the contents once by reading in the 
entire file, and once by storing the lines in a list and then looping over 
each line.

## 10-2. Learning C: 
You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:

message = "I really like dogs."

message.replace('dog', 'cat')

'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.

## 10-3. Simpler Code: 
The program file_reader.py in this section uses a temporary
variable, lines, to show how splitlines() works. You can skip the temporary
variable and loop directly over the list that splitlines() returns:
for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section,
to make them more concise.

## 10-4. Guest: 
Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.

## 10-5. Guest Book: 
Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.

## 10-6. Addition: 
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text 
instead of a number.

## 10-7. Addition Calculator: 
Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.

## 10-8. Cats and Dogs: 
Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. 
Write a program that tries to read these files and print the contents of the 
file to the screen. Wrap your code in a try-except block to catch the 
FileNotFound error, and print a friendly message if a file is missing. Move 
one of the files to a different location on your system, and make sure the 
code in the except block executes properly.

## 10-9. Silent Cats and Dogs: 
Modify your except block in Exercise 10-7 to fail silently if either file is 
missing.

## 10-10. Common Words: 
Visit Project Gutenberg (https://gutenberg.org ) and find
a few texts you’d like to analyze. Download the text files for these works, or
copy the raw text from your browser into a text file on your computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:

line = "Row, row, row your boat"
line.count('row')
2
line.lower().count('row')
3

Notice that converting the string to lowercase using lower() catches all
appearances of the word you’re looking for, regardless of how it’s formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.

## 10-11. Favorite Number: 
Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message “I know your favorite
number! It’s _____.”