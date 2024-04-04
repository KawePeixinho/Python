import time

seg = int(input('digite a quantidade de tempo em segundos: '))

while seg > 0:
    print(seg)
    time.sleep(1)
    seg-=1

print('tempo esgotado')

