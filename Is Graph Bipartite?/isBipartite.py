class Solution:
    def isBipartite(self, grafo: List[List[int]]):
        # cores: 0 = não colorido, 1 = vermelho, -1 = azul
        cores = [0] * len(grafo)
        
        def dfs(no, cor):
            cores[no] = cor
            for vizinho in grafo[no]:
                if cores[vizinho] == cor:
                    return False
                if cores[vizinho] == 0 and not dfs(vizinho, -cor):
                    return False
            return True
        
        for no in range(len(grafo)):
            if cores[no] == 0 and not dfs(no, 1):
                return False
        
        return True
