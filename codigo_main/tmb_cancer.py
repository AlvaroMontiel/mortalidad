from codigo_main import poblacion_ine as ine
from codigo_main import num_def_cancer as deis
import pandas as pd
import os
from time import time
def tmb_cancer(dataframe_1, dataframe_2, periodo, tabular, region=0, comuna=0, sexo=0, edad_quinquenal = False):
       df = dataframe_1
       per = periodo
       tab = tabular
       reg = region
       com = comuna
       sex = sexo
       df2 = dataframe_2

       if edad_quinquenal == False:
              #######################
              #### NUMERADOR !!! ####
              #######################
              defunciones = deis.num_muertes_cancer(df, per, tab, comuna=com, region=reg, sexo=sex, edad_quinquenal=False)
              if tab == 1:
                     keys = ""
                     for llave, tupla in defunciones.items():
                            numerador_tupla = tupla
                            keys = llave
                     numerador, label = numerador_tupla
              elif tab == 2:
                     keys = ""
                     for llave, tupla in defunciones.items():
                            numerador_tupla = tupla
                            keys = llave
                     numerador, label = numerador_tupla
              elif tab == 3:
                     tuplas = []
                     numerador = []
                     label = []
                     keys = []
                     for llave, valor in defunciones.items():
                            tuplas.append(valor)
                            keys.append(llave)
                     for tupla in tuplas:
                            numerador.append(tupla[0])
                            label.append(tupla[1])
              elif tab == 4:
                     tuplas = []
                     numerador = []
                     label = []
                     keys = []
                     for llave, valor in defunciones.items():
                            tuplas.append(valor)
                            keys.append(llave)
                     for tupla in tuplas:
                            numerador.append(tupla[0])
                            label.append(tupla[1])
              elif tab == 5:
                     tuplas = []
                     numerador = []
                     label = []
                     keys = []
                     for llave, valor in defunciones.items():
                            tuplas.append(valor)
                            keys.append(llave)
                     for tupla in tuplas:
                            numerador.append(tupla[0])
                            label.append(tupla[1])

              ########################
              ##### DENOMINADOR ######
              ########################
              periodo_poblacion = per.split("-")
              per_inicial = int("".join(periodo_poblacion[0]))
              per_final = int("".join(periodo_poblacion[1]))
              tipo_per = (per_final - per_inicial) + 1

              if tipo_per % 2 > 0:
                     a = 0
                     b = 0
                     for i in range(0, tipo_per):
                            a += 1
                            b = b + a
                     ano_poblacion = int((per_inicial + (b / a)) - 1)
                     denominador = ine.poblacion(df2, ano_poblacion, sex, reg, com, edad_quinquenal=False)
              elif tipo_per % 2 == 0:
                     # Crea dos años que se deben invocar el la función
                     if per_final - per_inicial == 1:
                            pob_inicial = ine.poblacion(df2, per_inicial, sex, reg, com, edad_quinquenal=False)
                            pob_final = ine.poblacion(df2, per_final, sex, reg, com, edad_quinquenal=False)
                            denominador = int((pob_inicial + pob_final) / 2)
                     elif per_final - per_inicial > 1:
                            a = 0
                            b = 0
                            for i in range(0, tipo_per):
                                   a += 1
                                   b = b + a
                                   per1 = int(per_inicial + ((b / a) - 0.5) - 1)
                                   per2 = int(per_inicial + ((b / a) + 0.5) - 1)
                                   pob_inicial = ine.poblacion(df2, per1, sex, reg, com, edad_quinquenal=False)
                                   pob_final = ine.poblacion(df2, per2, sex, reg, com, edad_quinquenal=False)
                                   denominador = int((pob_inicial + pob_final) / 2)

              #########################
              ## TASAS DE MORTALIDAD ##
              #########################
              base100mil = 100000
              if type(numerador) == int:
                     tmb = ((numerador/tipo_per)/denominador) * base100mil
              elif type(numerador) == list:
                     tmb_num = []
                     num = numerador
                     for muertes in num:
                             mortalidad = (muertes/tipo_per)/denominador * base100mil
                             tmb_num.append(mortalidad)
                     tmb_numdesc = list(zip(tmb_num, label))
                     tmb = dict(zip(keys, tmb_numdesc))
       elif edad_quinquenal == True:
              #######################
              #### NUMERADOR !!! ####
              #######################
              defunciones = deis.num_muertes_cancer(df, per, tab, comuna=com, region=reg, sexo=sex, edad_quinquenal=True)
              if tab == 1 or tab == 2:
                     keys = list()
                     numerador = list()
                     for llave, valor in defunciones.items():
                            numerador.append(valor)
                            keys.append(llave)


              ########################
              ##### DENOMINADOR ######
              ########################
              periodo_poblacion = per.split("-")
              per_inicial = int("".join(periodo_poblacion[0]))
              per_final = int("".join(periodo_poblacion[1]))
              tipo_per = (per_final - per_inicial) + 1

              if tipo_per % 2 > 0:
                     a = 0
                     b = 0
                     for i in range(0, tipo_per):
                            a += 1
                            b = b + a
                     ano_poblacion = int((per_inicial + (b / a)) - 1)
                     denominador = ine.poblacion(df2, ano_poblacion, sex, reg, com, edad_quinquenal=True)
              elif tipo_per % 2 == 0:
                     # Crea dos años que se deben invocar el la función
                     if per_final - per_inicial == 1:
                            pob_inicial = ine.poblacion(df2, per_inicial, sex, reg, com, edad_quinquenal=True)
                            pob_final = ine.poblacion(df2, per_final, sex, reg, com, edad_quinquenal=True)
                            denominador = list()
                            for i in range(0, 17):
                                   denominador.append(int((pob_inicial[i] + pob_final[i]) / 2))
                     elif per_final - per_inicial > 1:
                            a = 0
                            b = 0
                            for i in range(0, tipo_per):
                                   a += 1
                                   b = b + a
                                   per1 = int(per_inicial + ((b / a) - 0.5) - 1)
                                   per2 = int(per_inicial + ((b / a) + 0.5) - 1)
                                   pob_inicial = ine.poblacion(df2, per1, sex, reg, com, edad_quinquenal=True)
                                   pob_final = ine.poblacion(df2, per2, sex, reg, com, edad_quinquenal=True)
                                   denominador = list()
                                   for i in range(0, 17):
                                          denominador.append(int((pob_inicial[i] + pob_final[i]) / 2))

              #########################
              ## TASAS DE MORTALIDAD ##
              #########################
              base100mil = 100000
              if tab == 1 or tab == 2:
                     tasa_mortalidad = list()
                     llave_nueva = list()
                     for keys, valor in defunciones.items():
                            llave_nueva.append(keys)
                            numerador = ((float(valor) / tipo_per) / denominador[keys-1])*base100mil
                            tasa_mortalidad.append(numerador)
                     tmb = dict(zip(llave_nueva, tasa_mortalidad))
              elif tab == 3 or tab == 4 or tab == 5:
                     tasa1 = list()
                     tasa2 = list()
                     tasa3 = list()
                     tasa4 = list()
                     tasa5 = list()
                     tasa6 = list()
                     tasa7 = list()
                     tasa8 = list()
                     tasa9 = list()
                     tasa10 = list()
                     tasa11 = list()
                     tasa12 = list()
                     tasa13 = list()
                     tasa14 = list()
                     tasa15 = list()
                     tasa16 = list()
                     tasa17 = list()
                     cie1 = list()
                     cie2 = list()
                     cie3 = list()
                     cie4 = list()
                     cie5 = list()
                     cie6 = list()
                     cie7 = list()
                     cie8 = list()
                     cie9 = list()
                     cie10 = list()
                     cie11 = list()
                     cie12 = list()
                     cie13 = list()
                     cie14 = list()
                     cie15 = list()
                     cie16 = list()
                     cie17 = list()
                     for key in defunciones.keys():
                            if key == 1:
                                   for i in defunciones[1]:
                                          (label, valor) = i
                                          cie1.append(label)
                                          tasa1.append(float(((valor/tipo_per)/ denominador[0]) * base100mil))
                            elif key == 2:
                                   for i in defunciones[2]:
                                          (label, valor) = i
                                          cie2.append(label)
                                          tasa2.append(float(((valor/tipo_per)/ denominador[1]) * base100mil))
                            elif key == 3:
                                   for i in defunciones[3]:
                                          (label, valor) = i
                                          cie3.append(label)
                                          tasa3.append(float(((valor / tipo_per) / denominador[2]) * base100mil))
                            elif key == 4:
                                   for i in defunciones[4]:
                                          (label, valor) = i
                                          cie4.append(label)
                                          tasa4.append(float(((valor / tipo_per) / denominador[3]) * base100mil))
                            elif key == 5:
                                   for i in defunciones[5]:
                                          (label, valor) = i
                                          cie5.append(label)
                                          tasa5.append(float(((valor / tipo_per) / denominador[4]) * base100mil))
                            elif key == 6:
                                   for i in defunciones[6]:
                                          (label, valor) = i
                                          cie6.append(label)
                                          tasa6.append(float(((valor / tipo_per) / denominador[5]) * base100mil))
                            elif key == 7:
                                   for i in defunciones[7]:
                                          (label, valor) = i
                                          cie7.append(label)
                                          tasa7.append(float(((valor / tipo_per) / denominador[6]) * base100mil))
                            elif key == 8:
                                   for i in defunciones[8]:
                                          (label, valor) = i
                                          cie8.append(label)
                                          tasa8.append(float(((valor / tipo_per) / denominador[7]) * base100mil))
                            elif key == 9:
                                   for i in defunciones[9]:
                                          (label, valor) = i
                                          cie9.append(label)
                                          tasa9.append(float(((valor / tipo_per) / denominador[8]) * base100mil))
                            elif key == 10:
                                   for i in defunciones[10]:
                                          (label, valor) = i
                                          cie10.append(label)
                                          tasa10.append(float(((valor / tipo_per) / denominador[9]) * base100mil))
                            elif key == 11:
                                   for i in defunciones[11]:
                                          (label, valor) = i
                                          cie11.append(label)
                                          tasa11.append(float(((valor / tipo_per) / denominador[10]) * base100mil))
                            elif key == 12:
                                   for i in defunciones[12]:
                                          (label, valor) = i
                                          cie12.append(label)
                                          tasa12.append(float(((valor / tipo_per) / denominador[11]) * base100mil))
                            elif key == 13:
                                   for i in defunciones[13]:
                                          (label, valor) = i
                                          cie13.append(label)
                                          tasa13.append(float(((valor / tipo_per) / denominador[12]) * base100mil))
                            elif key == 14:
                                   for i in defunciones[14]:
                                          (label, valor) = i
                                          cie14.append(label)
                                          tasa14.append(float(((valor / tipo_per) / denominador[13]) * base100mil))
                            elif key == 15:
                                   for i in defunciones[15]:
                                          (label, valor) = i
                                          cie15.append(label)
                                          tasa15.append(float(((valor / tipo_per) / denominador[14]) * base100mil))
                            elif key == 16:
                                   for i in defunciones[16]:
                                          (label, valor) = i
                                          cie16.append(label)
                                          tasa16.append(float(((valor / tipo_per) / denominador[15]) * base100mil))
                            elif key == 17:
                                   for i in defunciones[17]:
                                          (label, valor) = i
                                          cie17.append(label)
                                          tasa17.append(float(((valor / tipo_per) / denominador[16]) * base100mil))
                     tupla1 = list(zip(tasa1, cie1))
                     tupla2 = list(zip(tasa2, cie2))
                     tupla3 = list(zip(tasa3, cie3))
                     tupla4 = list(zip(tasa4, cie4))
                     tupla5 = list(zip(tasa5, cie5))
                     tupla6 = list(zip(tasa6, cie6))
                     tupla7 = list(zip(tasa7, cie7))
                     tupla8 = list(zip(tasa8, cie8))
                     tupla9 = list(zip(tasa9, cie9))
                     tupla10 = list(zip(tasa10, cie10))
                     tupla11 = list(zip(tasa11, cie11))
                     tupla12 = list(zip(tasa12, cie12))
                     tupla13 = list(zip(tasa13, cie13))
                     tupla14 = list(zip(tasa14, cie14))
                     tupla15 = list(zip(tasa15, cie15))
                     tupla16 = list(zip(tasa16, cie16))
                     tupla17 = list(zip(tasa17, cie17))
                     defunciones.update({1: tupla1})
                     defunciones.update({2: tupla2})
                     defunciones.update({3: tupla3})
                     defunciones.update({4: tupla4})
                     defunciones.update({5: tupla5})
                     defunciones.update({6: tupla6})
                     defunciones.update({7: tupla7})
                     defunciones.update({8: tupla8})
                     defunciones.update({9: tupla9})
                     defunciones.update({10: tupla10})
                     defunciones.update({11: tupla11})
                     defunciones.update({12: tupla12})
                     defunciones.update({13: tupla13})
                     defunciones.update({14: tupla14})
                     defunciones.update({15: tupla15})
                     defunciones.update({16: tupla16})
                     defunciones.update({17: tupla17})
                     tmb = defunciones

       return tmb


# path = os.path.abspath("/Users/alvaro/Documents/Data Science/Python/proyectos/rpc/tasas_mortalidad_v5/datasets/DEF_2010_2018.csv")
# path2 = os.path.abspath("/Users/alvaro/Documents/Data Science/Python/proyectos/rpc/tasas_mortalidad_v5/datasets/estimaciones-y-proyecciones-2002-2035-comunas.xlsx")
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
# tabular = 3
# sexo = 2
# region = 0
# comuna = 2104
# periodo = "2014-2018"
#
# start_time = time()
# a = tmb_cancer(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region, edad_quinquenal = True)
# print("_"*10)
# print("_"*10)
# print("_"*10)
# print(f"tasa mortalidad_beta bruta, para lista tabular: {tabular}, "
#       f"region: {region}, comuna: {comuna}, sexo: {sexo}, periodo: {periodo}: {a}")
# print("_"*10)
# print("_"*10)
# print("_"*10)
# elapsed_time = time() - start_time
# print(f"Tiempo de ejecución: %0.2f" % elapsed_time)
