import subprocess

print("\n\n----------------------------------------------\n\n")
print("Test 1 : Exercice 1 - Chiffrements et déchiffrements")
print("---------------------")

scriptname = "cesar.py"

print("Test chiffrement César")

proc = subprocess.Popen(["python3", scriptname, "B", "c", "SALUTZ"], stdout=subprocess.PIPE)
result = proc.communicate()[0].decode()

assert result.strip() == "TBMVUA", "Wrong encryption"

print("Test chiffrement César : OK")
print("---------------------")

print("Test déchiffrement César")

proc = subprocess.Popen(["python3", scriptname, "B", "d", "SALUT"], stdout=subprocess.PIPE)
result = proc.communicate()[0].decode()

assert result.strip() == "RZKTS", "Wrong decryption"

print("Test déchiffrement César : OK")
print("---------------------")

scriptname = "subst_mono.py"
key = "XCRINLSAOZWUYTQVHFDJMKGEPB"

print("Test chiffrement mono")

proc = subprocess.Popen(["python3", scriptname, key, "c", "CECIESTUNTEST"], stdout=subprocess.PIPE)
result = proc.communicate()[0].decode()

assert result.strip() == "RNRONDJMTJNDJ", "Wrong encryption"

print("Test chiffrement mono : OK")
print("---------------------")

print("Test déchiffrement mono")

proc = subprocess.Popen(["python3", scriptname, key, "d", "CFXKQRXYXFRAN"], stdout=subprocess.PIPE)
result = proc.communicate()[0].decode()
assert result.strip() == "BRAVOCAMARCHE", "Wrong decryption"

print("Test déchiffrement mono : OK")

print("\n\n----------------------------------------------\n\n")
