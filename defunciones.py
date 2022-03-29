from parametros_calculos import ParametrosCalculos
from codigo_main import buscar_faltantes as fal

class NumeroDefunciones(ParametrosCalculos):
    def __init__(self, ruta_defunciones, ruta_poblacion, periodo, enfermedad,
                 edad=0, region=None, comuna=None, agrupacion_enfermedad=None):
        super().__init__(ruta_defunciones, ruta_poblacion, periodo, enfermedad,
                         edad=0, region=None, comuna=None)
        self.edad = edad
        self.region = region
        self.comuna = comuna
        self.agrupacion_enfermedad = agrupacion_enfermedad
        self.num_defunciones = NumeroDefunciones.numero_defunciones(self)

    def dataframe_defunciones(self):
        print("Creando el objeto ParametrosCalculos")
        datos = ParametrosCalculos(self.ruta_defunciones, self.ruta_poblacion,
                                 self.periodo, self.enfermedad, self.edad,
                                 self.region, self.comuna)

        df_ = datos.defunciones_filtradas
        print("Objeto ParametrosCalculos creado")
        return df_

    def numero_defunciones(self):
        print("Se está ejecutando el método numero_defunciones")
        df = self.dataframe_defunciones()
        # Todas las causas del capítulo
        if self.agrupacion_enfermedad == None:
            cap_diag1 = df['CAPITULO_DIAG1'].to_list()
            glosa_diag1 = df['GLOSA_CAPITULO_DIAG1'].to_list()
            cod_sexo = [1, 2, 9]
            if self.edad == 0:
                num_defunciones = []
                num_defunciones2 = []
                for sexo in cod_sexo:
                    parametro_filtro = [sexo]
                    defunciones_lista = []
                    defunciones_lista.append(df[df['SEXO'].isin(parametro_filtro)].shape[0])
                    defunciones_lista.append(sexo)
                    num_defunciones.append(defunciones_lista)
                defunciones_ambos_sexos = 0
                for i in range(1, 3):
                    parametro_filtro = [i]
                    defunciones_ambos_sexos += df[df['SEXO'].isin(parametro_filtro)].shape[0]
                num_defunciones.append([defunciones_ambos_sexos, 3])
                for defunciones in num_defunciones:
                    defunciones.append(glosa_diag1[0])
                num_defunciones2.append(num_defunciones)
                dicc_num_defunciones = dict(zip(cap_diag1, num_defunciones2))
                print(dicc_num_defunciones)

            elif self.edad >= 1:
                if self.edad == 1:
                    def_hombres = []
                    def_mujeres = []
                    def_sexo_desconido = []
                    edad_cat_ambos_sexos = []
                    edades_faltantes_hombres = []
                    edades_faltantes_mujeres = []
                    edades_faltantes_desconocido = []
                    for sexo in cod_sexo:
                        print(f"SEXO = {sexo}")
                        parametro_filtro = "SEXO == " + str(sexo)
                        df_ = df.query(parametro_filtro).copy()
                        edad_cat = df_['EDAD_CAT'].values.tolist()
                        edades_faltantes = fal.faltante(edad_cat)

                        if len(edades_faltantes) == 0:
                            df_ = df_.groupby(['EDAD_CAT']).count()
                            if sexo == 1:
                                def_hombres.append(df_['DIAG1'].values.tolist())
                                edades_faltantes_hombres.append(edades_faltantes)
                            elif sexo == 2:
                                def_mujeres.append(df_['DIAG1'].values.tolist())
                                edades_faltantes_mujeres.append(edades_faltantes)
                            elif sexo == 9:
                                def_sexo_desconido.append(df_['DIAG1'].values.tolist())
                                edades_faltantes_desconocido.append(edades_faltantes)
                        elif len(edades_faltantes) >= 1:
                            df_ = df_.groupby(['EDAD_CAT']).count()
                            if sexo == 1:
                                def_hombres.append(df_['DIAG1'].values.tolist())
                                edades_faltantes_hombres.append(edades_faltantes)
                            elif sexo == 2:
                                def_mujeres.append(df_['DIAG1'].values.tolist())
                                edades_faltantes_mujeres.append(edades_faltantes)
                            elif sexo == 9:
                                def_sexo_desconido.append(df_['DIAG1'].values.tolist())
                                edades_faltantes_desconocido.append(edades_faltantes)
                    llave = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
                    print(f"edades faltantes largo = {len(edades_faltantes_hombres)}, edades faltantes hombres {edades_faltantes_hombres}")
                    print(len(edades_faltantes_mujeres))
                    print(len(edades_faltantes_desconocido))
                    if len(edades_faltantes_hombres[0]) == 0:
                        contador = 0
                        for categoria_edad in llave:
                            sub_lista = []
                            sub_lista.append(categoria_edad)
                            sub_lista.append(def_hombres[contador])
                            sub_lista.append(1)
                            sub_lista.append(glosa_diag1)
                            def_hombres[contador] = sub_lista
                            contador += 1
                        print(def_hombres)
                    elif len(edades_faltantes_hombres[0]) >= 1:
                        for edad in edades_faltantes_hombres[0]:
                            llave.remove(edad)
                        contador = 0
                        for categoria_edad in llave:
                            sub_lista = []
                            sub_lista.append(categoria_edad)
                            sub_lista.append(def_hombres[contador])
                            sub_lista.append(1)
                            sub_lista.append(glosa_diag1)
                            def_hombres[contador] = sub_lista
                            contador += 1
                        print(def_hombres)
                    llave = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

                    if len(edades_faltantes_mujeres) == 0:
                        contador = 0
                        for categoria_edad in llave:
                            sub_lista = []
                            sub_lista.append(categoria_edad)
                            sub_lista.append(def_mujeres[contador])
                            sub_lista.append(1)
                            sub_lista.append(glosa_diag1)
                            def_hombres[contador] = sub_lista
                            contador += 1
                        print(def_mujeres)
                    else:
                        for edad in edades_faltantes_mujeres:
                            llave.remove(edad)
                        contador = 0
                        for categoria_edad in llave:
                            sub_lista = []
                            sub_lista.append(categoria_edad)
                            sub_lista.append(def_mujeres[contador])
                            sub_lista.append(1)
                            sub_lista.append(glosa_diag1)
                            def_hombres[contador] = sub_lista
                            contador += 1
                        print(def_mujeres)

                    llave = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
                    if len(edades_faltantes_desconocido) == 0:
                        for edad in edades_faltantes_desconocido:
                            llave.remove(edad)
                        contador = 0
                        for categoria_edad in llave:
                            sub_lista = []
                            sub_lista.append(categoria_edad)
                            sub_lista.append(def_sexo_desconido[contador])
                            sub_lista.append(1)
                            sub_lista.append(glosa_diag1)
                            def_hombres[contador] = sub_lista
                            contador += 1
                        print(def_sexo_desconido)
                    else:
                        for edad in edades_faltantes_desconocido:
                            llave.remove(edad)
                        contador = 0
                        for categoria_edad in llave:
                            sub_lista = []
                            sub_lista.append(categoria_edad)
                            sub_lista.append(def_sexo_desconido[contador])
                            sub_lista.append(1)
                            sub_lista.append(glosa_diag1)
                            def_hombres[contador] = sub_lista
                            contador += 1
                        print(def_sexo_desconido)

                # 1: 0-17, 2: 18-59, 3: 60 y mas
                elif self.edad == 2:
                    pass
                elif self.edad == 3:
                    pass
        # Causas en grupos de 3 caracteres CIE10, ej. C15-C26
        elif self.agrupacion_enfermedad == 1:
            if self.edad == 0:
                pass
            elif self.edad >= 1:
                if self.edad == 1:
                    pass
                elif self.edad == 2:
                    pass
                elif self.edad == 3:
                    pass
        elif self.agrupacion_enfermedad == 2:
            pass
        elif self.agrupacion_enfermedad == 3:
            pass

        # el RETURN que debe ir: dicc_num_defunciones
        return print("Trabajando para usted")


if __name__ == '__main__':
    path_defunciones = "/Users/alvaro/Documents/Data_Science/datasets/defunciones/DEF_2010_2018.csv"
    path_poblacion = "/Users/alvaro/Documents/Data_Science/datasets/poblacion/estimaciones-y-proyecciones-2002-2035-comunas.xlsx"
    periodo = "2014-2018"
    enfermedad = 2
    region = 2
    edad = 1
    comuna = None

    defunciones = NumeroDefunciones(path_defunciones, path_poblacion, periodo=periodo ,
                                    enfermedad=enfermedad, region=region, comuna=comuna, edad=edad)

    print(defunciones.num_defunciones)
    # print("*************")
    # import pandas as pd
    # print("*************")
    # df = pd.read_csv(path_defunciones, sep=';', encoding='Latin',
    #                  dtype={21: str, 36: str, 37: str, 38: str, 39: str,
    #                         40: str, 41: str, 42: str, 43: str, 44: str,
    #                         45: str, 46: str, 47: str, 48: str, 49: str,
    #                         50: str, 58: str, 60: str, 64: str, 67: str,
    #                         69: str, 70: str, 71: str, 73: str, 76: str,
    #                         82: str, 86: str, 89: str, 90: str, 91: str,
    #                         93: str, 96: str, 97: str, 98: str, 99: str,
    #                         100: str})
    # print("*************")
    # cod_sexo = [1, 2, 9]
    # df = df.query('CAPITULO_DIAG1 == "C00-D48"')
    # print("*************")
    # edad = df['EDAD_CANT'].values.tolist()
    # edad_tipo = df['EDAD_TIPO'].values.tolist()
    # edades = list(zip(edad, edad_tipo))
    # print("edades en un tupla")
    # edad_categoria = list()
    # for tupla in edades:
    #     if tupla[1] == 1:
    #         if tupla[0] >= 1 and tupla[0] <= 4:
    #             edad_categoria.append(1)
    #         elif tupla[0] >= 5 and tupla[0] <= 9:
    #             edad_categoria.append(2)
    #         elif tupla[0] >= 10 and tupla[0] <= 14:
    #             edad_categoria.append(3)
    #         elif tupla[0] >= 15 and tupla[0] <= 19:
    #             edad_categoria.append(4)
    #         elif tupla[0] >= 20 and tupla[0] <= 24:
    #             edad_categoria.append(5)
    #         elif tupla[0] >= 25 and tupla[0] <= 29:
    #             edad_categoria.append(6)
    #         elif tupla[0] >= 30 and tupla[0] <= 34:
    #             edad_categoria.append(7)
    #         elif tupla[0] >= 35 and tupla[0] <= 39:
    #             edad_categoria.append(8)
    #         elif tupla[0] >= 40 and tupla[0] <= 44:
    #             edad_categoria.append(9)
    #         elif tupla[0] >= 45 and tupla[0] <= 49:
    #             edad_categoria.append(10)
    #         elif tupla[0] >= 50 and tupla[0] <= 54:
    #             edad_categoria.append(11)
    #         elif tupla[0] >= 55 and tupla[0] <= 59:
    #             edad_categoria.append(12)
    #         elif tupla[0] >= 60 and tupla[0] <= 64:
    #             edad_categoria.append(13)
    #         elif tupla[0] >= 65 and tupla[0] <= 69:
    #             edad_categoria.append(14)
    #         elif tupla[0] >= 70 and tupla[0] <= 74:
    #             edad_categoria.append(15)
    #         elif tupla[0] >= 75 and tupla[0] <= 79:
    #             edad_categoria.append(16)
    #         elif tupla[0] >= 80:
    #             edad_categoria.append(17)
    #     elif tupla[1] >= 2:
    #         edad_categoria.append(1)
    # df['EDAD_CAT'] = edad_categoria
    # print(df[['EDAD_CANT','EDAD_CAT']].head())
    #
    # for i in cod_sexo:
    #     print(i)
    #     x = "SEXO == " + str(i)
    #     df_ = df.query(x).copy()
    #     edad_cat = df_['EDAD_CAT'].values.tolist()
    #     edades_faltantes = fal.faltante(edad_cat)
    #
    #     if len(edades_faltantes) < 1:
    #         num_defunciones = df.groupby(['EDAD_CAT', 'SEXO']).count().values.tolist()
    #         print(f"Numero de defunciones: {num_defunciones}")
    #     else:
    #         pass
    #
