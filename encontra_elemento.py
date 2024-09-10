def encontra_elemento():

    def encontra_elemento(elemento, array):

        for i in range(len(array)):
            if array[i] == elemento:
                return True, i
        return False, -1

    alimentos = ["batata", "cenoura", "picles", "ovos"]

    print("Qual alimento você quer verificar?")
    elemento_a_verificar = input()

    encontrado, indice = encontra_elemento(elemento_a_verificar, alimentos)

    if encontrado:
        print(f"{elemento_a_verificar} está na lista e é o elemento de índice {indice}.")
    else:
        print(f"{elemento_a_verificar} não está na lista.")