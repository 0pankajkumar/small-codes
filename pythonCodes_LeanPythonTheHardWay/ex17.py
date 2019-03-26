from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

indata = open(from_file).read()

print " The input file is %d bytes long" % len(indata)

print "does the output file exists? %r" % exists(to_file)
print "Ready, hit enter to continue, ctrl+c to abort"
raw_input()

out_file = open("to_file",'w')
out_file.write(indata)

print "Alright , all done."