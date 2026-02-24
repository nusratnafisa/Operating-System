d={}
n = int(input("Enter the number of entries: "))

for s in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    d.update({key: value})

print(d)
p=0
sum=0
i=1

for f in range(n):
 if(i==n):
    break
 for x,y in d.items():
    if(x==i):
        p=p+y
        sum = sum + p
        print(sum)
        break
 i=i+1

avgtime= sum/4 
print(avgtime)
      



