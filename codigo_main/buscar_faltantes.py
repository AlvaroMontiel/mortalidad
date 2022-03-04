def faltante(edad_quinquenal):
    llave = edad_quinquenal
    valor = edad_quinquenal
    unicos = dict(zip(llave, valor))
    valores = list()
    for llave in unicos.keys():
        valores.append(llave)
    lista_ordenada = sorted(valores)
    lista_ideal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    for i in lista_ordenada:
        for a in lista_ideal:
            if i == a:
                lista_ideal.remove(i)


    return lista_ideal

