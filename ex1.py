


print "HI,I'm Bablu. Let's learn a lot together"

try:
	a=int(raw_input())
except:
	print "Asshole atleast enter an integer"
	a=-1
print a
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate=float(raw_input("Enter Rate:"))
if h<=40:
    print h*rate
if h>40:
    newrate=rate*1.5
    print h*newrate