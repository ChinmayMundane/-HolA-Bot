import numpy as np
t = int(input())
for i in range(t):
    l=int(input())
    n=list(map(int,input().split()))
    rev = n[::-1]
    arr = np.array(rev)
    for r in range(l):
        print(arr[r], end=" ")
    print(end="\n")
    for i in range(3,l,3):
        print(n[i]+3, end=" ")
    print(end="\n")
    # print(n[3]+3,n[6]+3)

    for j in range(5,l,5):
        print(n[j]-7)

    
    print(n[3]+n[4]+n[5]+n[6]+n[7])
    





    
