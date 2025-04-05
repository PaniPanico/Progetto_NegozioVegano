import json
import os

PATH_INVENTORY = "products.json"
PATH_PROFIT = "profits.json"
PATH_TMP_SALES = "tmp_sale.json"

def input_value(type,text):

    """
    Consente l'inserimento di valori controllando che l'utente non inserisca valori non validi

    Args:
        type: il tipo della variabile che si desidera inserire
        text(str): Il nome della variabile che verrà mostrato all'utente a schermo 

    Returns:
        x: il valore valido della variabile
    """

    while True:
        try:
            x = type(input(text + ": "))
            break
        except Exception as e:
            print("Errore: ", e)
            print("Reinserire " + text.lower())
            continue
    return x
    

def load_data(path):

    """
    Carica i dati presenti in un file .json in un dizionario

    Args:
        path(str): percorso del file .json

    Returns:
        data: il dizionario caricato con i dati presenti sul file .json
    """
    
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_data(path, data):

    """
    Salva un dizionario in un file .json

    Args:
        path(str): percorso del file .json
        data: dizionario da salvare nel file .json
    Returns:
        None
    """
    
    with open(path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_new_product(name, quant, net, gross):

    """
    Aggiunge un nuovo prodotto in inventario 

    Args:
        name(str): nome del prodotto
        quant(int): quantità del prodotto
        net(float): prezzo di acquisto del prodotto
        gross(float): prezzo di vendita del prodotto
    Returns:
        None
    """
          
    inventory = load_data(PATH_INVENTORY)
    inventory[name] = {
        'quantity': quant,
        "net": net,
        "gross": gross
    }
    print(f"Prodotto {name} aggiunto con successo.")   
    # Scrivi i dati aggiornati nel file
    save_data(PATH_INVENTORY,inventory)

def update_product(name,quant):
    
    """
    Se il prodotto è già presente in inventario ne aggiorna la quantità

    Args:
        name(str): nome del prodotto
        quant(int): quantità del prodotto da aggiungere
    Returns:
        None
    """
   
    inventory = load_data(PATH_INVENTORY)
    # Aggiungi il nuovo prodotto se non esiste già
    if name in inventory:
        inventory[name]['quantity'] += quant
        print(f"prodotto esistente: quantità aggiornata")
    save_data(PATH_INVENTORY,inventory)


def tmp_sales(name,quant):
    
    """
    Registra i prodotti venduti e salva la vendita in un file .json

    Args:
        name(str): nome del prodotto
        quant(int): quantità del prodotto da aggiungere
    Returns:
        None
    """
    
    inventory = load_data(PATH_INVENTORY)
    t_sale = load_data(PATH_TMP_SALES)
    
    if name not in t_sale:
        t_sale[name]={'quantity':quant, 'gross_price':inventory[name]['gross'],'net_price':inventory[name]['net']}
    else:
        new_quant = quant + t_sale[name]['quantity']
        t_sale[name]={'quantity':new_quant, 'gross_price':inventory[name]['gross'],'net_price':inventory[name]['net']}
    
    save_data(PATH_TMP_SALES,t_sale)


def print_tmp_sales():

    """
    Mostra all'utente le informazioni relative alla vendita
    """
    
    t_sale = load_data(PATH_TMP_SALES)
    tot = 0
    
    print("VENDITA REGISTRATA")
    
    for name in t_sale:
        tot += float(t_sale[name]['quantity'])*t_sale[name]["gross_price"]
        print(f"- {t_sale[name]['quantity']} x {name} = €{(float(t_sale[name]['quantity'])*t_sale[name]['gross_price']):.2f}")
    
    print(f"TOTALE: €{tot:.2f}")
     

def del_file(path):
   
    """
    Elimina il file identificato da path(in questo programma lo useremo solo per le vendite registrate)

    Args:
        path(str): percorso del file da eliminare
    """
    if os.path.exists(path):
        os.remove(path)


def remove_product_quantity(name, quant):
    
    """
    rimuove la quantità di un determinato prodotto dall'inventario

    Args:
        name(str): nome del prodotto
        quant(int): quantità del prodotto da rimuovere
    Returns:
        None
    """
   
    inventory = load_data(PATH_INVENTORY)
    
    if inventory[name]['quantity'] >= quant :
        inventory[name]['quantity'] -= quant
        save_data(PATH_INVENTORY,inventory)
        tmp_sales(name,quant)
    elif inventory[name]['quantity'] < quant :
        print("Errore di inventario/Prodotto non disponibile!")
        print("La quantità disponibile in inventario è ", inventory[name]['quantity'])      
    


def update_profits():
   
    """
    Aggiorna i profitti del negozio registrando in un file .json il profitto lordo e il profitto netto
    """

    t_sale = load_data(PATH_TMP_SALES)

    if os.path.exists(PATH_PROFIT):
        profit = load_data(PATH_PROFIT)
        tot_net = profit["NET"]
        tot_gross = profit["GROSS"]
    else:
        tot_net = 0
        tot_gross = 0
    
    for name in t_sale:
        tot_net += float(t_sale[name]['quantity'])*t_sale[name]["net_price"]
        tot_gross += float(t_sale[name]['quantity'])*t_sale[name]["gross_price"]
    
    profit = {"NET":tot_net,"GROSS":tot_gross}
    save_data(PATH_PROFIT,profit)



    
  



    

