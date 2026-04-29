"""
Projekt 1: Personlig citatbank
Ett menybaserat program för att hantera citat med filhantering.
"""

import random
import json

def ladda_citat_fran_fil(filnamn):
    """
    Laddar citat från en textfil.
    
    Parametrar:
        filnamn (str): Namnet på filen att läsa från
    
    Returnerar:
        list: En lista med alla citat (varje rad är ett citat)
              Returnerar tom lista om filen inte finns.
    """
    f = open(filnamn, "r", encoding="utf8")
    citat_dikt = json.load(f)
    print(citat_dikt[0])
    f.close()
    return citat_dikt


def spara_citat_till_fil(citatlista, filnamn):
    """
    Sparar alla citat till en textfil.
    
    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    with open(filnamn, "w", encoding="utf8") as f:
        json.dump(citatlista, f, ensure_ascii=False, indent=4)


def visa_alla_citat(citatlista):
    """
    Skriver ut alla citat med numrering.
    
    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """
    if not citatlista:
        print("Inga citat att visa.")
        return
    for i, citat in enumerate(citatlista, 1):
        print(f"{i}. {citat['citat']} - {citat['person']}")


def lagg_till_citat(citatlista, filnamn):
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.
    
    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i
    
    Returnerar:
        bool: True om citatet lades till, False annars
    """
    nytt_citat = input("Ge mig ditt citat!! ")
    författare = input("Vem är författaren!!!! ")
    if nytt_citat and författare:
        citatlista.append({"person": författare, "citat": nytt_citat})
        spara_citat_till_fil(citatlista, filnamn)
        print("Citat tillagt!")
        return True
    else:
        print("Citat eller författare kan inte vara tom.")
        return False


def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.
    
    Parametrar:
        citatlista (list): Listan att välja citat från
    """
    if not citatlista:
        print("Inga citat att slumpa från.")
        return
    slumpat = random.choice(citatlista)
    print(f"Slumpat citat: {slumpat['citat']} - {slumpat['person']}")


def huvudprogram(filnamn):
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # Ladda befintliga citat
    citatlista = ladda_citat_fran_fil(filnamn)
    
    menu_active = True
    while menu_active:
        print("\nMeny:")
        print("1. Lägg till ett citat")
        print("2. Visa alla citat")
        print("3. Slumpa ett citat")
        print("4. Spara citat till fil")
        print("5. Avsluta")
        choice = input("Välj ett alternativ: ")
        
        if choice == "1":
            lagg_till_citat(citatlista, filnamn)
        elif choice == "2":
            visa_alla_citat(citatlista)
        elif choice == "3":
            slumpa_citat(citatlista)
        elif choice == "4":
            spara_citat_till_fil(citatlista, filnamn)
            print("Citat sparade till fil.")
        elif choice == "5":
            print("Avslutar programmet.")
            menu_active = False
        else:
            print("Ogiltigt val, försök igen.")


        
    
    # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
    # 5. Vid val 4: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram("data.json")

