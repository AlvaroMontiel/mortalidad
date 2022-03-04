import pandas as pd
from codigo_main import tablas_latex
import os

path = os.path.abspath(
       "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_1990_2018.csv")
path2 = os.path.abspath(
       "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/estimaciones-y-proyecciones-2002-2035-comunas.xlsx")

df1 = pd.read_csv(path, sep=";", encoding='Latin',
                  dtype={21: str, 36: str, 37: str, 38: str, 39: str,
                         40: str, 41: str, 42: str, 43: str, 44: str,
                         45: str, 46: str, 47: str, 48: str, 49: str,
                         50: str, 58: str, 60: str, 64: str, 67: str,
                         69: str, 70: str, 71: str, 73: str, 76: str,
                         82: str, 86: str, 89: str, 90: str, 91: str,
                         93: str, 96: str, 97: str, 98: str, 99: str,
                         100: str})

df2 = pd.read_excel(path2)
print('Data frames cargados')
tabular = 2
sexo = 0
region = 0
comuna = 2101
periodo = "2014-2018"
print('Variables cargadas')
a = tablas_latex.crear_tablas(df1, df2, periodo=periodo, tabular=tabular, sexo=sexo, comuna=comuna, region=region, edad_quinquenal = False)
print(f"Tabla para: \nlista tabular: {tabular}, \nregion: {region}, \ncomuna: {comuna}, \nsexo: {sexo}, \nperiodo: {periodo} \n {a}")
