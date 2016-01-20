#-*- coding: utf-8 -*-
from Bio import AlignIO
from Bio import motifs
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import Phylo
from Bio.Align.Applications import MuscleCommandline
from StringIO import StringIO
from Bio.Emboss.Applications import NeedleCommandline
from Bio import motifs

import os

os.system('clear')
x = 0

def alignmentread():
	alignment = AlignIO.read('file.phy', 'phylip')
	tekst = ""
	tekst += open('file.phy').read()
	print "Dane z pliku:\n" + tekst + "\n\nWynik:\n"

	print "Alignment length %i" % alignment.get_alignment_length()
	for record in alignment :
		print record.seq, record.id

def alignmentparse():
	#przyklad funkcji alignio.parse z rozdziału 6.1
	alignments = AlignIO.parse("file.phy", "phylip")
	for alignment in alignments:
    		print(alignment)
    		print("")

def alignmentwrite():
	#przyklad funkcji alignio.write z rozdziału 6.2i
	align1 = MultipleSeqAlignment([
             SeqRecord(Seq("ACTGCTAGCTAG", generic_dna), id="Alpha"),
             SeqRecord(Seq("ACT-CTAGCTAG", generic_dna), id="Beta"),
             SeqRecord(Seq("ACTGCTAGDTAG", generic_dna), id="Gamma"),
         ])

	align2 = MultipleSeqAlignment([
             SeqRecord(Seq("GTCAGC-AG", generic_dna), id="Delta"),
             SeqRecord(Seq("GACAGCTAG", generic_dna), id="Epsilon"),
             SeqRecord(Seq("GTCAGCTAG", generic_dna), id="Zeta"),
         ])

	align3 = MultipleSeqAlignment([
             SeqRecord(Seq("ACTAGTACAGCTG", generic_dna), id="Eta"),
             SeqRecord(Seq("ACTAGTACAGCT-", generic_dna), id="Theta"),
             SeqRecord(Seq("-CTACTACAGGTG", generic_dna), id="Iota"),
         ])

	my_alignments = [align1, align2, align3]
	AlignIO.write(my_alignments, "alignmentwrite.phy", "phylip")
	print "Zapisano sekwencje do pliku alignmentwrite.phy"

def clustalw():
	#przyklad narzedzia clustalW z rozdziału 6.4.1 + mozna walnac to drzewo zo jest pod koniec tego rozdzialu
	align = AlignIO.read("opuntia.aln", "clustal")
	print(align)
	print ("")
	tree = Phylo.read("opuntia.dnd", "newick")
	Phylo.draw_ascii(tree)

def muscle():
	#przyklad narzedzia MUSCLE z rozdziału 6.4.2
	muscle_cline = MuscleCommandline(input="opuntia.fasta")
	stdout, stderr = muscle_cline()
	align = AlignIO.read(StringIO(stdout), "fasta")
	print(align)


def creatingamotif():
	# 14.1.1  Creating a motif from instances + 14.1.2  Creating a sequence logo
	instances = [Seq("TACAA"),
	Seq("TACGC"),
	Seq("TACAC"),
	Seq("TACCC"),
	Seq("AACCC"),
	Seq("AATGC"),
	Seq("AATGC"),
	]
	m = motifs.create(instances)
	print(m)
	print(m.counts)
	print "Slowo konsensusowe " + m.consensus


def writingmotifs():
	#14.3  Writing motifs
        instances = [Seq("TACAA"),
        Seq("TACGC"),
        Seq("TACAC"),
        Seq("TACCC"),
        Seq("AACCC"),
        Seq("AATGC"),
        Seq("AATGC"),
        ]
        m = motifs.create(instances)
	with open("Arnt.sites") as handle:
		 arnt = motifs.read(handle, "sites")
	print "Motif in pfm format"
	print(arnt.format("pfm"))
	print "\n\n Motif in arnt format"
	print(arnt.format("jaspar"))
	print "\n\n Motif in transfac format"
	print(arnt.format("transfac"))
def pwm():
	# 14.4  Position-Weight Matrices
        instances = [Seq("TACAA"),
        Seq("TACGC"),
        Seq("TACAC"),
        Seq("TACCC"),
        Seq("AACCC"),
        Seq("AATGC"),
        Seq("AATGC"),
        ]
        m = motifs.create(instances)

	pwm = m.counts.normalize(pseudocounts=0.5)
	print(pwm)
def pssm():
	# 14.5  Position-Specific Scoring Matrices
        instances = [Seq("TACAA"),
        Seq("TACGC"),
        Seq("TACAC"),
        Seq("TACCC"),
        Seq("AACCC"),
        Seq("AATGC"),
        Seq("AATGC"),
        ]
        m = motifs.create(instances)

        pwm = m.counts.normalize(pseudocounts=0.5)

	pssm = pwm.log_odds()
	print(pssm)

def instances():
	# 14.6  Searching for instances
	instances = [Seq("TACAA"),
        Seq("TACGC"),
        Seq("TACAC"),
        Seq("TACCC"),
        Seq("AACCC"),
        Seq("AATGC"),
        Seq("AATGC"),
        ]
        m = motifs.create(instances)
        print "Szukane instancje"
	print(m) 
	test_seq=Seq("TACACTGCATTACAACCACTGCCGATCGGGATCGTATTCGAACGCATCGACTAGCTACGATCGTACGATCGACTATGCATCGAAGTCGATCAAGCATTA", m.alphabet)
	print "\nDlugosc sekwencji testowej:" 
	print len(test_seq)
	print "\nZnalezione instancje w sekwencji testowej: "
	for pos, seq in m.instances.search(test_seq):
		print("%i %s" % (pos, seq))

def comparing():
	# 14.8  Comparing motifs
        instances = [Seq("TACAA"),
        Seq("TACGC"),
        Seq("TACAC"),
        Seq("TACCC"),
        Seq("AACCC"),
        Seq("AATGC"),
        Seq("AATGC"),
        ]
        m = motifs.create(instances)
        pwm = m.counts.normalize(pseudocounts=0.5)
	background = {'A':0.3,'C':0.2,'G':0.2,'T':0.3}
        pssm = pwm.log_odds(background)
	
	with open("REB1.pfm") as handle:
		m_reb1 = motifs.read(handle, "pfm")
	m_reb1.consensus
	print(m_reb1.counts)
	m_reb1.pseudocounts = {'A':0.6, 'C': 0.4, 'G': 0.4, 'T': 0.6}
	m_reb1.background = {'A':0.3,'C':0.2,'G':0.2,'T':0.3}
	pssm_reb1 = m_reb1.pssm
	print(pssm_reb1)
	distance, offset = pssm.dist_pearson(pssm_reb1)
	print("distance = %5.3g" % distance)
	print("offset = %5.3g" % offset)

	print "Offset to roznica miedzy poczatkami slow konsensusowych, w badanym wypadku najlepsze dopasowanie slow konsensusowych jest nastepujace: "
	print "m: bbTACGCbb"
	print "m_reb1: GTTACCCGG"


def wyjscie():
	print "Dobranoc!"

while (x != '0'):
	print "1. Bio.AlignIO\n2. Bio.Motifs\n"
	x = raw_input(	"	11.alignmentread.\n" +
					"	12.alignmentparse.\n" +
					"	13.alignmentwrite.\n" +
					"	15.clustalw.\n" +
					"	16.muscle.\n\n" +
					"	21.creating a motif.\n" +
					"	25.writing motifs.\n" +
					"	26.Position-Weight Matrices.\n" +
					"	27.Position-Specific Scoring Matrices.\n" +
					"	28.Instances.\n" +
					"	29.Comparing.\n\n" +

					"0. Wyjscie\n\n" +
					"Wybierz co chcesz zrobic: " )

	cases = {	'11':alignmentread,
				'12':alignmentparse,
				'13':alignmentwrite,
				'15':clustalw,
				'16':muscle,
				'21':creatingamotif,
				'25':writingmotifs,
				'26':pwm,
				'27':pssm,
				'28':instances,
				'29':comparing,

				'0':wyjscie,
				}
	try:
		os.system('clear')
		print "\nWybrales opcje: " + str(x) + " " + str(cases[x])
		if x != '0':
			cases[x]()
		else:
			print "\nDobranoc!"
	except IOError, error:
		print "\nzly znak"
		print"\n"+error

	raw_input("\n\nPress Enter to continue...")
	os.system('clear')
