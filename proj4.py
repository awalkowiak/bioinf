u=[]
v=[]
slownik=[]
slownik2=[]
file = open('u', 'rU').readlines()
print file
for line in file:
	line = line[0:-1]	
	u.append(line)	
	for letter in line:
		if letter not in slownik:
			slownik.append(letter)
file2 = open('v', 'rU').readlines()
print file2
for line in file2:
	line = line[0:-1]	
	v.append(line)	
	for letter in line:
		if letter not in slownik2:
			slownik2.append(letter)

L = len(line)

profil_U = {}
profil_V = {}

for i in range(len(slownik)):
	for j in range(L):
		profil_U[slownik[i]] = 