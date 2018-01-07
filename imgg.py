A = [(171, 130, 14), (171, 130, 14), (170, 131, 14), (170, 131, 14), (170, 131, 14), (169, 130, 13), (169, 130, 13), (170, 131, 14), (170, 131, 14), (170, 131, 14), (168, 129, 12)]
B = [(58, 97, 16), (57, 96, 17), (57, 96, 17), (59, 98, 19), (59, 96, 19), (65, 101, 27), (59, 95, 21), (59, 95, 21), (62, 98, 26), (57, 93, 21), (56, 92, 22), (58, 94, 24)]
a = len(A)
b = len(B)

def flag1(flag):
	if flag == 0:
		return 0
	else:
		return 1

def flag2(flag):
	if flag == 0:
		print("Match")
	else:
		print("Not a match")

def cmp(x,y):
	for i in range(3) :
		if x[i]==y[i]:
			flag = 0
		else:
			flag = 1
			break
	flag1(flag)

def compp():
	for i in range(min(a,b)):
		c = cmp(A[i],B[i])
		if c == 0:
			flag = 0
			continue
		else:
			flag = 1
			break
	flag2(flag)

if a!=b:
	print("A and B will be compared till  " + str(min(a,b)))
	compp()
else:
	compp()