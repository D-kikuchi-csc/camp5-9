a=int(input())
b=list(map(int, input().split()))
c=list(map(int, input().split()))

T=""
for i in range(a):
    T+=str(abs(b[i]-c[i]))+" "

print(T)