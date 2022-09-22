# cook your dish here
t=int(input())
for i in range(t):
    str=input()
    str=str[1::]
    s=[len(x) for x in str.split()]
    for i in range(len(s)):
        if i==len(s)-1:
            print(s[i])
        else:
            print(s[i],end=',')