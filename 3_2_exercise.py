try:
	inp = raw_input("enter hours: " )
	hours = float(inp)
	inp = raw_input("enter rate: ")
	rate = float(inp)
except:
	print "error"
	quit()

if hours <= 40:
	pay = rate*hours
else:
	pay = rate*40 + (rate * 1.5 * (hours-40))
print pay

def sleep():
    time = 2035
    print(time)