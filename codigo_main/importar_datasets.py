import os
import pandas as pd

path = os.path.abspath("D:\proyectos_programación\Python\RPC\software_tasas_mortalidad_v4\datasets\estimaciones-y-proyecciones-2002-2035-comunas.xlsx")
print(path)

df = pd.read_excel(path)

print(df.head())