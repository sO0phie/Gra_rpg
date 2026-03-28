from funkcje import akcja as ak
from funkcje import statystyki as s
import time

print("Czas rozpocząć nową historię...")
time.sleep(1)
s.imie = input("Imię bohatera, który przejdzie do historii: ")

print("Udowodnij, że jesteś godzien tytułu bohatera! Przejdz poziom wstępny")
time.sleep(2)
ak.test()

s.klasa = input(f"Dobrze, a zatem {s.imie}, wybierz swoją ścieżkę: rycerza, łucznika czy czarodzieja ")

if s.klasa == "rycerz":
    s.miecz.append("drewniany")
    s.miecz.append(2)
    print(f'Jako nagrodę dostajesz {s.miecz[0]} miecz')

if s.klasa == "łucznik":
    s.luk.append("zwykły")
    s.luk.append(3)
    print(f'Jako nagrodę dostajesz {s.luk[0]} łuk')

if s.klasa == "czarodziej":
    s.ksiega_zaklec.append("początkującą")
    s.ksiega_zaklec.append(2)
    print(f'Jako nagrodę dostajesz {s.ksiega_zaklec[0]} księgę zaklęć')

while True:
    print("---"*20)
    if len(s.inventory) != 0:
        print("Możesz coś sprzedać!")
    if len(s.miecz) != 0:
        miejsce:input = input("Gdzie chcesz pójść? Do wyboru masz: miasto, pole bitwy, miejsce treningu ")
    elif len(s.luk) != 0:
        miejsce:input = input("Gdzie chcesz pójść? Do wyboru masz: miasto, pole bitwy, strzelnica ")
    elif len(s.ksiega_zaklec) != 0:
        miejsce:input = input("Gdzie chcesz pójść? Do wyboru masz: miasto, pole bitwy, biblioteka ")
    ak.kierunek(miejsce)
    if s.postac[0] <= 0:
        break
