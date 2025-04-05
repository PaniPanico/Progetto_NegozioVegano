import utilities

while True:
    command = input("\nInserisci un comando: ").strip().lower()
    if command == "aggiungi":
        utilities.add_product()
    elif command == "elenca":
        utilities.list_product()
    elif command == "vendita":
        utilities.sell_product()
    elif command == "profitti":
        utilities.print_profit()
    elif command == "aiuto":
        utilities.print_help()
    elif command == "chiudi":
        exit("Bye bye")
    else:
        print("Comando non valido")
        utilities.print_help()
        