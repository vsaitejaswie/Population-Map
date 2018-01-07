"""print("enter no of tuples for A")
a = input()
a = int(a)

print("enter no of tuples for B")
b = input()
b = int(b)"""

print("------------------------------")
A = [(171, 130, 14), (171, 130, 14), (170, 131, 14), (170, 131, 14), (170, 131, 14), (169, 130, 13), (169, 130, 13), (170, 131, 14), (170, 131, 14), (170, 131, 14), (168, 129, 12)]
B = [(58, 97, 16), (57, 96, 17), (57, 96, 17), (59, 98, 19), (59, 96, 19), (65, 101, 27), (59, 95, 21), (59, 95, 21), (62, 98, 26), (57, 93, 21), (56, 92, 22), (58, 94, 24)]
a = len(A)
b = len(B)

#comment this if you give values directly
"""def enterv(rng,arr) :
	for i in range(rng):
		print("Enter R : ")
		r = input()
		r = int(r)
		print("Enter G : ")
		g = input()
		g = int(g)
		print("Enter B : ")
		b = input()
		b = int(b)
		arr.append((r,g,b))

print("fill tuples in A")
enterv(a,A)
print("fill tuples in B")
enterv(b,B)"""
#till here

def cmp(x,y):
	for i in range(3) :
		if x[i]==y[i]:
			flag = 0
		else:
			flag = 1
			break
	if flag == 0:
		return 0
	else:
		return 1

def compp():
	for i in range(a):
		c = cmp(A[i],B[i])
		if c == 0:
			flag = 0
			continue
		else:
			flag = 1
			break
			"""for j in range(3):
				if A[i][j] != B[i][j]:
					print("check at " + str(j+1) + " in tuple " + str(i+1))"""
	if flag == 0:
		print("Match")
	else:
		print("Not a match")

if a!=b:
	print("Not a match")
	exit()
else:
	compp()