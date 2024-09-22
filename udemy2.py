#data types in python
# we have four types of data in python like integer,float,boolean and string.

#write a program that adds a digit in a two digit number.

two_digit_number=input("please enter any two digit number\n")

digit1=int(two_digit_number[0])
digit2=int(two_digit_number[1])

print("the required output is",digit1+digit2)

#building body mass calculator

height=int(input("please enter your height in meter:-"))
weight=int(input("please enter your weighgt in kg:-"))
 #BMI=(int(weight)/int(height)*int(height))
BMI=(weight/height**2)
print(BMI)

#calculatinn how many weeks you have left
age=input("please enter your age:-")
rem=90-int(age)
rem=rem*52
print(f"you have {rem} weeks left ")
