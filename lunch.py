# Lunch script
#
# This script is a basic script that give you the menu of the day and the price of the meal. 
# You need to enter a day of the week
#
# Inputs :
#   nothing, the program will ask you to enter a day of the week
#
# Change log :
#   05/10/2026 : Drafting the file header
#   05/10/2026 : Adding the script of lunch
#
# Author : Éléonore Deladoeuille <eldeladoeuille@airfrance.fr>
#
# Remarks : 
#   

import json

mon_dico={
    "lundi": ["curry", "riz", 10],
    "mardi": ["pâtes", "légumes", 9],
    "mercredi": ["pommes de terre", "haricots verts", 10],
    "jeudi": ["soupe", "pain fromage", 8],
    "vendredi": ["pizza", "salade", 9]
    }

def menu_jour(jour):
    '''renvoie le menu du jour donné en argument'''
    if jour in mon_dico:
        return mon_dico[jour]
    else:
        return "Jour non valide"
    
def prix_jour(jour):
    '''renvoie le prix du plat du jour donné en argument'''
    #pas forcément utile car on peut directement accéder au prix via le dico
    if jour in mon_dico:
        return mon_dico[jour][2]
    else:
        return "Jour non valide"

def modifier_menu(jour, plat1=None, plat2=None, prix=None):
    '''modifie le menu du jour donné en argument'''
    if jour in mon_dico:
        if plat1 is not None:
            mon_dico[jour][0] = plat1
        if plat2 is not None:
            mon_dico[jour][1] = plat2
        if prix is not None:
            mon_dico[jour][2] = prix
    else:
        print("Jour non valide")
    return

def afficher_menu(jour=None):
    '''affiche le menu du jour et le prix du plat du jour et modifie le menu du lundi si le jour n'est pas valide'''
    if jour is None:
        menu_jour_input = input("Entrez un jour de la semaine (lundi, mardi, mercredi, jeudi, vendredi): ")
    else:
        menu_jour_input = jour
    menu = menu_jour(menu_jour_input)
    if menu != "Jour non valide":
        print("Menu du", menu_jour_input, ":", menu[0], "et", menu[1], "- Prix:", menu[2], "€")
    else :
        print("Respecter l'écriture : lundi, mardi, mercredi, jeudi, vendredi")
        modifier_menu("lundi","carottes","puree",6)
    return

afficher_menu()

afficher_menu("lundi")

#"menu.json" le nom du fichier qui va être créé
#"w" pour dire qu'on va écrire dans le fichier
#encoding="utf-8" : gère correctement les accents
#ensure_ascii=False : conserve les caractères comme é ou à
#indent=4 : pour avoir une indentation : json plus lisible
#json.dump : ecrire directement dans un fichier
with open("menu.json","w", encoding="utf-8") as fichier:
    json.dump(mon_dico,fichier,ensure_ascii=False,indent=4)