# cook your dish t
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split(" "))
    dist=((a-c)**2+(b-d)**2)**0.5
    print("Distance: ""%0.2f" % dist)