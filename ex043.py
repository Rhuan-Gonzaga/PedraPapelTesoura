from random import randint
from time import sleep
print("\n\n======= PEDRA PAPEL E TESOURA =======")

print("""SUAS OPÇÕES: 
     [0] PEDRA
     [1] PAPEL
     [2] TESOURA""")

vl = ("PEDRA", "PAPEL", "TESOURA")
jog1 = int(input("\nQUAL A SUA JOGADA? "))
jog2 = randint(0, 2) #gera um valor aleatorio
sleep(1) 

print("JO")
sleep(1) #demora 1seg p mostrar na tela
print("KEN")
sleep(1)
print("PO!!")
print("\n")

print("-=-" * 10)
print("O JOGADOR ESCOLHEU {}".format(vl[jog1])) 
print("O COMPUTADOR ESCOLHEU {}".format(vl[jog2]))
print("-=-" * 10)


if jog1 == 0 and jog2 == 2 or jog1 == 2 and jog2 == 1 or jog1 == 1 and jog2 == 0: #verifico se o JOGADOR venceu
    print("O JOGADOR VENCEU!!")
    print("\n")
elif jog2 == 0 and jog1 == 2 or jog2 == 2 and jog1 == 1 or jog2 == 1 and jog1 == 0: #verifico se o COMPUTADOR venceu
    print("O COMPUTADOR VENCEU!!")
    print("\n")
else:
    print("EMPATOU!!") #verifico se EMPATOU
    print("\n")
