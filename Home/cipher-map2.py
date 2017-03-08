def recall_password(cipher_grille, ciphered_password, steps=4):
    password=''
    mixed=zip(cipher_grille, ciphered_password)
    password+="".join([x[1][i] for x in mixed for i in range(len(x[0])) if x[0][i]=='X'])
    return password+(recall_password([row[::-1] for row in zip(*cipher_grille)], ciphered_password, steps-1) if steps > 1 else '')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
