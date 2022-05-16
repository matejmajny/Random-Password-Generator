from colorama import *
import random
import pyperclip
init()
def shuffle(chars):
    return ''.join(random.sample(chars, len(chars)))
print(Fore.RED)
long = input("How many characters do you want your password to be? ")
symbols = input("Do you want special characters? ")
numbers = input("Do you want numbers? ")
capital = input("Do you want capital letters? ")
print("\n\n")


letters = shuffle("qwertyuiopasdfghjklzxcvbnm")

#capitals
if capital == "yes":
    capital_letters = shuffle("QWERTYUIOPASDFGHJKLZXCVBNM")
else:
    capital_letters = ""

#special
if symbols == "yes":
    special = shuffle("!@#$%^&*()_+{}[]<>?/|")
else:
    special = ""

#numbers
if numbers == "yes":
    numbers1 = shuffle("1234567890")
else:
    numbers1 = ""

long = int(long)
final = shuffle(capital_letters + special + numbers1 + letters)

print(Fore.GREEN + "Your generated password is: " + final + Fore.BLUE)
copy = input("Do you want copy your password? ")

if copy == "yes":
    pyperclip.copy(final)

print("\n\n" + Fore.RED)
input("Push ENTER for exit...")
