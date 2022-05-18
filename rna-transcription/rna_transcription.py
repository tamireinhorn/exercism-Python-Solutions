rna_dict = {"G": "C", "C": "G", "T":"A", "A":"U"}

def to_rna(dna_strand):
    return ''.join([rna_dict.get(nucleotide) for nucleotide in dna_strand])
