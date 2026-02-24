dict1={}                                     #empty ekta dictonary niyechi dict1 
n = int(input("Enter the range: "))          # dictonary er size niyechi

for s in range(n):                           # dict1 er input niyechi jeikhane key range er sathe milano thakbe
    key = s
    value = int(input("Enter value: "))
    dict1.update({key: value})
print("dict1:",dict1)

print('\n')
dict2 = dict1.copy()                         #dict2 hoilo dict1 er copy

print("dict2:",dict2)

print('\n')

dict3={}                                     # arekta empty dict3 niyechi 

for s in range(n):                           # eikahne dict3 er ke dict1 er size er korechi but value gula 0 hobe as oikhane total ek ekta proccess sesh hobe koto time legeche seita rakhbo
    key = s
    value = 0
    dict3.update({key: value})

print("dict3:",dict3)

print('\n')

Q = int(input("Enter the quantum number: "))    #quantum number 

sum=0
while( len(dict1)!=0) :                        #eikhane ei loop totokhon cholbe jotokhon nah dict1 er len zero hoy as amra dict1 er jei value gula zero hoye jabe execution er time seigula remove kore dibo
 done=[]                                       # ei list e jei dict1 er value gula zero hobe tader key gula insert korbo jate last e dict1 theke pop out kore dite pari
 for K in dict1:                              
     if (dict1[K]>=Q):                          # eikhane check korbe je dict1 e proccess er burst time er value gula Q er theke boro naki soman, jodi ei condition fulfil kore tokhon sum er sathe Q er valu jog dibe and oi proccess er burst time theke Q er value baad dibe

        sum=sum+Q
        dict1[K]= dict1[K] - Q

     elif( dict1[K]<Q):                            #eikhane check korbe je proccess er burst time Q er theke choto kina , taile oi burst time tai sumer sathe jog dibe er mane hoilo oi proccess fully execute hoyeche tai ore burst time zero dibe 

        sum = sum + dict1[K]
        dict1[K]=0
        done.append(K)                             #dict1 e burst time zero dewa mane oita r execution comeplete tai oita dict 1 theke proccess tah baad dibo tai done er mode oitar key rekhe disi.. and dict3 teh same key teh sum er value insert korechi.
        dict3[K] = sum
    
 for x in done:                                   #dict1 theke jeigula proccess sehs oigula baad diyechi as done er modhe oi proccess er key gula rekhe diyechilam
    dict1.pop(x)   

print("dict1:",dict1)

print('\n')

print("dict3:",dict3)

print('\n')

#waiting time calculation
WT={}                      # ei WT teh total time - burst time tah rakhbo mane ekta proccess dhori p1 sesh howar kotha 21s (burst time) but sesh hoyeche 32s(total time) tokhon p1 majhe wait koreche seita ber kore eita r modhe rakhbo
sum_WT=0
for k in dict3:
   if k in dict2:
      value=dict3[k]-dict2[k]                   
      WT.update({k: value})
      sum_WT=sum_WT+value         # shob gula proccess er waiting time sum korbo

print("waiting time:",WT)

print('\n')

print("total waiting time:",sum_WT)

print("avg time:",sum_WT/n ) # average time = total waiting time / total number of proccess( n)



     

