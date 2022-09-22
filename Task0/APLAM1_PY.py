import functools
T=int(input())
for i in range(T):
    a1 , d , n = (map(int,input().split()))
    lst=[]
    for j in range(1,n+1):
        a_n=a1+(j-1)*d
        lst.append(a_n)
        print(a_n,end =" ")
    sqr=list(map(lambda x : x**2,lst))
    print("")
    for i in sqr:
        print(i,end=" ")
    print("")
    print(functools.reduce(lambda a,b: a+b,sqr))
        
    
     