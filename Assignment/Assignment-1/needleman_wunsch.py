from Bio import SeqIO

def read_fasta(file):
    sequences = []
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(str(record.seq))
    return sequences

sequences = read_fasta("APOBEC3A.fasta")


def load_blosum62(file):
    blosum62 = {}
    with open(file) as f:
        lines = f.readlines()
        amino_acids = lines[0].split() 
        for line in lines[1:]:
            parts = line.split()
            row_acid = parts[0]  
            scores = list(map(int, parts[1:]))  
            blosum62[row_acid] = dict(zip(amino_acids, scores))
    return blosum62
def needleman_wunsch(seq1, seq2, gap_penalty, blosum62):
    n = len(seq1)
    m = len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        score_matrix[i][0] = gap_penalty * i
    for j in range(1, m + 1):
        score_matrix[0][j] = gap_penalty * j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i-1][j-1] + blosum62[seq1[i-1]][seq2[j-1]]
            delete = score_matrix[i-1][j] + gap_penalty
            insert = score_matrix[i][j-1] + gap_penalty
            score_matrix[i][j] = max(match, delete, insert)

    return score_matrix[n][m]

if __name__ == "__main__":
    blosum62 = load_blosum62("BLOSUM62.txt")
    gap_penalty = -5
    sequences = read_fasta("APOBEC3A.fasta")

    ans=(0,1)
    res=-1
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            score = needleman_wunsch(sequences[i], sequences[j], gap_penalty, blosum62)
            if score>res:
                res=score
                ans=(i,j)
    print(f"The most similar sequences are {ans[0]+1} and {ans[1]+1} with a similarity score of {res}")
