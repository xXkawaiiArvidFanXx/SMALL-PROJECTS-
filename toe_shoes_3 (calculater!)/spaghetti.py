print("我哋幾時會收到作業")
print("官員我點樣攞個漢堡包")
print("我什么时候能收到任务们")
import math
import os
import sys
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def typo():
        """Till när någon skriver fel"""
        print(
)



history = []
svar=0
# --- Funktioner för beräkningar ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Fel! Division med noll.\n GÖR OM GÖR RÄTT"
    return x / y


# --- Huvudprogram ---
def kalkylator():
    print("Välj operation:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")
    print("Du kan använda ans för senaste svaret")
    print("q. Om du vill avsluta kalkylatorn")
    print("-" * 20) # Separator för tydlighet
    print("Nedan visas din kalkulator historik:")
    print(history) # jag visar historiken freak & freakier


    while True:
        # Ta emot användarinmatning för det är typ koolt
        val = input("Ange val från åvan\n GÖR DET NU ")

        # Kontrollera om användaren vill avsluta
        if val.lower() == 'q':
            print("Avslutar kalkylatorn.")
            break

        # Kontrollera om valet är giltigt
        if val in ('1', '2', '3', '4'):
            try:
            
            
                num1_input = input("Ange första numret: ")
                num2_input = input("Ange andra numret: ")
                def parse_input(inp):
                        inp = inp.strip()
                        if inp.lower().startswith('ans'):
                                index = -1
                        
                                try:
                                    index = int(inp[3:])  
                                except ValueError:
                                    raise ValueError("Ogiltig format")
                                if not history:
                                    raise ValueError("Inga tidigare svar")
                                if index < 0:
                                    return history[-1] 
                                elif index < len(history):
                                    return history[index]
                                else:
                                    raise ValueError("Index utanför range")
                        else:
                            return float(inp)
                num1 = parse_input(num1_input)
                num2 = parse_input(num2_input)
            except ValueError as e:
                print(f"FEL!!!!!!!!!: {e}")
                continue

            if val == '1':
                print(f"Resultat: {num1} + {num2} = {add(num1, num2)}")
                svar = num1+num2
            elif val == '2':
                print(f"Resultat: {num1} - {num2} = {subtract(num1, num2)}")
                svar = num1 - num2
            elif val == '3':
                print(f"Resultat: {num1} * {num2} = {multiply(num1, num2)}")
                svar = num1 * num2
            elif val == '4':
                print(f"Resultat: {num1} / {num2} = {divide(num1, num2)}")
                svar = num1 / num2

            # HÄR LÄGGER VI TILL HISTORIA I VÄRLDN
            history.append(svar)
            print("-" * 20) # Separator för tydlighet
            print(history) # jag visar historiken yaoi och yuri
        else:
            print("Ogiltigt val, försök igen.")

# Kör kalkylatorn
if __name__ == "__main__":
    kalkylator()
