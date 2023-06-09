def count(s,m,n):
    #table[i] will be storing the number of sol foe value i.we need  n+1 rows asthe table is constructed  in bottom up manner  usiing the basecase (n+0) intialize all table values  as 0\
    table =[0 for k in range(n+1)]
    print(table)
    table[0]=1
    for i in range(0,m):
        for j in range(s[i],n+1):
            table[j]+=table[j-s[i]]
            print(table)
    return table[n]
arr=[1,2,3]
#1,1,1/1,2/2,1/3
m=len(arr)
n=4#1111,112,13,22
x=count(arr,m,n)
print(x)
        
