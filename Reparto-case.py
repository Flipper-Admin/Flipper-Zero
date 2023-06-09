import pyfiglet
import random

def print_large_text(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

def generate_random_code():
    code = random.randint(1000, 9999) # Genera un codice casuale a 4 cifre
    return code

def show_novità_option():
    code  = generate_random_code()
    print(f"Per adesso nessuna novità. {code}")

def show_compiti_option():
    code = generate_random_code()
    print(f"Le cose da fare Lunedì saranno scritte. {code}")

def show_versioni_option():
    code = generate_random_code()
    print(f"V1.0 - 09/06/2023. {code}")

if __name__ == "__main__":
    print_large_text("Flipper-Reparto-Case")
    ("""
    
                   Discord
                FlipperZero#3552
    
    """)
    
    options = {
        "1": show_novità_option,
        "2": show_compiti_option,
        "3": show_versioni_option
    }
    
    print("[1] Novità")
    print("[2] Cose da fare")
    print("[3] Versioni")
    
    option = input("type: ")
    
    if option in options:
        options[option]()
    else:
        print("Opzione non valida")
