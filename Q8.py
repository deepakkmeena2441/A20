def count(s):

    l=[e for e in s if ord(e)>=65 and ord(e)<=90]
    
    s=[d for d in s if ord(d)>=97 and ord(d)<=122]
    print("upper case in string is ",len(l))
    print("lower case in string is",len(s))




s=input()
count(s)