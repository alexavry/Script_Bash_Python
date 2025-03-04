import subprocess

def afficher_menu():
    print("Veuillez choisir un script à exécuter :")
    print("1. Voir les infos sur www.supdevinci.fr")
    print("2. Voir les partitions du disque")
    print("3. Voir le moniteur btop")
    print("4. Avoir le nombre de caractères d'un fichier")
    print("5. Se connecter en ssh a un hote")
    print("6. Avoir la date et l'heure a un instant T")
    print("7. Ping une IP ou un site web")
    print("8. Quitter")

def lancer_le_script(choice):
    scripts = {
        "1": "./script1.sh",
        "2": "./script2.sh",
        "3": "./script3.sh",
        "4": "./script4.sh",
        "5": "./script5.sh",
        "6": "./script6.sh",
        "7": "./script7.sh"
    }

    if choice in scripts:
        script_path = scripts[choice]
        print("Exécution du script", choice)
        subprocess.run(['bash', script_path])
    elif choice == "6":
        print("au revoir")
        exit(0)
    else:
        print("invalide veuillez réessayer")

def main():
    while True:
        afficher_menu()
        choice = input("Entrez votre choix [1-6] : ")
        lancer_le_script(choice)
print("---------------------------------------------")
print("------------ Le mod menu de alex ------------")
print("---------------------------------------------")
main()

