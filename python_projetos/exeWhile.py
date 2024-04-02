nome = input('digite o seu nome: ')
tamanho_nome = len(nome)

cont = 0
simb = 0
new_name = ''
while cont < tamanho_nome:
    letra = nome[cont]           #adiciona cada letra por vez na variavel
    new_name += '*'+letra        #armazana as letras e soma com * no meio de cada uma delas
    cont+=1                      #adiciona +1 no cont
print(new_name)                  #exibe na tela

#-----------------parte de testes---------------------------------------
    # while simb < cont:      #condição para adicionar * entre as letras
    #     simb+=1
    #     print('*')

# tamanho_nome *= nome[::] + '*'
# print(tamanho_nome)