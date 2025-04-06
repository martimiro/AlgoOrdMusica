'''
BUBBLE SORT
COMPLEXITAT: O(n²)
'''

class BubbleSort:
    def bubble_sort(self, llista):
        n = len(llista)

        for i in range(n-1):
            # Prints de la llista per terminal
            print("Iteració: " + str(i))
            print(llista)

            swapped = False
            for j in range(n-i-1):
                # Comparem element de la llista amb el seu següent
                if llista[j] > llista[j+1]:
                    # Si el primer element de la llista és mes gran que el següent, fem swap.
                    llista[j], llista[j+1] = llista[j+1], llista[j]
                    swapped = True
            if not swapped:
                break

        return llista;