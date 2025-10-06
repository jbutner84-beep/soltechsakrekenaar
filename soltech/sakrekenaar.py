# Funksie vir optel
def plus(a, b):
    return a + b

# Funksie vir aftrek
def minus(a, b):
    return a - b

# Funksie vir vermeenigvuldig
def maal(a, b):
    return a * b

# Funksie vir deling
def deel(a, b):
    # Voorkom deling deur nul
    if b == 0:
        return "Fout: Kan nie deur nul deel nie."
    return a / b

# Begin van die hoofprogram
def sakrekenaar():
    # Sentinel waarde om die loop te beheer
    loop_aktief = True

    # Herhaal tot verkies om te stop
    while loop_aktief:
        print("\n--- Sakrekenaar ---")
        print("1. Plus (+)")
        print("2. Minus (-)")
        print("3. Maal (*)")
        print("4. Deel (/)")
        print("5. Verwyder uitset")
        print("6. Stop program")

        keuse = input("Kies 'n opsie (1-6): ")

        if keuse == "6":
            loop_aktief = False  # Sentinel verander om loop te stop
            print("Program beëindig.")
        elif keuse == "5":
            # Verwyder uitset deur skerm skoon te maak
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
        elif keuse in ["1", "2", "3", "4"]:
            try:
                a = float(input("Voer eerste getal in: "))
                b = float(input("Voer tweede getal in: "))

                if keuse == "1":
                    print("Uitset:", plus(a, b))
                elif keuse == "2":
                    print("Uitset:", minus(a, b))
                elif keuse == "3":
                    print("Uitset:", maal(a, b))
                elif keuse == "4":
                    print("Uitset:", deel(a, b))
            except ValueError:
                print("Fout: Voer asseblief geldige getalle in.")
        else:
            print("Ongeldige keuse. Probeer weer.")

# Roep die sakrekenaar funksie aan
sakrekenaar()