f = open("word", "w")
N = 4


def writeLetter(i, j, k, file=f):
    f.write(str(i) + "," + str(j) + "," + str(k) + "\n")


def writeLetters(i, j, file=f):
    for k in range(N):
        writeLetter(i, j, k, f)


# Leaving 0 below the diagonal
for i in range(N-1):
    for j in range(i+1, N):
        writeLetters(j, i)

# Leaving 0 above the diagonal
for i in range(N-1, 0, -1):
    for j in range(i-1, -1, -1):
        writeLetters(j, i)

f.close()
