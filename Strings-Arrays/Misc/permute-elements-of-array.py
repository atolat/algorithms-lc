# Permute elements of an array - EPi

def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
