"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
inicio : fim : passo(quantidade que irá pular os caracteres, padrão é de um em um)

Obs.: a função len retorna a qtd 
de caracteres da str
"""

nome = 'kawe'
frase = 'o rato roeu a roupa do rei de roma'

print(nome[3])

#fatiamento

# em python o ultimo indice não é exibido, mas basta colocar um número a mais

print(nome[::-1]) #invertido
print(nome[:0:-len(nome)])
print(nome[2:]) #pega do indice 2 e vai até o final
print(nome[2:4]) #pega do indice 2 e vai até o indice 4
print(nome[:3]) #do inicio até o indice 3

print(frase[0:len(frase):1]) #texto normal
print(frase[::-1]) #texto invertido

print(len(nome))

#armazenando a quantidade de letras em uma variavel

nomequant = len(nome)

print(nomequant)