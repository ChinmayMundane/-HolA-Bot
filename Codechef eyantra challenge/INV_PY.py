# cook your dish here
t=int(input())
for i in range(t):
    N = int(input())
    d1 = dict(input().split() for i in range(N))
    m=int(input())
    l1 = list(input().split() for i in range(m))
    s=0
    for i in l1:
        if i[0]=='DELETE' and i[1] in d1 and int(i[2])<int(d1[i[1]]):
            d1[i[1]]=int(d1[i[1]])-int(i[2])
            print("DELETED Item",i[1])
        elif i[0]=='DELETE' and i[1] in d1 and int(i[2])>int(d1[i[1]]):
            print("Item",i[1],"could not be DELETED")
        elif i[0]=='ADD' and i[1] not in d1:
            d1[i[1]]=i[2]
            print("ADDED Item",i[1])
        elif i[0]=='ADD' and i[1] in d1:
            d1[i[1]]=int(d1[i[1]])+int(i[2])
            print("UPDATED Item",i[1])
        elif i[0]=='DELETE' and i[1] not in d1:
            print("Item",i[1],"does not exist")
        elif i[0]=='DELETE' and i[1] in d1 and int(i[2])==int(d1[i[1]]):
            d1[i[1]]=int(d1[i[1]])-int(i[2])
            print("DELETED Item",i[1])
    for i in d1:
        s=s+int(d1[i])
    print("Total Items in Inventory:",s)