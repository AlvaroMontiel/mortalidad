# -*- coding: latin-1 -*-
import pandas as pd
from time import time
import tmb_cancer

df1 = pd.read_csv('DEF_2010_2018.csv', sep=";", encoding='latin-1',
                  dtype={21: str, 36: str, 37: str, 38: str, 39: str,
                         40: str, 41: str, 42: str, 43: str, 44: str,
                         45: str, 46: str, 47: str, 48: str, 49: str,
                         50: str, 58: str, 60: str, 64: str, 67: str,
                         69: str, 70: str, 71: str, 73: str, 76: str,
                         82: str, 86: str, 89: str, 90: str, 91: str,
                         93: str, 96: str, 97: str, 98: str, 99: str,
                         100: str})

df2 = pd.read_excel('estimaciones-y-proyecciones-2002-2035-comunas.xlsx')

tabular = 3
sexo = 0
region = 2
comuna = 0
periodo = "2014-2018"

start_time = time()
a = tmb_cancer.tmb_cancer(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region)
print("="*50)
print(f"tasa mortalidad bruta, para lista tabular: {tabular}, region: {region}, comuna: {comuna}, sexo: {sexo}, periodo: {periodo}: {a}")
print("="*50)
elapsed_time = time() - start_time
print(f"Tiempo de ejecución: {elapsed_time}")
print("="*50)

# periodo = "2009-2013"
# print("="*50)
# b = tmb_cancer.tmb_cancer(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region)
# print(f"tasa mortalidad bruta, para lista tabular: {tabular}, region: {region}, comuna: {comuna}, sexo: {sexo}, periodo: {periodo}: {b}")
# elapsed_time = time() - start_time
# print(f"Tiempo de ejecución: {elapsed_time}")
# print("="*50)

# periodo = "2009-2013"
# print("="*50)
# c = tmb_cancer.tmb_cancer(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region)
# print(f"tasa mortalidad bruta, para lista tabular: {tabular}, region: {region}, comuna: {comuna}, sexo: {sexo}, periodo: {periodo}: {c}")
# elapsed_time = time() - start_time
# print(f"Tiempo de ejecución: {elapsed_time}")
# print("="*50)
#====================================================
# tabular = 4
# sexo = 2
# region = 2
# comuna = 0
# periodo = "2014-2018"
# print("="*50)
# b = tmb_cancer.tmb_cancer(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region)
# print(f"tasa mortalidad bruta, para lista tabular: {tabular}, region: {region}, comuna: {comuna}, sexo: {sexo}, periodo: {periodo}: {b}")
# elapsed_time = time() - start_time
# print(f"Tiempo de ejecución: {elapsed_time}")
# print("="*50)
#
# periodo = "2009-2013"
# print("="*50)
# c = tmb_cancer.tmb_cancer(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region)
# print(f"tasa mortalidad bruta, para lista tabular: {tabular}, region: {region}, comuna: {comuna}, sexo: {sexo}, periodo: {periodo}: {c}")
# elapsed_time = time() - start_time
# print(f"Tiempo de ejecución: {elapsed_time}")
# print("="*50)

