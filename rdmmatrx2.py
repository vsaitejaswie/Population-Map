import math

print ("enter no of rows")
n = input()
n = int(n)

print ("enter no of columns")
m = input()
m = int(m)

print ("enter your range")
l = input()
l = int(l)

arr = []

for i in range(n):
	arr.append([])
	for j in range(m):
		arr[i].append(math.pow(9,j+1)%(((i+1)+(j+1)))*(5*(7+i+j)))
		
print(arr)

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
	print("----------------")
	print(arr[r][c])
	print("----------------")