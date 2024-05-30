s = input()
li = 'abcdefghijklmnopqrstuvwxyz'

for i in li:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1, end=" ")