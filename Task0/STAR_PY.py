# cook your dish here
t= int(input())
for i in range(t):
    l=int(input())
    for i in range(l):
        for j in range(l-i):
            if j!=0 and (j+1)%5==0:
                print("#", end="")
            else:
                print("*", end="")
        print("")