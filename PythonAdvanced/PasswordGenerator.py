import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Time fo easy Level!

password=""

for new in range(0,nr_numbers):
    password=password+random.choice(letters)

for new in range(0, nr_numbers):
    password = password + random.choice(numbers)

for new in range(0, nr_numbers):
    password = password + random.choice(symbols)
#simple version of password
print("your simple password is ",password)

#Try to the harder version of it.The letters ,symbols and digits should be mixed randomly

#Try to write this code seperately!

password_list=list(password)
#print(password_list)
random.shuffle(password_list)
#print(password_list)
new_password=''.join(password_list)
print(f"Your very strong password is {new_password}")
