from loading import load_directory
from kmers import stream_kmers

def intersection(A,B):
        inter = list(set(A) & set(B))
        return inter


def similarity(A, inter, B):
    # --- To complete ---
    simA = len(inter)/(len(A)+len(inter))
    simB = len(inter)/(len(B)+len(inter))
    return simA, simB

def jaccard(A, inter, B):
    # --- To complete ---
    J = len(inter)/(len(A)+len(B)+len(inter))
    return J

def concatenate(d):
    for genome in d.keys():
        if len(d[genome])>1:
            s = "".join([str(item) for item in d[genome]])
            d[genome] = s
        else:
            d[genome] = d[genome][0]
    return d

if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21

    filenames = list(files.keys())
    files = concatenate(files)
    for i in range(len(files)):
        A = stream_kmers(files[filenames[i]], k)
        for j in range(i+1, len(files)):
            B = stream_kmers(files[filenames[j]], k)
            inter = intersection(A,B)
            print(filenames[i], filenames[j], jaccard(A, inter, B), similarity(A, inter, B))
