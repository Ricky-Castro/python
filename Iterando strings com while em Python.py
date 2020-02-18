"""

Interando strings com while em Python

"""

minha_string = 'o rato roeu a roupa do rei de roma.'
tamanho_string = len(minha_string)

# print(minha_string.count('r'))

c = 0

nova = ''

while c < tamanho_string:

    if minha_string[c] == 'r':
        nova += minha_string[c].upper()
    else:
        nova += minha_string[c]

    c += 1

print(nova)

