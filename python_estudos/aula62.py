"""
while -> break e continue

o break serve para quebrar o loop

o continue faz uma pausa dependendo da condição que 
fizermos e logo em seguida retorna com o loop
"""

cont = 0

while cont < 25:
    cont+=1

    if cont == 15:
        print('quinze')
        continue
    print(cont)

print('fim')


#se utilizarmos if cont >=10 and cont <=15: continue
#os numeros do 10 ao 15, nao serao exibidos caso nao coloquemos nada
#alem do continue dentro da condição