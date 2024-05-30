T = int(input())
room = []
for _ in range(T):
    h,w,n = map(int, input().split())

    floor = n%h
    room_num = (n//h) + 1
    if floor == 0:
        floor = h
        room_num -= 1

    room.append(f'{floor}{room_num:02}')

for i in room:
    print(i)
