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


mon_dico={
    "lundi": ["curry", "riz", 10],
    "mardi": ["pâtes", "légumes", 9],
    "mercredi": ["pommes de terre", "haricots verts", 10],
    "jeudi": ["soupe", "pain fromage", 8],
    "vendredi": ["pizza", "salade", 9]
    }

def menu_jour(jour):
    if jour in mon_dico:
        return mon_dico[jour]
    else:
        return "Jour non valide"
    
def prix_jour(jour):
    if jour in mon_dico:
        return mon_dico[jour][2]
    else:
        return "Jour non valide"

def afficher_menu():
    menu_jour_input = input("Entrez un jour de la semaine (lundi, mardi, mercredi, jeudi, vendredi): ")
    menu = menu_jour(menu_jour_input)
    if menu != "Jour non valide":
        print("Menu du", menu_jour_input, ":", menu[0], "et", menu[1], "- Prix:", menu[2], "€")
    else :
        print("Respecter l'écriture : lundi, mardi, mercredi, jeudi, vendredi")
    return

afficher_menu()
