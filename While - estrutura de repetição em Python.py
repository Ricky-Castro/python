"""
While em python
utilizado para realizar açoes enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores.
"""
"""
while True: # loop infinito pois nunca será false
    nome = input('Qual é o seu nome?')
    print(f'Olá {nome}!')
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1


print(f'Agora x é igual a {x}')


