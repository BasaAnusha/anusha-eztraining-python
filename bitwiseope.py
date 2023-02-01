1.write the program toget 2 numbers as input both the numbers will be less than or equal to 15 to perform bitwise and ,or,xor operator
code    
        n1,n2=int(input("enter n1:")),int(input("enter n2:"))
print(n1&n2)
print(n1|n2)
print(~n1)
print(~n2)
print(n1^n2)

###2.program to map a list


      n=int(input("size"))
a=list(map(int,input("numbers:").strip().split()))[:n]
print(a)



3.program of a heart
print(" ","*"," ","*","" )
print("*"," ","*"," ","*")
print("","*"," ","  *","")
print(" ","*",""," *"," ")
print(" "," ","*"," "," ")


4.triangle

print("*",'*','*')
print( " *", "*")
print(" ","*"," ")

5.divisible by both 2 and 5

n=int(input("enter a number:"))
if n%2==0 and n%5==0:
    print("divisible by both 2 and 5")
else:
    print("not divisible by both 2 and 5")

5.printing name
n='anu'
i=str(n)

i=1
while i<=10:
    print(n)
    i=i+1

 

6. program for loop

code:       for i in range(1,11):
                 print(i)


 #with jump or step value for even:
           for j in range(2,11,2):
                print(j)

#for  odd

            for k in range(3,12,2):




program to play with numbers

code:       import random
n=random.randrange(1,50)
guess=int(input("enter any number"))
while n!=guess:
      if guess<n:
          print("too low")
          guess=int(input("enter the number again:"))
      elif  guess>n:
          print("too high!")
          guess=int(input("enter the number again:"))
      else:
            break
print("you guessed it right")






                   print(k)
    

