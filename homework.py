x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)



x = 5
print(not(x>4 and x<11))
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))


x = 100

print(x > 40 and x < 90)
print(x > 30 or x < 400)
print(not(x > 3 and x < 10))



thislist = ["orange", "apple", "banana","cherry"]
print(thislist[2])
print(thislist[3])
print(thislist[0])

thislist = ["orange", "banana", "cherry", "orange", "kiwi", "melon","mango"]
print(thislist[2:5])
print(thislist[0]) 
print(thislist[6])
print(thislist[1:6])
print(thislist[0:6])



thislist = ["apple", "banana","cherry","orange", "kiwi", "melon","mango"]
print(thislist[3])
print(thislist[4])
print(thislist[0:5])
print('thislist[1:7] ====> {}'.format(thislist[1:7]))

thislist = ["apple", "banana","cherry","orange", "kiwi","mango"]
thislist[1]= "orange"
thislist[2:4] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[2:4] = ["mango"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(3, "watermelon")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(3, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("watermelon")
print(thislist)


# the difference between insert and append is that insert inserts an item anywhere you specify while append automaticaly puts it at the end

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)






# i dont know how to do 9, sorry

thislist = ["apple", "banana", "cherry", "orange", "melon", "mango"]
thislist.insert(2, "grapes")
print(thislist)



thislist.append("grapes")
print(thislist)


tropical = ["mango", "pineapple", "papaya"]

tropicalisthislist = thislist + tropical
print(tropicalisthislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "melon", "mango"]
thislist.pop(2)
thislist.pop()


thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()

thislist = ["apple", "banana", "cherry", "orange", "melon", "mango"]
for x in thislist:
 print(x)



y = 5

for i in range(1,11):
    print(y,'x', i, '=', y*i)












