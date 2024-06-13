n = int(input())
arr = []
endPoint= 0
answer= 0

for i in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

for newStart, newEnd in arr:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd

print(answer)

