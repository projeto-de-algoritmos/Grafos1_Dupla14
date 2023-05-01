## Exercício "Clone Graph"
O objetivo deste exercício é implementar um algoritmo que faça a cópia de um grafo, onde cada nó contém um valor inteiro e uma lista de nós adjacentes.

O grafo é representado por um objeto `Node`, onde `node.val` é o valor do nó e `node.neighbors` é uma lista de referências para seus nós adjacentes.

O algoritmo deve retornar uma cópia do grafo.

### Exemplo de entrada e saída
**Entrada:**
1 -- 2
| |
4 -- 3

node = [[2,4],[1,3],[2,4],[1,3],[1,3]]

**Saída:**
1 -- 2
| |
4 -- 3


**Explicação:**
O grafo original é dado pela entrada. A cópia do grafo é idêntica, mas cada nó é uma referência diferente.

### Observações
- O número de nós do grafo não excede 100.
- Cada nó do grafo possui um valor inteiro entre 1 e 100.
- Os nós do grafo são únicos, isto é, não há nós duplicados.
- Não há loops no grafo, isto é, nenhum nó é adjacente a si mesmo.
- O grafo pode ser desconexo, isto é, pode haver nós que não são alcançáveis a partir de outros nós.



