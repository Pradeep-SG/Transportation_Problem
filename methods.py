from functions import *


def nwc_rule(supply, demand, arr, r, c):
    ans = 0
    while r > 0 and c > 0:
        if supply[0] < demand[0]:
            r, ans, arr = modify(arr, supply, demand, ans, r, 0, 0, 0, 0, 0)
        else:
            c, ans, arr = modify(arr, demand, supply, ans, c, 1, 0, 0, 0, 0)
    return ans


def vam(supply, demand, arr, r, c):
    ans = 0
    while r > 0 and c > 0:
        row, col = find_max(arr, r, c)
        if supply[row] < demand[col]:
            r, ans, arr = modify(arr, supply, demand, ans, r, 0, row, col, row, col)
        else:
            c, ans, arr = modify(arr, demand, supply, ans, c, 1, col, row, row, col)
    return ans


def lcc(supply, demand, arr, r, c):
    ans = 0
    while r > 0 and c > 0:
        row, col = find_min(arr, r, c)
        if supply[row] < demand[col]:
            r, ans, arr = modify(arr, supply, demand, ans, r, 0, row, col, row, col)
        else:
            c, ans, arr = modify(arr, demand, supply, ans, c, 1, col, row, row, col)
    return ans