# cook your dish here
def dec_to_binary(n,s):
    if n>=1:
        dec_to_binary(n//2,s)
        s.append(n%2)
    return s
    
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=[]
        k=dec_to_binary(n,a)
        l=len(k)
        for i in range(8-len(k)):
            print(0,end="")
        for i in k:
            print(i,end="")
        print("")
        
        