#!/usr/bin/python3
import sys

# Usage: python3 cesar.py clef c/d phrase
# Returns the result without additional text
# Only for capital characters

def f(x, shift):
    """ Encrypt the letter x with Caesar cipher. """
    ord_x = ord(x)
    ord_y = ((ord_x + shift - ord("A")) % 26) + ord("A")
    return str(chr(ord_y))

def f_1(x, shift):
    """ Decrypt the letter x with Caesar cipher. """
    ord_x = ord(x)
    ord_y = ((ord_x - shift - ord("A")) % 26) + ord("A")
    return str(chr(ord_y))

def usage():
    print("Usage: python3 cesar.py <A-Z> <c, d> <Ciphertext>")
    sys.exit(1)

def main():
    assert len(sys.argv) == 4, usage()

    shift_l = sys.argv[1]
    option = sys.argv[2]
    text = sys.argv[3]
    shift = ord(shift_l) - ord('A')

    ans = str()
    for c in text:
        if option == "c":
            ans += f(c, shift)
        elif option == "d":
            ans += f_1(c, shift)
        else:
            usage()
    print(ans)
    return

main()

"""
# tests
$ python3 cesar.py R c ATTAQUESURLUTECEDEMAIN
>>> RKKRHLVJLICLKVTVUVDRZE
$ python3 cesar.py N d IVIRYNPELCGBYBTVR
>>> VIVELACRYPTOLOGIE
"""
