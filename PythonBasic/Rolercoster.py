print(f"This is python rolercoster program!\nJust give answers of some simple questions ,then you will able to ride on it !")

print("\n\n\nwelcome  to our Roler coster ride!.")
height=int(input("Please enter your height in cm: "))
bill=0

if height>=120:
    print("You can ride !")
    age=int(input("Please enter your age :"))
    if age<12:
        bill=+5
    elif age<18 :
        bill=+7
    else:
        bill=+12
    photo=input("Do you want to take photo 'Y' or 'N': ")
    if photo=="Y":
       bill+=1
    elif photo=="N":
        bill=bill
    else:
        print(f"invalid input! you can't take photo .")

    print(f"your total bill is: ${bill}.\nEnjoy The Ride!")                       
else :
    print("you can't ride !")
