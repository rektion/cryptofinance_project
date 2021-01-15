from random import randint
import matplotlib.pyplot as plt

def main_retention_block(puissance_hashage):
    n_bloc = 0
    block_offi = 0
    temps = 0
    temps = temps + randint(0,100)
    if temps > puissance_hashage:
        return (0, 1)
    n_bloc = n_bloc + 1
    temps = temps + randint(0,100)
    if temps > puissance_hashage:
        return (1, 1)
    n_bloc = n_bloc + 1
    while n_bloc - block_offi > 1:
        temps = temps + randint(0,100)
        if temps > puissance_hashage:
            block_offi = block_offi + 1
        else:
            n_bloc = n_bloc + 1
    return (n_bloc, block_offi + 2)

def main_double_depense(puissance_hashage, n_conf, tolerance, bloc_premines):
    temps = 0
    n_block = 0
    while bloc_premines != n_conf and bloc_premines != tolerance:
        if randint(0,100) > puissance_hashage:
            bloc_premines = bloc_premines - 1
            n_block = n_block + 1
        else:
            bloc_premines = bloc_premines + 1
    if bloc_premines == n_conf:
        return (bloc_premines, n_block)
    else:
        return (0, n_block)
    # On part de notre avance préminée jusqu'a atteindre n_conf sans atteindre la tolérance.


def minage_honnete(puissance_hashage):
    if randint(0,100) < puissance_hashage:
        return 1
    else:
        return 0

def calc_rendement_retention_block(n, puissance_hashage):
    esp_self = 0
    esp_hon = 0
    for i in range(n):
        tmp = main_retention_block(puissance_hashage)
        esp_hon = esp_hon + tmp[1]*puissance_hashage/100
        esp_self = esp_self + tmp[0]
    return esp_self/esp_hon

def calc_rendement_double_depense(n, puissance_hashage, n_conf, tolerance, bloc_premines, montant_double_dep):
    esp_self = 0
    esp_hon = 0
    for i in range(n):
        tmp = main_double_depense(puissance_hashage, n_conf, tolerance, bloc_premines)
        esp_hon = esp_hon + tmp[1]*puissance_hashage/100*12.5
        if tmp[0] != 0:
            esp_self = esp_self + tmp[0]*12.5 + montant_double_dep
    return esp_self/esp_hon

def affichage_retention_de_block(n):
    val = []
    for i in range(1,100):
        val.append(calc_rendement_retention_block(n, i))
    plt.plot(range(1,100), val)
    plt.title('Selfish mining')
    plt.xlabel("Puissance de hashage (%)")
    plt.ylabel("Rendement de l'attaque")
    plt.show()

def affichage_double_dep(n, n_conf, retard_max, n_premine, montant_double_dep):
    val = []
    for i in range(1,100):
        val.append(calc_rendement_double_depense(n, i, n_conf, retard_max, n_premine, montant_double_dep))
    plt.plot(range(1,100), val)
    plt.title('Attaque à la double dépense')
    plt.xlabel("Puissance de hashage (%)")
    plt.ylabel("Rendement de l'attaque")
    plt.show()

def menu_double_dep():
    n = int(input("Veuillez entrer le nombre de simulations : "))
    n_conf = int(input("Veuillez entrer le nombre de confirmations demandées par le vendeur : "))
    retard_max = int(input("Veuillez entrez le nombre de blocs de retard maximum autorisés par rapport à la blockchain officielle : "))
    if retard_max > 0:
        retard_max = -retard_max
    n_premine = int(input("Veuillez entrer le nombre de blocs préminés : "))
    montant_double_dep = float(input("Veuillez entrer le montant de la double dépense (en Bitcoin) : "))
    print("Simulations en cours, veuillez patienter...")
    affichage_double_dep(n, n_conf, retard_max, n_premine, montant_double_dep)

def menu_egoiste():
    n = int(input("Veuillez entrer le nombre de simulations : "))
    print("Simulations en cours, veuillez patienter...")
    affichage_retention_de_block(n)

def menu():
    entry = 0
    while True:
        if entry == '1':
            menu_egoiste()
        if entry == '2':
            menu_double_dep()
        if entry == '3':
            return
        print("Veuillez choisir une simulation : ")
        print("1. Minage Egoiste")
        print("2. Double dépense")
        print("3. Quitter le programme")
        entry = input("")

menu()