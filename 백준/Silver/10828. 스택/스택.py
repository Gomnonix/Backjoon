import sys 
# 표준입출력: 더 빨리 입력을 받는다

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        array.append(int(cmd[1]))

    elif cmd[0] == "top":
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])

    elif cmd[0] == "size":
        print(len(array))

    elif cmd[0] == "empty":
        if len(array) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "pop":
        if len(array) == 0:
            print(-1)
        else:
            print(array.pop())