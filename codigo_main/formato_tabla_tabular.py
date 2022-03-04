def formato_tabla_tabular3(datos1, datos2, i):
    lista1 = list()
    for key, value in datos1.items():
        lista2 = list()
        lista2.append(key)
        lista2.append(i)
        if len(value) == 0:
            lista2.append(0)
            lista2.append(0)
        elif len(value) == 1:
            for elemento in value:
                if elemento[0] == i:
                    lista2.append(elemento[1])
                    valor2 = datos2.get(key)
                    for valor in valor2:
                        lista2.append(round(valor[0], 2))
                elif elemento[0] != i:
                    lista2.append(0)
                    lista2.append(0)
        elif len(value) >1:
            contador = 0
            for tupla in value:
                if tupla[0] == i:
                    contador += 1
                elif tupla[0] != i:
                    pass
            if contador == 0:
                lista2.append(0)
                lista2.append(0)
            elif contador > 0:
                for tupla in value:
                    if tupla[0] == i:
                        lista2.append(tupla[1])
                        valor2 = list()
                        valor2 = datos2.get(key)
                        for valor in valor2:
                            if valor[1] == i:
                                lista2.append(round(valor[0],2))
        lista1.append(lista2)
    return lista1
