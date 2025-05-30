# Algorismes d'ordenació aplicats a la música

## **Apunts teòrics**

### Bubble Sort
#### *Complexitat: O(n²)*

Recorre l'array valor per valor. Cada un d'aquests el compara amb el valor següent. En el cas que aquest últim sigui més petit que el primer, s'intercanvien posicions de manera que el més petit va al davant i el més gran es queda darrera. Aplica aquest procediemnt tantes vegades com sigui necessari per acabar d'ordenar tota la llista.

### Bucket Sort
#### *Complexitat: O(n²)*

Es distribueix tots els elements a ordenar en un nombre finit de caselles. Cada una d'aquestes, només pot acollir elements que compleixin una certa condició. Aquestes condicions hauran de ser exclusives per evitar que un element es pugui incloure en dues caselles. Al final, amb un altre algorisme d'ordenació, ordenem cada una d'aquestes caselles.

### Insertion Sort
#### *Complexitat: O(n²)*

Aquest algorisme construeix una subllista que es va ordenant inserint cada element a la posició que li pertoca en aquesta subllista.

### Merge Sort
#### *Complexitat: O(nlog(n))*

Segueix la filosofia de Dividir i Vèncer. Funciona d'una forma recursiva i es basa en anar dividint l'array en dues parts, ordenar aquestes i finalment tornar-les a ajuntar fent un merge.