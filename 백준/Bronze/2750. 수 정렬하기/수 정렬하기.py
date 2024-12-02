N = int(input())
nums = []

for _ in range(N):
    M = int(input())
    nums.append(M)
    
nums.sort()

for i in nums:
    print(i)