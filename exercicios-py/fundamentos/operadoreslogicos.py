True or False
print(7!=3 and 2 > 3)
#and
print('')
print('and')
print(True and True)
print(True and False)
print(False and False)
#or
print('')
print('OR')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
#XOR
print('')
print("XOR")
print(True != True)
print(True != False)
print(False != True)
print(False != False)
print('')
print('operador unário de negação')
print('')
print(not True)
print(not False)
print('')
print(not 0)
print(not 1)
print (not not 1)
print(not not 0)
print('')
#cuidado
print(True & True)
print(False | True)
print(True ^ False)
#exercicios
print('')
print('')
saldo = 1000
salario = 4000
despesas = 1000
saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)

print('')
print('exercicios')
trabalho_terca = True
trabalho_quinta= True

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
nada = not sorvete
print('tv50={} tv32={} sorvete={} nada={}'.format (tv_50, sorvete, tv_32, nada))


