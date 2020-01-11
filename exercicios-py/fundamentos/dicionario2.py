pessoa = {'nome': 'Thiago', 'idade': 23, 'cursos': ['web moderno', 'powerbi', 'msproject', 'machine learning']}
pessoa['idade'] = 24
pessoa['cursos'].append('Python')
pessoa['nome'] = 'Thiago Pires'
print(pessoa)
print(pessoa.pop('idade'))
print(pessoa)
print(pessoa.update({'idade': 23, 'sexo':'masculino'}))
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)