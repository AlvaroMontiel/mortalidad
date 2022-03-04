import pandas as pd
from codigo_main import num_def_cancer as mc
from codigo_main import tmb_cancer as tasas
from codigo_main  import igualar_tablas as tb
from tabulate import tabulate
import os
from codigo  import formato_tabla as tb2

def crear_tablas(dataframe_1, dataframe_2, periodo, tabular, region=0, comuna=0, sexo=0, edad_quinquenal = False):
    df = dataframe_1
    df2 = dataframe_2
    per = periodo
    tab = tabular
    reg = region
    com = comuna
    sex = sexo

    if edad_quinquenal == False:
        if tabular == 1 or tabular ==2:
            if sexo == 0:
                num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                    edad_quinquenal=False)
                tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                        edad_quinquenal=False)
                if tabular == 1:
                    tabla = list()
                    tabla2 = list()
                    for a, i in num_muertes.items():
                        tabla.append(a)
                        tabla.append(i[0])
                    tabla.append(round(tasa,2))
                    tabla2.append(tabla)
                    tabla_final = tabulate(tabla2, headers=['Causa', 'Nº Defunciones', 'Tasa Mortalidad Bruta'])
                elif tabular == 2:
                    tabla = list()
                    tabla2 = list()
                    for a, i in num_muertes.items():
                        tabla.append(a)
                        tabla.append(i[0])
                    tabla.append(round(tasa, 2))
                    tabla2.append(tabla)
                    tabla_final = tabulate(tabla2, headers=['Causa', 'Nº Defunciones', 'Tasa Mortalidad Bruta'])
            elif sexo != 0:
                if sexo == 1:
                    num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                        edad_quinquenal=False)
                    tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                            edad_quinquenal=False)
                    tabla = list()
                    tabla2 = list()
                    for a, i in num_muertes.items():
                        tabla.append(a)
                        tabla.append(i[0])
                    tabla.append(round(tasa, 2))
                    tabla2.append(tabla)
                    tabla_final = tabulate(tabla2, headers=['\nCausa', 'Nº Defunciones\nHombres', 'Tasa Mortalidad Bruta'])
                elif sexo == 2:
                    num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                        edad_quinquenal=False)
                    tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                            edad_quinquenal=False)
                    tabla = list()
                    tabla2 = list()
                    for a, i in num_muertes.items():
                        tabla.append(a)
                        tabla.append(i[0])
                    tabla.append(round(tasa, 2))
                    tabla2.append(tabla)
                    tabla_final = tabulate(tabla2, headers=['\nCausa', 'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta'])
                elif sexo == 3:
                    num_muertesh = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=1,
                                                        edad_quinquenal=False)
                    tasah = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=1,
                                            edad_quinquenal=False)
                    num_muertesm = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=2,
                                                        edad_quinquenal=False)
                    tasam = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=2,
                                            edad_quinquenal=False)
                    tabla = list()
                    tabla2 = list()
                    for a, i in num_muertesh.items():
                        tabla.append(a)
                        tabla.append(i[0])
                    tabla.append(round(tasah, 2))
                    for a, i in num_muertesm.items():
                        tabla.append(i[0])
                    tabla.append(round(tasam, 2))
                    tabla2.append(tabla)
                    tabla_final = tabulate(tabla2, headers=['\nCausa', 'Nº Defunciones\nHombres',
                                                            'Tasa Mortalidad Bruta\nHombres', 'Nº Defunciones\nMujeres',
                                                            'Tasa Mortalidad Bruta\nMujeres'])

        elif tabular == 3 or tabular == 4 or tabular == 5:
            if sexo == 0:
                num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=0,
                                                    edad_quinquenal=False)
                tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=0,
                                        edad_quinquenal=False)
                tabla = list()
                for llave, valor in num_muertes.items():
                    a = list()
                    a.append(llave)
                    a.append(valor[0])
                    tabla.append(a)
                i = 0
                for valor in tasa.values():
                    tabla[i].append(round(valor[0],2))
                    i += 1
                tabla_final = tabulate(tabla, headers = ['Causa', 'Nº Defunciones', 'Tasa de Mortalidad Bruta'])
            elif sexo != 0:
                if sexo == 1:
                    num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                        edad_quinquenal=False)
                    tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                            edad_quinquenal=False)
                    tabla = list()
                    for llave, valor in num_muertes.items():
                        a = list()
                        a.append(llave)
                        a.append(valor[0])
                        tabla.append(a)
                    i = 0
                    for valor in tasa.values():
                        tabla[i].append(round(valor[0], 2))
                        i += 1
                    tabla_final = tabulate(tabla, headers=['Causa', 'Nº Defunciones\nHombres', 'Tasa de Mortalidad Bruta\nHombres'])
                elif sexo == 2:
                    num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                        edad_quinquenal=False)
                    tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                            edad_quinquenal=False)
                    tabla = list()
                    for llave, valor in num_muertes.items():
                        a = list()
                        a.append(llave)
                        a.append(valor[0])
                        tabla.append(a)
                    i = 0
                    for valor in tasa.values():
                        tabla[i].append(round(valor[0], 2))
                        i += 1
                    tabla_final = tabulate(tabla, headers=['Causa', 'Nº Defunciones\nMujeres', 'Tasa de Mortalidad Bruta\nMujeres'])
                #### ambos sexos tienen diferencias en los códigos cie 10, por tumores específicos de hombres y mujeres,
                #### por lo tanto arroja error al recorrer las listas separadas por sexo
                ### NOTA: PENSAR UNA FORMA DE SOLUCIONARLO
                elif sexo == 3:
                    num_muertesh = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=1, edad_quinquenal=False)
                    tasah = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=1, edad_quinquenal=False)
                    num_muertesm = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=2, edad_quinquenal=False)
                    tasam = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=2, edad_quinquenal=False)

                    num_muertesh_igualada = tb.ajusta_tabla_cie(num_muertesh, tabular)
                    tasah_igualada = tb.ajusta_tabla_cie(tasah, tabular)
                    num_muertesm_igualada = tb.ajusta_tabla_cie(num_muertesm, tabular)
                    tasam_igualada = tb.ajusta_tabla_cie(tasam, tabular)
                    tabla = list()
                    for llave, valor in num_muertesh_igualada.items():
                        a = list()
                        a.append(llave)
                        a.append(valor[0])
                        tabla.append(a)
                    i = 0
                    for valor in tasah_igualada.values():
                        tabla[i].append(round(valor[0], 2))
                        i += 1
                    i = 0
                    for llave, valor in num_muertesm_igualada.items():
                        tabla[i].append(llave)
                        tabla[i].append(valor[0])
                        i += 1
                    i = 0
                    for valor in tasam_igualada.values():
                        tabla[i].append(round(valor[0], 2))
                        i += 1
                    tabla_final = tabulate(tabla, headers=['Causa', 'Nº Defunciones\nHombres',
                                                           'Tasa de Mortalidad Bruta\nHombres',
                                                           'Causa', 'Nº Defunciones\nMujeres',
                                                           'Tasa de Mortalidad Bruta\nMujeres'])
    elif edad_quinquenal == True:
        if tabular == 1 or tabular ==2:
            if sexo == 0:
                num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                    edad_quinquenal=True)
                tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                        edad_quinquenal=True)
                ## if len(tasa) == 17:
                if tabular == 1:
                    tabla = list()
                    for key, value in num_muertes.items():
                        a = list()
                        a.append(key)
                        a.append('C00-D48')
                        a.append(value)
                        tabla.append(a)
                    i = 0
                    for value in tasa.values():
                        tabla[i].append(round(value,2))
                        i += 1
                    tabla_final = tabulate(tabla, headers=['Grupo edad', 'Causa', 'Nº Defunciones', 'Tasa Mortalidad Bruta'])
                elif tabular == 2:
                    tabla = list()
                    for key, value in num_muertes.items():
                        a = list()
                        a.append(key)
                        a.append('C00-C97')
                        a.append(value)
                        tabla.append(a)
                    i = 0
                    for value in tasa.values():
                        tabla[i].append(round(value, 2))
                        i += 1
                    tabla_final = tabulate(tabla, headers=['Grupo edad', 'Causa', 'Nº Defunciones', 'Tasa Mortalidad Bruta'])
                ## elif len(tasa) < 17:
                ##    pass
            elif sexo == 1:
                num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                    edad_quinquenal=True)
                tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                        edad_quinquenal=True)
                if tabular == 1:
                    tabla = list()
                    for key, value in num_muertes.items():
                        a = list()
                        a.append(key)
                        a.append('C00-D48')
                        a.append(value)
                        tabla.append(a)
                    i = 0
                    for value in tasa.values():
                        tabla[i].append(round(value, 2))
                        i += 1
                    tabla_final = tabulate(tabla,
                                           headers=['Grupo edad', 'Causa', 'Nº Defunciones\nHombres', 'Tasa Mortalidad Bruta\nHombres'])
                elif tabular == 2:
                    tabla = list()
                    for key, value in num_muertes.items():
                        a = list()
                        a.append(key)
                        a.append('C00-C97')
                        a.append(value)
                        tabla.append(a)
                    i = 0
                    for value in tasa.values():
                        tabla[i].append(round(value, 2))
                        i += 1
                    tabla_final = tabulate(tabla,
                                           headers=['Grupo edad', 'Causa', 'Nº Defunciones\nHombres', 'Tasa Mortalidad Bruta\nHombres'])
            elif sexo == 2:
                num_muertes = mc.num_muertes_cancer(df, per, tab, reg, com, sex,
                                                    edad_quinquenal=True)
                tasa = tasas.tmb_cancer(df, df2, per, tab, reg, com, sex,
                                        edad_quinquenal=True)
                if tabular == 1:
                    tabla = list()
                    for key, value in num_muertes.items():
                        a = list()
                        a.append(key)
                        a.append('C00-D48')
                        a.append(value)
                        tabla.append(a)
                    i = 0
                    for value in tasa.values():
                        tabla[i].append(round(value, 2))
                        i += 1
                    tabla_final = tabulate(tabla,
                                           headers=['Grupo edad', 'Causa', 'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta\nMujeres'])
                elif tabular == 2:
                    tabla = list()
                    for key, value in num_muertes.items():
                        a = list()
                        a.append(key)
                        a.append('C00-C97')
                        a.append(value)
                        tabla.append(a)
                    i = 0
                    for value in tasa.values():
                        tabla[i].append(round(value, 2))
                        i += 1
                    tabla_final = tabulate(tabla,
                                           headers=['Grupo edad', 'Causa', 'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta\nMujeres'])
            elif sexo == 3:
                num_muertesh = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=1,
                                                    edad_quinquenal=True)
                tasah = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=1,
                                        edad_quinquenal=True)
                num_muertesm = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=2,
                                                    edad_quinquenal=True)
                tasam = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=2,
                                        edad_quinquenal=True)
                if len(num_muertesh) == 17 and len(num_muertesm) == 17:
                    if tabular == 1:
                        tabla = list()
                        for key, value in num_muertesh.items():
                            a = list()
                            a.append(key)
                            a.append('C00-D48')
                            a.append(value)
                            tabla.append(a)
                        i = 0
                        for value in tasah.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        i = 0
                        for key, value in num_muertesm.items():
                            tabla[i].append(key)
                            tabla[i].append(value)
                            i += 1
                        i = 0
                        for value in tasam.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        tabla_final = tabulate(tabla,
                                               headers=['Grupo edad\nHombres', 'Causa', 'Nº Defunciones\nHombres',
                                                        'Tasa Mortalidad Bruta\nHombres', 'Grupo edad\nMujeres',
                                                        'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta\nMujeres'])
                    elif tabular == 2:
                        tabla = list()
                        for key, value in num_muertesh.items():
                            a = list()
                            a.append(key)
                            a.append('C00-C97')
                            a.append(value)
                            tabla.append(a)
                        i = 0
                        for value in tasah.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        i = 0
                        for key, value in num_muertesm.items():
                            tabla[i].append(key)
                            tabla[i].append(value)
                            i += 1
                        i = 0
                        for value in tasam.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        tabla_final = tabulate(tabla,
                                               headers=['Grupo edad\nHombres', 'Causa', 'Nº Defunciones\nHombres',
                                                        'Tasa Mortalidad Bruta\nHombres', 'Grupo edad\nMujeres',
                                                        'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta\nMujeres'])
                elif len(num_muertesh) < 17 or len(num_muertesm) < 17:
                    num_muertesh_igualada = tb.iguala_tabla(num_muertesh)
                    tasah_igualada = tb.iguala_tabla(tasah)
                    num_muertesm_igualada = tb.iguala_tabla(num_muertesm)
                    tasam_igualada = tb.iguala_tabla(tasam)
                    if tabular == 1:
                        tabla = list()
                        for key, value in num_muertesh_igualada.items():
                            a = list()
                            a.append(key)
                            a.append('C00-D48')
                            a.append(value)
                            tabla.append(a)
                        i = 0
                        for value in tasah_igualada.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        i = 0
                        for key, value in num_muertesm_igualada.items():
                            tabla[i].append(key)
                            tabla[i].append(value)
                            i += 1
                        i = 0
                        for value in tasam_igualada.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        tabla_final = tabulate(tabla,
                                               headers=['Grupo edad\nHombres', 'Causa', 'Nº Defunciones\nHombres',
                                                        'Tasa Mortalidad Bruta\nHombres', 'Grupo edad\nMujeres',
                                                        'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta\nMujeres'])
                    elif tabular == 2:
                        tabla = list()
                        for key, value in num_muertesh_igualada.items():
                            a = list()
                            a.append(key)
                            a.append('C00-C97')
                            a.append(value)
                            tabla.append(a)
                        i = 0
                        for value in tasah_igualada.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        i = 0
                        for key, value in num_muertesm_igualada.items():
                            tabla[i].append(key)
                            tabla[i].append(value)
                            i += 1
                        i = 0
                        for value in tasam_igualada.values():
                            tabla[i].append(round(value, 2))
                            i += 1
                        tabla_final = tabulate(tabla, headers=['Grupo edad\nHombres', 'Causa', 'Nº Defunciones\nHombres', 'Tasa Mortalidad Bruta\nHombres', 'Grupo edad\nMujeres', 'Nº Defunciones\nMujeres', 'Tasa Mortalidad Bruta\nMujeres'])


        elif tabular == 3 or tabular == 4 or tabular == 5:
            if sexo == 0:
                datos1 = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=0, edad_quinquenal=True)
                datos2 = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=0, edad_quinquenal=True)
                tabla_maxima = tb2.formato_tabla(datos1, datos2, tabular)
                for tabla in tabla_maxima:
                    tablas_causas = tabulate(tabla, headers=(["Grupo de edad", "Causa", "Número\nDefunciones", "Tasa Mortalidad\nBruta" ]))
                    print(tablas_causas)
                tabla_final = "Fin proceso"
            elif sexo != 0:
                if sexo == 1:
                    datos1 = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=1, edad_quinquenal=True)
                    datos2 = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=1, edad_quinquenal=True)
                    tabla_maxima = tb2.formato_tabla(datos1, datos2, tabular)
                    for tabla in tabla_maxima:
                        tablas_causas = tabulate(tabla, headers=(
                        ["Grupo de edad", "Causa", "Número Defunciones\nHombres", "Tasa Mortalidad Bruta\nHombres"]))
                        print(tablas_causas)
                    tabla_final = "Fin proceso"
                elif sexo == 2:
                    datos1 = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=2, edad_quinquenal=True)
                    datos2 = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=2, edad_quinquenal=True)
                    tabla_maxima = tb2.formato_tabla(datos1, datos2, tabular)
                    for tabla in tabla_maxima:
                        tablas_causas = tabulate(tabla, headers=(
                            ["Grupo de edad", "Causa", "Número Defunciones\nMujeres",
                             "Tasa Mortalidad Bruta\nMujeres"]))
                        print(tablas_causas)
                    tabla_final = "Fin proceso"
                elif sexo == 3:
                    datos1_hombres = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=1, edad_quinquenal=True)
                    datos2_hombres = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=1, edad_quinquenal=True)
                    datos1_mujeres = mc.num_muertes_cancer(df, per, tab, reg, com, sexo=2, edad_quinquenal=True)
                    datos2_mujeres = tasas.tmb_cancer(df, df2, per, tab, reg, com, sexo=2, edad_quinquenal=True)

                    lista_maxima_hombres = tb2.formato_tabla(datos1_hombres, datos2_hombres, tabular)
                    lista_maxima_mujeres = tb2.formato_tabla(datos1_mujeres, datos2_mujeres, tabular)

                    i = 0
                    lista_ambos_sexos = list()
                    valores_mujeres = list()

                    for listas in lista_maxima_mujeres:
                        for datos in listas:
                            val_muj = list()
                            val_muj.append(datos[1])
                            val_muj.append(datos[2])
                            val_muj.append(datos[3])
                            val_muj = tuple(val_muj)
                            valores_mujeres.append(val_muj)

                    for listas in lista_maxima_hombres:
                        lista_previa = list()
                        for datos in listas:
                            a = valores_mujeres[i]
                            datos.append(a[0])
                            datos.append(a[1])
                            datos.append(a[2])
                            i += 1
                            lista_previa.append(datos)
                        lista_ambos_sexos.append(lista_previa)

                    for tabla in lista_ambos_sexos:
                        tablas_causas = tabulate(tabla, headers=(
                            ["Grupo de edad", "Causa\nHombres", "Número Defunciones\nHombres",
                            "Tasa Mortalidad Bruta\nHombres", "Causa\nMujeres",
                            "Número Defunciones\nMujeres", "Tasa Mortalidad Bruta\nMujeres"]))
                        print(tablas_causas)
                        print("****\n"*5)

                    tabla_final = "Fin proceso"

    return tabla_final

# path = os.path.abspath("/Users/alvaro/Documents/Data Science/Python/proyectos/rpc/tasas_mortalidad_v5/datasets/DEF_2010_2018.csv")
# path2 = os.path.abspath("/Users/alvaro/Documents/Data Science/Python/proyectos/rpc/tasas_mortalidad_v5/datasets/estimaciones-y-proyecciones-2002-2035-comunas.xlsx")
#
# df1 = pd.read_csv(path, sep=";", encoding='Latin',
#                   dtype={21: str, 36: str, 37: str, 38: str, 39: str,
#                          40: str, 41: str, 42: str, 43: str, 44: str,
#                          45: str, 46: str, 47: str, 48: str, 49: str,
#                          50: str, 58: str, 60: str, 64: str, 67: str,
#                          69: str, 70: str, 71: str, 73: str, 76: str,
#                          82: str, 86: str, 89: str, 90: str, 91: str,
#                          93: str, 96: str, 97: str, 98: str, 99: str,
#                          100: str})
#
# df2 = pd.read_excel(path2)
#
# tabular = 5
# sexo = 3
# region = 0
# comuna = 2101
# periodo = "2014-2018"
# a = crear_tablas(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region, edad_quinquenal = True)
# print(f"Tabla para: \nlista tabular: {tabular}, \nregion: {region}, \ncomuna: {comuna}, \nsexo: {sexo}, \nperiodo: {periodo}: {a}")

# for i in a:
#     print("==="*50)
#     print(i)


#
# tabular = 1
# sexo = 3
# region = 0
# comuna = 2301
# periodo = "2014-2018"
# a = crear_tablas(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region, edad_quinquenal = True)
# print(f"Tabla para: \nlista tabular: {tabular}, \nregion: {region}, \ncomuna: {comuna}, \nsexo: {sexo}, \nperiodo: {periodo}: \n {a}")
# print("==="*50)

# tabular = 1
# sexo = 2
# region = 0
# comuna = 0
# periodo = "2014-2018"
# a = crear_tablas(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region, edad_quinquenal = True)
# print(f"Tabla para: \nlista tabular: {tabular}, \nregion: {region}, \ncomuna: {comuna}, \nsexo: {sexo}, \nperiodo: {periodo}: \n {a}")
# print("==="*50)
# tabular =1
# sexo = 3
# region = 0
# comuna = 0
# periodo = "2014-2018"
# a = crear_tablas(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region, edad_quinquenal = True)
# print(f"Tabla para: \nlista tabular: {tabular}, \nregion: {region}, \ncomuna: {comuna}, \nsexo: {sexo}, \nperiodo: {periodo}: \n {a}")
# print("==="*50)