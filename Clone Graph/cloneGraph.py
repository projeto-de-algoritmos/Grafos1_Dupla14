# Definição da classe Node
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Função principal
class Solution:
    def cloneGraph(self, node: 'Node'):
        if not node:
            return None
        
        # Dicionário que mapeia cada nó original para seu clone
        clone_map = {}
        visited = set()
        
        def clone(node):
            # Se o nó já foi visitado, retorna seu clone correspondente
            if node in clone_map:
                return clone_map[node]
            
            # Cria um novo clone do nó
            clone_node = Node(node.val)
            
            # Adiciona o clone ao dicionário
            clone_map[node] = clone_node
            
            # Visita todos os vizinhos do nó original e cria clones dos mesmos
            for neighbor in node.neighbors:
                clone_neighbor = clone(neighbor)
                clone_node.neighbors.append(clone_neighbor)
            
            return clone_node
        
        # Chama a função clone para criar o clone do nó inicial
        return clone(node)
