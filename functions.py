import numpy as np


def max_diff(arr, diff_lst, maxim, i, axis):
    lst = list(arr[i]) if axis == 0 else list(arr[:, i])
    lst.sort()
    if len(lst) > 1:
        diff = lst[1] - lst[0]
    else:
        diff = lst[0]
    diff_lst.append(diff)
    return max(maxim, diff)


def dummies(arr, row, col, minim, diff, x, i):
    temp = np.zeros([row, col], int)
    arr = np.append(arr, temp, x)
    minim.append(diff)
    return arr, i + 1, minim


def modify(arr, minim, maxim, result, index, x, i, j, a, b):
    maxim[j] -= minim[i]
    result += (arr[a][b] * minim[i])
    # print(arr[i][j], '*', minim[i], end=' <-> ')
    minim.pop(i)
    arr = np.delete(arr, i, x)
    return index - 1, result, arr


def find_max(arr, r, c):
    diff_row = []
    diff_col = []
    maxim = -1
    for i in range(r):
        maxim = max_diff(arr, diff_row, maxim, i, 0)
    for i in range(c):
        maxim = max_diff(arr, diff_col, maxim, i, 1)
    k = -1
    for i in diff_col:
        if i == maxim:
            k = diff_col.index(i)
            break
    for i in diff_row:
        if i == maxim:
            k = diff_row.index(i)
            break
    else:
        lst = list(arr[:, k])
        return lst.index(min(lst)), k
    lst = list(arr[k])
    return k, lst.index(min(lst))


def find_min(arr, r, c):
    minim = arr.min()
    for i in range(r):
        for j in range(c):
            if arr[i][j] == minim:
                return i, j