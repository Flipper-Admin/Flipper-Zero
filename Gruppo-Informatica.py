import pyfiglet
def print_large_text(text):
  ascii_art = pyfliget.figlet_format(text)
  print(ascii_art)
print_lage_text("Flipper-Reparto-Informatica")

print("""

                   Discord
                FlipperZero#3552

""")
import random
def generate_random_code():
  code = random.randint(1000, 9999) # Genera un codice casuale a 4 cifre
  return code
def show_novità_option():
  code  = generate_random_code()
  print(f"Per adesso nessuna novià {code}")
 def show_cosedafare_option():
   code = generate_random_code()
   print(f"Le cose da fare Lunedi sarà scritto {code}")
 def show_versioni_option():
   code = generate_random_code()
   print(f"V1.0 09/06/2023 {code}")
 
if __name__ == "__main__":
  options = {
    "1" show_novità_option,
    "2" show_cosedafare_options,
    "3" show_versioni_options
    }
print("[1] Novità")
print("[2] Cose da fare")
print("[3] Versioni")
option = imput ("type: ")
if option in options:
  options[option]()
  else:
    print("Opzione non valida")
