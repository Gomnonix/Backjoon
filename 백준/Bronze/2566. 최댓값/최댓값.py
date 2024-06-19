arr1 = []
arr2 = []

for _ in range(9):
    arr1.append(list(map(int, input().split())))

for i in arr1:
    arr2.append(max(i))

max_val = max(arr2)
a = arr2.index(max_val)
b = arr1[a].index(max_val)

print(max_val)
print(a+1, b+1)
