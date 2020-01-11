# Operador de membro
lista = [1,2,3,'Ana', 'Carla']
print(2 in lista)
print('Ana' not in lista)
print('')

# Operador de identidade
x = 3
y = 3
z = 3
print(x,y,z)
print(x is y)
print(z is y)
print(x is not z)
print('')

lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]
print(lista_a is lista_b)
print(lista_a is lista_c)
print(lista_b is not lista_c)