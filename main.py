import grafo
import networkx as nx

def menu():
    print("\nOpções:")
    print("1. Carregar grafo")
    print("2. Ordem do grafo")
    print("3. Tamanho do grafo")
    print("4. Vizinhos de um vértice")
    print("5. Grau de um vértice")
    print("6. Sequência de graus do grafo")
    print("7. Excentricidade de um vértice")
    print("8. Raio do grafo")
    print("9. Diâmetro do grafo")
    print("10. Centro do grafo")
    print("11. Busca em Largura e Árvore de Largura (em GraphML)")
    print("12. Distância e Caminho Mínimo")
    print("13. Centralidade de Proximidade C")
    print("0. Sair")

if __name__ == "__main__":
    grafo_atual = None

    while True:
        menu()
        escolha = input("Escolha uma opção (ou 'q' para sair): ")

        if escolha == '1':
            arquivo_grafo = input("Informe o caminho para o arquivo GraphML: ")
            grafo_atual = grafo.ler_grafo(arquivo_grafo)
            if grafo_atual:
                print("Grafo carregado com sucesso.")
        elif escolha == '2':
            if grafo_atual:
                ordem = grafo.ordem_do_grafo(grafo_atual)
                print("Ordem do grafo:", ordem)
            else:
                print("Grafo não carregado.")
        elif escolha == '3':
            if grafo_atual:
                tamanho = grafo.tamanho_do_grafo(grafo_atual)
                print("Tamanho do grafo:", tamanho)
            else:
                print("Grafo não carregado.")
        elif escolha == '4':
            if grafo_atual:
                vertice = int(input("Informe o vértice: "))
                if(vertice<1 or vertice>grafo.ordem_do_grafo(grafo_atual)):
                    print("\nErro: VERTICE INVALIDO")
                else:
                    vizinhos = grafo.vizinhos_do_vertice(grafo_atual, vertice)
                print("Vizinhos de", vertice, ":", vizinhos)
            else:
                print("Grafo não carregado.")
        elif escolha == '5':
            if grafo_atual:
                vertice = int(input("Informe o vértice: "))
                if (vertice < 1 or vertice > grafo.ordem_do_grafo(grafo_atual)):
                    print("\nErro: VERTICE INVALIDO")
                else:
                    grau = grafo.grau_do_vertice(grafo_atual, vertice)
                    print("Grau de", vertice, ":", grau)
            else:
                print("Grafo não carregado.")
        elif escolha == '6':
            if grafo_atual:
                sequencia = grafo.sequencia_de_graus(grafo_atual)
                print("Sequência de graus do grafo:", sequencia)
            else:
                print("Grafo não carregado.")
        elif escolha == '7':
            if grafo_atual:
                vertice = input("Informe o vértice: ")
                excentricidade = grafo.excentricidade(grafo_atual, vertice)
                print("Excentricidade de", vertice, ":", excentricidade)
            else:
                print("Grafo não carregado.")
        elif escolha == '8':
            if grafo_atual:
                raio = grafo.raio_do_grafo(grafo_atual)
                print("Raio do grafo:", raio)
            else:
                print("Grafo não carregado.")
        elif escolha == '9':
            if grafo_atual:
                diametro = grafo.diametro_do_grafo(grafo_atual)
                print("Diâmetro do grafo:", diametro)
            else:
                print("Grafo não carregado.")
        elif escolha == '10':
            if grafo_atual:
                centro = grafo.centro_do_grafo(grafo_atual)
                print("Centro do grafo:", centro)
            else:
                print("Grafo não carregado.")
        elif escolha == '11':
            if grafo_atual:
                vertice_inicial = input("Informe o vértice inicial para a busca em largura: ")
                sequencia_visitados, arestas_nao_arvore = grafo.arvore_de_busca_em_largura(grafo_atual, vertice_inicial)
                print("Sequência de vértices visitados:", sequencia_visitados)
                print("Arestas que não fazem parte da árvore em largura:", arestas_nao_arvore)
                ##
                #bfs_tree = grafo.arvore_de_busca_em_largura_e_graphml(grafo_atual, vertice_inicial, "saida.graphml")
                #nx.write_graphml(bfs_tree, "arvore_busca_largura.graphml")
                #print("Árvore de busca em largura gerada e salva em 'arvore_busca_largura.graphml'.")
                ##
            else:
                print("Grafo não carregado.")
        elif escolha == '12':
            if grafo_atual:
                origem = input("Informe o vértice de origem: ")
                destino = input("Informe o vértice de destino: ")
                distancia, caminho_minimo = grafo.distancia_e_caminho_minimo(grafo_atual, origem, destino)
                if distancia != float('inf'):
                    print(f"Distância mínima de {origem} para {destino}: {distancia}")
                    print(f"Caminho mínimo: {caminho_minimo}")
                else:
                    print("Não há caminho entre os vértices.")
            else:
                print("Grafo não carregado.")
        elif escolha == '13':
            if grafo_atual:
                vertice = input("Informe o vértice para calcular a centralidade de proximidade C: ")
                centralidade_c = grafo.centralidade_de_proximidade_C(grafo_atual, vertice)
                print(f"Centralidade de proximidade C de {vertice}: {centralidade_c}")
            else:
                print("Grafo não carregado.")
        elif escolha == 'q':
            break
        else:
            print("Opção inválida. Tente novamente.")
