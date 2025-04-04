from AlgoOrdMusica.serie import Serie
from AlgoOrdMusica.AlgorismesOrdenacio.bubbleSort import BubbleSort

def main():
    serie = Serie()                                                     # Creem objecte llista
    llista = serie.generarLlista()                                      # Generem objecte llista

    print("La seria dodecafonica aleatoria és: ")
    print(llista)

    bubble = BubbleSort()
    print("Llista ordenada: ")
    llista_ord = bubble.bubble_sort(llista)
    print(llista_ord)


if __name__ == "__main__":
    main()