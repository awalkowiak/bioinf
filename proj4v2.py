import os
os.system('cls')
print "###############################"
print "#                             #"
print "#  Elementy bioinformatyki    #"
print "#       projekt nr 4          #"
print "#                             #"
print "###############################"

def pobieranie_danych(plik):
	x = 1
	dane = []
	tmp = []
	file = open(plik, 'rU').readlines()
	for line in file:
		line = line[0:-1]	
		tmp = []		
		for letter in line:
			tmp.append(letter)
		dane.insert(x,tmp)
		x=x+1
	return dane
def pobieranie_macierzy(plik):
	macierz = []
	y=1
	file = open(plik, 'rU').readlines()
	for linia in file:
		linia = linia[0:-1]
		tmp = []
		tmp = linia.split(' ')
		macierz.insert(y,tmp)
		y=y+1
	return macierz
	
def okreslanie_slownika(dopasowanie):
	slownik = []
	for word in dopasowanie:
		for letter in word:
			if letter not in slownik:
				 slownik.append(letter)
	slownik.sort(reverse=1)
	return slownik
	
def obliczanie_profilu(dopasowanie, slownik):
	#inicjalizacja
	x=1
	profil = []
	L = len(dopasowanie[0])
	for letter in slownik:
		tmp = []
		for i in range(L):
			tmp.append(0.)
		profil.insert(x,tmp)
		x=x+1
	#obliczanie
	for kolumna in range(L):
		for rzad in range(len(dopasowanie)):
			for x in range(len(slownik)):
				if slownik[x] == dopasowanie[rzad][kolumna]:
					profil[x][kolumna] = profil[x][kolumna] + 1
				
	for i in range(len(profil)):
		for j in range(len(profil[i])):
			profil[i][j] = profil[i][j] / len(dopasowanie)
			profil[i][j] = round(profil[i][j], 3)
	return profil
	
def slowo_konsensusowe(slownik, profil):
	#inicjalizacja
	slowo_kons = []
	L = len(profil[0])
	for i in range(L):
		slowo_kons.append("")
	#obliczanie
	for kolumna in range(L):
		temp1 = 0
		temp2 = 0
		for rzad in range(len(slownik)):
			temp1 = profil[rzad][kolumna]
			if temp1 >= temp2:
				slowo_kons.pop(kolumna)
				slowo_kons.insert(kolumna, slownik[rzad])
				temp2 = temp1
	return slowo_kons

def srednie_podobienstwo_kolumn_profili(profil1, profil2, macierz, slownik):
	sr_pod = []
	for i in range(len(profil1[0])):
		tmp = []
		for j in range(len(profil2[0])):
			tmp.append(0.)
		sr_pod.append(tmp)
	for i in range(len(profil1[0])):
		for j in range(len(profil2[0])):
			for row1 in range(len(profil1)):
				for row2 in range(len(profil2)):
					if slownik[row1] == '-' and slownik[row2] == '-':
						sr_pod[i][j] = sr_pod[i][j]
					else:
						sr_pod[i][j] = sr_pod[i][j] + float(macierz[row1][row2]) * profil1[row1][i] * profil2[row2][j]
			sr_pod[i][j] = round(sr_pod[i][j], 3)
	return sr_pod

def maks_podobienstwo_dopasowania_przedrostkow(sr_pod, dopasowanie1, dopasowanie2):
	S = []
	x=1
	# if len(dopasowanie1[0]) == 1:
		# ilosckolumna = len(dopasowanie1)
	# else:
		# ilosckolumna = len(dopasowanie1[0])
	# if len(dopasowanie2[0]) == 1:
		# ilosckolumnb = len(dopasowanie2)
	# else:
		# ilosckolumnb = len(dopasowanie2[0])
	for letter in range(len(dopasowanie1[0])+1):
		tmp = []
		for i in range(len(dopasowanie2[0])+1):
			tmp.append(0)
		S.insert(x,tmp)
		x=x+1
	#brzeg tabeli
	S[0][0] = 0
	for i in range(len(S)):
		for k in range(i):
			S[i][0] = S[i][0] - 2 # S(i,0) = Sumak=1...i(srpod(kolumna, '-')), z zalozenia s(x,'-') < 0
	for j in range(len(S[0])):
		for k in range(j):
			S[0][j] = S[0][j] - 2 # S(0,j) = Sumak=1...j(srpod('-', kolumna)), z zalozenia s('-',x) < 0
	#srodek tabeli
	for i in range(1,len(S)):
		for j in range(1,len(S[0])):
			a = S[i-1][j-1] + sr_pod[i-1][j-1]
			b = S[i][j-1] - 2
			c = S[i-1][j] - 2
			S[i][j] = max(a,b,c)	
			S[i][j] = round(S[i][j], 3)
	return S
	
def dopasowanie_profil_profil(S, dopasowanie1, dopasowanie2):
	dopasowanie = []
	i = len(S)-1
	j = len(S[0])-1
	#print i, j
	while i > 0 and j > 0:
		kolumna = []	
		if S[i-1][j-1] >= S[i][j-1] and S[i-1][j-1] >= S[i-1][j]:
			i -= 1
			j -= 1
			for row in range(len(dopasowanie1)):
				literka = dopasowanie1[row][i]
				kolumna.append(literka)
			for row in range(len(dopasowanie2)):
				literka = dopasowanie2[row][j]
				kolumna.append(literka)
		elif S[i][j-1] >= S[i-1][j-1] and S[i][j-1] >= S[i-1][j]:
			j -= 1
			for row in range(len(dopasowanie1)):
				literka = '-'
				kolumna.append(literka)
			for row in range(len(dopasowanie2)):
				literka = dopasowanie2[row][j]
				kolumna.append(literka)
		else:	
			i -= 1
			for row in range(len(dopasowanie1)):
				literka = dopasowanie1[row][i]
				kolumna.append(literka)
			for row in range(len(dopasowanie2)):
				literka = '-'
				kolumna.append(literka)
		#print i, j
		dopasowanie.append(kolumna)
	dopasowanie.reverse()
	dopasowaniewynik = []
	for kolumna in range(len(dopasowanie[0])):
		tmp = []
		for wiersz in range(len(dopasowanie)):
			tmp.append(dopasowanie[wiersz][kolumna])
		dopasowaniewynik.append(tmp)
	
	return dopasowaniewynik
	
dane1 = pobieranie_danych('u')
macierz_podobienstwa = pobieranie_macierzy('macierz.txt')
slownik1 = okreslanie_slownika(dane1)
profil1 = obliczanie_profilu(dane1, slownik1)
sk1 = slowo_konsensusowe(slownik1, profil1)
print "Wielodopasowanie z pliku 1:"
for i in dane1:
	print i
print "\nMacierz podobienstwa liter:"
for i in macierz_podobienstwa:
	print i
#print slownik1
print "\nProfil wielodopasowania dla danych z pliku 1:"
for i in profil1:
	print i
print "Slowo konsensusowe: " + str(sk1)

print "\n"
dane2 = pobieranie_danych('v')
profil2 = obliczanie_profilu(dane2, slownik1)
srpod = srednie_podobienstwo_kolumn_profili(profil1, profil2, macierz_podobienstwa, slownik1)
print "\nWielodopasowanie z pliku 2:"
for i in dane2:
	print i
print "\nProfil wielodopasowania dla danych z pliku 2:"
for i in profil2:
	print i
print "\nSrednie podobienstwo kolumn profili wielodopasowan z pliku 1 i 2"
for i in srpod:
	print i
	
maks_pod_dop_przedr = maks_podobienstwo_dopasowania_przedrostkow(srpod, dane1, dane2)
print "\nMaksymalne podobienstwo dopasowania przedrostkow:"
for i in maks_pod_dop_przedr:
	print i
	
print "\nWynikowe wielodopasowanie na podstawie zlaczania profili"
for i in dane1:
	print i
print ""
for i in dane2:
	print i
print ""
wynik = dopasowanie_profil_profil(maks_pod_dop_przedr, dane1, dane2)
for i in wynik:
	print i

tmp =[]
wynik = []
for i in dane1:
	tmp.append(i)
c=len(tmp) -1
print "\n\nKLASTERYZACJA"
print "Poszczegolne kroki klasteryzacji (wybierane slowa do dopasowania):"
while  c > 0:
	slowowyj1 = []
	slowowyj2 = []
	p1 = []
	p2 = []
	p1 = obliczanie_profilu(tmp[0], slownik1)
	p2 = obliczanie_profilu(tmp[1], slownik1)
	sp1 = []
	sp1 = srednie_podobienstwo_kolumn_profili(p1, p2, macierz_podobienstwa, slownik1)
	if len(tmp) > 2:
		for i in range(len(tmp)):
			for j in range(len(tmp)):
				if i != j:
					profili, profilj = [], []
					profili = obliczanie_profilu(tmp[i], slownik1)
					profilj = obliczanie_profilu(tmp[j], slownik1)
					sr_pod_prof = []
					sr_pod_prof = srednie_podobienstwo_kolumn_profili(profili, profilj, macierz_podobienstwa, slownik1)
					if sr_pod_prof > sp1:
						sp1 = sr_pod_prof
						slowowyj1 = tmp[i]
						slowowyj2 = tmp[j]
	else:
		slowowyj1 = tmp[0]
		slowowyj2 = tmp[1]
	tmp1=[]
	tmp2=[]
	print "\nwybrane klastry do zlaczenia:"
	print slowowyj1
	print slowowyj2
	if len(slowowyj1[0]) == 1: tmp1.append(slowowyj1)
	else: tmp1 = slowowyj1
	if len(slowowyj2[0]) == 1: tmp2.append(slowowyj2)
	else: tmp2 = slowowyj2
	ps1 = obliczanie_profilu(tmp1, slownik1)
	ps2 = obliczanie_profilu(tmp2, slownik1)
	sr_pod_prof = srednie_podobienstwo_kolumn_profili(ps1, ps2, macierz_podobienstwa, slownik1)
	mpdp = maks_podobienstwo_dopasowania_przedrostkow(sr_pod_prof, tmp1, tmp2)
	wynik = dopasowanie_profil_profil(mpdp, tmp1, tmp2)
	tmp.append(wynik)
	idxi = tmp.index(slowowyj1)
	tmp.remove(slowowyj1)
	idxj = tmp.index(slowowyj2)
	tmp.remove(slowowyj2)
	c-=1
	print "\nPozostale klastry:"
	for i in tmp:
		print i
	print "===="
	
print "ostateczny wynik klasteryzacji dla sekwencji:"
for i in dane1:
	print i
print ""
for i in tmp[0]:
	print i