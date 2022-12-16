A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
C = [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]

def testGauss(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            for ind in range(len(A[0])):
                A[j][ind] -= A[j][i] / A[i][i] * A[i][ind]

    for i in range(len(A)-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = A[j][i] / A[i][i]
            A[j][i] -= factor * A[i][i]
            A[j][-1] -= factor * A[i][-1]

    for i in A:
        print(i)

testGauss(B)
