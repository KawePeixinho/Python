nome = input('nome: ')
procura = input('o que está procurando: ')

if procura in nome:
    print(f'{procura} está em {nome}')
else:
    print(f'{procura} não está em {nome}')