print('-'*10, 'Qual a Letra que Mais Repete?', '-'*10)

frase = input('escreva uma frase: ')

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letras_atual = frase[i]
    qtd_letra_atual = frase.count(letras_atual)

    if letras_atual == ' ':
        i+=1
        continue

    if qtd_apareceu_mais_vezes < qtd_letra_atual:
        qtd_apareceu_mais_vezes = qtd_letra_atual
        letra_apareceu_mais_vezes = letras_atual


    i+=1

print(
    'A letra que apareceu mais vezes foi '
    f'{letra_apareceu_mais_vezes.upper()} que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)