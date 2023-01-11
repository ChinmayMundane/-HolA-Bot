# cook your dish here
T=int(input())
for i in range(T):
    s=input()
    s=s.lower()
    l=len(s)
    if s[l-1::-1]==s[0::1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")