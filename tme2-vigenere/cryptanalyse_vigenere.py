# Sorbonne Université 3I024 2022-2023
# TME 2 : Cryptanalyse du chiffre de Vigenere
#
# Etudiant.e 1 : RATTANAVAN Laura 28633935
# Etudiant.e 2 : XU Audic 21101955

import sys, getopt, string, math

# Alphabet français
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fréquence moyenne des lettres en français
freq_FR = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
def recup_freq_FR(nom_fichier):
    """
    Renvoie le tableau de frequence des lettres de la langue
    francaise a partir du texte Germinal.
    """
    tab = [0.0 for i in range(26)]
    fichier = open(nom_fichier, "r")
    texte = fichier.read()

    for c in texte:
        index = (ord(c) - ord("A")) % 26
        tab[index] += 1

    tab = [tab[i]/len(texte) for i in range(26)]

    return tab

# Question 1)
freq_FR = recup_freq_FR("data/germinal_nettoye")

# print("freq_fr =", freq_FR)


def decalage(x, d):
    """
    Decale la lettre x de d.
    x: lettre -> String
    d: decalage -> Int
    """
    ord_x = ord(x)
    ord_y = ((ord_x + d - ord("A")) % 26) + ord("A")

    return str(chr(ord_y))

def decalage_inv(x, d):
    """
    Decale la lettre x de -d.
    x: lettre -> String
    d: decalage -> Int
    """
    ord_x = ord(x)
    ord_y = ((ord_x - d - ord("A")) % 26) + ord("A")

    return str(chr(ord_y))


# Chiffrement César
def chiffre_cesar(txt, key):
    """
    Chiffre le texte txt avec le chiffrement de Cesar avec la cle key.
    txt -> String
    key -> Int
    return -> String
    """
    res = str()
    for c in txt:
        res += decalage(c, key)

    return res

# Déchiffrement César
def dechiffre_cesar(txt, key):
    """
    Dechiffre le texte txt avec le chiffrement de Cesar avec la cle key.
    txt -> String
    key -> Int
    return -> String
    """
    res = str()
    for c in txt:
        res += decalage_inv(c, key)

    return res

# Chiffrement Vigenere
def chiffre_vigenere(txt, key):
    """
    Chiffre le texte txt avec le chiffrement de Vigenere avec la cle key.
    txt -> String
    key -> List[Int]
    return -> String
    """
    res = str()
    for c in txt:
        index = len(res) % len(key)
        temp_key = key[index]
        res += decalage(c, temp_key)
    return res


# Déchiffrement Vigenere
def dechiffre_vigenere(txt, key):
    """
    Dechiffre le texte txt avec le chiffrement de Vigenere avec la cle key.
    txt -> String
    key -> List[Int]
    return -> String
    """
    res = str()
    for c in txt:
        index = len(res) % len(key)
        temp_key = key[index]
        res += decalage_inv(c, temp_key)

    return res


# Analyse de fréquences
def freq(txt):
    """
    Renvoie le tableau du nombre des occurences de chaque lettre dans txt.
    txt -> String
    return -> List[Float]
    """
    hist = [0.0] * len(alphabet)

    for c in txt:
        index = (ord(c) - ord("A") ) % len(alphabet)
        hist[index] += 1

    return hist


# Renvoie l'indice dans l'alphabet
# de la lettre la plus fréquente d'un texte
def lettre_freq_max(txt):
    """
    Renvoie l'indice dans l'alphabet de la lettre la plus fréquente d'un texte.
    txt -> String
    return -> Int
    """
    hist = freq(txt)
    mx = hist[0]
    mx_index = 0

    for i in range(1, len(hist)):
        if mx < hist[i]:
            mx_index = i
            mx = hist[i]

    return mx_index


# indice de coïncidence
def indice_coincidence(hist):
    """
    Renvoie l'indice de coincidence:
        IC = Sum_{i=0}^{25} [(n_i)(n_i-1)] / [n(n-1)]
    hist -> List[Int]
    Return -> Float
    """
    # Calculons d'abord le nombre total de lettres
    n = 0
    for i in range(len(hist)):
        n += hist[i]

    # Calculons IC
    IC = 0.0
    for i in range(26):
        n_i = hist[i]
        IC += (n_i*(n_i -1)) / (n*(n-1))

    return IC


# Recherche la longueur de la clé
def longueur_clef(cipher):
    """
    Cherche la longueur de la clef entre 3 et 20. Si ne trouve pas, alors renvoie 0.
    cipher -> String
    return -> Int
    """
    # Remplissons les l colonnes
    for l in range(3, 21):
        colonnes = [str() for i in range(l)]
        for i in range(len(cipher)):
            index = i % l
            colonnes[index] += cipher[i]

        # Calculons les IC_i
        Liste_IC = [0.0] * l
        for i in range(l):
            hist = freq(colonnes[i])
            Liste_IC[i] = indice_coincidence(hist)

        # Calculons le IC moyen
        sum = 0
        for i in range(l):
            sum += Liste_IC[i]
        IC_moyen = sum/l

        if (IC_moyen > 0.06):
            return l

    return 0


# Renvoie le tableau des décalages probables étant donné la longueur de la clé
# en utilisant la lettre la plus fréquente de chaque colonne
def clef_par_decalages(cipher, key_length):
    """
    Renvoie le tableau des décalages probables étant donné la longueur de la clé
    en utilisant la lettre la plus fréquente de chaque colonne.
    cipher -> String
    key_length -> Int
    Return -> List[Int]
    """
    decalages = [0] * key_length
    # Construisons le mot decoupé en colonnes
    colonnes = [str()] * key_length
    i = 0
    for x in cipher:
        colonnes[i] += x
        i = (i+1) % key_length

    # Trouvons la lettre la plus frequente par colonnes
    for i in range(key_length):
        freq_max = lettre_freq_max(colonnes[i])
        decalages[i] = (freq_max - 4) % 26
        # indice(e) dans l'alphabet = 4

    return decalages


# Cryptanalyse V1 avec décalages par frequence max
def cryptanalyse_v1(cipher):
    """
    Cryptanalyse V1 se base en 2 etapes:
    - Trouver la longueur de la clé à l'aide de l'IC moyen par colonnes.
    - Trouve la cle en se basant sur la lettre la plus frequente.
    cipher -> String
    return -> String
    """
    key_length = longueur_clef(cipher)
    decalages = clef_par_decalages(cipher, key_length)
    res = dechiffre_vigenere(cipher, decalages)

    # Question 9
    # On a 18 tests sur 100 qui passent avec V1.
    # Les tests echoues sont dus a un mauvais tableau "decalages".
    # Cependant la taille de la cle est correcte.
    # Notre méthode de cryptanalyse se base sur la lettre la plus fréquente
    # que l'on assimile au 'e', qui n'est pas tout le temps vérifiée.
    return res


################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V2.

# Indice de coincidence mutuelle avec décalage
def indice_coincidence_mutuelle(h1,h2,d):
    """
    Calcule l'indice de coincidence mutuelle du texte 1 et du
    texte 2 qui a été décalé de d positions.
    h1 -> List[Int]
    h2 -> List[Int]
    d -> Int
    return -> Float
    """
    # Calcul du nombre total de lettres dans texte 1
    n1 = 0
    for i in range(len(h1)):
        n1 += h1[i]

    # Calcul du nombre total de lettres dans texte 2
    n2 = 0
    for i in range(len(h2)):
        n2 += h2[i]

    # Calcul de l'indice de coincidence mutuelle
    sum = 0
    for i in range(len(alphabet)):
        j = (i + d) % len(alphabet)
        sum += (h1[i]*h2[j])

    return sum / (n1 * n2)


# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en comparant l'indice de décalage mutuel par rapport
# à la première colonne
def tableau_decalages_ICM(cipher, key_length):
    """
    Renvoie le tableau des décalages probables étant
    donné la longueur de la clé
    en comparant l'indice de décalage mutuel par rapport
    à la première colonne.
    cipher -> String
    key_length -> Int
    return -> List[Int]
    """
    decalages = [0] * key_length

    # Découpage du texte cipher en key_length colonnes
    colonnes = [str()] * key_length
    index = 0
    for x in cipher:
        colonnes[index] += x
        index = (index + 1) % key_length

    # Cherchons pour chaque colonne i quel décalage d par rapport à la colonne 1
    # maximise l'ICM
    h1 = freq(colonnes[0]) # tableau des occurences de la colonne 1 (référence)
    for i in range(1, key_length):
        ICM_max = 0 # ICM max pour la colonne i
        ICM = 0 # ICM à comparer au ICM max
        d_ICM_max = 0 # décalage maximixant l'ICM

        for d in range(26):
            # h2: tableau des occurences de la colonne i qui aurait été
            # décalée de d positions
            h2 = freq(colonnes[i])
            ICM = indice_coincidence_mutuelle(h1,h2,d)
            if ICM_max < ICM:
                ICM_max = ICM
                d_ICM_max = d

        decalages[i] = d_ICM_max

    return decalages


# Cryptanalyse V2 avec décalages par ICM
def cryptanalyse_v2(cipher):
    """
    Cryptanalyse V2 se base en 2 etapes:
    - Trouver la longueur de la clé à l'aide de l'IC moyen par colonnes.
    - Trouve la cle en se basant sur la valeur ICM.
    cipher -> String
    return -> String
    """
    key_length = longueur_clef(cipher)
    tab = tableau_decalages_ICM(cipher, key_length)

    msg = str()
    for i in range(len(cipher)):
        lettre = str(cipher[i])
        msg += dechiffre_cesar(lettre, tab[i%key_length])
    # msg est crypte avec le cle de la premiere colonne

    # Identifions la lettre la plus frequente de msg pour deduire cette cle
    cle = (lettre_freq_max(msg) - 4) % 26
    # Puisqu'on considere e la lettre la plus frequente
    res = dechiffre_cesar(msg, cle)

    # Question 12
    # On valide donc 45 tests au lieu de 18 dans la V1.

    # Apres avoir analysé quelques tests non validés: 5, 6, 11, 12, 13, 16
    # - Bonne longueur de la cle
    # - Mauvais tableau de decalages
    # Cela est dû à: avoir l'ICM max ne correspond pas forcement au bon décalage.
    # Dans le test 6, on obtient:
    #   [0, 9, 12, 15, 17, 3, 3, .24., 6, 24]
    # Au lieu de :
    #   [0, 9, 12, 15, 17, 3, 3, .10., 6, 24]
    # Et l'ICM lorsque i=7 et d=24 vaut 0.07
    # Alors que le second ICM lorsque i=7 et d=10 vaut: 0.06
    # Donc le calcul d'ICM n'est pas toujours fiable.

    return res


################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V3.

# Prend deux listes de même taille et
# calcule la correlation lineaire de Pearson
def correlation(X, Y):
    """
    Calcule la correlation de Pearson.
    Les entrees X et Y correspondent a des histogrammes de
    frequences.
    On considere X et Y des listes de meme la taille.
    X -> List[Int]
    Y -> List[Int]
    return -> Float
    """
    n = len(X)

    # Calculons les esperances
    Xb = 0 # Esperance de X
    Yb = 0 # Esperance de Y
    for i in range(n):
        Xb += X[i]
        Yb += Y[i]
    Xb /= n
    Yb /= n

    # Calculons le numerateur
    numerateur = 0
    for i in range(n):
        numerateur += (X[i] - Xb) * (Y[i] - Yb)

    # Calculons les 2 termes du denominateur
    t1 = 0
    t2 = 0
    for i in range(n):
        t1 += (X[i] - Xb)**2
        t2 += (Y[i] - Yb)**2

    return numerateur / ((t1*t2)**0.5)


# Renvoie la meilleur clé possible par correlation
# étant donné une longueur de clé fixée
def clef_correlations(cipher, key_length):
    """
    Renvoie la meilleur clé possible par correlation
    étant donné une longuer de clé fixée.
    cipher -> String
    key_lengh -> Int
    return -> String
    """
    key = [0] * key_length
    score = 0.0

    # Découpage du texte cipher en key_length colonnes
    colonnes = [str()] * key_length
    index = 0
    for x in cipher:
        colonnes[index] += x
        index = (index + 1) % key_length

    X = freq_FR # histogramme de fréquence d'un texte FR

    # Cherchons pour chaque colonne i le décalage
    # d qui maximise la corrélation avec freq_FR
    for i in range(key_length):
        mx_corre = 0
        d_mx = 0
        for d in range(len(alphabet)):
            temp = dechiffre_cesar(colonnes[i], d)
            Y = freq(temp)
            temp_corre = correlation(X, Y)

            if temp_corre > mx_corre:
                mx_corre = temp_corre
                d_mx = d
        key[i] = d_mx
        score += mx_corre

    score /= key_length
    return (score, key)


# Cryptanalyse V3 avec correlations
def cryptanalyse_v3(cipher):
    """
    Cryptanalyse V3 se base sur le score de correlation de Pearson,
    Afin de trouver la cle secrete, en meme temps que la longueur de la cle.
    cipher -> String
    return -> String
    """
    TAILLE_MAX = 21

    # Trouvons la cle secrete a l'aide de la correlation de Pearson.
    score_mx = 0
    key_mx = []
    for l in range(1, TAILLE_MAX):
        score, key = clef_correlations(cipher, l)
        if score_mx < score:
            score_mx = score
            key_mx = key

    res = dechiffre_vigenere(cipher, key_mx)
    return res

    # Question 15
    # On valide 94 tests sur 100.

    # En comparant les textes qui ne sont pas passés ([81, 86, 88, 89, 94, 96]):
    # Pour les textes 89 et 94, il s'agit d'une mauvaise longueur de clé.
    # Cependant, on remarque que la longueur qu'on obtient
    # est un diviseur de la longueur de la vraie clé.

    # Pour les autres textes, un ou deux décalages sont incorrects.
    # En regardant le texte clair découpé en colonnes,
    # En observant colonne par colonne, il y a peu de lettre E et/ou
    # beaucoup d'une autre lettre. Le test semble donc avoir échoué
    # car on a calculé une corrélation de Pearson élevée pour un
    # certain décalage mais qui n'est pas le bon décalage.


################################################################
# NE PAS MODIFIER LES FONCTIONS SUIVANTES
# ELLES SONT UTILES POUR LES TEST D'EVALUATION
################################################################


# Lit un fichier et renvoie la chaine de caracteres
def read(fichier):
    f=open(fichier,"r")
    txt=(f.readlines())[0].rstrip('\n')
    f.close()
    return txt

# Execute la fonction cryptanalyse_vN où N est la version
def cryptanalyse(fichier, version):
    cipher = read(fichier)
    if version == 1:
        return cryptanalyse_v1(cipher)
    elif version == 2:
        return cryptanalyse_v2(cipher)
    elif version == 3:
        return cryptanalyse_v3(cipher)

def usage():
    print ("Usage: python3 cryptanalyse_vigenere.py -v <1,2,3> -f <FichierACryptanalyser>", file=sys.stderr)
    sys.exit(1)

def main(argv):
    size = -1
    version = 0
    fichier = ''
    try:
        opts, args = getopt.getopt(argv,"hv:f:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-v"):
            version = int(arg)
        elif opt in ("-f"):
            fichier = arg
    if fichier=='':
        usage()
    if not(version==1 or version==2 or version==3):
        usage()

    print("Cryptanalyse version "+str(version)+" du fichier "+fichier+" :")
    print(cryptanalyse(fichier, version))

if __name__ == "__main__":
    main(sys.argv[1:])
