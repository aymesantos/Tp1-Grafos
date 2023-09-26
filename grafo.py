import networkx as nx


# Função para ler um grafo a partir de um arquivo GraphML e definir pesos nas arestas
def ler_grafo(file_path):
    grafo = nx.read_graphml(file_path)

    # Define pesos nas arestas com base nos atributos "weight"
    for u, v, data in grafo.edges(data=True):
        data['weight'] = float(data.get('weight', 1.0))

    return grafo

# Função para retornar a ordem do grafo
def ordem_do_grafo(grafo):
    return grafo.order()

# Função para retornar o tamanho do grafo
def tamanho_do_grafo(grafo):
    return grafo.size()

# Função para retornar os vizinhos de um vértice fornecido
def vizinhos_do_vertice(grafo, vertice):
    return list(grafo.neighbors(vertice))

# Função para determinar o grau de um vértice fornecido
def grau_do_vertice(grafo, vertice):
    return grafo.degree(vertice)

# Função para retornar a sequência de graus do grafo
def sequencia_de_graus(grafo):
    return [grau for _, grau in grafo.degree()]

# Função para determinar a excentricidade de um vértice (considerando pesos)
def excentricidade(grafo, vertice):
    excentricidades = nx.eccentricity(grafo, v=vertice)
    return max(excentricidades.values())

# Função para determinar o raio do grafo (considerando pesos)
def raio_do_grafo(grafo):
    return nx.radius(grafo)

# Função para determinar o diâmetro do grafo (considerando pesos)
def diametro_do_grafo(grafo):
    return nx.diameter(grafo)


# Função para determinar o centro do grafo
def centro_do_grafo(grafo):
    return nx.center(grafo)

# Função para determinar a árvore de busca em largura
def arvore_de_busca_em_largura(grafo, vertice_inicial):
    bfs_tree = nx.bfs_tree(grafo, source=vertice_inicial)
    return bfs_tree

# Função para determinar distância e caminho mínimo (considerando pesos)
def distancia_e_caminho_minimo(grafo, origem, destino):
    try:
        caminho_minimo = nx.shortest_path(grafo, source=origem, target=destino, weight='weight')
        distancia = nx.shortest_path_length(grafo, source=origem, target=destino, weight='weight')
        return distancia, caminho_minimo
    except nx.NetworkXNoPath:
        return "Não há caminho entre os vértices."

# Função para determinar a centralidade de proximidade C de um vértice
def centralidade_de_proximidade_C(grafo, vertice):
    N = grafo.order()
    distancias = nx.single_source_shortest_path_length(grafo, vertice)
    total_distancias = sum(distancias.values())
    if total_distancias == 0:
        return 0.0
    return (N - 1) / total_distancias


