from os import environ
import pygame
import warnings
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #Tar bort massa onödig info text
# cred till våning 1 på åva, super goated devs, speciellt alla 3
warnings.filterwarnings("ignore", message="pkg_resources is deprecated*", category=UserWarning) #Tar bort massa onödig info text
def backgroundmusic(filväg):
    """Spelar en bakgrundsmusik. Skicka in sökvägen till filen som en sträng.
    Exempel: backgroundmusic("ljud/bakgrundsmusik.wav")"""
    pygame.mixer.init()
    pygame.mixer.music.load(filväg)
    pygame.mixer.music.play(-1)  # Spela i loop


def sound(filväg):
    """Spelar en ljudfil. Skicka in sökvägen till filen som en sträng.
    Exempel: sound("ljud/kiosken.wav")"""
    pygame.init()
    
    try:
        ljud = pygame.mixer.Sound(filväg)  #Deklarerar "ljud" som ljud filen
        ljud.play()                         #Spelar Ljudet
        
        while pygame.mixer.get_busy(): #Pausar programet medans Ljud spelas
            pygame.time.Clock().tick(10) #Gör loppen långsammare (Snällare mot datorn)
    except Exception as e:                      #hanterar om ljudet inte finns
        print(f"Kunde inte spela ljud: {e}")


def stopmusic():
    """Stoppar bakgrundsmusiken som spelas."""
    pygame.mixer.music.stop()