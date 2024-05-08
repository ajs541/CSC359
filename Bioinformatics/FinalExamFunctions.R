library(bio3d)
library(NameNeedle)

# Question 4 a
protein1 <- read.pdb("~/Test/CSC359-1/Bioinformatics/protein1.pdb")
protein2 <- read.pdb("~/Test/CSC359-1/Bioinformatics/protein2.pdb")
protein1Bad <- pdbseq(protein1)
protein2Bad <- pdbseq(protein2)
protein1seq <- paste(protein1Bad, collapse = "")
protein2seq <- paste(protein2Bad, collapse = "")
# Question 4 b
aln_nw <- needles(
    protein1seq,
    protein2seq,
    data.frame(MATCH = 2, MISMATCH = -1, GAP = -1, GAPCHAR = "-")
)
aln_split_1 <- strsplit(aln_nw$align1, "")[[1]]
aln_split_2 <- strsplit(aln_nw$align2, "")[[1]]

aln_together <- seqbind(aln_split_1, aln_split_2)
rownames(aln_together$ali) <- c("protein1", "protein2")
names(aln_together$id) <- c("protein1", "protein2")
real_alignment <- seqidentity(aln_together)
colnames(real_alignment) <- c("protein1", "protein2")
rownames(real_alignment) <- c("protein1", "protein2")
print(real_alignment)

# Question 4 c
protein1_resno_inds <- which(aln_together$ali["protein1", ] != "-")
protein2_resno_inds <- which(aln_together$ali["protein2", ] != "-")
names(protein1_resno_inds) <- names(protein1Bad)
names(protein2_resno_inds) <- names(protein2Bad)
p1.inds <- protein1_resno_inds[which(protein1_resno_inds %in% protein2_resno_inds)]
p2.inds <- protein2_resno_inds[which(protein2_resno_inds %in% protein1_resno_inds)]
matched_resno <- data.frame(
    "protein1" = names(p1.inds),
    "protein2" = names(p2.inds)
)
print(matched_resno)
protein1_sel <- atom.select(
    protein1,
    elety = "CA",
    resno = as.numeric(matched_resno$protein1)
)
protein2_sel <- atom.select(
    protein2,
    elety = "CA",
    resno = as.numeric(matched_resno$protein2)
)
# print(protein1_sel)
# print(protein2_sel)
protein2_fit <- fit.xyz(
    protein1$xyz,
    protein2$xyz,
    protein1_sel$xyz,
    protein2_sel$xyz
)
print(protein2_fit[1:6])
print(protein2$xyz[1:6])
protein1_protein2_rmsd <- rmsd(
    protein1$xyz, protein2_fit,
    a.inds = protein1_sel$xyz,
    b.inds = protein2_sel$xyz
)
print(protein1_protein2_rmsd)
