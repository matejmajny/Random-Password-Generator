import string_utils, os, pyperclip, random
from colorama import *
init()

idk = "yes"

while idk == "yes":
    print(Fore.RESET + "")
    long = input("How long should your password be? ")
    symbols = input("Do you want special symobls?")
    numbers = input("Do you want numbers? ")
    capital = input("Do you want capital letters? ")
    print("\n\n")


    letters = string_utils.shuffle("qwertyuiopasdfghjklzxcvbnm")

    #capitals
    if capital == "yes":
        capital_letters = string_utils.shuffle("QWERTYUIOPASDFGHJKLZXCVBNM")
    else:
        capital_letters = ""

    #special
    if symbols == "yes":
        special = string_utils.shuffle("&@&{Łßß÷")
    else:
        special = ""

    #numbers
    if numbers == "yes":
        numbers1 = string_utils.shuffle("1234567890")
    else:
        numbers1 = ""

    long = int(long)
    final = string_utils.shuffle(capital_letters + special + numbers1 + letters)
    final = final[:long]

    print(Fore.GREEN + "Your generated password is: " + final + Fore.BLUE)
    copy = input("Do you want copy your password? ")

    if copy == "yes":
        pyperclip.copy(final)

    #repeat system
    print(Fore.CYAN + "")
    idk = input("\nDo you want to repeat? ")
    
    if idk == "yes":
        os.system('cls') #windows
        os.system('clear') #linux

print("\n\n" + Fore.RED)
input("Push ENTER for exit...")