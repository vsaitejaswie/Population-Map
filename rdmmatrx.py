import numpy as np 

print ("enter no of rows")
n = input()
n = int(n)

print ("enter no of columns")
m = input()
m = int(m)

print ("enter your range")
l = input()
l = int(l)

arr = np.random.randint(l, size = (m,n))

print("----------------")
print("----------------")

while 1:
	print("enter row no")
	r = input()
	r = int(r)
	if r>n:
		print("invalid entry")
		continue

	print("enter col no")
	c = input()
	c = int(c)
	if c>m:
		print("invalid entry")
		continue

	print(arr[r,c])
	print("----------------")