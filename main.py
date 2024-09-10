# Aula 13 - Exercício de revisão 1
# Usando o Github, crie um protótipo de um console de jogos. Ele deve exibir um menu com os jogos disponíveis e perguntar ao usuário qual deles deseja jogar. Se a resposta for válida, o jogo correspondente deve ser executado


import adivinha_numero
import carros
import encontra_elemento


print(f"Olá, seja bem vindo às minhas aplicações, desenvolvidas em Python.")

menu = """ Escolha o número referente à aplicação que deseja utilizar:

1 - Jogo de adivinhação
2 - Gerenciamento de estoque
3 - Encontre o elemento
"""

entrada_usuario = input(menu)

if entrada_usuario == "1":
    adivinha_numero.adivinha_numero()
elif entrada_usuario == "2":
    carros.carros()
elif entrada_usuario == "3":
    encontra_elemento.encontra_elemento() 

    #PRECISA ARRUMAR O GERENCIAMENTO DE ESTOQUE