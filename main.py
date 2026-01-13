import json
import os
#creation liste
service_orangr=[]
soldes = {
    'montants': 400000
}
fichier = 'compte.json'
#cette condition verifie si ce fichier n'existe pas
if not os.path.exists(fichier):
    with open(fichier, 'w', encoding= 'utf-8') as fichier_json:
        json.dump(soldes,fichier_json,indent=4)

# Charger l'historique existant
historique_trans = 'historique_transfert.json'
if os.path.exists(historique_trans):
    with open(historique_trans, 'r') as f:
        service_orangr = json.load(f)
else:
    service_orangr = []


#===========================================Menu principal=====================================================================

def menu():
    print("  ")
    print("--Yonde sa xaliss si soutoura--")
    print("\n Pour acceder au service orange money taper  '#144#'")
    # print("#144#")

#===========================================Fonction principal=====================================================================

#fonction menu principal
def menu_om():
    print("\n Bienvenu dans le service orange money ")
    print("1. Consulter votre solde")
    print("2. Acheter du credit")
    print("3. Effectuer un transfert")
    print("0. annuler")

# affiche menu om
def afficher_orange_money():
    while True:
        
        menu_om()
        try:
            compose=int(input("Choix option: ")) 
            if compose == 1:
                consulter()
                break

            elif compose == 2:
                achat_credit()
                break

            elif compose==3:
                transfert()
                break

            elif compose==0:
                afficher_orange_money()
                break

            else:
             print("Choix inconnu !.")

            break
        except ValueError:
            print("Probleme de connexion ou code non valide.")

#===========================================Consulter le solde=====================================================================

# menu consulter le solde
def menu_consulter_solde():
    print('-' *30)
    print("\n Consulter votre solde")
    print("1. Solde compte om")
    print("2. Mon condamne")
    print("3. Reception international")
    print('-' *30)
    print("0. precedent")
    print("9. accueil")
    print('-' *30)


def consulter():
    while True:
        menu_consulter_solde()
        
        try:
            choix_menu= int(input("Choix option: "))
            if choix_menu == 1:
                affiche_consulter_solde()
                break

            elif choix_menu == 2:
                condamne()
                break

            elif choix_menu==3:
                international()
                break

            elif choix_menu==0:
                afficher_orange_money()
                break
           

            else:
             print("Probleme de connexion ou code non valide.")

            break
        except ValueError:
            print("Probleme de connexion ou code non valide.")
# consulter le solde
def affiche_consulter_solde():
    while True:
        code = 1234
        try:
            confirmation()
            with open(fichier,'r') as f:
                    soldes=json.load(f)
                    print('-' *30)
                    print(f" Le solde de votre compte om est de {soldes['montants']}")
                    print('-' *30)
                    choix= int(input("Choix menu du solde : "))
                    if choix==0:
                        consulter()
                        break
                    elif choix==9:
                        afficher_orange_money()
                        break
                    else:
                        print("Probleme de connexion ou code non valide.")
                        break
                    break
            # else:
            #     print("Oups ! Code incorret")
            #     break
                
        except ValueError:
            print

def condamne():
     while True:
        try:
                print("Votre condamne est vide")
                choix= int(input("retoune a consultation :  "))
                if choix==0:
                    consulter()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break
                else:
                    print("Probleme de connexion ou code non valide.")
                    break
        except ValueError:
            print

def international():
     while True:
        # menu_consulter_solde()
        try:
                print("Votre Reception international est vide")
                choix= int(input("retoune a consultation: "))
                if choix==0:
                    consulter()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break
                else:
                    print("Probleme de connexion ou code non valide.")
                    break
        except ValueError:
                    print("Probleme de connexion ou code non valide.")
             

#===========================================acheter du credit=====================================================================
# achat de credit
def menu_cacheter_credit():
    print('-' *30)
    print("\n Achat credit")
    print("1. Mon numero")
    print("2. Avec un autre numero")
    print("3. Avec un numero promobile")
    print('-' *30)
    print("0. precedent")
    print("9. accueil")

def achat_credit():
    while True:
        menu_cacheter_credit()
        try:
            choix_menu= int(input("Veullez choisir un menu de consultation : "))
            if choix_menu == 1:
                Menu_achat()
                break

            elif choix_menu == 2:
                mon_autre_numero()
                break

            elif choix_menu==3:
                mon_numero_promobile()
                break

            elif choix_menu==0:
                afficher_orange_money()
                break
            elif choix_menu==9:
                    afficher_orange_money()
                    break

            else:
             print("Probleme de connexion ou code non valide.")

            break
        except ValueError:
            print("Probleme de connexion ou code non valide.")

#sous menu de achat de credit mon numero
def Menu_achat():
    print('-' *30)
    print("\n Mon numero")
    print("1. credit Telephonique")
    print("2. Pass Ilimix")
    print("3. Pass Internet")
    print('-' *30)
    print("0. Precedent")
    print("9. Accueil")
    print('-' *30)

    while True:
        try:
            choix= int (input(" choisi un option : "))
            if choix == 1:
                mon_numero()
                break
            elif choix== 2:
                print("erreur indisponible pour une maintenance")
                break
            elif choix == 3:
                Internet()
                break
            elif choix == 0:
                achat_credit()
                break
            elif choix == 9:
                afficher_orange_money()
                break
        except ValueError:
            print("choix incorrect!")

def confirmation():
    while True:
        try:
            code= int(input("Veuillez saisir votre code secret : "))
            if code == 1234:
                break
            else:
                print("Code incorrect veuillez ressayer")
                break
        except ValueError:
            print("Code incorrect !")
#forfait internet
def Internet():
    print('-' *30)
    print("\n Forfait internet")
    print("1. 100Mo 500fcf")
    print("2. 500Mo 1000fcf")
    print("3. 1Go 2000fcf")
    print('-' *30)
    print("0. Precedent")
    print("9. Accueil")
    while True:
        try:
            choix = int (input("Choix option : "))
            if choix == 1:
                forfait = {
                    'pass': '100Mo',
                    'prix':500
                }
                confirmation()
                with open(fichier,'r') as f:
                    soldes=json.load(f)
                soldes['montants']  -= forfait["prix"]
                print('-' *30)
                print(f"Bravo! vous avez acheter un forfait interne de {forfait['pass']} a {forfait['prix']}")
                print(f"Votre solde orange money est {soldes['montants']}")
                print('-' *30)
                break
            elif choix == 2:
                forfait = {
                    'pass': '500Mo',
                    'prix':1000
                }
                confirmation()
                with open(fichier,'r') as f:
                    soldes=json.load(f)
                soldes['montants']  -= forfait["prix"]
                print('-' *30)
                print(f"Bravo! vous avez acheter un forfait interne de {forfait['pass']} a {forfait['prix']}")
                print(f"Votre solde orange money est {soldes['montants']}")
                print('-' *30)
                break
            elif choix == 3:
                forfait = {
                    'pass': '1Go',
                    'prix':2000
                }
                confirmation()
                with open(fichier,'r') as f:
                    soldes=json.load(f)
                soldes['montants']  -= forfait["prix"]
                print('-' *30)
                print(f"Bravo! vous avez acheter un forfait interne de {forfait['pass']} a {forfait['prix']}")
                print(f"Votre solde orange money est {soldes['montants']}")
                print('-' *30)
                break
            elif choix == 0:
                break
            elif choix == 9:
                break
            else:
                print("Oups!")
        except ValueError:
            print("Choix incorrect !")

# sauvegarde le soldes
def sauvegarde_montant(soldes):
  try:
    with open(fichier, 'w') as f:
      json.dump(soldes, f, indent=4)
      print(f"compteur sauvegardé dans {fichier}")
  except Exception as e:
    print(f"Erreur lors de la sauvegarde: {e}")

# achat de credit telephonique
def mon_numero():
    while True:
        try:
            montant= int(input("Veuillez saisir le montant : "))
            if montant > 0:
                    confirmation()
                    with open(fichier,'r') as f:
                        soldes=json.load(f)
                    if soldes['montants'] >= montant:
                            soldes['montants'] -= montant
                            sauvegarde_montant(soldes)
                            print('-' *30)

                            print(f"Credit de {montant} acheté avec succès! Solde restant: {soldes['montants']}")
                            print('-' *30)

                    else:
                            print("Votre solde est insuffisant!")
            else:
                print("Incorrect veuillez resaisir")
                
            choix= int(input("retoune a consultation: "))
            if choix==0:
                    achat_credit()
                    break
            elif choix==9:
                    afficher_orange_money()
                    break
            else:
                print("incorrect veuillez resaisir")
        except ValueError:
            print("numero incorrect resaisi")

def mon_autre_numero():
    while True:
        try:
            mon_numero= (input("Veuillez saisir votre numero : "))
            if len(str(mon_numero))== 9:
                montant= int(input("Veuillez saisir le montant : "))
                if montant > 0:
                    # code= int(input("Veuillez saisir votre code secret : "))
                    # if code == 1234:
                    confirmation()
                    if soldes['montants'] >= montant:
                            soldes['montants'] -= montant
                            sauvegarde_montant(soldes)
                            print('-' *30)

                            print(f"Credit de {montant} acheté avec succès! Solde restant: {soldes['montants']}")
                            print('-' *30)

                    else:
                            print("Votre solde est insuffisant!")
                    # else:
                    #     print("Code incorrect veuillez ressayer")
                choix= int(input("Retoune a consultation: "))
                if choix == 0:
                    achat_credit()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break
            else:
                print("Incorrect veuillez resaisir")
        except ValueError:
            print("Numero incorrect resaisi")

def mon_numero_promobile():
    while True:
        try:
            mon_numero= (input("Veuillez saisir votre numero : "))
            if len(str(mon_numero))== 9:
                montant= int(input("Veuillez saisir le montant : "))
                if montant > 0:
                    # code= int(input("Veuillez saisir votre code secret : "))
                    # if code == 1234:
                    confirmation()
                    if soldes['montants'] >= montant:
                            soldes['montants'] -= montant
                            sauvegarde_montant(soldes)
                            print('-' *30)

                            print(f"Credit de {montant} acheté avec succès! Solde restant: {soldes['montants']}")
                            print('-' *30)

                    else:
                            print("Votre solde est insuffisant!")
                    # else:
                    #     print("Code incorrect veuillez ressayer")
                else:
                    print("Montant invalide")

                choix= int(input("Retoune a consultation: "))
                if choix==0:
                    achat_credit()
                    break
            else:
                print("Incorrect veuillez resaisir")
        except ValueError:
            print("Numero incorrect resaisi")

#===========================================effectuer de transfert=====================================================================
# Menu du transfert
def menu_transfert():
    print('-' *30)
    print("\n Transfert d'argent")
    print("1. Transfert National")
    print("2. Transfert international")
    print("3. annuler un transfert")
    print("4. Historique de Transaction")
    print('-' *30)
    print("0. precedent")
    print("9. accueil")
    print('-' *30)

#sauvegarder le historique des transaction
def sauvegarde_historique():
    try:
        historique_trans = 'historique_transfert.json'
        with open(historique_trans, 'w') as f:
            json.dump(service_orangr, f, indent=4)
            print("Historique sauvegardé dans historique_transfert.json")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de l'historique: {e}")

def transfert():
    while True:
        menu_transfert()
        
        try:
            choix_menu= int(input("Veullez choisir un menu pour le transfert: "))
            if choix_menu == 1:
                transfert_national()
                break

            elif choix_menu == 2:
                transfert_international()
                break

            elif choix_menu==3:
                annulation_transfert()
                break
            elif choix_menu==4:
                afficher_historique()
                break

            elif choix_menu==0:
                afficher_orange_money()
                break
            elif choix_menu==9:
                    afficher_orange_money()
                    break

            else:
             print("Probleme de connexion ou code non valide.")

            break
        except ValueError:
            print("Probleme de connexion ou code non valide.")

#transfert national
def transfert_national():
    while True:
        try:
            numero= input("Veuillez donner votre numero : ")
            if len(numero) == 9:
                montan= int(input("Veuillez le montant a transferer : "))
                confirmation()
                with open(fichier,'r') as f:
                        soldes=json.load(f)
                if soldes['montants'] >= montan:
                            soldes['montants'] -= montan
                            sauvegarde_montant(soldes)

                            service_orangr.append({'numero': numero, 'montant': montan})
                            sauvegarde_historique()
                            print("-" * 30)
                            print(f"Transfert de {montan} réussi avec succès! Solde restant: {soldes['montants']}")
                            print("-" * 30)

                else:
                            print("Solde insuffisant pour ce transfert!")
                    
                choix= int(input("Accueil : "))
                if choix ==0:
                    transfert()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break
                else:
                    print("Choix incorrect!")
            else:
                print("Incorrect veuillez resaisir")
        except ValueError:
            print("Erreur de connexion veuillez retentez")

# transfert international
def transfert_international():
    while True:
        # global soldes
        try:
            mon_numero= input("Veuillez saisir votre numero : ")
            if len(mon_numero) == 9:
                montan= int(input("Veuillez le montant a transferer : "))
                if montan>0:
                    # code_secret= int(input("Veuillez saisir votre code secret : "))
                    confirmation()
                    with open(fichier,'r') as f:
                        soldes=json.load(f)
                    if soldes['montants'] >= montan:
                            soldes['montants'] -=  montan
                            sauvegarde_montant(soldes)

                            service_orangr.append({'numero': mon_numero, 'montant': montan})
                            sauvegarde_historique()

                            print("-" * 30)
                            print(f"Transfert international de {montan} réussi! Solde restant: {soldes['montants']}")
                            print("-" * 30)
                    else:
                            print("Solde insuffisant pour ce transfert!")
                choix= int(input("Accueil : "))
                if choix ==0:
                    transfert()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break
                else:
                    print("Choix incorrect!")
            else:
                print("Incorrect veuillez resaisir")
        except ValueError:
            print("Erreur de connexion veuillez retentez")

#annulation du transfert
def annulation_transfert():
    print("\n Annulation du transfert")
    if not service_orangr:
        print("Aucun transfert à annuler.")
        return
    
    last_transfer = service_orangr[-1]
    while True:
        afficher_historique()
        numero = input("Veuillez saisir le numéro du destinataire : ")
        try:
            montant = int(input("Veuillez saisir le montant du transfert : "))
        except ValueError:
            print("Montant invalide. Veuillez ressayer.")
            continue
        if numero == last_transfer['numero'] and montant == last_transfer['montant']:
            break
        else:
            print("Erreur de choix. Veuillez ressayer.")

    print("1. Oui")
    print("2. Non")
    while True:
        try:
            choix = int(input("Confirmer l'annulation ? "))
            if choix == 1:
                confirmation()
                with open(fichier,'r') as f:
                        soldes=json.load(f)
                soldes['montants'] += montant
                sauvegarde_montant(soldes)
                service_orangr.pop()
                sauvegarde_historique()
                print("-" * 30)
                print(f"Annulation réussie. Nouveau solde : {soldes['montants']}")
                print("-" * 30)
                break
            elif choix == 2:
                print("Annulation annulée.")
                break
            else:
                print("Choix incorrect.")
        except ValueError:
            print("Choix incorrect.")

#Afficher l'historique de la transaction
def afficher_historique():
    print("\n Historique de transaction")
    historique_trans = 'historique_transfert.json'
    try:
        with open(historique_trans, 'r') as historique:
            list_trans = json.load(historique)
            if list_trans:
                for trans in list_trans:
                    print(f"- {trans}")  # Ajustez selon la structure de vos données
            else:
                print("Aucune transaction trouvée.")
    except json.JSONDecodeError:
        print("Erreur lors de la lecture du fichier historique.")
#===========================================Programme principal=====================================================================

#principal programme
while True:
        menu()
        while True:
            code_om="#144#"
            try:
                code=input("Veuillez composer le code OM : ")
                
                break
            except ValueError:
                print("Probleme de connexion ou code non valide.")

        if code == code_om:
            afficher_orange_money()
            # print("avec success")
        else:
            print("incorrect")
