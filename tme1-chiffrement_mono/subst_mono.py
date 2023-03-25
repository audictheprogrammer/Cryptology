#!/usr/bin/python3
import sys

# Usage: python3 subst_mono.py clef c/d phrase
# Returns the result without additional text

def f(x, new_alpha):
    """ Encrypt the letter x with monoalphabetic substitution ciper. """
    n = ord(x) - ord("A")
    return new_alpha[n]

def f_1(x, new_alpha):
    """ Decrypt the letter x with monoalphabetic substitution ciper. """
    for i in range(len(new_alpha)):
        if new_alpha[i] == x:
            # i is the ith letter of old_alpha
            return str(chr(i + ord("A")))
    return str()

def main():
    assert len(sys.argv) == 4, "Wrong argv. Please input alphabet, option, text"
    new_alpha = sys.argv[1]
    option = sys.argv[2]
    text = sys.argv[3]
    assert len(new_alpha) == 26, "Incorrect alphabet"

    ans = str()
    for i in range(len(text)):
        if option == "c":
            # print("Le", text[i], "est devenu un", f(text[i], new_alpha))
            ans += f(text[i], new_alpha)
        else:
            ans += f_1(text[i], new_alpha)

    print(ans)
    return

main()
