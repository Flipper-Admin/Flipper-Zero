print("""
######################################################################################################
# Title: Flipper-zero-3.0                                                                            #
# YouTube:                                                                                           #
# Site web: localhost:8000                                                                           #
######################################################################################################

""")

print("""

 ██████  █     █  ████    ████   ██████  █████
 █       █        █   ██  █   █  █       █    █
 ██████  █     █  ████    ████   ██████  █████
 █       █     █  █       █      █       █    █
 █       ████  █  █       █      ██████  █     █
 
                   DISCORD:
                FlipperZero#3552
     
""")

import random

def generate_random_numbers():
    for i in range(1, 8):
        numbers = [random.randint(1, 100) for _ in range(10)]  # Genera 10 numeri casuali da 1 a 100
        filename = f"file_{i}.txt"
        with open(filename, "w") as file:
            file.write("\n".join(str(num) for num in numbers))
        print(f"Codici di accesso {filename} : {', '.join(str(num) for num in numbers)}")

if __name__ == "__main__":
    generate_random_numbers()
    
import random

def generate_random_code():
    code = random.randint(1000, 9999)  # Genera un codice casuale a 4 cifre
    return code

def show_password_option():
    code = generate_random_code()
    print(f"443BFJK94586LSJF8846 {code}")

def show_privacy_option():
    code = generate_random_code()
    print(f"Ogni codice di accesso inviato e totalmente random nessuno puo vedere i dati di accesso nemmeno il tool {code}")

def show_help_option():
    code = generate_random_code()
    print(f"Una volta aperto il tool eseguendo il comando python Flipper_zero.py si puo vedere dei file contenenti dei codici e aprendo il nostro sito e inserendololi piu la password privata cioe l'opzione [1] rispettando gli spazi potrai accedere al tua account Flipper-Membro {code}")

def show_about_option():
    code = generate_random_code()
    print(f"Questo tool e stato creato per un nostro sito dove poblicheremo ogni aggiornamento del nostro nuovo progetto acnhe del nostro tool ci saranno modifiche  {code}")

if __name__ == "__main__":
    options = {
        "1": show_password_option,
        "2": show_privacy_option,
        "3": show_help_option,
        "4": show_about_option
    }

    print("[1] Password")
    print("[2] Privacy")
    print("[3] Help")
    print("[4] About")

    option = input("type: ")
    if option in options:
        options[option]()
    else:
        print("Opzione non valida")

