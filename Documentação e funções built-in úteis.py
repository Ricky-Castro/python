num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

# num_2 = int(num_2)
# num_1 = int(num_1)

# isnumeric isdigit isdecimal

# Checa numeros e positivos
# print(num_1.isnumeric())
# print(num_2.isnumeric())

# if num_1.isdigit() and num_2.isdigit():
 #   num_1 = int(num_1)
 #   num_2 = int(num_2)

  #  print (num_1 + num_2)
# else:
  #  print('Favor digitar apenas números!')

try:
    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
except:
    print('Error')


