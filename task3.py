import random
a = []
for i in range(100):
     a.append(random.randint(0,100))
print(a)

result = []

for num in a:
     if (num%7==0):
        if num%5==0:
            2+2
        else:
            result.append(num)
    
for v in result:
    if result.count(v)>1:
        while result.count(v)>1:
            result.remove(v)

print(result)