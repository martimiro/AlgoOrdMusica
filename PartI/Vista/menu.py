from Vista.serie import Serie
from Model.bubbleSort import BubbleSort
from Model.bucketSort import BucketSort


"""
FER MENU.MOSTRAROPCIONS
"""

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

                # Cas entrada incorrecta
                if(entrada != 1 and entrada != 2 and entrada != 3):
                    print("ERROR: L'entrada no és correcta.")
                # Cas entrada = 1 (inserir la propia serie)
                elif(entrada == 1):
                    print("En construcció")
                # Cas entrada = 3 (sortir)
                elif(entrada == 3):
                    print("Gràcies, fins la propera!")
                    return 
                # Cas entrada = 2 (generar aleatori)
                else:
                    entrada = 0
                    # Creem objecte llista
                    serie = Serie()

                    # Generem objecte llista                                        
                    llista = serie.generarLlista()
                    print("\nLa seria dodecafonica aleatoria és: ")
                    print(str(llista)+"\n")
    
                    while(entrada == 0 or entrada < 0 or entrada > 1): 
                        try:                       
                            print("============ MENÚ ==============")
                            print("[1] Bubble Sort.")
                            print("[2] Bucket Sort.")
                            print("================================")

                            entrada = input("Escull una opció: ")
                            entrada = int(entrada)

                            # Cas entrada = 1 (bubbleSort)
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
                            # Cas entrada incorrecta
                            else:
                                print("ERROR: L'entrada no és correcta.")

                        except ValueError:
                            print("ERROR: L'entrada no és correcta.")
                            entrada = 0
            except ValueError:
                print("ERROR: L'entrada no és correcta.")
                entrada = 0