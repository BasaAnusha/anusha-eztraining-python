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
                  
