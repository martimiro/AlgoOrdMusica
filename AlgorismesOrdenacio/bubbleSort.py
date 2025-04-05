'''
BUBBLE SORT
COMPLEXITAT: O(n²)
'''

class BubbleSort:
    def bubble_sort(self, llista):
        n = len(llista)

        for i in range(n-1):
            print("Iteració: " + str(i))
            print(llista)

            swapped = False
            for j in range(n-i-1):
                if llista[j] > llista[j+1]:
                    llista[j], llista[j+1] = llista[j+1], llista[j]
                    swapped = True
            if not swapped:
                break

        return llista;