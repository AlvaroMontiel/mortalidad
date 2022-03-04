def poblacion(dataframe, agno, sexo=0, region=0, comuna=0, edad_quinquenal=False):
    df = dataframe
    ano = agno
    def pob_total_pais(dataframe, agno):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        total_personas = dataframe[filtro_agno].sum()
        return total_personas

    def pob_total_pais_sexo(dataframe, agno, sexo):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        sexo = str(sexo)
        if sexo == "hombre" or sexo == "masculino" or sexo == "1":
            sexo = 1
        elif sexo == "mujer" or sexo == "femenino" or sexo == "2":
            sexo = 2
        df_pais_sexo = dataframe[(dataframe.Sexo == sexo)]
        total_personas = df_pais_sexo[filtro_agno].sum()
        return total_personas

    def pob_region(dataframe, region, agno):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_region = dataframe[(dataframe.Region == region)]
        total_personas = df_region[filtro_agno].sum()
        return total_personas

    def pob_region_sexo(dataframe, region, agno, sexo):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_region = dataframe[(dataframe.Region == region)]
        df_region_sexo = df_region[(df_region.Sexo == sexo)]
        df_region_sexo_agno = df_region_sexo[filtro_agno].sum()
        total_personas = df_region_sexo_agno
        return total_personas

    def pob_comuna(dataframe, comuna, agno):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_comuna = dataframe[(dataframe.Comuna == comuna)]
        total_personas_comuna = df_comuna[filtro_agno].sum()
        return total_personas_comuna

    def pob_comuna_sexo(dataframe, comuna, agno, sexo):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        sexo_2 = str(sexo)
        if sexo_2 == "hombre" or sexo_2 == "masculino" or sexo_2 == "1":
            sexo_2 = 1
        elif sexo_2 == "mujer" or sexo_2 == "femenino" or sexo_2 == "2":
            sexo_2 = 2

        df_comuna = dataframe[(dataframe.Comuna == comuna)]
        df_comuna_sexo = df_comuna[(df_comuna.Sexo == sexo_2)]
        total_personas_comuna_sexo_agno = df_comuna_sexo[filtro_agno].sum()
        return total_personas_comuna_sexo_agno

    def pob_total_pais_quinquenio(dataframe, agno):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_agno = dataframe.groupby(['Edad'], as_index=False).sum()
        q1 = df_agno[['Edad', filtro_agno]].query('Edad >= 0 & Edad <= 4')
        q2 = df_agno[['Edad', filtro_agno]].query('Edad >= 5 & Edad <= 9')
        q3 = df_agno[['Edad', filtro_agno]].query('Edad >= 10 & Edad <= 14')
        q4 = df_agno[['Edad', filtro_agno]].query('Edad >= 15 & Edad <= 19')
        q5 = df_agno[['Edad', filtro_agno]].query('Edad >= 20 & Edad <= 24')
        q6 = df_agno[['Edad', filtro_agno]].query('Edad >= 25 & Edad <= 29')
        q7 = df_agno[['Edad', filtro_agno]].query('Edad >= 30 & Edad <= 34')
        q8 = df_agno[['Edad', filtro_agno]].query('Edad >= 35 & Edad <= 39')
        q9 = df_agno[['Edad', filtro_agno]].query('Edad >= 40 & Edad <= 44')
        q10 = df_agno[['Edad', filtro_agno]].query('Edad >= 45 & Edad <= 49')
        q11 = df_agno[['Edad', filtro_agno]].query('Edad >= 50 & Edad <= 54')
        q12 = df_agno[['Edad', filtro_agno]].query('Edad >= 55 & Edad <= 59')
        q13 = df_agno[['Edad', filtro_agno]].query('Edad >= 60 & Edad <= 64')
        q14 = df_agno[['Edad', filtro_agno]].query('Edad >= 65 & Edad <= 69')
        q15 = df_agno[['Edad', filtro_agno]].query('Edad >= 70 & Edad <= 74')
        q16 = df_agno[['Edad', filtro_agno]].query('Edad >= 75 & Edad <= 79')
        q17 = df_agno[['Edad', filtro_agno]].query('Edad >= 80')
        q1 = q1[filtro_agno].sum()
        q2 = q2[filtro_agno].sum()
        q3 = q3[filtro_agno].sum()
        q4 = q4[filtro_agno].sum()
        q5 = q5[filtro_agno].sum()
        q6 = q6[filtro_agno].sum()
        q7 = q7[filtro_agno].sum()
        q8 = q8[filtro_agno].sum()
        q9 = q9[filtro_agno].sum()
        q10 = q10[filtro_agno].sum()
        q11 = q11[filtro_agno].sum()
        q12 = q12[filtro_agno].sum()
        q13 = q13[filtro_agno].sum()
        q14 = q14[filtro_agno].sum()
        q15 = q15[filtro_agno].sum()
        q16 = q16[filtro_agno].sum()
        q17 = q17[filtro_agno].sum()

        total_personas = [q1, q2, q3, q4, q5, q6, q7, q8, q9,
                          q10, q11, q12, q13, q14, q15, q16, q17]
        return total_personas

    def pob_total_pais_sexo_quinquenio(dataframe, agno, sexo):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        sexo = str(sexo)
        if sexo == "hombre" or sexo == "masculino" or sexo == "1":
            sexo = 1
        elif sexo == "mujer" or sexo == "femenino" or sexo == "2":
            sexo = 2
        df_pais_sexo = dataframe[(dataframe.Sexo == sexo)]
        df_agno = df_pais_sexo.groupby(['Edad'], as_index=False).sum()
        q1 = df_agno[['Edad', filtro_agno]].query('Edad >= 0 & Edad <= 4')
        q2 = df_agno[['Edad', filtro_agno]].query('Edad >= 5 & Edad <= 9')
        q3 = df_agno[['Edad', filtro_agno]].query('Edad >= 10 & Edad <= 14')
        q4 = df_agno[['Edad', filtro_agno]].query('Edad >= 15 & Edad <= 19')
        q5 = df_agno[['Edad', filtro_agno]].query('Edad >= 20 & Edad <= 24')
        q6 = df_agno[['Edad', filtro_agno]].query('Edad >= 25 & Edad <= 29')
        q7 = df_agno[['Edad', filtro_agno]].query('Edad >= 30 & Edad <= 34')
        q8 = df_agno[['Edad', filtro_agno]].query('Edad >= 35 & Edad <= 39')
        q9 = df_agno[['Edad', filtro_agno]].query('Edad >= 40 & Edad <= 44')
        q10 = df_agno[['Edad', filtro_agno]].query('Edad >= 45 & Edad <= 49')
        q11 = df_agno[['Edad', filtro_agno]].query('Edad >= 50 & Edad <= 54')
        q12 = df_agno[['Edad', filtro_agno]].query('Edad >= 55 & Edad <= 59')
        q13 = df_agno[['Edad', filtro_agno]].query('Edad >= 60 & Edad <= 64')
        q14 = df_agno[['Edad', filtro_agno]].query('Edad >= 65 & Edad <= 69')
        q15 = df_agno[['Edad', filtro_agno]].query('Edad >= 70 & Edad <= 74')
        q16 = df_agno[['Edad', filtro_agno]].query('Edad >= 75 & Edad <= 79')
        q17 = df_agno[['Edad', filtro_agno]].query('Edad >= 80')
        q1 = q1[filtro_agno].sum()
        q2 = q2[filtro_agno].sum()
        q3 = q3[filtro_agno].sum()
        q4 = q4[filtro_agno].sum()
        q5 = q5[filtro_agno].sum()
        q6 = q6[filtro_agno].sum()
        q7 = q7[filtro_agno].sum()
        q8 = q8[filtro_agno].sum()
        q9 = q9[filtro_agno].sum()
        q10 = q10[filtro_agno].sum()
        q11 = q11[filtro_agno].sum()
        q12 = q12[filtro_agno].sum()
        q13 = q13[filtro_agno].sum()
        q14 = q14[filtro_agno].sum()
        q15 = q15[filtro_agno].sum()
        q16 = q16[filtro_agno].sum()
        q17 = q17[filtro_agno].sum()

        total_personas = [q1, q2, q3, q4, q5, q6, q7, q8, q9,
                          q10, q11, q12, q13, q14, q15, q16, q17]
        return total_personas

    def pob_region_quinquenio(dataframe, region, agno):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_region = dataframe[(dataframe.Region == region)]
        df_agno = df_region.groupby(['Edad'], as_index=False).sum()
        q1 = df_agno[['Edad', filtro_agno]].query('Edad >= 0 & Edad <= 4')
        q2 = df_agno[['Edad', filtro_agno]].query('Edad >= 5 & Edad <= 9')
        q3 = df_agno[['Edad', filtro_agno]].query('Edad >= 10 & Edad <= 14')
        q4 = df_agno[['Edad', filtro_agno]].query('Edad >= 15 & Edad <= 19')
        q5 = df_agno[['Edad', filtro_agno]].query('Edad >= 20 & Edad <= 24')
        q6 = df_agno[['Edad', filtro_agno]].query('Edad >= 25 & Edad <= 29')
        q7 = df_agno[['Edad', filtro_agno]].query('Edad >= 30 & Edad <= 34')
        q8 = df_agno[['Edad', filtro_agno]].query('Edad >= 35 & Edad <= 39')
        q9 = df_agno[['Edad', filtro_agno]].query('Edad >= 40 & Edad <= 44')
        q10 = df_agno[['Edad', filtro_agno]].query('Edad >= 45 & Edad <= 49')
        q11 = df_agno[['Edad', filtro_agno]].query('Edad >= 50 & Edad <= 54')
        q12 = df_agno[['Edad', filtro_agno]].query('Edad >= 55 & Edad <= 59')
        q13 = df_agno[['Edad', filtro_agno]].query('Edad >= 60 & Edad <= 64')
        q14 = df_agno[['Edad', filtro_agno]].query('Edad >= 65 & Edad <= 69')
        q15 = df_agno[['Edad', filtro_agno]].query('Edad >= 70 & Edad <= 74')
        q16 = df_agno[['Edad', filtro_agno]].query('Edad >= 75 & Edad <= 79')
        q17 = df_agno[['Edad', filtro_agno]].query('Edad >= 80')
        q1 = q1[filtro_agno].sum()
        q2 = q2[filtro_agno].sum()
        q3 = q3[filtro_agno].sum()
        q4 = q4[filtro_agno].sum()
        q5 = q5[filtro_agno].sum()
        q6 = q6[filtro_agno].sum()
        q7 = q7[filtro_agno].sum()
        q8 = q8[filtro_agno].sum()
        q9 = q9[filtro_agno].sum()
        q10 = q10[filtro_agno].sum()
        q11 = q11[filtro_agno].sum()
        q12 = q12[filtro_agno].sum()
        q13 = q13[filtro_agno].sum()
        q14 = q14[filtro_agno].sum()
        q15 = q15[filtro_agno].sum()
        q16 = q16[filtro_agno].sum()
        q17 = q17[filtro_agno].sum()

        total_personas = [q1, q2, q3, q4, q5, q6, q7, q8, q9,
                          q10, q11, q12, q13, q14, q15, q16, q17]
        return total_personas

    def pob_region_sexo_quinquenio(dataframe, region, agno, sexo):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_region = dataframe[(dataframe.Region == region)]
        df_region_sexo = df_region[(df_region.Sexo == sexo)]
        df_agno = df_region_sexo.groupby(['Edad'], as_index=False).sum()
        q1 = df_agno[['Edad', filtro_agno]].query('Edad >= 0 & Edad <= 4')
        q2 = df_agno[['Edad', filtro_agno]].query('Edad >= 5 & Edad <= 9')
        q3 = df_agno[['Edad', filtro_agno]].query('Edad >= 10 & Edad <= 14')
        q4 = df_agno[['Edad', filtro_agno]].query('Edad >= 15 & Edad <= 19')
        q5 = df_agno[['Edad', filtro_agno]].query('Edad >= 20 & Edad <= 24')
        q6 = df_agno[['Edad', filtro_agno]].query('Edad >= 25 & Edad <= 29')
        q7 = df_agno[['Edad', filtro_agno]].query('Edad >= 30 & Edad <= 34')
        q8 = df_agno[['Edad', filtro_agno]].query('Edad >= 35 & Edad <= 39')
        q9 = df_agno[['Edad', filtro_agno]].query('Edad >= 40 & Edad <= 44')
        q10 = df_agno[['Edad', filtro_agno]].query('Edad >= 45 & Edad <= 49')
        q11 = df_agno[['Edad', filtro_agno]].query('Edad >= 50 & Edad <= 54')
        q12 = df_agno[['Edad', filtro_agno]].query('Edad >= 55 & Edad <= 59')
        q13 = df_agno[['Edad', filtro_agno]].query('Edad >= 60 & Edad <= 64')
        q14 = df_agno[['Edad', filtro_agno]].query('Edad >= 65 & Edad <= 69')
        q15 = df_agno[['Edad', filtro_agno]].query('Edad >= 70 & Edad <= 74')
        q16 = df_agno[['Edad', filtro_agno]].query('Edad >= 75 & Edad <= 79')
        q17 = df_agno[['Edad', filtro_agno]].query('Edad >= 80')
        q1 = q1[filtro_agno].sum()
        q2 = q2[filtro_agno].sum()
        q3 = q3[filtro_agno].sum()
        q4 = q4[filtro_agno].sum()
        q5 = q5[filtro_agno].sum()
        q6 = q6[filtro_agno].sum()
        q7 = q7[filtro_agno].sum()
        q8 = q8[filtro_agno].sum()
        q9 = q9[filtro_agno].sum()
        q10 = q10[filtro_agno].sum()
        q11 = q11[filtro_agno].sum()
        q12 = q12[filtro_agno].sum()
        q13 = q13[filtro_agno].sum()
        q14 = q14[filtro_agno].sum()
        q15 = q15[filtro_agno].sum()
        q16 = q16[filtro_agno].sum()
        q17 = q17[filtro_agno].sum()

        total_personas = [q1, q2, q3, q4, q5, q6, q7, q8, q9,
                          q10, q11, q12, q13, q14, q15, q16, q17]
        return total_personas

    def pob_comuna_quinquenio(dataframe, comuna, agno):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        df_comuna = dataframe[(dataframe.Comuna == comuna)]
        df_agno = df_comuna.groupby(['Edad'], as_index=False).sum()
        q1 = df_agno[['Edad', filtro_agno]].query('Edad >= 0 & Edad <= 4')
        q2 = df_agno[['Edad', filtro_agno]].query('Edad >= 5 & Edad <= 9')
        q3 = df_agno[['Edad', filtro_agno]].query('Edad >= 10 & Edad <= 14')
        q4 = df_agno[['Edad', filtro_agno]].query('Edad >= 15 & Edad <= 19')
        q5 = df_agno[['Edad', filtro_agno]].query('Edad >= 20 & Edad <= 24')
        q6 = df_agno[['Edad', filtro_agno]].query('Edad >= 25 & Edad <= 29')
        q7 = df_agno[['Edad', filtro_agno]].query('Edad >= 30 & Edad <= 34')
        q8 = df_agno[['Edad', filtro_agno]].query('Edad >= 35 & Edad <= 39')
        q9 = df_agno[['Edad', filtro_agno]].query('Edad >= 40 & Edad <= 44')
        q10 = df_agno[['Edad', filtro_agno]].query('Edad >= 45 & Edad <= 49')
        q11 = df_agno[['Edad', filtro_agno]].query('Edad >= 50 & Edad <= 54')
        q12 = df_agno[['Edad', filtro_agno]].query('Edad >= 55 & Edad <= 59')
        q13 = df_agno[['Edad', filtro_agno]].query('Edad >= 60 & Edad <= 64')
        q14 = df_agno[['Edad', filtro_agno]].query('Edad >= 65 & Edad <= 69')
        q15 = df_agno[['Edad', filtro_agno]].query('Edad >= 70 & Edad <= 74')
        q16 = df_agno[['Edad', filtro_agno]].query('Edad >= 75 & Edad <= 79')
        q17 = df_agno[['Edad', filtro_agno]].query('Edad >= 80')
        q1 = q1[filtro_agno].sum()
        q2 = q2[filtro_agno].sum()
        q3 = q3[filtro_agno].sum()
        q4 = q4[filtro_agno].sum()
        q5 = q5[filtro_agno].sum()
        q6 = q6[filtro_agno].sum()
        q7 = q7[filtro_agno].sum()
        q8 = q8[filtro_agno].sum()
        q9 = q9[filtro_agno].sum()
        q10 = q10[filtro_agno].sum()
        q11 = q11[filtro_agno].sum()
        q12 = q12[filtro_agno].sum()
        q13 = q13[filtro_agno].sum()
        q14 = q14[filtro_agno].sum()
        q15 = q15[filtro_agno].sum()
        q16 = q16[filtro_agno].sum()
        q17 = q17[filtro_agno].sum()

        total_personas = [q1, q2, q3, q4, q5, q6, q7, q8, q9,
                          q10, q11, q12, q13, q14, q15, q16, q17]
        return total_personas

    def pob_comuna_sexo_quinquenio(dataframe, comuna, agno, sexo):
        agno_string = str(agno)
        filtro_agno = "Poblacion" + " " + agno_string
        sexo = str(sexo)
        if sexo == "hombre" or sexo == "masculino" or sexo == "1":
            sexo = 1
        elif sexo == "mujer" or sexo == "femenino" or sexo == "2":
            sexo = 2
        df_comuna = dataframe[(dataframe.Comuna == comuna)]
        df_comuna_sexo = df_comuna[(df_comuna.Sexo == sexo)]
        df_agno = df_comuna_sexo.groupby(['Edad'], as_index=False).sum()
        q1 = df_agno[['Edad', filtro_agno]].query('Edad >= 0 & Edad <= 4')
        q2 = df_agno[['Edad', filtro_agno]].query('Edad >= 5 & Edad <= 9')
        q3 = df_agno[['Edad', filtro_agno]].query('Edad >= 10 & Edad <= 14')
        q4 = df_agno[['Edad', filtro_agno]].query('Edad >= 15 & Edad <= 19')
        q5 = df_agno[['Edad', filtro_agno]].query('Edad >= 20 & Edad <= 24')
        q6 = df_agno[['Edad', filtro_agno]].query('Edad >= 25 & Edad <= 29')
        q7 = df_agno[['Edad', filtro_agno]].query('Edad >= 30 & Edad <= 34')
        q8 = df_agno[['Edad', filtro_agno]].query('Edad >= 35 & Edad <= 39')
        q9 = df_agno[['Edad', filtro_agno]].query('Edad >= 40 & Edad <= 44')
        q10 = df_agno[['Edad', filtro_agno]].query('Edad >= 45 & Edad <= 49')
        q11 = df_agno[['Edad', filtro_agno]].query('Edad >= 50 & Edad <= 54')
        q12 = df_agno[['Edad', filtro_agno]].query('Edad >= 55 & Edad <= 59')
        q13 = df_agno[['Edad', filtro_agno]].query('Edad >= 60 & Edad <= 64')
        q14 = df_agno[['Edad', filtro_agno]].query('Edad >= 65 & Edad <= 69')
        q15 = df_agno[['Edad', filtro_agno]].query('Edad >= 70 & Edad <= 74')
        q16 = df_agno[['Edad', filtro_agno]].query('Edad >= 75 & Edad <= 79')
        q17 = df_agno[['Edad', filtro_agno]].query('Edad >= 80')
        q1 = q1[filtro_agno].sum()
        q2 = q2[filtro_agno].sum()
        q3 = q3[filtro_agno].sum()
        q4 = q4[filtro_agno].sum()
        q5 = q5[filtro_agno].sum()
        q6 = q6[filtro_agno].sum()
        q7 = q7[filtro_agno].sum()
        q8 = q8[filtro_agno].sum()
        q9 = q9[filtro_agno].sum()
        q10 = q10[filtro_agno].sum()
        q11 = q11[filtro_agno].sum()
        q12 = q12[filtro_agno].sum()
        q13 = q13[filtro_agno].sum()
        q14 = q14[filtro_agno].sum()
        q15 = q15[filtro_agno].sum()
        q16 = q16[filtro_agno].sum()
        q17 = q17[filtro_agno].sum()

        total_personas = [q1, q2, q3, q4, q5, q6, q7, q8, q9,
                          q10, q11, q12, q13, q14, q15, q16, q17]
        return total_personas

    if edad_quinquenal == False:
        if sexo == 0 and region == 0 and comuna == 0:
            total_personas = pob_total_pais(df, ano)
        elif sexo != 0 and (region == 0 and comuna == 0):
            total_personas = pob_total_pais_sexo(df, ano, sexo)
        elif sexo == 0 and (region != 0 or comuna != 0):
            if region != 0 and comuna == 0:
                total_personas = pob_region(df, region, ano)
            elif region == 0 and comuna != 0:
                total_personas = pob_comuna(df, comuna, ano)
        elif sexo != 0 and (region != 0 or comuna != 0):
            if region != 0 and comuna == 0:
                total_personas = pob_region_sexo(df, region, ano, sexo)
            elif region == 0 and comuna != 0:
                total_personas = pob_comuna_sexo(df, comuna, ano, sexo)
    elif edad_quinquenal == True:
        if sexo == 0 and region == 0 and comuna == 0:
            total_personas = pob_total_pais_quinquenio(df, ano)
        elif sexo != 0 and (region == 0 and comuna == 0):
            total_personas = pob_total_pais_sexo_quinquenio(df, ano, sexo)
        elif sexo == 0 and (region != 0 or comuna != 0):
            if region != 0 and comuna == 0:
                total_personas = pob_region_quinquenio(df, region, ano)
            elif region == 0 and comuna != 0:
                total_personas = pob_comuna_quinquenio(df, comuna, ano)
        elif sexo != 0 and (region != 0 or comuna != 0):
            if region != 0 and comuna == 0:
                total_personas = pob_region_sexo_quinquenio(df, region, ano, sexo)
            elif region == 0 and comuna != 0:
                total_personas = pob_comuna_sexo_quinquenio(df, comuna, ano, sexo)

    return total_personas



##################################################################################################################
##################################################################################################################
##################################################################################################################

# import pandas as pd
# import os
#
# path = os.path.abspath("/Users/alvaro/Documents/Data Science/Python/proyectos/rpc/tasas_mortalidad_v5/datasets/estimaciones-y-proyecciones-2002-2035-comunas.xlsx")
#
# df = pd.read_excel(path)
# ano = 2016
# sexo = 0
# region = 0
# comuna = 2101
#
# test = poblacion(df, ano, sexo, region, comuna, edad_quinquenal = True)
# print(f"nueva función: {test}")

