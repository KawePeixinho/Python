qtd_linhas = 3
qtd_colunas = 3

linha = 1

while linha <= qtd_linhas:              
    coluna = 1                          #criação da variavel coluna
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')    #exibição da linha e da coluna
        coluna+=1                       #soma +1 na var coluna
    linha+=1                            #soma +1 na var linha

print('fim')