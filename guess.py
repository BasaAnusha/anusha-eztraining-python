import random
n=random.randrange(1,6)
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
