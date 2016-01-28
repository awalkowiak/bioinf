import glob
import re
files = []
files = glob.glob('*.txt')

pattern = ['zamach', 'katastrof', 'klamstw', 'hanb', 'prezydent', 'samolot', 'TU-154', 'Macierewicz', 'wybuch', 'strzal', 'bomb', 'brzoz', 'komisj', 'wrak', 'sledztw', 'przyczyn', 'kabin', 'trotyl', 'krzyz', 'Rosj', 'Smolensk', 'wiez', 'pilo', 'slad', 'skrzydl', 'ofiar', 'swiadek', 'swiadk', 'Kaczyns', 'tupolew', 'mgl', 'dym', 'rozpyl', 'blad', 'zdrad', 'kabin', 'krzyk', 'nalega', 'skrzyn', 'lotnisk']

ptn = "                        "
#ptn = (ptn + str(p) for p in pattern)
for p in pattern:
	ptn = ptn + str(p) + "  "
print ptn
# for i in range(len(files)):
	# tekst = ""
	# tekst += open(files[i]).read()
	# slowa = []
	# slowa = re.split(' |\n', tekst)
	# count = str(files[i]) + ""
	# for word in pattern:
		# counter = 0
		# for slowo in slowa:
			# if word in slowo:
				# counter += 1
		# count = count + "    " + str(counter)
		# #print "w pliku " + str(files[i]) + " slowo: " + str(word) + " wystapilo: " + str(counter) + " razy."

	# print count + "\n"

wynik = []
wiersz = []
pliki = []
for word in pattern:
	wiersz = []
	#wiersz.append(word)
	for file in range(len(files)):
		tekst = ""

		tekst += open(files[file]).read()
		pliki.append(files[file])
		slowa = []
		slowa = re.split(' |\n', tekst)
		counter = 0
		for slowo in slowa:
			if word in slowo:
				counter += 1
			if word.capitalize() in slowo:
				counter += 1
		wiersz.append(counter)
	wynik.append(wiersz)
#print pliki
print wynik
zapis = open('wynik.txt', 'w')
strwyn = ""
for i in range(len(wynik)):
	#print i
	strwin=""
	for w in range(len(wynik[i])):
		#print wynik[i][w]
		if w < len(wynik[i])-1:
			strwin = strwin + str(wynik[i][w]) + ","
		else:
			strwin = strwin + str(wynik[i][w])
	#print strwin
	strwyn = strwyn + strwin + "\n"
print strwyn
zapis.writelines(strwyn)