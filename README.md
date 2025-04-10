# Algorismes d'ordenació aplicats a la música

## **Apunts teòrics**

### Bubble Sort
#### *Complexitat: O(n²)*

Recorre l'array valor per valor. Cada un d'aquests el compara amb el valor següent. En el cas que aquest últim sigui més petit que el primer, s'intercanvien posicions de manera que el més petit va al davant i el més gran es queda darrera. Aplica aquest procediemnt tantes vegades com sigui necessari per acabar d'ordenar tota la llista.

### Binnary Tree Short
#### *Complexitat: O(n²) no balancejat o O(n log n) balancejat*

Començem amb un arbre buit. Cada element de l'array es va inserint en un Binary Search Tree (BST). Quan l'arbre ja esta acabat, fem un inordre per obtenir la llista amb els valors ordenats.