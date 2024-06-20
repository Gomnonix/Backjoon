N = list(input())
N = sorted(N, reverse=True)

if N[-1] != "0":
    print(-1)
else: 
    sum_ls = 0
    for i in N:
        sum_ls += int(i)

    if sum_ls%3 != 0:
        print(-1)
    else:
        print("".join(N))
