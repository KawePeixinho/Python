"""
ID - a identificação do valor que está na memória 
id                  -> identidade 
-------------------------------------------------
"""
n1 = 'a'
n2 = 'b'

# print(id(n1))
# print(id(n2))

"""
Flag (bandeira)     -> marcar um local
None                -> Não valor
is e is not         -> é ou não é (tipo, valor, identidade)
-----------------------------------------------------------
"""
# var_teste = input('digite algo: ')
var_teste = True
passou_no_if = None

if var_teste:
    passou_no_if = True
    print('passou no if')
else:
    print('não passou no if')

if passou_no_if is None:
    print('não passou no if')
else:
    print('passou no if')