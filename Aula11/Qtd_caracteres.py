usuario = input('Digite o nome do usuário: ')
qtd_caracteres = len(usuario)

# print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar, pelo menos, 6 caracteres!')
else:
    print('Usuário cadaastrado com successo!')