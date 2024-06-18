n = [int(input()) for _ in range(9)]
arr = []
arr2 = []
sum_n = sum(n)
for i in range(9):
    for j in range(i+1, 9):
        if sum_n - n[i] - n[j] == 100:
            arr =[n[i], n[j]]
            break
    if arr:
        break

arr2 = [x for x in n if x not in arr]

for i in sorted(arr2): 
    print(i)