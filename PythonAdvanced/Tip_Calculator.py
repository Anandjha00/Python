print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tin_in_dollar=bill*tip/100
new_bill=tin_in_dollar+bill
each_person_bill=new_bill/people
print(f"Each person should pay{round(each_person_bill,2)}")


