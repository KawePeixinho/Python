print('='*35)

nome = input('diga-me o seu nome: ')
peso = float(input('diga-me o seu peso: '))
altura = float(input('diga-me a sua altura: '))
imc = peso / altura**2

print(f'o seu Indice de Massa Corporal (IMC) é: {imc:.1f}')

print('='*35)