# BAABB
# BB

def subsequence(A, B):
    i = 0
    for j in range(len(A)):
        if A[j] == B[i]:
            i += 1
        if i >= len(B):
            return True

    return False


print(subsequence("BBAA", "BB"))
