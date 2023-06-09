#lst =[190,90,80,70,60,50,40,30,20 ,10]
#pfts=[2,7,3,,4,27,3,5,1,1]
pfts=[20,50,30,10,20]
slots=[3,2,1,2,3]
final=[]
profits=[]
for i in range(max(slots),0,-1):
     print("i:",i)
     for j in range(len(slots)):
         print("j:",j)
         if i== slots[j]:
             final.append(pfts[j])
     print(j)
     profits.append(max(final))
     final.remove(max(final))
     print(profits)
print("total:",profits[::-1])
print("total:",sum(profits))
