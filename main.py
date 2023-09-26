import grafo  # Importe o seu módulo grafo.py

def exibir_menu():
    print("Opções:")
    print("1. Ordem do grafo")
    print("2. Tamanho do grafo")
    print("3. Vizinhos de um vértice")
    print("4. Grau de um vértice")
    # Adicione mais opções para as outras funções

def main():
    meu_grafo = grafo.criar_grafo_de_teste()  # Substitua por sua própria lógica para criar um grafo

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (ou 'q' para sair): ")

        if escolha == '1':
            ordem = grafo.ordem_do_grafo(meu_grafo)
            print(f"Ordem do grafo: {ordem}")
        elif escolha == '2':
            tamanho = grafo.tamanho_do_grafo(meu_grafo)
            print(f"Tamanho do grafo: {tamanho}")
        elif escolha == '3':
            vertice = input("Informe o vértice: ")
            vizinhos = grafo.vizinhos_do_vertice(meu_grafo, vertice)
            print(f"Vizinhos do vértice {vertice}: {vizinhos}")
        elif escolha == '4':
            vertice = input("Informe o vértice: ")
            grau = grafo.grau_do_vertice(meu_grafo, vertice)
            print(f"Grau do vértice {vertice}: {grau}")
        # Adicione mais casos para outras opções do menu
        elif escolha == 'q':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
