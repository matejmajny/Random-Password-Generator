import os, pyperclip, random
from colorama import *
init()

idk = "yes"
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
def shuffle(str):
    str = list(str)
    random.shuffle(str)
    return ''.join(str)
while idk == "yes":
    print(Fore.YELLOW + "")
    long = input("How many characters should your password be? (Y/n) ")
    symbols = input("Do you want special symobls? (Y/n) ")
    numbers = input("Do you want numbers? (Y/n) ")
    capital = input("Do you want capital letters? (Y/n) ")
    print("\n\n")
    symbols = symbols.lower()
    numbers = numbers.lower()
    capital = capital.lower()


    letters = shuffle("qwertyuiopasdfghjklzxcvbnm")

    #capitals
    if capital == "yes" or capital == "y" or capital == "":
        capital_letters = shuffle("QWERTYUIOPASDFGHJKLZXCVBNM")
    else:
        capital_letters = ""

    #special
    if symbols == "yes" or symbols == "y" or symbols == "":
        special = shuffle("!@#$%^&*()_+")
    else:
        special = ""

    #numbers
    if numbers == "yes" or numbers == "y" or numbers == "":
        numbers1 = shuffle("1234567890")
    else:
        numbers1 = ""

    long = int(long)
    final = shuffle(capital_letters + special + numbers1 + letters)
    final = final[:long]

    print(Fore.GREEN + "Your generated password is: " + final + Fore.BLUE)
    copy = input("Do you want copy your password? ")

    if copy == "yes":
        pyperclip.copy(final)

    #repeat system
    print(Fore.CYAN + "")
    idk = input("\nDo you want to generate another? ")
    
    if idk == "yes":
        clearConsole()

print("\n\n" + Fore.RED)
input("Push ENTER for exit...")