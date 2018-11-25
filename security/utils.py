from string import ascii_letters
from string import digits
from random import choice


def createHash():
    arr = ascii_letters + digits
    hash = ''
    for i in range(0, 12):
        hash += choice(arr)
    return hash
