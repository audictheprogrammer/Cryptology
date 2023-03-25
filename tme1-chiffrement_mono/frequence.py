#!/usr/bin/python3
import sys
# Usage: python3 frequence.py fichier_texte


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Occurences = {}
length = 0

# Ajoute les cles au dictionnaire avec une valeur de 0
for c in alphabet:
	Occurences[c] = 0

fichier_texte = sys.argv[1]
f = open(fichier_texte, "r")
texte = f.read()


for c in texte:
	if c in Occurences:
		# augmente de 1 la valeur
		Occurences[c] += 1
	length += 1

# affiche les occurences
for c in alphabet:
	if c in Occurences:
		print(c, Occurences[c]/length)


# Question 3: Les textes a distingues.
# 1 - 5
# 2 - 8
# 3 - 4
# 6 - 10
# 7 - 9
