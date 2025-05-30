'''
INSERTION SORT
COMPLEXITAT: O(n²)
'''

class InsertionSort:
    def insertion_sort(self, llista):
        n = len(llista)

        for i in range(1, n):
            key = llista[i]
            j = i - 1

            while j >= 0 and key < llista[j]:
                llista[j + 1] = llista[j]
                j -= 1
            llista[j + 1] = key

            print(f"Iteració: {i}")
            print(llista)

        return llista
