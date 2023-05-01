## Exercício "isBipartite"
O objetivo deste exercício é implementar um algoritmo para verificar se um grafo é bipartido ou não. 

Um grafo é bipartido se for possível dividir seus vértices em dois grupos independentes de tal forma que não haja arestas conectando vértices do mesmo grupo.

O grafo é representado por uma lista de adjacências, em que cada elemento é uma lista de inteiros que representam os vértices adjacentes ao vértice correspondente.

O algoritmo deve retornar `True` se o grafo é bipartido e `False` caso contrário.

### Exemplo de entrada e saída:
**Entrada:**
[[1,3], [0,2], [1,3], [0,2]]

**Saída:**
True


**Explicação:**

Este é um grafo simples com quatro vértices e quatro arestas. É possível colorir seus vértices em dois grupos independentes: o grupo {0, 2} e o grupo {1, 3}. Não há arestas conectando vértices do mesmo grupo, portanto o grafo é bipartido.

### Observações
- O número de vértices do grafo não excede 100.
- Cada lista de adjacências contém pelo menos um elemento e no máximo 100 elementos.
- Os valores dos vértices são inteiros entre 0 e 1000.
- Não há arestas duplicadas no grafo.