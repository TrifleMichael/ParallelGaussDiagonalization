import logging

import threading

import time

def test(s, s2):
    print(s)
    print(s2)


x = threading.Thread(target=test, args=("Ugabugoa", "Auuuga"))
x.start()
x.join()


def substractElement(i, j, k, arr):
    arr[i][k] -= arr[j][k] * arr[i][j] / arr[j][j]

def substractRow(i, j, arr):
    for k in range(len(arr[0])):
        substractElement(i, j, k, arr)

