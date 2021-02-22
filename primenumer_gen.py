for x in range(1,100):
    isprime=True
    for y in range(2,x): 
        if (x % y) == 0:
            print(x, "Not a PRIME!")
            isprime=False
            break
    if(isprime==True):
        print(x, "IS PRIME a PRIME!")
