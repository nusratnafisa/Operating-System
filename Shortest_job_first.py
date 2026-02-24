p=[]
s=[]
wt=s3=avg1=0
n = int(input("Enter the range: "))
for x in range(n):
  p.append(int(input("Enter the elements: ")))  
p.sort()
for x  in p :
    if x != p[n-1]:
     wt= wt + x
     s.append(wt)
     print(s)
for x in s:
   s3 = s3 + x
   print (s3)
avg1= s3/4
print(avg1)