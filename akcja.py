from . import statystyki as s
import time
from typing import List
import random

def test() -> None:
    print("-"*50)
    while True:
        if s.wrog_test[0] > 0:
            if s.postac[0] > 0:
                s.wrog_test[0] -= s.postac[1]
                print(f'Zadajesz {s.atak} obrażenia, Hp twojego przeciwnika: {s.wrog_test[0]}')
                time.sleep(1.5)
                s.postac[0] -= s.wrog_test[1]
                print(f'Przeciwnik zadaje {s.at_wrog_poczatek} obrażenia, twoje Hp: {s.postac[0]}')
                time.sleep(1.5)
            else:
                return print("Musisz jeszcze poćwiczyć")
        else:
            print("Jesteś gotowy do dalszych walk!")
            s.postac[0] = s.HP
            s.inventory.append("złoty medalion")
            return print("-"*50)

def manekin_treningowy() -> List:
    trening = []
    trening_hp = random.randint(5, 15)
    trening.append(trening_hp)
    return trening

def super_przeciwnik() -> List:
    boss = []
    hp_boss = random.randint(30, 50)
    at_boss = random.randint(10, 20)
    boss.append(hp_boss)
    boss.append(at_boss)
    return boss

def super_walka() -> None:
    boss = super_przeciwnik()
    print("Uwaga, nadchodzi coś grozniego! Szykuj się na dłuższą walkę!")
    time.sleep(2)
    print(f"Twój przeciwnik: HP: {boss[0]}, ATK: {boss[1]}")
    while True:
        if s.postac[0] > 0:
            if boss[0] <= 0:
                print(f"Gratulacje {s.imie}! Pokonałeś niebezpiecznego przeciwnika")
                s.postac[0] = s.HP
                s.pieniadze += random.randint(10, 20)
                for _ in range(3):
                    s.inventory.append(s.nagrody[random.randint(0, 5)])
                s.pokonanych -= 10
                return print(f"Twój obecny stan to {s.pieniadze} monet")
            else:
                x = random.randint(1, 3)
                if x == 1:
                    s.postac[0] -= boss[1]
                    print(f'Przeciwnik zadaje {boss[1]} obrażenia, twoje Hp: {s.postac[0]}')
                    time.sleep(1.5)
                elif x == 2:
                    at_1 = random.randint(5, 10)
                    s.postac[0] -= at_1
                    print(f'Przeciwnik zadaje {at_1} obrażenia, twoje Hp: {s.postac[0]}')
                    time.sleep(1.5)
                else:
                    at_2 = random.randint(1, 5)
                    s.postac[0] -= at_2
                    print(f'Przeciwnik zadaje {at_2} obrażenia, twoje Hp: {s.postac[0]}')
                    time.sleep(1.5)
                
                if s.klasa == "rycerz":
                    boss[0] -= s.miecz[1]
                    print(f'Zadajesz {s.miecz[1]} obrażenia, Hp twojego przeciwnika: {boss[0]}')
                    time.sleep(1.5)
                elif s.klasa == "łucznik":
                    boss[0] -= s.luk[1]
                    print(f'Zadajesz {s.luk[1]} obrażenia, Hp twojego przeciwnika: {boss[0]}')
                    time.sleep(1.5)
                else:
                    boss[0] -= s.ksiega_zaklec[1]
                    print(f'Zadajesz {s.ksiega_zaklec[1]} obrażenia, Hp twojego przeciwnika: {boss[0]}')
                    time.sleep(1.5)
        else:
            return print("Zostałeś pokonany!")

def wrogowie() -> List:
    wrog = []
    hp_wrog = random.randint(10, 20)
    at_wrog = random.randint(5, 10)
    wrog.append(hp_wrog)
    wrog.append(at_wrog)
    return wrog

def walka() -> None:
    if s.pokonanych != 10:
        wrog = wrogowie()
        print(f'Przeciwnik: HP {wrog[0]}, atak {wrog[1]}')
        inp = input("Rozpocząć walkę? ")
        if inp == "tak":
            print("-"*50)
            while True:
                if wrog[0] > 0:
                    if s.postac[0] > 0:
                        s.postac[0] -= wrog[1]
                        print(f'Przeciwnik zadaje {wrog[1]} obrażenia, twoje Hp: {s.postac[0]}')
                        time.sleep(1.5)
                        if s.klasa == "rycerz":
                            wrog[0] -= s.miecz[1]
                            print(f'Zadajesz {s.miecz[1]} obrażenia, Hp twojego przeciwnika: {wrog[0]}')
                            time.sleep(1.5)
                        elif s.klasa == "łucznik":
                            wrog[0] -= s.luk[1]
                            print(f'Zadajesz {s.luk[1]} obrażenia, Hp twojego przeciwnika: {wrog[0]}')
                            time.sleep(1.5)
                        else:
                            wrog[0] -= s.ksiega_zaklec[1]
                            print(f'Zadajesz {s.ksiega_zaklec[1]} obrażenia, Hp twojego przeciwnika: {wrog[0]}')
                            time.sleep(1.5)
                    else:
                        return print("Zostałeś pokonany!")
                else:
                    print(f"Gratulacje {s.imie}! Pokonałeś przeciwnika")
                    s.postac[0] = s.HP
                    s.pieniadze += random.randint(1, 10)
                    s.pokonanych += 1
                    s.inventory.append(s.nagrody[random.randint(0, 5)])
                    return print(f"Twój obecny stan to {s.pieniadze} monet")
        else:
            return print("Uciekasz z miejsca walki")
    else:
        super_walka()

def kierunek(miejsce:input) -> None:
    if miejsce == "miasto":
        inp = input("Masz możliwość pójścia: rynek ")
        if inp == "rynek":
            inp = input("Chcesz kupić czy sprzedać? ")
            if inp == "sprzedać":
                if len(s.inventory) != 0:
                    for i,v in enumerate(s.inventory):
                        print(f'Możesz sprzedać {v} za {s.cena} monet')
                        inp = input("Chcesz sprzedać? ")
                        if inp == "tak":
                            s.inventory.remove(v)
                            s.pieniadze += s.cena
                            return print(f"Pomyślnie sprzedano! Twój obecny stan wynosi {s.pieniadze} monet")
                        else:
                            return print("Do zobaczenia następnym razem!")
                else:
                    return print("Do zobaczenia następnym razem")
            else:
                if s.klasa == "rycerz":
                    if "drewniany" in s.miecz:
                        inp = input("Kolejny miecz: kamienny miecz, atak: 5 ,cena: 25 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 25:
                            s.pieniadze -= 25
                            s.miecz.remove(s.miecz[1])
                            s.miecz.remove("drewniany")
                            s.miecz.append("kamienny")
                            s.miecz.append(5)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "kamienny" in s.miecz:
                        inp = input("Kolejny miecz: żelazny miecz, atak: 10 ,cena: 60 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 60:
                            s.pieniadze -= 60
                            s.miecz.remove(s.miecz[1])
                            s.miecz.remove("kamienny")
                            s.miecz.append("żelazny")
                            s.miecz.append(10)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "żelazny" in s.miecz:
                        inp = input("Kolejny miecz: stalowy miecz, atak: 20 ,cena: 150 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 150:
                            s.pieniadze -= 150
                            s.miecz.remove(s.miecz[1])
                            s.miecz.remove("żelazny")
                            s.miecz.append("stalowy")
                            s.miecz.append(20)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "stalowy" in s.miecz:
                        inp = input("Kolejny miecz: miecz prawdziwego rycerza, atak: 50 ,cena: 500 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 500:
                            s.pieniadze -= 500
                            s.miecz.remove(s.miecz[1])
                            s.miecz.remove("stalowy")
                            s.miecz.append("prawdziwego rycerza")
                            s.miecz.append(50)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    else:
                        return print("Wygląda na to że nie ma lepszego miecza niż twój obecny!")

                elif s.klasa == "łucznik":
                    if "zwykły" in s.luk:
                        inp = input("Kolejny łuk: łuk początkującego, atak: 7 ,cena: 30 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 30:
                            s.pieniadze -= 30
                            s.luk.remove(s.luk[1])
                            s.luk.remove("zwykły")
                            s.luk.append("początkującego")
                            s.luk.append(7)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "początkującego" in s.luk:
                        inp = input("Kolejny łuk: wytrzymały łuk , atak: 12 ,cena: 45 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 45:
                            s.pieniadze -= 45
                            s.luk.remove(s.luk[1])
                            s.luk.remove("początkującego")
                            s.luk.append("wytrzymały")
                            s.luk.append(12)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "wytrzymały" in s.luk:
                        inp = input("Kolejny łuk: mocny łuk , atak: 20 ,cena: 80 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 80:
                            s.pieniadze -= 80
                            s.luk.remove(s.luk[1])
                            s.luk.remove("wytrzymały")
                            s.luk.append("mocny")
                            s.luk.append(20)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "mocny" in s.luk:
                        inp = input("Kolejny łuk: łuk prawdziwego łucznika , atak: 45 ,cena: 300 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 300:
                            s.pieniadze -= 300
                            s.luk.remove(s.luk[1])
                            s.luk.remove("mocny")
                            s.luk.append("prawdziwego łucznika")
                            s.luk.append(45)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    else:
                        return print("Wygląda na to że nie ma lepszego łuku niż twój obecny!")
                
                else:
                    if "początkującą" in s.ksiega_zaklec:
                        inp = input("Kolejna księga zaklęć: stara księga, atak: 10 ,cena: 45 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 45:
                            s.pieniadze -= 45
                            s.ksiega_zaklec.remove(s.ksiega_zaklec[1])
                            s.ksiega_zaklec.remove("początkującą")
                            s.ksiega_zaklec.append("stara")
                            s.ksiega_zaklec.append(10)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "stara" in s.ksiega_zaklec:
                        inp = input("Kolejna księga zaklęć: magiczna księga, atak: 20 ,cena: 100 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 100:
                            s.pieniadze -= 100
                            s.ksiega_zaklec.remove(s.ksiega_zaklec[1])
                            s.ksiega_zaklec.remove("stara")
                            s.ksiega_zaklec.append("magiczna")
                            s.ksiega_zaklec.append(20)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    elif "magiczna" in s.ksiega_zaklec:
                        inp = input("Kolejna księga zaklęć: księga prawdziwego czarodzieja, atak: 40 ,cena: 200 monet, kupić? ")
                        if inp == "tak" and s.pieniadze >= 200:
                            s.pieniadze -= 200
                            s.ksiega_zaklec.remove(s.ksiega_zaklec[1])
                            s.ksiega_zaklec.remove("magiczna")
                            s.ksiega_zaklec.append("prawdziwego czarodzieja")
                            s.ksiega_zaklec.append(40)
                            return print("Gratulujemy zakupu!")
                        else:
                            return print("Nie można kupić przedmiotu")
                    else:
                        print("Wygląda na to że nie ma lepszej księgi niż twoja obecna!")
    elif miejsce == "pole bitwy":
        walka()
    else:
        manekin = manekin_treningowy()
        if miejsce == "miejsce treningu":
            inp = input("Witaj w miejscu praktyk, w miejscu gdzie możesz stać się silniejszym, poprzez walkę z treningowym manekinem. Zacząć trening? ")
            if inp == "tak":
                print(f'Manekin gotowy, HP: {manekin[0]}')
                while True:
                    if manekin[0] > 0:
                        manekin[0] -= s.miecz[1]
                        print(f'HP manekina: {manekin[0]}')
                        time.sleep(1)
                    else:
                        praktyki_rycerz = random.randint(1, 5)
                        s.miecz[1] += praktyki_rycerz
                        return print(f"Gratulacje, dostajesz + {praktyki_rycerz} ATK, twój obecny atak wynosi {s.miecz[1]}")
            else:
                return print("Do zobaczenia następnym razem")
        elif miejsce == "strzelnica":
            inp = input("Witaj na strzelnicy, miejsce gdzie możesz stać się silniejszym, poprzez strzelanie i trafianie z łuku. Zacząć trening? ")
            if inp == "tak":
                print(f'Manekin gotowy, HP: {manekin[0]}')
                while True:
                    if manekin[0] > 0: 
                        traf = random.randint(1,3)
                        time.sleep(1)
                        if traf >= 2:
                            manekin[0] -= s.luk[1]
                            print(f'HP manekina: {manekin[0]}')
                        else:
                            print("Nie trafiono w manekin! Spróbuj ponownie")
                    else:
                        praktyki_lucznik = random.randint(1, 3)
                        s.luk[1] += praktyki_lucznik
                        return print(f"Gratulacje, dostajesz + {praktyki_lucznik} ATK, twój obecny atak wynosi {s.luk[1]}")
            else:
                return print("Do zobaczenia następnym razem")
            
        elif miejsce == "biblioteka":
            inp = input("Witaj w bibliotece, w miejscu gdzie zdobywasz wiedzę i stajesz się silniejszy, poprzez prawidłowe czytanie zaklęć. Zacząć trening? ")
            if inp == "tak":
                print(f'Manekin gotowy, HP: {manekin[0]}')
                while True:
                    if manekin[0] > 0:
                        czytanie = s.zaklecia[random.randint(0, 8)]
                        inp = input(f'Użyj zaklęcia {czytanie} ')
                        time.sleep(1)
                        if inp == czytanie:
                            manekin[0] -= s.ksiega_zaklec[1]
                            print(f'HP manekina: {manekin[0]}')
                        else:
                            print("Nieprawidłowo wypowiedziane zaklęcie! ")
                    else:
                        praktyki_czarodziej = random.randint(1, 3)
                        s.ksiega_zaklec[1] += praktyki_czarodziej
                        return print(f"Gratulacje, dostajesz + {praktyki_czarodziej} ATK, twój obecny atak wynosi {s.ksiega_zaklec[1]}")
            else:
                return print("Do zobaczenia następnym razem")
        else:
            return print("Wygląda na to, że wprowadziłeś niepoprawną komendę!")
