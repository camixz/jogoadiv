import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroS = random.randrange(1,101) 
rodada = 1
#print(numeroS)
#Definindo o número de tentativas e rodada
numeroTentativas = 10

print("Qual o nível de dificuldade?")
print("(1)-Fácil, (2)-Médio, (3)-Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    numero_tentativas = 20


elif(nivel == 2):
    numero_tentativas = 10

else:
    numero_tentativas = 2



while(rodada <= numeroTentativas):
    print('Tentativa',rodada, 'de' , numeroTentativas)

#Recebendo o chute do jgdor
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroS == chute):
        print('Você acertou!')
        break
    elif(chute>numeroS):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
    #numeroTentativas = numeroTentativas - 1
    rodada = rodada + 3


