# Hierdie program laat jou toe om produkte en pryse by te voeg, uitset te verwyder, en die totaal te sien

items = []

# Funksie om 'n item by die lys te voeg
def voeg_item_by():
    naam = input("Voer produknaam in: ")
    try:
        prys = float(input(f"Voer prys in vir {naam} (bv. 50.00): R"))
        items.append((naam, prys))
        print(f"{naam} is suksesvol bygevoeg teen R{prys:.2f}")
    except ValueError:
        print("Fout: Voer asseblief 'n geldige numeriese prys in.")

# Funksie om die uitset te verwyder (skerm skoon te maak)
def verwyder_uitset():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Funksie om alle produkte en totaal te vertoon
def vertoon_items():
    if not items:
        print("Geen items is gestoor nie.")
        return
    totaal = 0
    print("\n--- Gekoopte Produkte ---")
    for naam, prys in items:
        print(f"{naam:<10} R{prys:.2f}")
        totaal += prys
    print("-" * 20)
    print(f"Totaal     R{totaal:.2f}")

# Hoof loop met sentinel waarde
def pos_stelsel():
    loop_aktief = True
    while loop_aktief:
        print("\n--- POS Menu ---")
        print("1. Voeg item by")
        print("2. Vertoon items en totaal")
        print("3. Verwyder uitset")
        print("4. Stop program")

        keuse = input("Kies 'n opsie (1-4): ")

        if keuse == "1":
            voeg_item_by()
        elif keuse == "2":
            vertoon_items()
        elif keuse == "3":
            verwyder_uitset()
        elif keuse == "4":
            loop_aktief = False  # Sentinel verander om loop te beëindig
            print("Program beëindig.")
        else:
            print("Ongeldige keuse. Probeer weer.")

# Roep die POS stelsel aan
pos_stelsel()