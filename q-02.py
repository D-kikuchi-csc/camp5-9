n,l=(int(x) for x in input().split())
p=0
a=[]
for i in range(l):
    c=list(map(int, input().split()))
    a.append(c)
e=[0]*l
for u in range(n):
    M=[]
    for f in range(l):
        M.append(a[f][u])
    e[(M.index(max(M)))]+=1
Q=''
W=(max(e))
Q+=str(e.index(W)+1)+' '+str(W)
print(Q)

