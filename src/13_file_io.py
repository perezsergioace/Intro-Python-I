"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# f = open('./foo.txt', 'r')
# print(f.read())
# f.close()

with open('foo.txt') as file:
    print(file.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# f = open("bar.txt", "a")
# f.write('First Line \nSecond Line\nThird Line')
# f.close()

# with open('bar.txt') as new_file:
#     print(new_file.read())

random_text = """
First Line
Second Line
Third Line
"""

with open('bar.txt', 'w') as new_file:
    new_file.write(random_text)

with open('bar.txt') as new_file:
    print(new_file.read())
