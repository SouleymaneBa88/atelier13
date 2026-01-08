
#creation liste
service_orangr=[]
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
            compose=int(input(" veuillez choisir un menu: ")) 
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
            choix_menu= int(input("Veullez choisir un menu de consultation : "))
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
        # menu_consulter_solde()
        try:
            code=1234
            code_user= int(input("veuillez saisir votre mot de pass : "))
        
            if code_user == code:
                print("vous avez 40000")

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
                mon_numero()
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

def mon_numero():
    while True:
        try:
            mon_numero=(input("Veuillez saisir votre numero : "))
            if len(str(mon_numero))== 9:
                montant= int(input("Veuillez saisir le montant "))
                if montant > 0:
                    code= int(input("Veuillez saisir votre code secret"))
                    if code == 1234:
                        print("Credit acheter avec success!")
                    else:
                        print("code incorrect veuillez ressayer")
            else:
                print("incorrect veuillez resaisir")
                
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
                montant= (input("Veuillez saisir le montant "))
                if montant > 0:
                    print(" montant incorrect")
                    if code == 1234:
                        print("Credit acheter avec success!")
                    else:
                        print("code incorrect veuillez ressayer")
                choix= int(input("retoune a consultation: "))
                if choix == 0:
                    achat_credit()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break
            else:
                print("incorrect veuillez resaisir")
        except ValueError:
            print("numero incorrect resaisi")

def mon_numero_promobile():
    while True:
        try:
            mon_numero= (input("Veuillez saisir votre numero : "))
            if len(str(mon_numero))== 9:
                montant= int(input("Veuillez saisir le montant "))
                if montant > 0:
                    # print(" montant incorrect")
                    if code == 1234:
                        print("Credit acheter avec success!")
                    else:
                        print("code incorrect veuillez ressayer")
                else:
                    print("numero incorrect")

                choix= int(input("retoune a consultation: "))
                if choix==0:
                    achat_credit()
                    break
            else:
                print("incorrect veuillez resaisir")
        except ValueError:
            print("numero incorrect resaisi")

#===========================================effectuer de transfert=====================================================================
def menu_transfert():
    print("\n Transfert d'argent")
    print("1. Transfert National")
    print("2. Transfert international")
    # print("3. annuler un transfert")
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


def transfert_national():
    while True:
        try:
            numero=int(input("Veuillez donner votre numero : "))
            if len(numero) == 9:
                montan= int(input("Veuillez le montant a transferer : "))
                if montan>0:
                    code_secret= int(input("Veuillez saisir votre code secret : "))
                    if code_secret == 1234:
                        print("Transfert reussi avec sucess!")
                    else:
                        print("Echec du transfert!")
                choix= int(input("Accueil : "))
                if choix ==0:
                    transfert()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break

                else:
                    print("choix incorrect!")
            else:
                print("incorrect veuillez resaisir")
        except ValueError:
            print("erreur de connexion veuillez retentez")

def transfert_international():
    while True:
        try:
            mon_numero=int(input("Veuillez saisir votre numero : "))
            if mon_numero >= 9:
                montan= int(input("Veuillez le montant a transferer : "))
                if montan>0:
                    code_secret= int(input("Veuillez saisir votre code secret : "))
                    if code_secret == 1234:
                        print("Transfert reussi avec sucess!")
                    else:
                        print("Echec du transfert!")
                choix= int(input("Accueil : "))
                if choix ==0:
                    transfert()
                    break
                elif choix==9:
                    afficher_orange_money()
                    break

                else:
                    print("choix incorrect!")
            else:
                print("incorrect veuillez resaisir")
        except ValueError:
            print("erreur de connexion veuillez retentez")

# def annulation():
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

        
        