from Controller.serie import Serie
from Model.bubbleSort import BubbleSort
from Model.bucketSort import BucketSort
from Model.insertionSort import InsertionSort
from Model.mergeSort import MergeSort

class Menu:
    def menu(self):
        entrada = 0

        while(entrada == 0 or entrada > 3 or entrada < 0):
            try:
                print("============ MENÚ ==============")
                print("[1] Introdueix la seva sèrie.")
                print("[2] Genera una sèrie aletoria.")
                print("[3] Sortitr.")
                print("================================")

                entrada = input("Escull una opció: ")
                entrada = int(entrada)

                if(entrada != 1 and entrada != 2 and entrada != 3):
                    print("ERROR: L'entrada no és correcta.")
                elif(entrada == 1):
                    print("En construcció")
                elif(entrada == 3):
                    print("Gràcies, fins la propera!")
                    return 
                else:
                    entrada = 0
                    serie = Serie()

                    llista = serie.generarLlista()
                    print("\nLa seria dodecafonica aleatoria és: ")
                    print(str(llista)+"\n")
    
                    while(entrada == 0 or entrada < 0 or entrada > 1): 
                        try:                       
                            print("============ MENÚ ==============")
                            print("[1] Bubble Sort.")
                            print("[2] Bucket Sort.")
                            print("[3] Insertion Sort.")
                            print("[4] Merge Sort.")
                            print("[5] Sortir.")
                            print("================================")

                            entrada = input("Escull una opció: ")
                            entrada = int(entrada)

                            if(entrada == 1):
                                bubble = BubbleSort()
                                print("\nLlista ordenada: ")
                                bubble.bubble_sort(llista)
                                return
                            elif(entrada == 2):
                                bucket = BucketSort()
                                print("\nLlista ordenada: ")
                                bucket.bucket_sort(llista)
                                return
                            elif(entrada == 3):
                                inserction = InsertionSort()
                                print("\nLlista ordenada: ")
                                inserction.insertion_sort(llista)
                            elif(entrada == 4):
                                merge = MergeSort()
                                print("\nLlista ordenada: ")
                                merge.merge_sort(llista, 0, len(llista) - 1)
                            elif(entrada == 5):
                                print("Gràcies, fins la propesra!")
                                return 
                            else:
                                print("ERROR: L'entrada no és correcta.")

                        except ValueError:
                            print("ERROR: L'entrada no és correcta.")
                            entrada = 0
            except ValueError:
                print("ERROR: L'entrada no és correcta.")
                entrada = 0