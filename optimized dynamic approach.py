class solution:
   def coinchange(self,List,amount):
       dp=[amount+1]*(amount+1)
       dp[0]=0
       for a in range(1,amount+1):
           print("a:",a)
           for c in List:
               print("c:",c)
               if a-c>=0:
                   dp[a]=min(dp[a],1+dp[a-c])
                   print(a)
                   print("dp:",dp[a])
       return dp[amount] if dp[amount]!=amount+1 else -1
obj=solution()
List=[1,3,5,6]
amount=11
print(obj.coinchange(List,amount))
