n=int(input())
n=1000-n
m=[500,100,50,10,5,1]
c=0
for i in m:
    c=c+int(n/i)
    n=n%i
print(c)