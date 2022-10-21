import functions


############################################################################## Lancement du jeu #############################################################################################
def pendu(): 

    difficult, health = functions.level()
    word = functions.wordF()                                                                            # On choisi aléatoirement un Mot
    #print(word)  
    #print(health)                                                                                       

    mask_word = ""                                                                                      # On crée une variable pour le mot masque
    lettres_bonnes = ""                                                                                 # On crée une variable pour les bonnes lettres
    lettres_deja_passees = ""                                                                           # On crée une variable pour les lettres déjà proposées
    run = True                                                                                          # On attribue True à 'run' pour lancer la boucle while
   

    for i in word:                                                                                      # On crée le mot masqué en ajoutant un "_ " pour chaque lettre : TOTO -> (_ _ _ _ )
        mask_word += "_ "


    while run:                                                                                          # On démarre la boucle
        print("\n\n Vies restante:", health)                                                            # On affche les vies restantes
        print("Mot à deviner:", mask_word)                                                              # On affiche le mot masqué (_ _ _ _ _ _)
        proposition = functions.myUpper(input("Saisissez une lettre: "))                                # Input pour le choix de la lettre
        lettres_deja_passees += proposition + " "                                                       # On stock la proposition dans les lettres dèjà joués
        
        if proposition in word:                                                                             # Si la lettre proposée est dans le mot, on l'ajoute à la lste des bonnes lettres
            lettres_bonnes += proposition                           
            print("Voui! Encore! :) \n\n")                                                                  # Et on affiche un message
        
        else:           
            print("Noob! Essaye encore! ;) \n\n")    
            health -= 1
        

        mask_word = ""                                                                                  # On redéfinie mask_word de sorte :
        for i in word:                                                                                  # Pour chaque lettre du Mot
            if i in lettres_bonnes:                                                                         # Si elle est dans la liste des bonnes lettres on l'ajoute dans mask_word avec un espace (pour la lisibilité)
                mask_word += i + " "

            else:                                                                                           # Si elle n'y est pas on ajoute "_ "
                mask_word += "_ "
        
        
        if "_ " not in mask_word:                                                                       # Première condition d'arret : si il n'y run plus de '_' dans le mot masqué c'est gagné, run = False on arrête la boucle
            run = False
            print("=================== Bien joué ! :D ===================\n\n\n\n")
            print("Le mot à deviner était:", word)
            
            replay = input("\n\n\n\nSouhaitez vous rejouer ? (oui / non) ")                                 # On demande si on veut rejouer, si oui on fait appel à la fonction pendu
            if replay == "oui":
                pendu()

        if health == 0: 
            run = False                                                                                   # Deuxième condition d'arret : si la vie arrive à zero on arrête la boucle
            print("=================== Dommage c'est perdu! ===================\n\n\n\n")
            print("Le mot à deviner était:", word)
            
            replay = input("\n\n\n\nSouhaitez vous rejouer ? (oui / non) ")                                 # On demande si on veut rejouer, si oui on fait appel à la fonction pendu
            if replay == "oui":
                pendu()
            
        if difficult == 1 or difficult == 2:                                                               # Si la difficulté choisi n'est pas "Expert" on affiche les lettres déjà proposées
            print("Lettres déjà proposées:", lettres_deja_passees, "\n\n\n\n      **********      ")
            print("test")


pendu()

