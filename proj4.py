u=[]
v=[]
file = open('u', 'rU').readlines()
print file
for line in file:
	line = line[0:-1]	
	u.append(line)	
file2 = open('v', 'rU').readlines()
print file2
for line in file2:
	line = line[0:-1]	
	v.append(line)	
	
L = len(line)
print len(v)
profil_U = {}
profil_V = {}

for i in range len(u):
	for j in range (L):
		profil_U[i,j] = 