lista_uno = ['a', 'b', 'c', 'd', 'e', 'f']

for indice, letra in enumerate(lista_uno, start=1):
    print(f'{indice} - letra: {letra}')


diccionario = dict(enumerate(lista_uno, start=1))
print(diccionario)
