#y = 0
#numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
#for x in numbers: 
#  print(y = y + x) 

#allfruits = ["apple", "banana", "cherry"]
#for somefruit in allfruits:
#  print(somefruit)

#*
#**
#***

#total=0
#for i in range(2, 6):
#  print(total , ' + ', i , '===============>')
#  total = total + i
#  print('for loop total =' , total)

#print('FINAL TOTAL = ', total)



#1. write a program using for loop  to find the sum of all numbers stored in a list 

mytotal=0
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
for x in numbers:
    mytotal = mytotal + x
print(mytotal)

#2, write a program using for loop to print squares of all numbers present in a list
numbers = [1, 2, 4, 6, 11, 20]
for x in numbers:
    print(x ** 2)

### while loop
##while i <= 100:
  #print(i)
  #i = i+1

  #3. Write a program using while loop & for loop to print list of all fruits
fruits = ["apple", "orange", "kiwi"]
for x in fruits:
    print('for loop fruits :' ,x)

index = 0
while index < len(fruits):
    print('while loop fruits :' ,fruits[index])
    index = index+1


#4. Write a program using a while loop to print any number table 10*1 = 10*2 = 20 .......... 10*10 =100
x=1
y=7
z=10
while x <= z:
    print(y,'x', x, '=', y*x)
    x = x+1

#5. Write a program using while loop to print factorial of any given number ; eg 5 factorial = 5 * 4 * 3 * 2 * 1 = 120

factnumb= 5
factresult= 1
while factnumb >= 1:
    factresult = factresult * factnumb
    factnumb = factnumb-1

print('the factorial of 5 is', factresult)

#6. Write a program using for loop to iterate over the string, and print each characterin that string

testSTR= 'BALJEET SENSAI'
for x in testSTR:
    print(x)

#7 Write a program using a while and for loop to print the sum of first 5 natural numbers.

natnum = [1,2,3,4,5]
x = 0
for i in natnum:
    x = x + i
print('THE SUM', '=', x)

natnum = [1,2,3,4,5]

x = 1
y = 0
while x <= len(natnum):
  y = y + x
  x = x + 1

print('THE SUM','=',y)

                          