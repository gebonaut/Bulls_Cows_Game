from random import choice
from timeit import default_timer as timer

cisla = []
volba = []
pokus = 0
start_timer = 0
end_timer = 0

def nahodny_vyber_cisla() -> None:
    """Náhodně vytvoří 4 čísla a vyplní do listu čísla"""
    for i in range(4):
        cisla.append(choice(range(10)))
    if len(cisla) > len(set(cisla)) or cisla[0] == 0:
        cisla.clear()
        nahodny_vyber_cisla()

def oddelovac():
    """Vytiskne oddělovač"""
    print("-"*40)

def volba_hrace() -> None:
    """Požaduje vstup 4 čísel od hráče dle definovaných pravidel a uloží do listu volba"""
    volba_cisel = input('Guess the number: ')
    volba.clear()
    oddelovac()
    if kontrola_cisla(volba_cisel) == True:
        for cislo in volba_cisel:
            volba.append(int(cislo))
    else:
        print(kontrola_cisla(volba_cisel))
        oddelovac()
        volba_hrace()

def kontrola_cisla(zadane_cislo):
    """Kontroluje číslo zadané hráčem a vrací odpovídající hodnotu"""
    if len(zadane_cislo) != 4:
        return 'Incorrect input - only 4 digit number.'
    elif not zadane_cislo.isnumeric():
        return 'Incorrect input - only numerical value allowed.'
    elif int(zadane_cislo[0]) == 0:
        return 'Incorrect input - first number cannot be 0.'
    elif len(zadane_cislo) > len(set(zadane_cislo)):
        return 'Incorrect input - only unique values allowed.'
    else:
        return True

def vyhodnoceni() -> None:
    """Vyhodnocuje volbu uživatele a náhodná čísla, vypisuje stav"""
    bulls, cows = 0, 0
    cisla_na_text = ''.join([str(i) for i in volba])

    for i in range(4):
        if volba[i] == cisla[i]:
            bulls += 1
        elif volba[i] != cisla[i] and volba[i] in cisla:
            cows +=1
    if bulls != 4:
        print(f"{bulls} {'Bull' if bulls <= 1 else 'Bulls'}, {cows} {'Cow' if cows <= 1 else 'Cows'}")
        oddelovac()
        hra()
    else:
        end_timer = timer()
        print(f"{cisla_na_text} is correct!"
              f" You've guessed the right number in {pokus} {'guess' if pokus <= 1 else 'guesses'}! "
              f"It took you {str(end_timer-start_timer)[:3]} seconds!")
        oddelovac()

def hra() -> None:
    """Spouští hru a jednotlivé funkce"""
    global pokus
    pokus += 1
    if pokus == 1:
        start_timer = timer()
        nahodny_vyber_cisla()
        print('Hi there!')
        oddelovac()
        print("I've generated a random 4 digit number for you.\n"
              "Let's play a bulls and cows game.")
        oddelovac()
    volba_hrace()
    vyhodnoceni()

if __name__ == '__main__':
    hra()
