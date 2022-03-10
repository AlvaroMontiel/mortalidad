from importar_archivo import ImportarArchivo
from agrupacion_edad import AgrupacionEdad

class ParametrosCalculos(ImportarArchivo):
    '''
    Esta clase importa el dataset correspondiente a poblacion y defunciones y los procesa de acuerdo a los parámetros
    entregados por el usuario
    El método importar data set es heredado de la clase ImportarArchivo.py y sirve para crear los objetos que contienen
    los dataframes de poblacion y de defunciones
    '''
    def __init__(self, ruta_defunciones, ruta_poblacion, periodo, enfermedad, categoria_enfermedad,
                 sexo=None, region=None, comuna=None, edad=False):
        super().__init__(ruta_defunciones, ruta_poblacion)
        self.periodo = periodo
        self.enfermedad = enfermedad
        self.categoria_enfermedad = categoria_enfermedad
        self.sexo = sexo
        self.region = region
        self.comuna = comuna
        self.edad = edad
        self.datos = ParametrosCalculos.importar_dataframe(self)
        self.poblacion_filtrada = None
        self.defunciones_filtradas = None

    # la función crea un objeto Importar Archivo que contiene los dataframe defunciones y población
    def importar_dataframe(self):
        datos_ = ImportarArchivo(self.ruta_defunciones, self.ruta_poblacion)

        return datos_

    def agrupar_edad_poblacion(self):
        if self.edad == 0:
            pass
        elif self.edad >= 1:
            pass
    def agrupar_edad_defuncion(self):
        pass



    def filtrar_poblacion(self):
        pass

    def filtrar_defunciones(self):
        print(self.datos.defunciones.shape)
        periodo = self.periodo.split("-")
        per_inicial = int("".join(periodo[0]))
        per_final = int("".join(periodo[1]))
        b = per_final - per_inicial
        x = []
        if b == 0:
            x.append(per_inicial)
        elif b >= 1:
            b += 1
            for i in range(b):
                x.append(per_inicial)
                per_inicial += 1
        df = self.datos.defunciones[self.datos.defunciones['ANO_DEF'].isin(x)].copy()

        return df



if __name__ == "__main__":
    datos = ParametrosCalculos("/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv",
                               "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/poblacion_corto.xlsx",
                               "2014-2018", "cancer", 1)

    print(datos.filtrar_defunciones().shape)
