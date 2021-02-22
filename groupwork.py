#1
num=0
evlist = range(1,100)
while num in evlist:
    if num % 2 == 0:
       print(num, end =" ")


#2

odlist = range(1,100)
while num in odlist:
    if num % 2 != 0:
        print(num, end =" ")    
#3
for x in range(1,100):
    prime= True
    for y in range(2,x): 
        if (x % y) == 0:
            print(x, "this is not a prime number")
            prime=False
            break
    if (prime == True):
            print(x, "is a prime number")

#4 
            s1 = 10
            s2 = 20
            s3 = 30
            stotal = s1 + s2 + s3
            print(stotal)

            #5. It will print that they are both equal

            #6 I t will print a is greater than b

            
#5            
            for x in range(1,100):
                if (x%7) == 0:
                   print( x, "is divisible by 7")

            
#6            
            for x in range(1,100):
                if (x%5) == 0:
                   print( x, "is divisible by 5")
#7
num=0
evlist = range(1,11)
while num in evlist:
    if num % 2 == 0:
       print(num, end =" ")

num=0
evlist = range(1,11)
while num in evlist:
    if num % 2 != 0:
       print(num, end =" ")


#8
       numlist = [1,2,3,4,5,6,7,8,9,10,11]
       numlist.reverse
       print(numlist)




            




            







           

    
         


            
            






            