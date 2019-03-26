def print_two(*args):
    arg1, arg2 = arg
	print "arg1: %r , arg2: %r " % (arg1, arg2)
	
def print_two_again(arg1, arg2):
    print "arg1: %r  arg2: %r " % (arg1, arg2)
	
def print_none():
    print "I got nothing"
	
print_two("Pan","Kum")
print_two_again("Zed","Shaw")
print_none()