import random
import string

def print_large_text(text):
    print(text)

print_large_text("""
######################################################################################################
# Title: Flipper-zero-3.0                                                                            #
# YouTube:                                                                                           #
# Site web: localhost:8000                                                                           #
######################################################################################################
""")

print_large_text("V3.0")

def generate_random_numbers():
    for i in range(1, 8):
        numbers = [random.randint(1, 100) for _ in range(10)]  # Genera 10 numeri casuali da 1 a 100
        filename = f"file_{i}.txt"
        with open(filename, "w") as file:
            file.write("\n".join(str(num) for num in numbers))

generate_random_numbers()


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
    print(f"Questo tool e stato creato per un nostro sito dove pubblicheremo ogni aggiornamento del nostro nuovo progetto anche del nostro tool. Ci saranno modifiche {code}")

def show_account_option():
    code = generate_random_code()
    print(f"""
    
    Name: Kaliadmin
    
    Username: Kaliadmin
    
    Password: ********
    
    code access: ****-****-****-****
     
    email: **************@gmail.com
          
      {code}""")

def generate_account_password():
    print("Seleziona un'opzione:")
    print("[1] Genera solo account")
    print("[2] Genera solo password")
    print("[3] Genera account e password")
    print("[4] Genera password personalizzata")
    print("[5] Genera password casuale")
    print("[6] Esci")

    while True:
        choice = input("type: ")

        if choice == "1":
            account = generate_account()
            print(f"Account generato: {account}@gmail.com")
        elif choice == "2":
            password = generate_password()
            print(f"Password generata: {password}")
        elif choice == "3":
            account = generate_account()
            password = generate_password()
            print(f"Account generato: {account}@gmail.com")
            print(f"Password generata: {password}")
        elif choice == "4":
            custom_password = input("Inserisci la password personalizzata: ")
            print(f"Password generata: {custom_password}")
        elif choice == "5":
            length = int(input("Inserisci la lunghezza della password casuale: "))
            password = generate_random_password(length)
            print(f"Password generata: {password}")
        elif choice == "6":
            break
        else:
            print("Scelta non valida. Riprova.")

def generate_account():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    password_chars = random.choices(letters + digits + special_chars, k=10)
    random.shuffle(password_chars)
    password = ''.join(password_chars)

    return password

def generate_random_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password_chars = random.choices(chars, k=length)
    password = ''.join(password_chars)

    return password

def generate_binary_sentence():
    words = ["hello", "world", "python", "code", "binary", "programming"]
    sentence = " ".join(random.choice(words) for _ in range(random.randint(3, 6)))
    binary_code = ' '.join(format(ord(char), '08b') for char in sentence)
    return sentence, binary_code

def generate_random_binary_sentences(num_sentences):
    for _ in range(num_sentences):
        sentence, binary_code = generate_binary_sentence()
        print(f"Codice binario: {binary_code}")
        print()

if __name__ == "__main__":
    while True:
        print("[1] Password")
        print("[2] Privacy")
        print("[3] Help")
        print("[4] About")
        print("[5] Account")
        print("[6] Exit")

        option = input("type: ")
        if option == "1":
            show_password_option()
        elif option == "2":
            show_privacy_option()
        elif option == "3":
            show_help_option()
        elif option == "4":
            show_about_option()
        elif option == "5":
            show_account_option()
        elif option == "6":
            break
        else:
            print("Opzione non valida")

    generate_account_password()
    generate_random_binary_sentences(5)
