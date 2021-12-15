# #Un grupo de científicos está analizando una forma de vida inteligente extraterrestre en la reconocida área 52.
# Han descubierto que, sorprendentemente, estos usan las mismas letras que nosotros (26 letras, excluyendo la ñ)
# aunque su alfabeto posee un orden distinto. Se nos encomienda la tarea de reordenar un diccionario en español para
# que los extraterrestres puedan buscar palabras en nuestra lengua más fácilmente. Diseñar un algoritmo que dada un
# string que representa todas las letras del alfabeto ordenadas según los extraterrestres y una lista de palabras,
# devuelva una lista de palabras ordenadas (en el orden que entiendan los extraterrestres)
#
# # Ejemplo:
#
# # lista = ['miel', 'extraterrestre', 'al', 'automovil', 'auto', 'revestir']
#
# # alfabeto = 'zyxwvutsrqponmlkjihgfedcba'
#
#
# def ordenar_extraterrestre(desordenadas, orden_alfabeto):
#
#     # ordenada = ['revestir', 'miel', 'extraterrestre', 'auto', 'automovil', 'al']
#
#     return ordenada

def ordenar_extraterrestre(lista, alfabeto):
    for i in range(1, len(lista)):
        try:
            actual = alfabeto.index(lista[i][0])
            palabra_actual = lista[i]
            indice = i

            while indice > 0 and alfabeto.index(lista[indice - 1][0]) > actual:
                lista[indice] = lista[indice - 1]
                indice -= 1
            else:
                aux_index = 0
                while indice > 0 and alfabeto.index(lista[indice - 1][aux_index]) == alfabeto.index(palabra_actual[aux_index]):
                    aux_index += 1
                    print(aux_index)
                    if indice > 0 and alfabeto.index(lista[indice - 1][aux_index]) > alfabeto.index(palabra_actual[aux_index]):
                        lista[indice] = lista[indice - 1]
                        indice -= 1
                        lista[indice] = palabra_actual
                lista[indice] = palabra_actual
            lista[indice] = palabra_actual
        except IndexError:
            if len(lista[indice - 1]) > len(palabra_actual):
                print(lista[indice - 1])
                print(palabra_actual)
                lista[indice] = lista[indice - 1]
                #indice -= 1
                lista[indice-1] = palabra_actual
            else:
                lista[indice] = palabra_actual
                #indice -= 1
                lista[indice -1] = lista[indice - 1]
        continue
    return lista


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alfabeto = "zyxwvutsrqponmlkjihgfedcba"
    lista = ['extraterrestre', 'miel', 'automovil', 'auto', 'revestir', 'al','a','z']
    lst = ['extraterrestre', 'miel', 'automovil', 'auto', 'revestir', 'al']
    # lista = ['extraterrestre', 'miel', 'automovil', 'auto', 'revestir', 'al']
    lista_ordenada = ordenar_extraterrestre(lista, alfabeto)
    ordenada = ['revestir', 'miel', 'extraterrestre', 'auto', 'automovil', 'al']
    print("Desordenada: ", lst)
    print("Ordenada: ", lista_ordenada)
    print("Ordenada OK: ", ordenada)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
