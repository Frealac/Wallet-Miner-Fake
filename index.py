from colorama import init, Fore, Back, Style
init(convert=True)
import os
import sys
import time
import random
import string

### DONNE
liste = ['0.001ETH','0.005ETH','0.001ETH','0.003ETH','0.008ETH','0.01ETH','0.03ETH','0.07ETH','0.1ETH']
liste_btc = ['0.001BTC','0.005BTC','0.001BTC','0.003BTC','0.008BTC','0.01BTC','0.03BTC','0.07BTC','0.1BTC']
### DEF 
def adressegen(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))

def printeth():
    global ask_eth_adresse
    if random.randint(0,100000) < 1:
        eth_liste = random.choice(liste)
        print(Fore.GREEN + '0x'+adressegen(40)+' -----> '+eth_liste)
        print(Fore.BLUE + 'Envoie '+eth_liste+' à '+ask_eth_adresse)
        time.sleep(1)
        print(Fore.GREEN + 'Envoie Reussi !')
        time.sleep(0.5)
        print(Fore.WHITE + 'Relancement du programme !\n')
        time.sleep(4)
    else:
        print(Fore.RED+ '0x'+adressegen(40)+' -----> 0.000 ETH')


def printbtc():
    global ask_btc_adresse
    if random.randint(0,100000) < 1:
        liste_btc = random.choice(liste)
        print(Fore.GREEN + 'bc'+adressegen(40)+' -----> '+liste_btc)
        print(Fore.BLUE + 'Envoie '+liste_btc+' à '+ask_btc_adresse)
        time.sleep(1)
        print(Fore.GREEN + 'Envoie Reussi !')
        time.sleep(0.5)
        print(Fore.WHITE + 'Relancement du programme !\n')
        time.sleep(4)
    else:
        print(Fore.RED+ 'bc'+adressegen(40)+' -----> 0.000 BTC')


def f_len( var ):
    
    i = 0
    for f in var:
        i+=1
    return i


#fin de la fonction
print(Fore.GREEN + """  
      
$$\      $$\           $$\ $$\            $$\           $$\      $$\ $$\                               
$$ | $\  $$ |          $$ |$$ |           $$ |          $$$\    $$$ |\__|                              
$$ |$$$\ $$ | $$$$$$\  $$ |$$ | $$$$$$\ $$$$$$\         $$$$\  $$$$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  
$$ $$ $$\$$ | \____$$\ $$ |$$ |$$  __$$\\_$$  _|        $$\$$\$$ $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$$$  _$$$$ | $$$$$$$ |$$ |$$ |$$$$$$$$ | $$ |          $$ \$$$  $$ |$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$$  / \$$$ |$$  __$$ |$$ |$$ |$$   ____| $$ |$$\       $$ |\$  /$$ |$$ |$$ |  $$ |$$   ____|$$ |      
$$  /   \$$ |\$$$$$$$ |$$ |$$ |\$$$$$$$\  \$$$$  |      $$ | \_/ $$ |$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__/     \__| \_______|\__|\__| \_______|  \____/       \__|     \__|\__|\__|  \__| \_______|\__|      
                                                                                                       
                                            by Frealac    [FAKE MINER]                                                 
                                                                                                       
""")

ask_type = input("> Quelle type de crypto voulez vous ? (ETH/BTC) : ")
### ETH
if ask_type == "ETH":
    ask_eth_adresse = input("> Velliez entrée votre adresse ETH : ")
    List = [ 1, 2 , 3 , 4, 5]
    SizeList = f_len(List)   
    Size = f_len(ask_eth_adresse)
    if Size >= 42:
        print(Fore.RED + "Connexion à " + ask_eth_adresse + " ...")
        time.sleep(2)
        print(Fore.GREEN + "Connexion Reussi !")
        time.sleep(0.8)
        print(Fore.WHITE + "> Lancement du programe !\n")
        time.sleep(2)
        while  True:
            printeth()
    else:
        print(Fore.RED + "> Velliez mettre une adresse correcte ! ")

    
    
### BTC
if ask_type == "BTC":
    ask_btc_adresse = input("> Velliez entrée votre adresse BTC : ")
    List = [ 1, 2 , 3 , 4, 5]
    SizeList = f_len(List)   
    Size = f_len(ask_btc_adresse)
    if Size >= 42:
        print(Fore.RED + "Connexion à " + ask_btc_adresse + " ...")
        time.sleep(2)
        print(Fore.GREEN + "Connexion Reussi !")
        print(Fore.WHITE + "> Lancement du programe !\n")
        time.sleep(2)
        while  True:
            printbtc()
    else:
        print(Fore.RED + "> Velliez mettre une adresse correcte ! ")