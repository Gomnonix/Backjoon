n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))

for _ in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    arr_sum = []
    for j in range(m):
       arr_sum.append(arr1[i][j] + arr2[i][j])
    print(' '.join(map(str, arr_sum)))
