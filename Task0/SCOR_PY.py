# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=[]
    k=[]
    l=[]
    p=[]
    for i in range(n):
        st=[str(x) for x in input().split()]
        s.append(float(st[1]))
        k.append(st[0])
    for i in range(len(s)):
        if s[i]==max(s):
            l.append(i)
    for i in l:
        p.append(k[i])
    p.sort()
    for i in p:
        print(i)