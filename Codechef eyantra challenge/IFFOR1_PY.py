# cook your dish here
t=int(input())
for i in range(t):
    l=int(input())
    s=[]
    for i in range(l):
        if i==0:
            s.append(3)
        elif i%2==0:
            s.append(2*i)
        elif i%2!=0:
            s.append(i**2)
    for i in s:
        print(i, end=" ")
    print("")