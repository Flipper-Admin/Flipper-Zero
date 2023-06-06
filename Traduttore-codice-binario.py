import random

def text_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    binary = binary.replace(" ", "")
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def generate_random_binary_string(length):
    binary = ''.join(random.choice(['0', '1']) for _ in range(length))
    return binary

print("[1] Converti testo in binario")
print("[2] Converti binario in testo")
print("[3] Genera una stringa casuale di codice binario")

choice = input("Seleziona un'opzione: ")

if choice == "1":
    text = input("Inserisci il testo da convertire in binario: ")
    binary = text_to_binary(text)
    print("Codice binario:", binary)
elif choice == "2":
    binary = input("Inserisci il codice binario da convertire in testo: ")
    text = binary_to_text(binary)
    print("Testo:", text)
elif choice == "3":
    length = int(input("Inserisci la lunghezza della stringa binaria casuale: "))
    binary = generate_random_binary_string(length)
    print("Stringa casuale di codice binario:", binary)
else:
    print("Opzione non valida. Riprova.")
