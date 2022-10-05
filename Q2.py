def checkprime(n):
    c=0
    i=1
    while(i<=n):
        if n%i==0:
            c+=1
        i+=1   
    if(c==2):
        print("number is prime",n)
    else:
        print("number  is not prime")
        
        


n=int(input("enter the number"))
checkprime(n)