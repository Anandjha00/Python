print("welcome to the tip calculator")
bill=input("what was the total bill:-\n₹")
bill=float(bill)
tip=input("how much tip you like to give? 10,12,0r 15\n")
tip=int(tip)
tpeople=input("how much people to split the bill?\n")
tpeople=int(tpeople)
totaltip=bill*((tip)/100)
totalbill=bill+totaltip
fbill=totalbill/tpeople
print(f"each person should pay:- {round(fbill,2)}")