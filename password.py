#Password Generator Project
import random
# password will be generatored from these list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#prompts the user to input number of items they would want in their password
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#creats a list to store the random items picked
password = []

#for each number the user inputed we want to pick random items in that range
for i in range(1, nr_letters + 1):
  letter = random.choice(letters)
  password += letter
for num in range(1, nr_numbers + 1):
  number = random.choice(numbers)
  password += number
for sym in range(1, nr_symbols + 1):
  symbol = random.choice(symbols)
  password += symbol

#To make it hard to crack the password we want to suffle the password
#using the suffle function
random.shuffle(password)

#We have to store the suffled password in as string variable
#so the password gets printed as astring and not a list
password_str = ""
for char in password:
  password_str += char
print(password_str)
