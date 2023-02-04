EXCEPTION HANDLING
a=100
b=0
#TRY  ur telling that this may hve an error ,u try
try:
    print(a/b)
#EXCEPT EXCEPTION :u r saying that if error there in the program it was handled
except Exception as e:
    print("print that nnumber cant be divided :by zero",e)#this will print error also
#to check your program excecution goes till end or not
finally:
       print("bye")'''

***TRY EXCEPT AND FINALLY
a=10
b=0
try:
    print("resourse open:")
    print(a/b)
except Exception as e:
    print("print that odnt have second no as zero",e)
finally:
    print("resourse closed:")


#LIKE SPECILIZED DOCTOR

a=100
try:
    b=int(input("enter the number:"))
    print("resourse open")
    print(a/b)
except ZeroDivisionError  as e:
    print("please note that number cant be divided by  zero:",e)
except ValueError as e:
    print("invalid input number",e)
except Exception as e:
    print("other error:",e)
finally:
    print("resourse is closed")


RAISE EXCEPTION
x=3456676
if x%2!=0:
    raise Exception("x should be the evn number")
else:
    print("x is even number:")


###OOPS
***class computer:
    def config(self):
        print("yes")
lenova=computer()
computer.config()
dell=computer()
dell.config()


#VARIABLE AND VAR ACCESS IN CLASS AND METHOD
class computer:
    a=10
    b=20
    print("class variable  inside class",a)
    def config(self):
        c=100
        print("yes")
        print("instance access",self.b)

lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)

dell=computer()
print("dell",dell.a)
lenova.config()
   

q1="""who is the best cricket captain?
a.dhoni
b.virat
c.rohit
d.sachin"""
q2="""which is a immutable  among?
a.list
b.string
c.dictionary
d.set"""
q3="""which language among is easy to learn and robust?
a.c
b.java
c.python
d.data structures"""
q4="""what is your favourite sport?
a.cricket
b.kabaddi
c.volleyball
d.football"""
q5="""duration of the phase1 training?
a15 days
b.1 week
c.6 days
d.1 month"""
q6="""which movie among is most popular over the world recently?
a.kgf
b.kgfpart2
c.rrr
d.bahubhali"""
questions={q1:"a",q2:"b",q3:"c",q4:"b",q5:"c",q6:"c"}
name=input("hi:enter your name:")
print("hello",name,"welcome to the quiz")
score=0
for i  in questions:
    print()
    print(i)
    flag1=input("do you want to skip this question(yeS/no)")
    if flag1=="yeS":
         continue
    ans=input("enter your answer")
    if ans==questions[i]:
         print("wow!your answer is correct  you got a point")
         score=score+1
         print("your current score is:",score)
    else:
         print("your answer is wrong  you lose a point")
         score=score-1
         print("your current score is:",score)
     flag2=("do you want  to quit the quiz?type(yes/no)")
    if flag2=='yes':
         break
print("your total score is:",score)




###PROJECT2

                  

import time
def countdown(t):

    while t:
        mins,secs = divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t=t-1

    print("finished")
t=input("enter the time in seconds")
countdown(int(t))



###PROJECT3
name1=input("enter the name1:").lower()
name2=input("enter the name2:").lower()
#if you give first and last name
#with space inbetween
name1=name1.replace(" "," ")
name2=name2.replace(" "," ")
print(name1)
print(name2)

for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
count=len(name1+name2)
print(count)
if count>0:
      list1=["friends","lovers","affectionate","marriage","enemies","sisters"]
      while len(list1)>1:
          c=count%len(list1)
          s_index=c-1
          if s_index>=0:
              left=list1[:s_index]
              right=list1[s_index+1:]
              list1=right+left
          else:
              list1=list1[:len(list1)-1]
      print("Relationship:",list1[0])
else:
      print("enter different names")
