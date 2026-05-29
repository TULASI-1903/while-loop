#while loop()
'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)'''
'''a=10
while a>1:
    print("true")'''


'''a=10
while a>1:
    print("true")'''

'''a=10
while a>1:
    print(a)
    a=a-1'''
'''a=10
while a>1:
    a=a-1
    print(a)'''
'''a=20
while a>1:
    a=a-1
print(a)'''
'''a=30
while a>5:
    print(a)
    a+=5'''


'''a=30
while a>5:
    print(a)
    a-=1'''
'''a=10
while a>40:
    print(a)
    a+=1'''

'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for voting")
    else:
        print("not eligible for voting")'''

#range()
#the range function returns a sequence of numbers,starting from zero by default and increments by one by one and stop before a specify number
#start-stop-step
'''for i in range(21):
    print(i,end=" ")'''

'''for i in range(5,31):
    print(i)'''

'''for i in range(0,20,2):
    print(i)
for i in range(5,50,5):
    print(i)
for i in range(3,30,3):
    print(i)'''

#task
#student grades
'''while True:
    marks=int(input("enter the marks"))
    if marks in range(91,101):
        print("Grade_A")
    elif marks in range(81,91):
        print("Grade_B")
    elif marks in range(71,81):
        print("Grade_C")
    elif marks in range(50,71):
        print("Grade_D")
    else:
        print("Fail student.......")'''


#attendence report
'''students=int(input("enter the students"))
p=0
a=0
for i in range(1,students+1):
    print(f"students status {i}")
    status=input("p and a")
    if status=="p":
        p+=1
    elif status=="a":
        a+=1
print("Attendence Report......")
print("total students",studets)
print("total prsenties",p)
print("total absenties",a)'''
        
 
#BREAK
#the break statemwnt is used to terminate the entire loop
#CONTINUE
#the continue statement is used to skip the current iteration and rest of the code will continue
#PASS
#A pass statement is a null statement its does nothing but syntaaxically we need
#BREAK
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==12:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''


#CONTINUE
'''a=15
while a>2:
    print(a)
    a=a-1
    if a==10:
        continue'''
'''a=15
while a>2:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(25):
    if i==20:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''

#PASS
'''a=30
while a>10:
    print(a)
    a=a-1
    if a==15:
        pass'''

'''for i in range(15):
    if i==8:
        pass
    print(i)'''


        

















        
