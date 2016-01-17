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
i         ])

	my_alignments = [align1, align2, align3]
	AlignIO.write(my_alignments, "alignmentwrite.phy", "phylip")
	print "Zapisano sekwencje do pliku alignmentwrite.phy"

def alignmentslice():
	#przyklad obrabiania dopasowań z rozdziału 6.3
        pass	
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

def emboss():
	#przyklad narzedzia emboss z rozdziału 6.4.5
	needle_cline = NeedleCommandline(asequence="alpha.faa", bsequence="beta.faa",gapopen=10, gapextend=0.5, outfile="needle.txt")
	stdout, stderr = needle_cline()
	print(stdout + stderr)
	align = AlignIO.read("needle.txt", "emboss")
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

def jaspar():
	# 14.2.1  JASPAR
	pass

def meme():
	# 14.2.2  MEME
	pass

def transfac():
	# 14.2.3  TRANSFAC
	pass

def writingmotifs():
	#14.3  Writing motifs
	pass
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
	pass

def instances():
	# 14.6  Searching for instances
	pass

def comparing():
	# 14.8  Comparing motifs
	pass

def denovo():
	# 14.9  De novo motif finding
	pass

def wyjscie():
	print "Dobranoc!"

while (x != '0'):
	print "1. Bio.AlignIO\n2. Bio.Motifs\n"
	x = raw_input(	"	11.alignmentread.\n" +
					"	12.alignmentparse.\n" +
					"	13.alignmentwrite.\n" +
					"	14.alignmentslice.\n" +
					"	15.clustalw.\n" +
					"	16.muscle.\n" +
					"	17.emboss.\n\n" +
					"	21.creating a motif.\n" +
					"	22.reading motifs (jaspar).\n" +
					"	23.reading motifs (meme).\n" +
					"	24.reading motifs (transfac).\n" +
					"	25.writing motifs.\n" +
					"	26.Position-Weight Matrices.\n" +
					"	27.Position-Specific Scoring Matrices.\n" +
					"	28.Instances.\n" +
					"	29.Comparing.\n" +
					"	210.de novo.\n\n" +

					"0. Wyjscie\n\n" +
					"Wybierz co chcesz zrobic: " )

	cases = {	'11':alignmentread,
				'12':alignmentparse,
				'13':alignmentwrite,
				'14':alignmentslice,
				'15':clustalw,
				'16':muscle,
				'17':emboss,
				'21':creatingamotif,
				'22':jaspar,
				'23':meme,
				'24':transfac,
				'25':writingmotifs,
				'26':pwm,
				'27':pssm,
				'28':instances,
				'29':comparing,
				'210':denovo,

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
