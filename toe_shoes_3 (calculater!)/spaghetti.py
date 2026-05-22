from calculater_does_some_sounds import *
from desmos_got_none_on_this import *
import math
import os
import time
import sys as sys
import ast
import operator as op
print("我哋幾時會收到作業")
print("官員我點樣攞個漢堡包")
print("我什么时候能收到任务们")
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Operatörer som stöds
operators = {
    ast.Add: op.add, 
    ast.Sub: op.sub, 
    ast.Mult: op.mul,
    ast.Div: op.truediv, 
    ast.Pow: op.pow, 
    ast.USub: op.neg,
    ast.Mod: op.mod,
    ast.FloorDiv: op.floordiv
}

# Funktioner som stöds
functions = {
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'abs': abs,
    'log': math.log10,
    'ln': math.log,
    'exp': math.exp
}


class VariableCalculator:
    """En kalkulator som stöder variabler"""
    
    def __init__(self):
        self.variables = {'ans': 0, 'pi': math.pi, 'e': math.e}
        self.history = []
    
    def evaluate(self, node, variables):
        """Evaluera en AST-nod rekursivt"""
        
        # Konstanter (tal)
        if isinstance(node, ast.Constant):
            return node.value
        
        # Variabler
        elif isinstance(node, ast.Name):
            if node.id in variables:
                return variables[node.id]
            else:
                raise ValueError(f"Okänd variabel: {node.id}")
        

        elif isinstance(node, ast.BinOp):
            left = self.evaluate(node.left, variables)
            right = self.evaluate(node.right, variables)
            return operators[type(node.op)](left, right)
        
     
        elif isinstance(node, ast.UnaryOp):
            operand = self.evaluate(node.operand, variables)
            return operators[type(node.op)](operand)
        
        # Funktionsanrop
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in functions:
                    args = [self.evaluate(arg, variables) for arg in node.args]
                    return functions[func_name](*args)
                else:
                    raise ValueError(f"Okänd funktion: {func_name}")
        
        else:
            raise TypeError(f"Stöds ej: {type(node)}")
    
    def parse_and_calculate(self, expression):
        """
        Parsera och beräkna ett uttryck.
        Stöder:
        - Vanlig matematik: 2 + 3 * 4
        - Variabler: x + 5 (om x är definierad)
        - Funktioner: sqrt(16), sin(pi/2)
        - Exponenter: 2**3
        """
        try:
            # Kontrollera om det är variabeltilldelning (x = 5)
            if '=' in expression and not any(op in expression for op in ['==', '!=', '<=', '>=']):
                parts = expression.split('=', 1)
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    if var_name.isidentifier():  # Kolla om det är ett giltigt variabelnamn
                        value = self.parse_and_calculate(parts[1].strip())
                        self.variables[var_name] = value
                        return f"Variabeln {var_name} = {value}"
            
            # Parse och evaluera uttrycket
            ast_tree = ast.parse(expression, mode='eval')
            result = self.evaluate(ast_tree.body, self.variables)
            
            # Uppdatera 'ans' med senaste resultat
            self.variables['ans'] = result
            self.history.append(f"{expression} = {result}")
            
            return result
        
        except ValueError as e:
            raise ValueError(str(e))
        except SyntaxError:
            raise SyntaxError(f"Syntax fel i uttrycket: {expression}")
        except ZeroDivisionError:
            raise ZeroDivisionError("Division med noll är inte tillåtet")
        except Exception as e:
            raise Exception(f"Fel: {e}")
    
    def show_variables(self):
        """Visa alla definierade variabler"""
        print("\n--- Definierade variabler ---")
        for var, value in self.variables.items():
            if var not in ['pi', 'e']:  # Dölj konstanter för klarhet
                print(f"  {var} = {value}")
        if len([v for v in self.variables if v not in ['pi', 'e', 'ans']]) == 0:
            print("  (Ingen användardefinierade variabler ännu)")
    
    def show_history(self):
        """Visa beräkningshistorik"""
        print("\n--- Beräkningshistorik ---")
        if not self.history:
            print("  (Ingen historik ännu)")
        else:
            for i, entry in enumerate(self.history[-10:], 1):  # Visa senaste 10
                print(f"  {i}. {entry}")


def demo():
    """Demonstrera kalkulatorn"""
    calc = VariableCalculator()
    
    print("=" * 20)
    print("VARIABELTOLKANDE KALKULATOR - DEMO")
    print("=" * 20)
    
    # Demo 1: Enkla beräkningar
    print("\n1. Enkla beräkningar:")
    expressions = [
        "2 + 3",
        "10 * 5",
        "2**3",
        "sqrt(16)",
        "sin(0)"
    ]
    for expr in expressions:
        try:
            result = calc.parse_and_calculate(expr)
            print(f"  {expr} = {result}")
        except Exception as e:
            print(f"  FEL: {e}")
    
    # Demo 2: Variabler
    print("\n2. Variabeltilldelning:")
    var_assignments = [
        "x = 5",
        "y = 3",
        "z = x + y"
    ]
    for expr in var_assignments:
        try:
            result = calc.parse_and_calculate(expr)
            print(f"  {expr} -> {result}")
        except Exception as e:
            print(f"  FEL: {e}")
    
    # Demo 3: Använda variabler
    print("\n3. Använd variabler i beräkningar:")
    calc_with_vars = [
        "x * 2 + y",
        "z ** 2",
        "ans + 10"
    ]
    for expr in calc_with_vars:
        try:
            result = calc.parse_and_calculate(expr)
            print(f"  {expr} = {result}")
        except Exception as e:
            print(f"  FEL: {e}")
    
    # Visa status
    calc.show_variables()
    calc.show_history()
    
    print("\n" + "=" * 50)

def typo():
        """Till när någon skriver fel"""
        sound("toe_shoes_3 (calculater!)\MISINPUT.mp3")
        print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒
▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░▒▒▓██████████████▓▒░░░░░░░░░░░░░░▒▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓░░░░░░░░░░░░░░▓███████████████████▓▒░░░░░░░░░░░░░▒▓█████████████████▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓██████████████▓░░░░░░░░░░░░░▒████████████████████▓▒▒░░░░░░░░░░░░░▓█████████████████████████
████████████████████████░░░░░░░░░░░░░▓▓▓█████████████▓▓▓▓▓▒▒▒░░░░░░░░░░░░░▓█████████████████████████
█████████████████████████░░░░░░░░░░▒▒▓▓████████████████████▒▒░▓▓░░░░░░░░░░██████████████████████████
██████████████████████████░░░░░░░░░▓▒████▓███████████████▓██▓░▓█▒░░░░░░░▒███████████████████████████
███████████████████████████▓▒░░░░░░█▓████████████████████████▒▒█░░░░░░▒█████████████████████████████
███████████████████████████████▒▒░░▒▒████████████████████████▓▒▓░░░░▓███████████████████████████████
████████████████████████████████████▓████████████████████████▓▒▒░░░▒████████████████████████████████
█████████████████████████████████████▓███████████████████████▒▒▒░░▒▒░▒▒▓▓███████████████████████████
█████████████████████████████████████▓█████████▒▓█▓▒████████▓▒░░▒░░▒░▒░░▒▒▒▒████████████████████████
█████████████████████████████████████▓▓██████▓█▒███▒▓▓██████▓▒▒▒░▒░▒▒░▒░░░░▓████████████████████████
██████████████████████████████████████▒▓██████▓█████████████▒░░░░▒░░▒░░▒▓███████████████████████████
██████████████████████████████████████▒▒▒▓███████████████▓▒▒░░░▒░░▒▒████████████████████████████████
███████████████████████████████████████░▒▒▒▓█▓████▓█████▓▒▒░▒░░░░░▒▒████████████████████████████████
████████████████████████████████████████░░▒▒▒██████▓▒░▒▒▒▒░░░░░▓█▒░░░░░░░░░░░░░░░░░█████████████████
██████████████████████████████████████▒▒▒▒▒░▓██████▓▒░░░░░░░▒▒██▒░░░░░░░░░░░░░░░░░░░░░▒█████████████
███████████████████████████████▓░░░░░░░▓██▒░▓██████▓█▒░░░▒░▒███░░░░░░░░░░░░░░░░░░░░░░░░▓████████████
█████████████████████▒░░░░░░░░░░░░░░░░░▒████▓███████▓█▒░░░▓██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░███████████
██████████████████░░░░░░░░░░░░░░░░░░░░░░▓████████████▒█░░▒█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████
████████████████▒░░░░░░░░░░░░░░░░░░░░░░░░▓██████████▓█▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒███████
██████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████████▓██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓
█████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▓████████▓█▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒
████████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓███████████▒█▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
███████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓██▓▓██▒▓██▒▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▒▓▓▓▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
█████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░▒▒░░░░▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
███████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░▒▒░░▒▒░░░░░░░░░░░▓▒░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒▒▓░░░░▒▒░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▓▓▓▓▓▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒░▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▓▓▓▓▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒▒▒▒██▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
history = []

# --- Interaktiv Kalkylator (SMASKIG!) ---
def interactive_calculator():
    """Den smaskiga och interaktiva kalkylatorn!"""
    calc = VariableCalculator()
    
    while True:
        clear_terminal()
        
        print("INTERAKTIV VARIABELTOLK")
        
        # Visa nuvarande variabler
        print("NUVARANDE VARIABLER:")
        user_vars = {k: v for k, v in calc.variables.items() if k not in ['pi', 'e', 'ans']}
        if user_vars:
            for var, val in user_vars.items():
                print(f"   • {var:12} = {val}")
        else:
            print("   (Ingen användarvariabler ännu)")
        print()
        
        # Visa senaste resultat
        if calc.history:
            print("SENASTE RESULTAT:")
            for entry in calc.history[-3:]:
                print(f"   ✓ {entry}")
        else:
            print("SENASTE RESULTAT: (Ingen beräkningar än)")
        print()
        
        # Kommandomenyn
        print("━" * 60)
        print("KOMMANDON:")
        print("   [beräkning]  - Skriv en matematisk beräkning")
        print("   [var=värde]  - Definiera en variabel")
        print("   'help'       - Visa hjälp")
        print("   'vars'       - Visa alla variabler")
        print("   'history'    - Visa full historik")
        print("   'clear'      - Rensa historik")
        print("   'demo'       - Se demonstrationskod")
        print("   'quit'       - Avsluta kalkylatorn")
        print("━" * 60)
        print()
        
        # Ta emot inmatning
        user_input = input("Vad vill du beräkna?").strip()
        
        # Kontrollera speciella kommandon
        if user_input.lower() == 'quit':
            print("\n Vi ses senare, du smaskiga matematiker!")
            time.sleep(1)
            break
        
        elif user_input.lower() == 'help':
            print("""
╔═══════════════════════════════════════════════════════════╗
║ OPERATÖRER OCH FUNKTIONER FRÅN SODEXO KITCHEN             ║
╠═══════════════════════════════════════════════════════════╣
║ +, -, *, / (addition, subtraktion, multiplikation, div)   ║
║ **           (exponenter, t.ex. 2**3 = 8)                 ║
║ %            (modulo, t.ex. 10 % 3 = 1)                   ║
║ //           (heltalsdivision)                            ║
║                                                           ║
║ FUNKTIONER:                                               ║
║ sqrt(x)   - Kvadratrot      ln(x)   - Naturlig logaritm   ║
║ sin(x)    - Sinus           log(x)  - 10-logaritm         ║
║ cos(x)    - Cosinus         exp(x)  - e upphöjt till x    ║
║ tan(x)    - Tangens         abs(x)  - Absolutvärde        ║
║                                                           ║
║ KONSTANTER: pi, e, ans (senaste resultat)                 ║
║                                                           ║
║ EXEMPEL:                                                  ║
║ • 2 + 2 * 3                                               ║
║ • sqrt(16)                                                ║
║ • x = 5                                                   ║
║ • x ** 2 + 10                                             ║
║ • sin(pi/2)                                               ║
╚═══════════════════════════════════════════════════════════╝
            """)
            input("Tryck Enter för att fortsätta...")
        
        elif user_input.lower() == 'vars':
            calc.show_variables()
            input("\nTryck Enter för att fortsätta...")
        
        elif user_input.lower() == 'history':
            calc.show_history()
            input("\nTryck Enter för att fortsätta...")
        
        elif user_input.lower() == 'clear':
            calc.history = []
            print("Historiken är rensad!")
            time.sleep(1)
        
        elif user_input.lower() == 'demo':
            demo()
            input("\nTryck Enter för att fortsätta...")
        
        elif user_input == '':
            typo()
            time.sleep(10)
        
        else:
            # Försök beräkna uttrycket
            try:
                result = calc.parse_and_calculate(user_input)
                print()
                
                print(f" RESULTAT: {str(result):^34}")
                
                print()
                print(f" Sparat i 'ans' = {result}")
            except ValueError as e:
                typo()
                print(f" VÄRDEFEL: {e}")
            except SyntaxError as e:
                typo()
                print(f" SYNTAXFEL: {e}")
            except ZeroDivisionError as e:
                typo()
                print(f" DELNINGSFEL: {e}")
            except Exception as e:
                typo()
                print(f" FEL: {e}")
            
            input("\nTryck Enter för att fortsätta...")

# --- Huvudprogram ---
def kalkylator():

    while True:
        clear_terminal()
        backgroundmusic("toe_shoes_3 (calculater!)\MUSIC.mp3")
        # Ta emot användarinmatning för det är typ koolt
        # time.sleep(5)
        print("Välj operation:")
        print("-" * 20)
        print("1. Teckentolkande + Variabeltolkande calculette")
        print("-" * 20)
        print("2. Grafritande Verktyg")
        print("-" * 20)
        print("3. 3 Dimensionell grafritare (REKOMMENDERAR INTE)")
        print("-" * 20)
        print("4. Se Demo för Variabeltolk")
        print("-" * 20)
        print("Du kan använda ans för senaste svaret")
        print("-" * 20)
        print("q. Om du vill avsluta kalkylatorn")
        print("-" * 20) # Separator för tydlighet
        print("Nedan visas din kalkulator historik:")
        print("-" * 20)
        print(history) # jag visar historiken freak & freakier
        print("-" * 20)
        val = input("Ange val från åvan\n GÖR DET NU ")

        # Kontrollera om användaren vill avsluta
        if val.lower() == 'q':
            print("Avslutar kalkylatorn.")
            break

        # Kontrollera om valet är giltigt
        if val in ("1"):
            interactive_calculator()
            

        elif val in ("2"):
             typo()
             time.sleep(2)
             clear_terminal()
        elif val in ("3"):
             chipset()
        elif val in ("4"):
            demo()
             
        else:
            clear_terminal()
            typo()
            time.sleep(5)
            clear_terminal()
            print("Ogiltigt val, försök igen.")
            time.sleep(2)

# Kör kalkylatorn
if __name__ == "__main__":
    kalkylator()
