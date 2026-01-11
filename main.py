
#creation liste
service_orangr=[]
soldes = 400000

#===========================================Menu principal=====================================================================

def menu():
    print("Contact")
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
             print("Probleme de connexion ou code non valide.")

            break
        except ValueError:
            print("Probleme de connexion ou code non valide.")
#===========================================Consulter le solde=====================================================================
# menu consulter le solde
def menu_consulter_solde():
    print("\n Consulter votre solde")
    print("1. Solde compte om")
    print("2. Mon condamne")
    print("3. Reception international")
    print("0. precedent")
    print("9. accueil")

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

def affiche_consulter_solde():
    while True:
        global soldes
        # menu_consulter_solde()
        try:
            code=1234
            code_user= int(input("otre code secret : "))
        
            if code_user == code:
                print(f"Votre solde est: {soldes} Fcf")

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
            else:
                print("code incorrect veullez resaisir")
        except ValueError:
            print

def condamne():
     while True:
        # menu_consulter_solde()
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
def menu_cacheter_credit():
    print("\n Achat credit")
    print("1. Mon numero")
    print("2. Avec un autre numero")
    print("3. Avec un numero promobile")
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

def Menu_achat():
    print("\n Mon numero")
    print("1. credit Telephonique")
    print("2. Pass Ilimix")
    print("3. Pass Internet")
    print("0. Precedent")
    print("9. Accueil")
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

def Internet():
    print("\n Forfait internet")
    print("1. 100Mo 500fcf")
    print("2. 500Mo 1000fcf")
    print("3. 1Go 2000fcf")
    print("0. Precedent")
    print("9. Accueil")
    while True:
        global soldes
        try:
            choix = int (input("Choix option : "))
            if choix == 1:
                prix = 500
                quantiter = 100
                capacite = 'Mo'
                soldes -= prix
                print(f"Bravo! vous avez acheter un forfait interne de {quantiter}{capacite} a {prix}")
                print(f"Votre solde orange money est {soldes}")
                break
            elif choix == 2:
                prix = 1000
                quantiter = 500
                capacite = 'Mo'
                soldes -= prix
                print(f"Bravo! vous avez acheter un forfait interne de {quantiter}{capacite} a {prix}")
                print(f"Votre solde orange money est {soldes}")
                break
            elif choix == 3:
                prix = 2000
                quantiter = 1
                capacite = 'Go'
                soldes -= prix
                print(f"Bravo! vous avez acheter un forfait interne de {quantiter}{capacite} a {prix}")
                print(f"Votre solde orange money est {soldes}")
                break
            elif choix == 0:
                break
            elif choix == 9:
                break
            else:
                print("Oups!")
        except ValueError:
            print("Choix incorrect !")

# def forfait(prix,quantiter,capacite):
    # while True:
    #     Internet(prix,quantiter,capacite)
    #     global soldes
    #     soldes -= prix
    #     print(f"Bravo! vous avez acheter un forfait interne de {quantiter}{capacite} a {prix}")

def mon_numero():
    while True:
        global soldes
        try:
            montant= int(input("Veuillez saisir le montant : "))
            if montant > 0:
                  
                    confirmation()
                    if soldes >= montant:
                            soldes = soldes - montant
                            print(f"Credit de {montant} acheté avec succès! Solde restant: {soldes}")
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
        global soldes
        try:
            mon_numero= (input("Veuillez saisir votre numero : "))
            if len(str(mon_numero))== 9:
                montant= int(input("Veuillez saisir le montant : "))
                if montant > 0:
                    code= int(input("Veuillez saisir votre code secret : "))
                    # if code == 1234:
                    confirmation()
                    if soldes >= montant:
                            soldes = soldes - montant
                            print(f"Credit de {montant} envoyé au {mon_numero}. Solde restant: {soldes}")
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
        global soldes
        try:
            mon_numero= (input("Veuillez saisir votre numero : "))
            if len(str(mon_numero))== 9:
                montant= int(input("Veuillez saisir le montant : "))
                if montant > 0:
                    code= int(input("Veuillez saisir votre code secret : "))
                    # if code == 1234:
                    confirmation()
                    if soldes >= montant:
                            soldes = soldes - montant
                            print(f"Credit de {montant} acheté pour {mon_numero}. Solde restant: {soldes}")
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
def menu_transfert():
    print("\n Transfert d'argent")
    print("1. Transfert National")
    print("2. Transfert international")
    print("3. annuler un transfert")
    print("0. precedent")
    print("9. accueil")

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

def transfert_national():
    while True:
        global soldes
        try:
            numero= input("Veuillez donner votre numero : ")
            if len(numero) == 9:
                montan= int(input("Veuillez le montant a transferer : "))
                confirmation()
                if soldes >= montan:
                            soldes = soldes - montan
                            service_orangr.append({'numero': numero, 'montant': montan})
                            print(f"Transfert de {montan} réussi avec succès! Solde restant: {soldes}")
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

def transfert_international():
    while True:
        global soldes
        try:
            mon_numero= input("Veuillez saisir votre numero : ")
            if len(mon_numero) == 9:
                montan= int(input("Veuillez le montant a transferer : "))
                if montan>0:
                    code_secret= int(input("Veuillez saisir votre code secret : "))
                    confirmation()
                    if soldes >= montan:
                            soldes = soldes - montan
                            service_orangr.append({'numero': mon_numero, 'montant': montan})
                            print(f"Transfert international de {montan} réussi! Solde restant: {soldes}")
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

def annulation_transfert():
    print("\n Annulation du transfert")
    if not service_orangr:
        print("Aucun transfert à annuler.")
        return
    last_transfer = service_orangr[-1]
    while True:
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
                global soldes
                soldes += montant
                service_orangr.pop()
                print(f"Annulation réussie. Nouveau solde : {soldes}")
                break
            elif choix == 2:
                print("Annulation annulée.")
                break
            else:
                print("Choix incorrect.")
        except ValueError:
            print("Choix incorrect.")
        
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
