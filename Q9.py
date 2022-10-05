def check(s):
    
    for e in s:
        if e>=chr(90) or e<=chr(122) or e>=chr(65) or e<=chr(90) :
            return True

        

        
    return False





s=input("enter the sting")

if(check(s)==True):
   print("string is pangram")
else:
    print("string is not pangram")