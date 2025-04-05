from AlgoOrdMusica.serie import Serie
from AlgoOrdMusica.AlgorismesOrdenacio.bubbleSort import BubbleSort

class Menu:
    def menu(self):
        entrada = 0

        while(entrada == 0 or entrada > 2 or entrada < 0):
            try:
                print("== MENU ==")
                print("[1] Introdueix la seva sèrie.")
                print("[2] Genera una sèrie aletoria.")

                entrada = input("Escull una opció: ")
                entrada = int(entrada)

                # Cas entrada incorrecta
                if(entrada != 1 and entrada != 2):
                    print("ERROR: L'entrada no és correcta.")
                # Cas entrada = 1
                elif(entrada == 1):
                    print("En construcció")
                # Cas entrada = 2
                else:
                    # Creem objecte llista
                    serie = Serie()
                    # Generem objecte llista                                        
                    llista = serie.generarLlista()                                      

                    print("La seria dodecafonica aleatoria és: ")
                    print(str(llista)+"\n")

                    bubble = BubbleSort()
                    print("Llista ordenada: \n")
                    llista_ord = bubble.bubble_sort(llista)


            except ValueError:
                print("ERROR: L'entrada no és correcta.")
                entrada = 0