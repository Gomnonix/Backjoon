n = int(input())
a = input()

if "LL" not in a:
    print(a.count("S"))
else:
    print(a.count("S")+a.count("LL")+1)