people = int(input())
time = list(map(int, input().split()))
time.sort()
sumtime = []

sum = 0
for i in time:
    sum += i
    sumtime.append(sum)

sum_time = 0
for i in sumtime:
    sum_time += i

print(sum_time)