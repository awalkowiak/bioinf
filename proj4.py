u=[]
v=[]
slownik=[]
slownik2=[]
x = 1
profil_U = []
profil_V = []
slowo_kons1 = []
slowo_kons2 = []

# POBIERANIE DANYCH Z PLIKU 1
file = open('u', 'rU').readlines()
for line in file:
	line = line[0:-1]	
	tmp = []		
	for letter in line:
		tmp.append(letter)
		if letter not in slownik:
			slownik.append(letter)
	u.insert(x,tmp)
	x=x+1

# POBIERANIE DANYCH Z PLIKU 2
x = 1
file2 = open('v', 'rU').readlines()
for line in file2:
	line = line[0:-1]
	tmp = []
	for letter in line:
		tmp.append(letter)
		if letter not in slownik2:
			slownik2.append(letter)
	v.insert(x,tmp)
	x=x+1

L = len(line)

# INICJALIZACJA MACIERZY PROFILU DLA DANYCH Z PLIKU 1
x=1
for letter in slownik:
	tmp = []
	for i in range(L):
		tmp.append(0.)
	profil_U.insert(x,tmp)
	x=x+1
# INICJALIZACJA MACIERZY PROFILU DLA DANYCH Z PLIKU 1
x=1
for letter in slownik2:
	tmp = []
	for i in range(L):
		tmp.append(0.)
	profil_V.insert(x,tmp)
	x=x+1

# INICJALIZACJA SLOW KONSENSUSOWEGO DLA DANYCH Z PLIKOW 1 I 2
for i in range(L):
	slowo_kons1.append("")
	slowo_kons2.append("")

# OBLICZANIE MACIERZY PROFILU DLA DANYCH Z PLIKU 1
for kolumna in range(L):
	for rzad in range(len(u)):
		for x in range(len(slownik)):
			if slownik[x] == u[rzad][kolumna]:
				profil_U[x][kolumna] = profil_U[x][kolumna] + 1
				
for i in range(len(profil_U)):
	for j in range(len(profil_U[i])):
		profil_U[i][j] = profil_U[i][j] / len(slownik)
		
# OBLICZANIE MACIERZY PROFILU DLA DANYCH Z PLIKU 1
for kolumna in range(L):
	for rzad in range(len(v)):
		for x in range(len(slownik2)):
			if slownik2[x] == v[rzad][kolumna]:
				profil_V[x][kolumna] = profil_V[x][kolumna] + 1

for i in range(len(profil_V)):
	for j in range(len(profil_V[i])):
		profil_V[i][j] = profil_V[i][j] / len(slownik2)

# OBLICZANIE SLOWA KONSENSUSOWEGO DLA DANYCH Z PLIKU 1
for kolumna in range(L):
	temp1 = 0
	temp2 = 0
	for rzad in range(len(slownik)):
		temp1 = profil_U[rzad][kolumna]
		if temp1 >= temp2:
			slowo_kons1.pop(kolumna)
			slowo_kons1.insert(kolumna, slownik[rzad])
			temp2 = temp1
			
# OBLICZANIE SLOWA KONSENSUSOWEGO DLA DANYCH Z PLIKU 2
for kolumna in range(L):
	temp1 = 0
	temp2 = 0
	for rzad in range(len(slownik2)):
		temp1 = profil_V[rzad][kolumna]
		if temp1 >= temp2:
			slowo_kons2.pop(kolumna)
			slowo_kons2.insert(kolumna, slownik2[rzad])
			temp2 = temp1
		
# WYPISYWANIE WYNIKOW
print "Dane z pliku 1:" + "				" + "Dane z pliku 2:"
for i in range(len(u)):
	print str(u[i]) + "		" + str(v[i])
	
print "\nProfil:" + "				" + "Profil:"
for i in range(len(slownik)):
	print slownik[i] + " " + str(profil_U[i]) + "		" + slownik2[i] + " " + str(profil_V[i])
	
print  "sk:" + str(slowo_kons1) + "		sk:" + str(slowo_kons2) 