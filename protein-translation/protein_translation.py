M, P, L, S, T, C, TP, STOP = 'Methionine', 'Phenylalanine', 'Leucine', 'Serine', 'Tyrosine', 'Cysteine', 'Tryptophan', 'STOP'
codon_dict = {'AUG': M, 'UUU': P, 'UUC': P, 'UUA': L, 'UUG': L, 'UCU': S, 'UCC': S, 
'UCA': S, 'UCG': S, 'UAU': T, 'UAC': T, 'UGU': C, 'UGC': C, 'UGG': TP, 'UAA': STOP, 'UAG': STOP, 'UGA': STOP}
N = 3

def proteins(strand):
    codons = [strand[i:i+N] for i in range(0, len(strand), N)]
    protein_list = []
    for codon in codons:
        protein = codon_dict.get(codon)
        if protein == STOP:
            break
        else:
            protein_list.append(protein)
    return protein_list
        
 


 
# Codon                 | Protein
# :---                  | :---
# AUG                   | Methionine
# UUU, UUC              | Phenylalanine
# UUA, UUG              | Leucine
# UCU, UCC, UCA, UCG    | Serine
# UAU, UAC              | Tyrosine
# UGU, UGC              | Cysteine
# UGG                   | Tryptophan
# UAA, UAG, UGA         | STOP