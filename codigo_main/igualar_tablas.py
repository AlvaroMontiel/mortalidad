def iguala_tabla(datos):
    lista_ideal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    for llave in datos.keys():
        for elemento in lista_ideal:
            if llave == elemento:
                lista_ideal.remove(llave)
    nuevos_elementos = list()
    for elemento in lista_ideal:
        nuevos_elementos.append(0)
    nuevo_diccionario = dict(zip(lista_ideal, nuevos_elementos))
    datos.update(nuevo_diccionario)
    datos_final = dict(sorted(datos.items()))

    return datos_final

def ajusta_tabla_cie(datos, tabular):
    try:
        if tabular == 3:
            lista_ideal = ["C00-C14", "C15", "C16",
                           "C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97",
                           "C18-C21", "C22", "C25",
                           "C32", "C33-C34", "C43",
                           "C50", "C53", "C54-C55",
                           "C56", "C61", "C67",
                           "C70-C72", "C82-C85", "C90",
                           "C91-C95", "D00-D48"]
            ## lista_ideal queda con los valores que el diccionario no tiene
            for llave in datos.keys():
                for elemento in lista_ideal:
                    if llave == elemento:
                        lista_ideal.remove(llave)
            ## crea el diccionario que contiene los elementos faltantes con su valor 0
            nuevos_elementos = list()
            for elemento in lista_ideal:
                nuevos_elementos.append((0,0))
            nuevo_diccionario = dict(zip(lista_ideal, nuevos_elementos))
            datos.update(nuevo_diccionario)
            datos_final = dict(sorted(datos.items()))
        elif tabular == 4:
            lista_ideal = ["C00", "C01-C02", "C03-C06", "C07-C08", "C09", "C10", "C11", "C12-C13", "C14",
                           "C15", "C16", "C17", "C18", "C19-C20", "C21", "C22", "C23-C24", "C25", "C30-C31",
                           "C32", "C33-C34", "C37-C38", "C40-C41", "C43", "C44", "C45", "C46", "C47-C49",
                           "C50", "C51", "C52", "C53", "C54", "C55", "C56", "C57", "C58", "C60", "C61", "C62",
                           "C63", "C64", "C65", "C66", "C67", "C68", "C69", "C70-C72", "C73", "C74", "C75",
                           "C81", "C82-C86, C96", "C88", "C90", "C91", "C92-C94", "C95", "D45", "D46",
                           "C26, C39, C76-C80", "C97", "D37-D44, D47-D48"]
            ## lista_ideal queda con los valores que el diccionario no tiene
            for llave in datos.keys():
                for elemento in lista_ideal:
                    if llave == elemento:
                        lista_ideal.remove(llave)
            ## crea el diccionario que contiene los elementos faltantes con su valor 0
            nuevos_elementos = list()
            for elemento in lista_ideal:
                nuevos_elementos.append((0,0))
            nuevo_diccionario = dict(zip(lista_ideal, nuevos_elementos))
            datos.update(nuevo_diccionario)
            datos_final = dict(sorted(datos.items()))
        elif tabular == 5:
            lista_ideal = ["C00-C14", "C15-C26", "C30-C39",
                           "C40-C41", "C43-C44", "C45-C49",
                           "C50", "C51-C58", "C60-C63",
                           "C64-C68", "C69-C72", "C73-C75",
                           "C76-C80", "C81-C96", "D10-D36",
                           "D37-D48"]
            ## lista_ideal queda con los valores que el diccionario no tiene
            for llave in datos.keys():
                for elemento in lista_ideal:
                    if llave == elemento:
                        lista_ideal.remove(llave)
            ## crea el diccionario que contiene los elementos faltantes con su valor 0
            nuevos_elementos = list()
            for elemento in lista_ideal:
                nuevos_elementos.append((0,0))
            nuevo_diccionario = dict(zip(lista_ideal, nuevos_elementos))
            datos.update(nuevo_diccionario)
            datos_final = dict(sorted(datos.items()))
    except:
        pass

    return datos_final

