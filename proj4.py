import os
os.system('cls')
print "###############################"
print "#                             #"
print "#  Elementy bioinformatyki    #"
print "#       projekt nr 4          #"
print "#                             #"
print "###############################"
u=[]
v=[]
macierz=[]
slownik=[]
slownik2=[]
x = 1
profil_U = []
profil_V = []
profil_UV = []
slowo_kons1 = []
slowo_kons2 = []

# POBIERANIE DANYCH Z PLIKU 1
x = 1
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
slownik.sort(reverse=1)
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
slownik2.sort(reverse=1)
# POBIERANIE DANYCH Z PLIKU Z MACIERZA PODOBIENSTWA
y=1
file3 = open('macierz.txt', 'rU').readlines()
for linia in file3:
	linia = linia[0:-1]
	tmp = []
	tmp = linia.split(' ')
	macierz.insert(x,tmp)
	y=y+1
print "\nMacierz podobienstwa liter:"
for row in range(len(macierz)):
	print str(slownik[row]) + str(macierz[row])
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
		profil_U[i][j] = profil_U[i][j] / len(u)
		
# OBLICZANIE MACIERZY PROFILU DLA DANYCH Z PLIKU 1
for kolumna in range(L):
	for rzad in range(len(v)):
		for x in range(len(slownik2)):
			if slownik2[x] == v[rzad][kolumna]:
				profil_V[x][kolumna] = profil_V[x][kolumna] + 1

for i in range(len(profil_V)):
	for j in range(len(profil_V[i])):
		profil_V[i][j] = profil_V[i][j] / len(v)

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
		
# WYPISYWANIE WYNIKOW (PROFIL I SLOWO KONSENSUSOWE)
print "\nDane z pliku 1:" + "				" + "Dane z pliku 2:"
for i in range(len(u)):
	print str(u[i]) + "		" + str(v[i])
	
print "\nProfil:" + "					" + "Profil:"
for i in range(len(slownik)):
	print slownik[i] + " " + str(profil_U[i]) + "		" + slownik2[i] + " " + str(profil_V[i])
	
print  "sk:" + str(slowo_kons1) + "		sk:" + str(slowo_kons2) + "\n\n"

#ZLACZENIE DWOCH PROFILI
u2 = u
v2 = v
for row in u2:
	row.insert(2, "-")
for row in v2:
	row.insert(3, "-")	
uv = u2
for row in v2:
	uv.append(row)
	LL = len(row)
# ZLACZONE DWA WIELODOPASOWANIA
print "Scalone dwa wielodopasowania"
for i in range(len(uv)):
	print str(uv[i])	
	
# # INICJALIZACJA MACIERZY PROFILU DLA ZLACZONYCH DWOCH PROFILI
# x=1
# for letter in slownik:
	# tmp = []
	# for i in range(LL):
		# tmp.append(0.)
	# profil_UV.insert(x,tmp)
	# x=x+1
	
# # OBLICZANIE MACIERZY PROFILU DLA ZLACZONYCH DWOCH PROFILI
# for kolumna in range(LL):
	# for rzad in range(len(uv)):
		# for x in range(len(slownik)):
			# if slownik[x] == uv[rzad][kolumna]:
				# profil_UV[x][kolumna] = profil_UV[x][kolumna] + 1
				
# for i in range(len(profil_UV)):
	# for j in range(len(profil_UV[i])):
		# profil_UV[i][j] = profil_UV[i][j] / len(uv)
		
# print "\nProfil:"
# for i in range(len(slownik)):
	# print slownik[i] + " " + str(profil_UV[i])
	
# ALIGNMENT SIMILARITY S(pi,qj)=EaEb( s(a,b)pi(a)qj(b) )

print "\nSrednie podobienstwo dla poszczegolnych kolumn dopasowania profil-profil:\n"
S=[]
for i in range(len(uv[0])):
	S.append(0.)
	for row in range(len(profil_U)):
		for wiersz in range(len(profil_V)):
			if slownik[row] == '-' and slownik[wiersz] == '-':
				S[i] = S[i]
			elif i == 2:
				S[i] = S[i] + float(macierz[row][-1])
			else:
				
				S[i] = S[i] + float(profil_U[row][i-1]) * float(profil_V[wiersz][i-1]) * float(macierz[row][wiersz])
for i in range(len(uv[0])):
	for row in range(len(profil_V)):
		for wiersz in range(len(profil_U)):
			if slownik[row] == '-' and slownik[wiersz] == '-':
				S[i] = S[i]
			elif i == 3:
				S[i] = S[i] + float(macierz[row][-1])
			else:
				S[i] = S[i] + float(profil_U[row][i-1]) * float(profil_V[wiersz][i-1]) * float(macierz[row][wiersz])
				#S[i] = S[i]
for i in range(len(S)):
	print str(i+1) + ": " + str(S[i])

	
########################################################
########################################################
# SKLADANIE WIELODOPASOWAN W JEDNO PRZEZ KLASTERYZACJE #
########################################################
########################################################
print "\n####################################################"
print "SKLADANIE WIELODOPASOWAN W JEDNO PRZEZ KLASTERYZACJE"
print "####################################################"
su=[]
sv=[]
x = 1
# POBIERANIE DANYCH Z PLIKU 1
file = open('u', 'rU').readlines()
for line in file:
	line = line[0:-1]	
	tmp = []		
	for letter in line:
		tmp.append(letter)
	su.insert(x,tmp)
	x=x+1
# POBIERANIE DANYCH Z PLIKU 2
x = 1
file2 = open('v', 'rU').readlines()
for line in file2:
	line = line[0:-1]
	tmp = []
	for letter in line:
		tmp.append(letter)
	sv.insert(x,tmp)
	x=x+1
idx = [0, 0]

# SZUKANIE SLOW O NAJWIEKSZYM PODOBIENSTWIE 
def szukanieslowomaxpodob(a,b, idx):
	opd = 0 #optymalne dopasowanie -> max podobienstwo dopasowania slow (szukamy maks)
	opdtmp = 0
	for slowou in range(len(a)):
		for slowov in range(len(b)):
			for kolumna in range(len(a[0])):
				idxu = slownik.index(a[slowou][kolumna])
				idxv = slownik.index(b[slowov][kolumna])
				opdtmp = opdtmp + int(macierz[idxu][idxv])
		if opdtmp > opd:
			opd = opdtmp
			idx[0] = slowou
			idx[1] = slowov
	return idx	
#DEFINICJA METRYKI D(a,b)
def metrykad(a,b):
	if a == b:
		return 0
	elif a == '-' or b == '-':
		return 2
	else:
		return 1
		
def dopasowanieslow(slowou, slowov):
	d = []
	print ""
	print slowou
	print slowov
	kosztdopasowania = 0
	for i in range(len(slowou)):
		kosztdopasowania = kosztdopasowania + metrykad(slowou[i],slowov[i])
	print "koszt dopasowania = " + str(kosztdopasowania)
	x=1
	for letter in range(len(slowou)+1):
		tmp = []
		for i in range(len(slowov)+1):
			tmp.append(0)
		d.insert(x,tmp)
		x=x+1
	#brzeg tabeli
	d[0][0] = 0
	for i in range(len(d)):
		for k in range(i):
			d[i][0] = d[i][0] + metrykad(slowou[k], '-')
	for j in range(len(d[0])):
		for k in range(j):
			d[0][j] = d[0][j] + metrykad(slowov[k], '-')
	#srodek tabeli
	for i in range(1,len(d)):
		for j in range(1,len(d[0])):
			a = d[i-1][j-1] + metrykad(slowou[i-1],slowov[j-1])
			b = d[i][j-1] + metrykad('-',slowov[j-1])
			c = d[i-1][j] + metrykad(slowou[i-1],'-')
			d[i][j] = min(a,b,c)	
	
	print "tabela D(i,j):"
	for row in d:
		print row
	i, j = len(d)-1, len(d[0])-1
	krok = 0
	sciezka = []
	wynik = []
	wynslowo1 = []
	wynslowo2 = []
	while(i > 0 or j > 0):
		if d[i][j] > d[i][j-1]:
			j = j - 1
			wynslowo1.append('-')
			wynslowo2.append(slowov[j])
		elif d[i][j] > d[i-1][j]:
			i = i - 1
			wynslowo1.append(slowou[i])
			wynslowo2.append('-')
		elif d[i][j] > d[i-1][j-1]:
			i = i-1
			j = j-1
			wynslowo1.append(slowou[i])
			wynslowo2.append(slowov[j])
		elif d[i][j] == d[i][j-1]:
			j = j - 1
			wynslowo1.append('-')
			wynslowo2.append(slowov[j])
		elif d[i][j] == d[i-1][j]:
			i = i - 1
			wynslowo1.append(slowou[i])
			wynslowo2.append('-')
		else:
			i = i-1
			j = j-1
			wynslowo1.append(slowou[i])
			wynslowo2.append(slowov[j])
		
		krok = krok + 1
		if i == 0 and j > 1:
			j = j-1 
			wynslowo1.append('-')
			wynslowo2.append(slowov[j])
			krok = krok + 1
		elif i > 1 and j == 0:
			i = i - 1
			wynslowo1.append(slowou[i])
			wynslowo2.append('-')
			krok = krok + 1
		else:
			krok = krok
		#print i, j
		
		#sciezka.append(str(i) + ',' + str(j))
	print "krok = "	+ str(krok)
	#sciezka.reverse()
	#print sciezka
	wynslowo1.reverse()
	wynslowo2.reverse() 
	wynik.append(wynslowo1)
	wynik.append(wynslowo2)
	return wynik
		
sul = len(su)
dopasowanie = []
wyn = []
print "\nDopasowywanie poszczegolnych klastrow:"
for i in range(sul):
	szukanieslowomaxpodob(su, sv, idx)
	wyn =  dopasowanieslow(su[idx[0]], sv[idx[1]])
	dopasowanie.append(wyn[0])
	dopasowanie.append(wyn[1])
	su.pop(idx[0])
	sv.pop(idx[1])

print "\nWynikowe zlaczenie podanych sekwencji w jedno wielodopasowanie przy pomocy klasteryzacji:\n"
for slowo in dopasowanie:	
	print slowo