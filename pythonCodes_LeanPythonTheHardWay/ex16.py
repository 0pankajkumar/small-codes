from sys import argv

script, fileName = argv
print "We have this file to work upon %r" % fileName

target = open(fileName, "r")
print "The contents of the file are \n\n"
print target.read()
target.close()

print "Is the file too long?"
raw_input(" > ")

print "OK, We'll truncate it"

target = open(fileName, "w")
target.truncate()
target.close()
print "File has been flushed. \n File contents now are:"
target = open(fileName)
target.read()
target.close()
print "\n\n"

print "Write your lines now:"
target = open(fileName, "w")
target.write(raw_input())
target.close()
print "Bye"

