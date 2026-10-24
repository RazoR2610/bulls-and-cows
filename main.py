"""
main.py: druhý projekt do Engeto Online Python Akadémie

author: Roman Nagy
email: romankonagy@gmail.com
"""
import random

DLZKA_CISLA = 4
CIARA = "-----------------------------------------------"


def privitanie() -> None:
    """Vypise uvodny text hry."""
    print("Ahoj!")
    print(CIARA)
    print("Vygeneroval som náhodné " + str(DLZKA_CISLA) + "-miestne číslo.")
    print("Poďme si zahrať hru bulls and cows.")
    print(CIARA)
    print("Zadaj číslo:")
    print(CIARA)


def vytvor_tajne_cislo() -> str:
    """Vytvori tajne cislo s roznymi cislicami, ktore nezacina nulou."""
    cislice = "0123456789"
    tajne = random.choice("123456789")
    while len(tajne) < DLZKA_CISLA:
        cislica = random.choice(cislice)
        # cislica sa nesmie opakovat
        if cislica not in tajne:
            tajne = tajne + cislica
    return tajne


def skontroluj_tip(tip: str) -> str:
    """Skontroluje tip hraca a vrati chybovu spravu.

    Ak je tip v poriadku, vrati prazdny retazec.
    """
    if not tip.isdigit():
        return "Číslo môže obsahovať iba číslice."
    if len(tip) != DLZKA_CISLA:
        return "Číslo musí mať presne " + str(DLZKA_CISLA) + " číslice."
    if tip[0] == "0":
        return "Číslo nesmie začínať nulou."
    # set odstrani duplicity, takze ak je kratsi, nieco sa opakuje
    if len(set(tip)) != len(tip):
        return "Číslice sa nesmú opakovať."
    return ""


def spocitaj_bulls_cows(tajne: str, tip: str) -> tuple[int, int]:
    """Spocita bulls (spravna cislica aj miesto) a cows (iba cislica)."""
    bulls = 0
    cows = 0
    for i in range(len(tip)):
        if tip[i] == tajne[i]:
            bulls = bulls + 1
        elif tip[i] in tajne:
            cows = cows + 1
    return bulls, cows


def slovo(pocet: int, jednotne: str) -> str:
    """Vrati slovo v jednotnom alebo mnoznom cisle podla poctu."""
    if pocet == 1:
        return jednotne
    return jednotne + "s"


def hra() -> int:
    """Prebehne jedna hra, vrati pocet pokusov."""
    tajne = vytvor_tajne_cislo()
    pokusy = 0

    while True:
        tip = input(">>> ")
        chyba = skontroluj_tip(tip)
        if chyba != "":
            print(chyba)
            print(CIARA)
            continue

        pokusy = pokusy + 1
        bulls, cows = spocitaj_bulls_cows(tajne, tip)

        if bulls == DLZKA_CISLA:
            return pokusy

        print(str(bulls) + " " + slovo(bulls, "bull") + ", "
              + str(cows) + " " + slovo(cows, "cow"))
        print(CIARA)


def main() -> None:
    """Spusti hru a vypise vysledok."""
    privitanie()
    pokusy = hra()
    print("Správne, uhádol si číslo")
    if pokusy == 1:
        print("na 1 pokus!")
    elif pokusy < 5:
        print("na", pokusy, "pokusy!")
    else:
        print("na", pokusy, "pokusov!")
    print(CIARA)
    print("To je úžasné!")


if __name__ == "__main__":
    main()
