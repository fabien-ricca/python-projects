from random import choice

def split(text):        # On recode la fonction systeme .split()
    list = []
    mot = ''

    for i in text:
        if mot:   # Empty string is false!
            if i.isalpha():
                mot += i
            else:
                list.append(mot)
                mot = ''
        else:
            if i.isalpha():
                mot += i
            else:
                pass
    if mot:
        list.append(mot)

    return list

def lenf(mot):            # On recode la fonction systeme len()
    a = 0
    for i in mot:
        a += 1
    int(a)
    return a

def maj(character):     # On crée un dictionnaire minuscule vers majuscule en incluant les lettres avec accents
    dictionary = {
        "a" : "A",
        "b" : "B",
        "c" : "C",
        "d" : "D",
        "e" : "E",
        "f" : "F",
        "g" : "G",
        "i" : "I",
        "j" : "J",
        "k" : "K",
        "l" : "L",
        "m" : "M",
        "n" : "N",
        "o" : "O",
        "p" : "P",
        "q" : "Q",
        "r" : "R",
        "s" : "S",
        "t" : "T",
        "u" : "U",
        "v" : "V",
        "w" : "W",
        "x" : "X",
        "y" : "Y",
        "z" : "Z",
        "à" : "A",
        "â" : "A",
        "ä" : "A",
        "é" : "E",
        "è" : "E",
        "ê" : "E",
        "ë" : "E",
        "î" : "I",
        "ï" : "I",
        "ö" : "O",
        "ô" : "O",
        "ù" : "U",
        "ü" : "U",
        "ü" : "U",
        "ÿ" : "Y",
        "ç" : "C",

    }
    if character in dictionary:     # Si la lettre est dans le dictionnaire on retourne sa valeur
        return dictionary[character]
    else:
        return character            # Sinon on retourne la lettre telle quel

def myUpper(a=""):      # On recode la fonction .upper()
    if type(a) is str or a == "":
        b = ""
        for character in a:     # Pour chaque lettre de la chaine on vérifie si elle est présente dans le dictionnaire
            b += maj(character) # Si oui on la remplace et retourne sa nouvelle valeur
    else:
        print("Il ne faut saisir que des lettres svp.")
        return

    return b

########################################################### Choix de la difficulté et du nombres de vies #####################################################################################
def level():
    difficult = int(input("Quelle difficulté choisissez-vous (1, 2 ou 3) : \n 1 novice \n 2 avancé \n 3 expert\nVotre choix: "))
    if difficult == 1:
        health = 9
    elif difficult == 2:
        health = 6
    elif difficult == 3:
        health = 3
    return difficult, health

# print(level())

###################################################### Selection d'un mot aléatoirement dans le dictionnaire ################################################################################

def wordF():
    mot = ""
    text = open("/home/padawan/git/python-projects/dico.txt", "r", encoding = "ISO-8859-1")
    file = text.read() 
    text.close()
    file = myUpper(file)
    list_word = split(file)
    list = []
    for i in list_word:
        if lenf(i) > 4:
            list.append(i)
    mot += choice(list_word)

    return mot
# print(wordF())
