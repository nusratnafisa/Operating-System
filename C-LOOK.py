list1=list(map(int,input("enter value:").split()))
head=int(input("enter head:"))
dir=int(input("enter 1 if you want to move toward small numbers or else enter 0:"))
left=[]
right=[]
list2=[]
total=0
current=head

if head in list1:
    list1.remove(head)
    
for i in range(len(list1)):
  if list1[i]<head:
      left.append(list1[i])
  else:
      right.append(list1[i])
      
left.sort()
print("left queue:",left)
right.sort()
print("right queue:",right)

if dir == 1:
    left.reverse()
    right.reverse()
    for i in range(len(left)):
     s=abs(current-left[0])
     total=total+s
     list2.append(f"{current}--->{left[0]}={s}")
     current=left[0]
     left.remove(current)
        
    for i in range(len(right)):
     s=abs(right[0]-current)
     total=total+s
     list2.append(f"{current}--->{right[0]}={s}")
     current=right[0]
     right.remove(current)
else:
    for i in range(len(right)):
     s=abs(right[0]-current)
     total=total+s
     list2.append(f"{current}--->{right[0]}={s}")
     current=right[0]
     right.remove(current)
        
    for i in range(len(left)):
     s=abs(current-left[0])
     total=total+s
     list2.append(f"{current}--->{left[0]}={s}")
     current=left[0]
     left.remove(current)
    
print("Head Movement Sequence:")
for s in list2:
    print(s)
print(total)