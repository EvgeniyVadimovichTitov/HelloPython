from tkinter import N


def Fibonachi(N):
    if N == -1 or 0 < N <= 2:
        return 1
    if N == 0:
        return 0
    elif N > 2:
        return Fibonachi(N-1)+Fibonachi(N-2)
    else:
        return Fibonachi(N+2)-Fibonachi(N+1)
