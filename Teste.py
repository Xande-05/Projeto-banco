from random import randint
from time import sleep
jogador = dict()
print ('JOGADORES')
for c in range (1, 5):
    jogador[c] = randint (1, 6)
for k, v in jogador.items():
    print (f'O jogador {k} sorteou o número {v}')
    sleep (1)
print ('----------------------')
print ('RANKING DOS JOGADORES.')
print ('----------------------')
for c in jogador:
    print (f'{c}° lugar')
print ('FIM DO PROGRAMA!')