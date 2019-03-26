from sys import argv

script, user_input, surname = argv
prompt = '>> '
print "Hi %s %s, I am the %s script" % (user_input, surname, script)
print "I would like to ask."
print "Do you like %s %s?" % (user_input, surname)
likes = raw_input(prompt)

print "Where do you live %s?" % user_input
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
So you like %s who 
lives in %s
& has %s type of computer
''' % (likes, lives, computer )