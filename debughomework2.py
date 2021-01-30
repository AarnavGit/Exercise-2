fact2 = 1
fact1 = 5
fact3 = fact1
while fact1 > fact2:
   fact2 = fact2 * fact1
   fact1 = fact1 - 1

print('factorial of',fact3,'=',fact1)