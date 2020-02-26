# public int[] sumZero(int n) {
#         int[] A = new int[n];
#         for (int i = 0; i < n; ++i)
#             A[i] = i * 2 - n + 1;
#         return A;
#     }

def sumZero(n):
    A = [None] * n
    for i in range(n):
        A[i] = i * 2 - n + 1
    return A

print(sumZero(11))