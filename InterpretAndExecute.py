def substractElement(i, j, k, arr):
    try:
        arr[i][k] -= arr[j][k] * arr[i][j] / arr[j][j]
    except:
        print("Errur, tried to do", i, j, k)
        for i in arr:
            print(i)
        exit()

def substractRow(i, j, arr):
    for k in range(len(arr[0])):
        substractElement(i, j, k, arr)

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
f = open("word", "r")

arr = B

for line in f:
    all = line.split(",")[:-1]
    i = int(all[0])
    j = int(all[1])
    substractRow(i, j, arr)

for i in arr:
    print(i)
