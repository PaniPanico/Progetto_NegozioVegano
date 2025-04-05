import inventory

def add_product():

    """
    Gestisce l'aggiunta dei prodotti nell'inventario
    """

    while True:
        name = str(input("Nome del prodotto: ").strip().lower())
        quant = inventory.input_value(int,"Quantità")
        
        if name not in inventory.load_data(inventory.PATH_INVENTORY):
            net = inventory.input_value(float,"Prezzo di acquisto")
            gross = inventory.input_value(float,"Prezzo di vendita")
            inventory.save_new_product(name, quant, net, gross)
        else:
            inventory.update_product(name,quant)
        ask = input("Vuoi aggiungere altri prodotti? (si/no): ")
        
        if ask == "si":
            continue
        else:
            break

def list_product():

    """
    Elenca i prodotti in magazzino
    """

    data = inventory.load_data(inventory.PATH_INVENTORY)
    
    print(f"{'PRODOTTO':<35}{'QUANTITÀ':<10}{'PREZZO':<10}")
    for name in data:
        print(f"{name:<35} {data[name]['quantity']:<10} €{data[name]['gross']:<10.2f}")

def sell_product():

    """
    Gestisce le vendite dei prodotti
    """

    while True:
        name = input("Nome del prodotto: ")
        
        
        if name not in inventory.load_data(inventory.PATH_INVENTORY):
            print("Prodotto non disponibile!")
            continue
        else:
            quant = inventory.input_value(int,"Quantità")
            inventory.remove_product_quantity(name,quant)
        
        ask = input("Vuoi aggiungere altri prodotti? (si/no): ")
        if ask == "si":
            continue
        else:
            break
    
    inventory.update_profits()
    inventory.print_tmp_sales()
    inventory.del_file(inventory.PATH_TMP_SALES)

def print_help():
     
    """
    Restituisce all'utente tutti i possibili comandi
    """
     
    print("""I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma""")
    
def print_profit():
    profit = inventory.load_data(inventory.PATH_PROFIT)
    print(f"profitto lordo: €{profit['GROSS']:.2f} \t profitto netto: €{profit['GROSS']-profit['NET']:.2f} ")