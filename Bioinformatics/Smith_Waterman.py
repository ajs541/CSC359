from Bio import Seq, Align

seqX = Seq.Seq("CATGTTA")
seqY = Seq.Seq("CACTGTA")

aln = Align.PairwiseAligner(match_score=1.0)
aln.mismatch_score = -1.0
aln.open_gap_score = -2.0
aln.extend_gap_score = -2.0
alns = aln.align(seqX, seqY)
print(f"This local alignment had {len(alns)} optimal solutions.")
for alignment in alns:
    print(alignment)