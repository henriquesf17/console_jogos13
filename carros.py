# Crie um sistema de gerenciamento de estoque

def gerenciar_estoque_carros():
    carros = ["Kombi", "Fusca", "Ferrari F50", "Lamborghini", "Marea", "Uno"]

    def mostrar_carros():
        print("\nLista de carros no estoque:")
        for carro in carros:
            print(f"- {carro}")
        print()  # Para adicionar uma linha em branco

    def substituir_carro():
        carro_antigo = input("Qual carro será substituído? ")
        if carro_antigo in carros:
            carro_novo = input("Por qual carro ele será substituído? ")
            for i in range(len(carros)):
                if carros[i] == carro_antigo:
                    carros[i] = carro_novo
            print(f"{carro_antigo} foi substituído por {carro_novo}.\n")
        else:
            print(f"Erro: {carro_antigo} não está no estoque.\n")

    def adicionar_carro():
        nome = input("Qual o nome do carro a ser adicionado? ")
        carros.append(nome)
        print(f"{nome} foi adicionado ao estoque.\n")

    mensagem_inicial = '''
Boas-vindas ao sistema gerenciador de estoque!

Menu principal:
1 - Mostrar todos os carros
2 - Substituir carro
3 - Adicionar carro
0 - Sair
    '''

    print(mensagem_inicial)

    programa_em_execucao = True

    while programa_em_execucao:
        opcao_usuario = input("O que deseja fazer? ")

        if opcao_usuario == "1":
            mostrar_carros()
        elif opcao_usuario == "2":
            substituir_carro()
        elif opcao_usuario == "3":
            adicionar_carro()
        elif opcao_usuario == "0":
            print("Até mais!")
            programa_em_execucao = False
        else:
            print("Opção inválida\n")

# Chamando a função principal para iniciar o sistema
gerenciar_estoque_carros()