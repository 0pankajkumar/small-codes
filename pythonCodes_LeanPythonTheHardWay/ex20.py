#importing argv
from sys import argv

script , input_file = argv

#Prints all the file contents
def print_all(f):
    print f.read()
	
#prints 0th position of file but in my case prints nothing
def rewind(f):
    f.seek(0)

#Prints based upon whatever line number is passed
def print_a_line(line_count, f):
    print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

rewind(current_file)

print "Lets print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)