a = {1, 2, 3}
print(type(a))
a = set ('thiago')
print(a)
print('t' in a, 6 not in a, 'b' in a)
print({1, 2, 3} == {3,2,1,1})
print('')

#operacoes
c1 = {1,2}
c2 = {2,3}
print(c1.union(c2))
print(c1.intersection(c2))
#print(c1.update(c2))
print(c1)
print({1,2,3} - {2})
print(c1 - c2)
