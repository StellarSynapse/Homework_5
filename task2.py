import random
a = []

for i in range(10):
     a.append(random.randint(0,10))
print(a)

b = []
for i in range(10):
     b.append(random.randint(0,10))
print(b)

united = []
for i in a:
     for j in b:
          if i==j:
               united.append(i)


for num in united:
     if united.count(num)>1:
          while united.count(num)>1:
               united.remove(num)

          



print(united)

            



