#!/usr/bin/python3

import subprocess

print("\n\n----------------------------------------------\n\n")
print("Test 3 : Exercice 3 - Cryptanalyse d'un chiffrement mono-alphabétique")
print("---------------------")

scriptname = "crypt_auto_mono.py"
challenge = "textes/ex3/alexandre.binninger.challenge"
plaintext = "PUISENLESENVELOPPANTILNENOUSFAUTRIENAUTRECHOSEMAFOIPUISQUEJEMESUISDERANGEEDITLASARRIETTEDONNEZMOIUNELIVREDESAINDOUXMOIJADORELESPOMMESDETERREFRITESJEFAISUNDEJEUNERAVECDEUXSOUSDEPOMMESDETERREFRITESETUNEBOTTEDERADISOUIUNELIVREDESAINDOUXMADAMEQUENULACHARCUTIEREAVAITMISUNEFEUILLEDEPAPIERFORTSURUNEBALANCEELLEPRENAITLESAINDOUXDANSLEPOTSOUSLETAGEREAVECUNESPATULEDEBUISAUGMENTANTAPETITSCOUPSDUNEMAINDOUCELETASDEGRAISSEQUISETALAITUNPEUQUANDLABALANCETOMBAELLEENLEVALEPAPIERLEPLIALECORNAVIVEMENTDUBOUTDESDOIGTS"
print("Cryptanalyse itérative")

success = 0
for i in range (5):
	proc = subprocess.Popen(["python3", scriptname, challenge], stdout=subprocess.PIPE)
	result = proc.communicate()[0].decode()
	result_splitted = result.split()
	i = result_splitted.index("déchiffré")
	plaintext_student = result_splitted[i+1]
	differences = sum (1 for a, b in zip (plaintext_student.strip(), plaintext) if a != b)
	perc = differences / len(plaintext)
	if perc > 0.0 and perc <= 0.15 and len(plaintext_student.strip()) == len(plaintext):
		success += 1
		break

assert success >= 1, "Wrong plaintext"

print("Test cryptanalyse itérative : OK")


print("\n\n----------------------------------------------\n\n")


