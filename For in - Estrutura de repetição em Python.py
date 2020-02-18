"""
For in em Python

Iterando string com for
Função range(start=0, stop, step=1)

"""

# texto = 'Python'

# for letra in texto:
#    print(letra)


# for n in range(20, 10, -1):
#    print(n)

texto = 'Python'
nova = ''

for letra in texto:
    if letra == 't':
        nova += letra.upper()
    elif letra == 'h':
        nova += letra.upper()
    else:
        nova += letra

print(nova)

