from AlgoOrdMusica.Vista.serie import Serie
from AlgoOrdMusica.Model.bubbleSort import BubbleSort

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
                            print("================================")

                            entrada = input("Escull una opció: ")
                            entrada = int(entrada)

                            # Cas entrada incorrecta
                            if(entrada != 1):
                                print("ERROR: L'entrada no és correcta.")
                            # Cas entrada = 1 (bubbleSort)
                            elif(entrada == 1):
                                bubble = BubbleSort()
                                print("\nLlista ordenada: ")
                                bubble.bubble_sort(llista)

                        except ValueError:
                            print("ERROR: L'entrada no és correcta.")
                            entrada = 0
            except ValueError:
                print("ERROR: L'entrada no és correcta.")
                entrada = 0