import os
from getpass import getpass

from cry.crypt import crypt

try:
    while True:
        entrada = input('Path to input file: ').strip()
        if entrada == '':
            print(f"\033[1;31mThis can't be null!\033[m")
        else:
            break

    while True:
        saida = input('Path to output file: ').strip()
        if saida == '':
            print(f"\033[1;31mThis can't be null!\033[m")
        else:
            break

    password = getpass()
    crypt(p=password, i=entrada, o=saida)
except KeyboardInterrupt:
    print(f'\n\033[33mCanceled\033[m')
