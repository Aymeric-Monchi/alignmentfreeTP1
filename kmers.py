"""def kmer2str(val, k): #fonction débugage pour obtenir la réciproque de stream_kmers
     Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted

    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)"""

def encode(nucl):
    letters = ['A', 'C', 'T', 'G']
    if nucl not in letters:
        nucl = 'A'
    if nucl == 'A':
        return 0
    elif nucl == 'C':
        return 1
    elif nucl == 'T':
        return 2
    elif nucl == 'G':
        return 3

def r_encode(nucl):
    letters = ['A', 'C', 'T', 'G']
    if nucl not in letters:
        nucl = 'A'
    if nucl == 'A':
        return 2
    elif nucl == 'C':
        return 3
    elif nucl == 'T':
        return 0
    elif nucl == 'G':
        return 1

def stream_kmers(text, k):
    # --- To complete ---
    list_kmer = []
    kmer = 0
    mask = (1<<((k-1)*2))-1
    rkmer = 0
    for i in range(k-1):
        kmer <<= 2
        kmer += encode(text[i]) #fonction encode à définir
        rkmer >>= 2
        rkmer += r_encode(text[i])
    for nucl in text[(k-1):]:
        kmer = kmer & mask #retirer nucléotide à gauche
        kmer <<= 2
        rkmer >>= 2
        kmer += encode(nucl)
        rkmer += r_encode(nucl)
        list_kmer.append(max(kmer,rkmer))
    return list_kmer

if __name__ == "__main__":
    list = stream_kmers("CAGT", 3)
