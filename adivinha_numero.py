
#Var

def adivinha_numero():

 alvo = 12
    
 try:

    chute = int(input("Digite um número entre 0 e 100: "))

    if chute == alvo:
            print("Parabéns, você acertou!")
    elif chute > alvo:
            print("Que pena, mais sorte na próxima. Tente um valor mais baixo.")
    else:
            print("Que pena, mais sorte na próxima. Tente um valor mais alto.")

 except  ValueError:
    print ("O valor digitado deve ser um número inteiro")
