from methods import *


r = int(input('Enter the number of sources : '))
c = int(input('Enter the number of destination : '))
lst = []
supply = []
demand = []
print('Enter the transportation costs in matrix form one by one : ')
for i in range(r * c):
    lst.append(int(input()))
arr = np.array(lst).reshape(r, c)

print('Enter the supply one by one : ')
for i in range(r):
    supply.append(int(input()))

print('Enter the demand one by one : ')
for i in range(c):
    demand.append(int(input()))

# Unbalanced -> balanced
if sum(supply) < sum(demand):
    arr, r, supply = dummies(arr, 1, c, supply, sum(demand) - sum(supply), 0, r)
elif sum(supply) > sum(demand):
    arr, c, demand = dummies(arr, r, 1, demand, sum(supply) - sum(demand), 1, c)
print(arr)

s_temp = supply.copy()
d_temp = demand.copy()
nwc_ans = nwc_rule(s_temp, d_temp, arr, r, c)
print('NorthWest Corner Method : ', nwc_ans)

s_temp = supply.copy()
d_temp = demand.copy()
lcc_ans = lcc(s_temp, d_temp, arr, r, c)
print('Least Cost Cell Method : ', lcc_ans)

s_temp = supply.copy()
d_temp = demand.copy()
vam_ans = vam(s_temp, d_temp, arr, r, c)
print('Vogel’s Approximation Method : ', vam_ans)
