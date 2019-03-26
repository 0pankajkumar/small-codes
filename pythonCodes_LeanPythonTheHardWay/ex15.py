from sys import argv

scriptwa, file_name = argv 

txt = open(file_name)

print "Here is your file %r" % file_name
print txt.read()

print "\n\n\n Type your file name again"
fileAgain = raw_input('>')

txtAgain = open(fileAgain)

print "Here's your file AGAIN %r" % fileAgain
print txtAgain.read()