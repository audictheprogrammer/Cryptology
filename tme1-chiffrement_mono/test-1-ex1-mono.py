import subprocess

print("\n\n----------------------------------------------\n\n")
print("Test 1 : Exercice 1 - Fréquences")
print("---------------------")

print("Test fréquences")
Alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
precision = 10**(-3)
scriptname = "frequence.py"
filename = "textes/germinal_very_small_nettoye"
frequences = [0.0962566844919786, 0.0106951871657754, 0.026737967914438502,
              0.053475935828877004, 0.15508021390374332, 0.0,
              0.0053475935828877, 0.016042780748663103, 0.058823529411764705,
              0.0, 0.0053475935828877, 0.0427807486631016,
              0.03208556149732621, 0.06951871657754011, 0.058823529411764705,
              0.026737967914438502, 0.0, 0.06417112299465241,
              0.10160427807486631, 0.08021390374331551, 0.06951871657754011,
              0.0213903743315508, 0.0, 0.0053475935828877,
              0.0, 0.0]

proc = subprocess.Popen(["python3", scriptname, filename], stdout=subprocess.PIPE)
result = proc.communicate()[0].decode()
values = result.split()[1::2] # Keeps only an array of frequences

assert len(values) == len(Alph), "Missing letters"
for i in range(len(Alph)):
	assert abs(frequences[i] - float(values[i])) < precision, "Wrong frequence for " + Alph[i]
print("Test fréquences : OK")

print("\n\n----------------------------------------------\n\n")

