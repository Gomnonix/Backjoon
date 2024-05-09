nums = int(input())
sits = input()

sits_s = sits.count('S')
sits_l = sits.count('LL')

cups = 0
if sits_l > 0:
    cups += sits_s + (sits_l + 1) 
    print(cups)
    
else:
    cups += sits_s
    print(cups)
