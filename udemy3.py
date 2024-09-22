#conditional statements in python

#take input from user and cheak the number is odd ar even

num=int(input("please enter a number:-\n"))

if num%2==0:
    print("number is even:", num)
else:
    print("number is odd:",num)  

#using multiple if else statement try to create BMI 2.0
height=float(input('please enter your height in metre:'))
weight=float(input("please enter your weight in kg:"))  
BMI=weight/height**2
if BMI<18.5:
    print("you are underweight")
elif BMI<=24.9:
    print("you have a healthy weight range")   
elif BMI<=30:
    print("you are overweight")
else:
    print('you are obses')         

#try to find out the entered year by user is leap or not
year=int(input("please enter a year "))
if year%4>=1:
    print('this is not a leap year')
    if year%100==0:
        print("this is not a leap year")  
        if year%400>=1:
            print('this is not a leap year')
else:
    print("This is  a leap year")

#using multiple if else statement try to make an automatic pizza delivery program

print("Thank you for choosing Python Pizza delivery")
pizza_size=input('what size of pizza you want? s,m or l\n')
add_pepperoni=input("do you want to add pepparoni on it? y or n\n")
extra_cheese=input('you want to add extra chees:\n')
bill=0
if pizza_size=="s":
    bill+=200
elif pizza_size=="m":
    bill+=350
elif pizza_size=="l":
    bill+=500
if add_pepperoni=="y":
    if pizza_size=="s":
        bill+=50
    else:
        bill+=100
if extra_cheese=="y":
    bill+=50
print(f"you bill is{bill}")

