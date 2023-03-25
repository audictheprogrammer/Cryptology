#!/usr/bin/python3
import sys
from math import *
from random import *

# Usage python3 crypt_auto_mono.py file
# Where file contains the ciphertext
# It is recommended to write a few functions for this exercise


def e(mot, dict_tetra):
    """ Fonction recursive calculant la somme des logarithmes du nombre
     d'occurences des tetragrammes.
    """
    if len(mot) == 4:
        if mot in dict_tetra:
            return dict_tetra[mot]
        return 0.001
    sum = 0
    for i in range(3, len(mot)):
        mot_temp = mot[i-3] + mot[i-2] + mot[i-1] + mot[i]
        sum += log(e(mot_temp,dict_tetra))
    return sum

def sub_2char(texte, decryption_key, encryption_key):
    n1 = randint(0, 25)
    n2 = randint(0, 25)
    while (n2 == n1):
        n2 = randint(0, 25)

    char1 = decryption_key[n1]
    char2 = decryption_key[n2]

    new_decryption_key = swap(decryption_key, char1, char2)
    new_encryption_key = swap(encryption_key,char2,char1)

    res = str()
    for i in range(len(texte)):
        if texte[i] == char1:
            res += str(char2)
        elif texte[i] == char2:
            res += str(char1)
        else:
            res += texte[i]

    return res, new_decryption_key, new_encryption_key

def swap(string, char1, char2):
    res = str()
    for c in string:
        if c == char1:
            res += char2
        elif c == char2:
            res += char1
        else:
            res += c
    return res


nom_fichier = sys.argv[1]
fichier = open(nom_fichier, "r")

dict_tetra = {}
f = open("nb_tetra_fr.csv", "r")

for ligne in f: # Convertion du fichier de tétras en dictionnaire
    dict_tetra[str(ligne[:4])] = int(ligne[5:])

ciphertext = fichier.read().replace('\n',"")  # Lire et enlever les sauts de ligne du texte chiffré
ciphertext_eval = e(ciphertext,dict_tetra)
encryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = ""
plaintext_eval = 0
decryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

iter = 0
nb_iter = 5000
eps = 1
cpt = 0
old_text = ciphertext
old_eval = ciphertext_eval
while (iter < nb_iter and cpt <= 400):
    plaintext, new_decryption_key, new_encryption_key = sub_2char(old_text, decryption_key, encryption_key)
    plaintext_eval = e(plaintext,dict_tetra)
    if old_eval + eps < plaintext_eval:
        old_text = plaintext
        old_eval = plaintext_eval
        encryption_key = new_encryption_key
        decryption_key = new_decryption_key
        cpt = 0
    else:
        cpt += 1
    iter += 1

f.close()
fichier.close()

# Do not modify these lines except for variable names
print ("texte chiffré\n" + ciphertext)
print ("évaluation " + str(ciphertext_eval))
print ("\nAprès " + str(iter) + " itérations, texte déchiffré\n" + plaintext)
print ("substitution appliquée au texte fourni " + encryption_key)
print ("clef " + decryption_key)
print ("évaluation " + str(plaintext_eval))
