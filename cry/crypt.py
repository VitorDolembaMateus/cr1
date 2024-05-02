def crypt(i, o, p):
    """
    encrypt and decrypt archives using a password by bitwise
    :type i: string
    :type o: string
    :type p: string
    :param i: path to archive to be encrypted ou decrypted
    :param o: path to output archive
    :param p: password of encrypt
    :return: True if encrypted the file, and false if failure
    """
    #verify if file exists
    try:
        filei = open(i, 'rb')
        file = filei.read()
        filei.close()
    except FileNotFoundError:
        print(f'\033[31mFile Not found!\033[m')
        return False

    if len(p) > 0:
        p = list(p)
        for i, c in enumerate(p):
            p[i] = ord(c)
    else:
        print(f'\033[33mEmpty password: The file will not be encrypted\033[m')
        return False

    try:
        fileo = open(o, 'xb')
    except FileExistsError:
        while True:
            r = input(f'\033[1;31mFile already exists!\033[0;33m overwrite?(y/n)\033[m ').strip().lower()
            if r in 'yn':
                if r in 'y':
                    fileo = open(o, 'wb')
                    break
                else:
                    print(f'\033[33mCanceled\033[m')
                    return False

    cp = 0
    print()
    for i, byte in enumerate(file):
        if cp >= len(p):
            cp = 0
        try:
            fileo.write((byte ^ p[cp]).to_bytes())
        except OverflowError:
            print(f'caractere ({chr(p[cp])}) inválido')
            return False
        cp += 1
        print(f"\r{(i / len(file)) * 100:.2f}%", end='')
    print()
    fileo.close()
    print(f'\033[1mEncrypt/Decrypt done successfully!\033[m')
    return True
