import time 

while True:
    for i in ["/","-","|","\\","|"]:
	    time.sleep(0.05)
	    print "%s\r" % i,