"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
""" 
variavel = "kawe"
print(f'{variavel:->15}')
print(f'{variavel:=<15}')
print(f'{variavel:+^15}')

print(f'{10000000:,.2f}')

print(f'{10000000:-<25,.2f}')