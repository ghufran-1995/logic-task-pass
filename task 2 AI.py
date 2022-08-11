
min = int(input("Enter the min : "))
max = int(input("Enter the max : "))
for i in range(min,max + 1):
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(j)