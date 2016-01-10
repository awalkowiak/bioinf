from Bio import AlignIO

import os
os.system('cls')
x = 0

def alignment(case):
	opcje = {'stockholm':'file.sth', 'phylip':'file.phy'}
	print opcje[case]
	alignment = AlignIO.read(open(opcje[case]), case)
	print "Alignment length %i" % alignment.get_alignment_length()
	for record in alignment :
		print record.seq, record.id


while (x != '9'):
	x = raw_input("1.Opcja stockholm.\n2.Opcja phylip.\n3.Opcja 3.\n0.Wyjscie\nWybierz co chcesz zrobic: ")
	print "\nWybrales opcje: " + str(x)
	cases = ['opcja0','stockholm', 'phylip']
	
	alignment(cases[int(x)])
	
	raw_input("Press Enter to continue...")
	os.system('cls')