def num_muertes_cancer(dataframe, periodo, tabular, region=0, comuna=0, sexo=0, edad_quinquenal=False):
    periodo = periodo.split("-")
    per_inicial = int( "".join(periodo[0]))
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
    df_agno = dataframe[dataframe['ANO_DEF'].isin(x)].copy()
    reg = list()
    com = list()
    reg.append(region)
    com.append(comuna)
    total_defunciones = []

    if (tabular == 1 or tabular == 2) and edad_quinquenal == False:
        if tabular == 1:
            df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48"')
            llave = ["C00-D48"]
            if sexo == 0 and region == 0 and comuna == 0:
                valor_1 = []
                valor_2 = []
                valor_1.append(df_agno_tabularx['CAPITULO_DIAG1'].shape[0])
                valor_2.append("Todos los tumores")
                valor = list(zip(valor_1, valor_2))
                muertes_grupo = dict(zip(llave, valor))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append("Todos los tumores, en hombres")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append("Todos los tumores, en mujeres")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores, en hombres en la regi??n {region}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
                    elif sexo == 2:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores, en mujeres en la regi??n {region}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores, en hombres en la comuna {comuna}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
                    elif sexo == 2:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores, en mujeres en la comuna {comuna}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)]
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append(f"Todos los tumores, en la regi??n {region}")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo_sexo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo_sexo
                elif comuna != 0:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)]
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append(f"Todos los tumores, en la comuna {comuna}")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo_sexo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo_sexo
        elif tabular == 2:
            llave = ["C00-C97"]
            df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"')
            df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                     'CODIGO_GRUPO_DIAG1 == "C97"')
            if sexo == 0 and region == 0 and comuna == 0:
                valor_1 = []
                valor_2 = []
                valor_1.append(df_agno_tabularx['CAPITULO_DIAG1'].shape[0])
                valor_2.append("Todos los tumores malignos")
                valor = list(zip(valor_1, valor_2))
                muertes_grupo = dict(zip(llave, valor))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append("Todos los tumores malignos, en hombres")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append("Todos los tumores malignos, en mujeres")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores malignos, en hombres en la regi??n {region}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
                    elif sexo == 2:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores malignos, en mujeres en la regi??n {region}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores malignos, en hombres en la comuna {comuna}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
                    elif sexo == 2:
                        valor_1 = []
                        valor_2 = []
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        valor_1.append(df_agno_tabular_b['CAPITULO_DIAG1'].shape[0])
                        valor_2.append(f"Todos los tumores malignos, en mujeres en la comuna {comuna}")
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo_sexo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo_sexo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)]
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append(f"Todos los tumores malignos, en la regi??n {region}")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo_sexo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo_sexo
                elif comuna != 0:
                    valor_1 = []
                    valor_2 = []
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)]
                    valor_1.append(df_agno_tabular_a['CAPITULO_DIAG1'].shape[0])
                    valor_2.append(f"Todos los tumores malignos, en la comuna {comuna}")
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo_sexo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo_sexo

    if (tabular == 1 or tabular == 2) and edad_quinquenal == True:
        from codigo_main import buscar_faltantes as fal
        edad = df_agno['EDAD_CANT'].values.tolist()
        edad_tipo = df_agno['EDAD_TIPO'].values.tolist()
        edades = list(zip(edad, edad_tipo))
        edad_quinquenal = list()
        for tupla in edades:
            if tupla[1] == 1:
                if tupla[0] >= 1 and tupla[0] <= 4:
                    edad_quinquenal.append(1)
                elif tupla[0] >= 5 and tupla[0] <= 9:
                    edad_quinquenal.append(2)
                elif tupla[0] >= 10 and tupla[0] <= 14:
                    edad_quinquenal.append(3)
                elif tupla[0] >= 15 and tupla[0] <= 19:
                    edad_quinquenal.append(4)
                elif tupla[0] >= 20 and tupla[0] <= 24:
                    edad_quinquenal.append(5)
                elif tupla[0] >= 25 and tupla[0] <= 29:
                    edad_quinquenal.append(6)
                elif tupla[0] >= 30 and tupla[0] <= 34:
                    edad_quinquenal.append(7)
                elif tupla[0] >= 35 and tupla[0] <= 39:
                    edad_quinquenal.append(8)
                elif tupla[0] >= 40 and tupla[0] <= 44:
                    edad_quinquenal.append(9)
                elif tupla[0] >= 45 and tupla[0] <= 49:
                    edad_quinquenal.append(10)
                elif tupla[0] >= 50 and tupla[0] <= 54:
                    edad_quinquenal.append(11)
                elif tupla[0] >= 55 and tupla[0] <= 59:
                    edad_quinquenal.append(12)
                elif tupla[0] >= 60 and tupla[0] <= 64:
                    edad_quinquenal.append(13)
                elif tupla[0] >= 65 and tupla[0] <= 69:
                    edad_quinquenal.append(14)
                elif tupla[0] >= 70 and tupla[0] <= 74:
                    edad_quinquenal.append(15)
                elif tupla[0] >= 75 and tupla[0] <= 79:
                    edad_quinquenal.append(16)
                elif tupla[0] >= 80:
                    edad_quinquenal.append(17)
            elif tupla[1] >= 2:
                edad_quinquenal.append(1)
        df_agno['EDAD_QUINQ'] = edad_quinquenal
        llave = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        if tabular == 1:
            if sexo == 0 and region == 0 and comuna == 0:
                df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                edades_faltantes = fal.faltante(edad_quinquenal)
                if len(edades_faltantes) < 1:
                    df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                    valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                    muertes_grupo = dict(zip(llave, valor_1))
                    total_defunciones = muertes_grupo
                else:
                    df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                    valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                    for edad in edades_faltantes:
                        llave.remove(edad)
                    muertes_grupo = dict(zip(llave, valor_1))
                    total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48" and SEXO == 1')
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48" and SEXO == 2')
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
            if sexo != 0 and (region != 0 or comuna != 0):
                    if sexo != 0 and region != 0 and comuna == 0:
                        if sexo == 1:
                            df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48" and SEXO == 1').copy()
                            df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                            edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                            edades_faltantes = fal.faltante(edad_quinquenal)
                            if len(edades_faltantes) < 1:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                            else:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                for edad in edades_faltantes:
                                    llave.remove(edad)
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                        elif sexo == 2:
                            df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48" and SEXO == 2').copy()
                            df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                            edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                            edades_faltantes = fal.faltante(edad_quinquenal)
                            if len(edades_faltantes) < 1:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                            else:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                for edad in edades_faltantes:
                                    llave.remove(edad)
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                    elif sexo != 0 and region == 0 and comuna != 0:
                        if sexo == 1:
                            df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48" and SEXO == 1').copy()
                            df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                            edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                            edades_faltantes = fal.faltante(edad_quinquenal)
                            if len(edades_faltantes) < 1:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                            else:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                for edad in edades_faltantes:
                                    llave.remove(edad)
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                        elif sexo == 2:
                            df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48" and SEXO == 2').copy()
                            df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                            edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                            edades_faltantes = fal.faltante(edad_quinquenal)
                            if len(edades_faltantes) < 1:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
                            else:
                                df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ", "SEXO"]).count()
                                valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                                for edad in edades_faltantes:
                                    llave.remove(edad)
                                muertes_grupo_sexo = dict(zip(llave, valor_1))
                                total_defunciones = muertes_grupo_sexo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
                elif comuna != 0:
                    df_agno_tabularx = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
        elif tabular == 2:
            reg = list()
            reg.append(region)
            if sexo == 0 and region == 0 and comuna == 0:
                df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                         'CODIGO_GRUPO_DIAG1 == "C97"')
                edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                edades_faltantes = fal.faltante(edad_quinquenal)
                if len(edades_faltantes) < 1:
                    df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                    valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                    muertes_grupo = dict(zip(llave, valor_1))
                    total_defunciones = muertes_grupo
                else:
                    df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                    valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                    for edad in edades_faltantes:
                        llave.remove(edad)
                    muertes_grupo = dict(zip(llave, valor_1))
                    total_defunciones = muertes_grupo

            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                    df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C97"')
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 1')
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                    df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C97"')
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 2')
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                        df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C97"')
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1')
                        edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                        edades_faltantes = fal.faltante(edad_quinquenal)
                        if len(edades_faltantes) < 1:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                        else:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            for edad in edades_faltantes:
                                llave.remove(edad)
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                    elif sexo == 2:
                        df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                        df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C97"')
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2')
                        edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                        edades_faltantes = fal.faltante(edad_quinquenal)
                        if len(edades_faltantes) < 1:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                        else:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            for edad in edades_faltantes:
                                llave.remove(edad)
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                        df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C97"')
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1')
                        edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                        edades_faltantes = fal.faltante(edad_quinquenal)
                        if len(edades_faltantes) < 1:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                        else:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            for edad in edades_faltantes:
                                llave.remove(edad)
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                    elif sexo == 2:
                        df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                        df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                                 'CODIGO_GRUPO_DIAG1 == "C97"')
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2')
                        edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                        edades_faltantes = fal.faltante(edad_quinquenal)
                        if len(edades_faltantes) < 1:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
                        else:
                            df_agno_tabularx = df_agno_tabularx.groupby("EDAD_QUINQ").count()
                            valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                            for edad in edades_faltantes:
                                llave.remove(edad)
                            muertes_grupo_sexo = dict(zip(llave, valor_1))
                            total_defunciones = muertes_grupo_sexo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                    df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C97"')
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
                elif comuna != 0:
                    df_agno_tabular = df_agno.query('CAPITULO_DIAG1 == "C00-D48"').copy()
                    df_agno_tabularx = df_agno_tabular.query('CODIGO_GRUPO_DIAG1 == "C00-C14"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C30-C39"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C43-C44"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C50"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C60-C63"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C69-C72"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C76-C80"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                                                             'CODIGO_GRUPO_DIAG1 == "C97"')
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                    edad_quinquenal = df_agno_tabularx['EDAD_QUINQ'].values.tolist()
                    #print(f"edades quinquenales: {edad_quinquenal}")
                    edades_faltantes = fal.faltante(edad_quinquenal)
                    if len(edades_faltantes) < 1:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo
                    else:
                        df_agno_tabularx = df_agno_tabularx.groupby(["EDAD_QUINQ"]).count()
                        valor_1 = df_agno_tabularx["DIAG1"].values.tolist()
                        for edad in edades_faltantes:
                            llave.remove(edad)
                        muertes_grupo_sexo = dict(zip(llave, valor_1))
                        total_defunciones = muertes_grupo_sexo

    if (tabular == 3 or tabular == 4 or tabular == 5) and edad_quinquenal == False:
        if tabular == 5:
            df_agno_tabularx = df_agno.query(
                'CODIGO_GRUPO_DIAG1 == "C00-C14" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C30-C39" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C40-C41" | CODIGO_GRUPO_DIAG1 == "C43-C44" | CODIGO_GRUPO_DIAG1 == "C45-C49" | CODIGO_GRUPO_DIAG1 == "C50" | CODIGO_GRUPO_DIAG1 == "C51-C58" | CODIGO_GRUPO_DIAG1 == "C60-C63" | CODIGO_GRUPO_DIAG1 == "C64-C68" | CODIGO_GRUPO_DIAG1 == "C69-C72" | CODIGO_GRUPO_DIAG1 == "C73-C75" | CODIGO_GRUPO_DIAG1 == "C76-C80" | CODIGO_GRUPO_DIAG1 == "C81-C96" | CODIGO_GRUPO_DIAG1 == "C97" | CODIGO_GRUPO_DIAG1 == "D00-D09" | CODIGO_GRUPO_DIAG1 == "D10-D36" | CODIGO_GRUPO_DIAG1 == "D37-D48"')

            if sexo == 0 and region == 0 and comuna == 0:
                a = df_agno_tabularx.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'], as_index=False).count()
                llave = []
                valor_1 = []
                valor_2 = []
                for codigo in a['CODIGO_GRUPO_DIAG1']:
                    llave.append(codigo.strip())
                for valor1 in a['CAPITULO_DIAG1']:
                    valor_1.append(valor1)
                for valor2 in a['GLOSA_GRUPO_DIAG1']:
                    valor_2.append(valor2.strip())
                valor = list(zip(valor_1, valor_2))
                muertes_grupo = dict(zip(llave, valor))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                    a = df_agno_tabular_a.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'], as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['CODIGO_GRUPO_DIAG1']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['GLOSA_GRUPO_DIAG1']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                    a = df_agno_tabular_a.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'], as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['CODIGO_GRUPO_DIAG1']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['GLOSA_GRUPO_DIAG1']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        a = df_agno_tabular_b.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['CODIGO_GRUPO_DIAG1']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['GLOSA_GRUPO_DIAG1']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        a = df_agno_tabular_b.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['CODIGO_GRUPO_DIAG1']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['GLOSA_GRUPO_DIAG1']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        a = df_agno_tabular_b.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['CODIGO_GRUPO_DIAG1']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['GLOSA_GRUPO_DIAG1']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        a = df_agno_tabular_b.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['CODIGO_GRUPO_DIAG1']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['GLOSA_GRUPO_DIAG1']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)]
                    a = df_agno_tabular_a.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                  as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['CODIGO_GRUPO_DIAG1']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['GLOSA_GRUPO_DIAG1']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif comuna != 0:
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)]
                    a = df_agno_tabular_a.groupby(by=['CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                  as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['CODIGO_GRUPO_DIAG1']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['GLOSA_GRUPO_DIAG1']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

        if tabular == 3:
            df_agno_tabularx = df_agno.query(
                'CODIGO_GRUPO_DIAG1 == "C00-C14" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C30-C39" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C40-C41" | CODIGO_GRUPO_DIAG1 == "C43-C44" | CODIGO_GRUPO_DIAG1 == "C45-C49" | CODIGO_GRUPO_DIAG1 == "C50" | CODIGO_GRUPO_DIAG1 == "C51-C58" | CODIGO_GRUPO_DIAG1 == "C60-C63" | CODIGO_GRUPO_DIAG1 == "C64-C68" | CODIGO_GRUPO_DIAG1 == "C69-C72" | CODIGO_GRUPO_DIAG1 == "C73-C75" | CODIGO_GRUPO_DIAG1 == "C76-C80" | CODIGO_GRUPO_DIAG1 == "C81-C96" | CODIGO_GRUPO_DIAG1 == "C97" | CODIGO_GRUPO_DIAG1 == "D00-D09" | CODIGO_GRUPO_DIAG1 == "D10-D36" | CODIGO_GRUPO_DIAG1 == "D37-D48"').copy()
            tabular_glosa = []
            tabular_cod = []
            tabular_cuenta = []

            for i in df_agno_tabularx['CODIGO_CATEGORIA_DIAG1']:
                if i == \
                        "C00" or i == "C01" or i == "C02" or i == \
                        "C03" or i == "C04" or i == "C05" or i == \
                        "C06" or i == "C07" or i == "C08" or i == \
                        "C09" or i == "C10" or i == "C11" or i == \
                        "C12" or i == "C13" or i == "C14":
                    tabular_cod.append("C00-C14")
                    tabular_glosa.append("Tumores malignos del labio de la cavidad bucal y la faringe")
                    tabular_cuenta.append("***")

                elif i == "C15":
                    tabular_cod.append("C15")
                    tabular_glosa.append("Tumor malignos del es??fago")
                    tabular_cuenta.append("***")
                elif i == "C16":
                    tabular_cod.append("C16")
                    tabular_glosa.append("Tumor maligno del est??mago")
                    tabular_cuenta.append("***")
                elif i == "C18" or i == "C19" or i == "C20" or i == "C21":
                    tabular_cod.append("C18-C21")
                    tabular_glosa.append("Tumor maligno del colon, recto y ano")
                    tabular_cuenta.append("***")
                elif i == "C22":
                    tabular_cod.append("C22")
                    tabular_glosa.append("Tumor maligno del h??gado y de las v??as biliares intrahep??ticas")
                    tabular_cuenta.append("***")
                elif i == "C25":
                    tabular_cod.append("C25")
                    tabular_glosa.append("Tumor maligno del p??ncreas")
                    tabular_cuenta.append("***")
                elif i == "C32":
                    tabular_cod.append("C32")
                    tabular_glosa.append("Tumor maligno de la laringe")
                    tabular_cuenta.append("***")
                elif i == "C33" or i == "C34":
                    tabular_cod.append("C33-C34")
                    tabular_glosa.append("Tumor maligno de la tr??quea de los bronquios y del pulm??n")
                    tabular_cuenta.append("***")
                elif i == "C43":
                    tabular_cod.append("C43")
                    tabular_glosa.append("Melanoma maligno de la piel")
                    tabular_cuenta.append("***")
                elif i == "C50":
                    tabular_cod.append("C50")
                    tabular_glosa.append("Tumor maligno de la mama")
                    tabular_cuenta.append("***")
                elif i == "C53":
                    tabular_cod.append("C53")
                    tabular_glosa.append("Tumor maligno del cuello del ??tero")
                    tabular_cuenta.append("***")
                elif i == "C54" or i == "C55":
                    tabular_cod.append("C54-C55")
                    tabular_glosa.append("Tumor maligno de otras partes y las no especificadas del ??tero")
                    tabular_cuenta.append("***")
                elif i == "C56":
                    tabular_cod.append("C56")
                    tabular_glosa.append("Tumor maligno del ovario")
                    tabular_cuenta.append("***")
                elif i == "C61":
                    tabular_cod.append("C61")
                    tabular_glosa.append("Tumor maligno de la pr??stata")
                    tabular_cuenta.append("***")
                elif i == "C67":
                    tabular_cod.append("C67")
                    tabular_glosa.append("Tumor maligno de la vejiga urianria")
                    tabular_cuenta.append("***")
                elif i == "C70" or i == "C71" or i == "C72":
                    tabular_cod.append("C70-C72")
                    tabular_glosa.append(
                        "Tumor maligno de las meninges del enc??falo y de otras partes del sistema nervioso central")
                    tabular_cuenta.append("***")
                elif i == "C82" or i == "C83" or i == "C84" or i == "C85":
                    tabular_cod.append("C82-C85")
                    tabular_glosa.append("Linfoma no Hodgkin")
                    tabular_cuenta.append("***")
                elif i == "C90":
                    tabular_cod.append("C90")
                    tabular_glosa.append("Mieloma M??ltiple y tumores malignos de c??lulas plasm??ticas")
                    tabular_cuenta.append("***")
                elif i == "C91" or i == "C92" or i == "C93" or i == "C94" or i == "C95":
                    tabular_cod.append("C91-C95")
                    tabular_glosa.append("Leucemia")
                    tabular_cuenta.append("***")
                elif i == \
                        "C17" or i == "C23" or i == "C24" or i == \
                        "C26" or i == "C30" or i == "C31" or i == \
                        "C37" or i == "C38" or i == "C39" or i == \
                        "C40" or i == "C41" or i == "C44" or i == \
                        "C45" or i == "C46" or i == "C47" or i == \
                        "C48" or i == "C49" or i == "C51" or i == \
                        "C52" or i == "C57" or i == "C58" or i == \
                        "C60" or i == "C62" or i == "C63" or i == \
                        "C64" or i == "C65" or i == "C66" or i == \
                        "C68" or i == "C69" or i == "C73" or i == \
                        "C74" or i == "C75" or i == "C76" or i == \
                        "C77" or i == "C78" or i == "C79" or i == \
                        "C80" or i == "C81" or i == "C86" or i == \
                        "C88" or i == "C96" or i == "C97":
                    tabular_cod.append(
                        "C17, C23-C24, C26-C31, C37-C41, C44-C49, "
                        "C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, "
                        "C88,C96-C97")
                    tabular_glosa.append("Resto de tumores malignos")
                    tabular_cuenta.append("***")
                elif i == \
                        "D00" or i == "D01" or i == "D02" or i == \
                        "D03" or i == "D04" or i == "D05" or i == \
                        "D06" or i == "D07" or i == "D09" or i == \
                        "D10" or i == "D11" or i == "D12" or i == \
                        "D13" or i == "D14" or i == "D15" or i == \
                        "D16" or i == "D17" or i == "D18" or i == \
                        "D19" or i == "D20" or i == "D21" or i == \
                        "D22" or i == "D23" or i == "D24" or i == \
                        "D25" or i == "D26" or i == "D27" or i == \
                        "D28" or i == "D29" or i == "D30" or i == \
                        "D31" or i == "D32" or i == "D33" or i == \
                        "D34" or i == "D35" or i == "D36" or i == \
                        "D37" or i == "D38" or i == "D39" or i == \
                        "D40" or i == "D41" or i == "D42" or i == \
                        "D43" or i == "D44" or i == "D45" or i == \
                        "D46" or i == "D47" or i == "D48":
                    tabular_cod.append("D00-D48")
                    tabular_glosa.append("Resto de tumores")
                    tabular_cuenta.append("***")
            df_agno_tabularx['tabular'] = tabular_cod
            df_agno_tabularx['tabular_glosa'] = tabular_glosa

            if sexo == 0 and region == 0 and comuna == 0:
                a = df_agno_tabularx.groupby(by=['tabular', 'tabular_glosa'], as_index=False).count()
                llave = []
                valor_1 = []
                valor_2 = []
                for codigo in a['tabular']:
                    llave.append(codigo.strip())
                for valor1 in a['CAPITULO_DIAG1']:
                    valor_1.append(valor1)
                for valor2 in a['tabular_glosa']:
                    valor_2.append(valor2.strip())
                valor = list(zip(valor_1, valor_2))
                muertes_grupo = dict(zip(llave, valor))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'], as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'], as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)]
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'],
                                                  as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif comuna != 0:
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)]
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'],
                                                  as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

        if tabular == 4:
            tabular_glosa = []
            tabular_cod = []
            df_agno_tabularx = df_agno.query(
                'CODIGO_GRUPO_DIAG1 == "C00-C14" | CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                'CODIGO_GRUPO_DIAG1 == "C30-C39" | CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                'CODIGO_GRUPO_DIAG1 == "C43-C44" | CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                'CODIGO_GRUPO_DIAG1 == "C50" | CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                'CODIGO_GRUPO_DIAG1 == "C60-C63" | CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                'CODIGO_GRUPO_DIAG1 == "C69-C72" | CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                'CODIGO_GRUPO_DIAG1 == "C76-C80" | CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                'CODIGO_GRUPO_DIAG1 == "C97" | '
                'CODIGO_GRUPO_DIAG1 == "D37-D48"').copy()

            for i in df_agno_tabularx['CODIGO_CATEGORIA_DIAG1']:
                if i == "C00":
                    tabular_cod.append("C00")
                    tabular_glosa.append("Tumor maligno del Labio")
                elif i == "C01" or i == "C02":
                    tabular_cod.append("C01-C02")
                    tabular_glosa.append("Tumor maligno de la Lengua")
                elif i == "C03" or i == "C04" or i == "C05" or i == "C06":
                    tabular_cod.append("C03-C06")
                    tabular_glosa.append("Tumor maligno de la Cavidad Oral")
                elif i == "C07" or i == "C08":
                    tabular_cod.append("C07-C08")
                    tabular_glosa.append("Tumor maligno de las Gl??ndulas Salivales")
                elif i == "C09":
                    tabular_cod.append("C09")
                    tabular_glosa.append("Tumor maligno de la Am??gdala")
                elif i == "C10":
                    tabular_cod.append("C10")
                    tabular_glosa.append("Tumor maligno de la Orofar??nge")
                elif i == "C11":
                    tabular_cod.append("C11")
                    tabular_glosa.append("Tumor maligno de la Nasofaringe")
                elif i == "C12" or i == "C13":
                    tabular_cod.append("C12-C13")
                    tabular_glosa.append("Tumor maligno de la Hipofaringe")
                elif i == "C14":
                    tabular_cod.append("C14")
                    tabular_glosa.append("Tumor maligno de otros sitios y de los mal definidos del Labio, Cavidad Bucal y Faringe")
                elif i == "C15":
                    tabular_cod.append("C15")
                    tabular_glosa.append("Tumor maligno del Es??fago")
                elif i == "C16":
                    tabular_cod.append("C16")
                    tabular_glosa.append("Tumor maligno del Est??mago")
                elif i == "C17":
                    tabular_cod.append("C17")
                    tabular_glosa.append("Tumor maligno del Intestino Delgado")
                elif i == "C18":
                    tabular_cod.append("C18")
                    tabular_glosa.append("Tumor maligno del Colon")
                elif i == "C19" or i == "C20":
                    tabular_cod.append("C19-C20")
                    tabular_glosa.append("Tumor maligno del Recto")
                elif i == "C21":
                    tabular_cod.append("C21")
                    tabular_glosa.append("Tumor maligno del Ano y del Conducto Anal")
                elif i == "C22":
                    tabular_cod.append("C22")
                    tabular_glosa.append("Tumor maligno del H??gado y de las V??as Biliares Intrahep??ticas")
                elif i == "C23" or i == "C24":
                    tabular_cod.append("C23-C24")
                    tabular_glosa.append("Tumor maligno de la Ves??cula Biliar y de las V??as Biliares")
                elif i == "C25":
                    tabular_cod.append("C25")
                    tabular_glosa.append("Tumor maligno del p??ncreas")
                elif i == "C30" or i == "C31":
                    tabular_cod.append("C30-C31")
                    tabular_glosa.append("Tumor maligno de las Cavidades Nasales y Senos Paranasales")
                elif i == "C32":
                    tabular_cod.append("C32")
                    tabular_glosa.append("Tumor maligno de la Laringe")
                elif i == "C33" or i == "C34":
                    tabular_cod.append("C33-C34")
                    tabular_glosa.append("Tumor maligno de la Tr??quea de los Bronquios y del Pulm??n")
                elif i == "C37" or i == "C38":
                    tabular_cod.append("C37-C38")
                    tabular_glosa.append("Tumor maligno de otros ??rganos tor??cicos")
                elif i == "C40" or i == "C41":
                    tabular_cod.append("C40-C41")
                    tabular_glosa.append("Tumor maligno de los Huesos y de los Cart??lagos Articulares")
                elif i == "C43":
                    tabular_cod.append("C43")
                    tabular_glosa.append("Melanoma maligno de la piel")
                elif i == "C44":
                    tabular_cod.append("C44")
                    tabular_glosa.append("Otros tumores malignos de la piel")
                elif i == "C45":
                    tabular_cod.append("C45")
                    tabular_glosa.append("Mesotelioma")
                elif i == "C46":
                    tabular_cod.append("C46")
                    tabular_glosa.append("Sarcoma de Kaposi")
                elif i == "C47" or i == "C48" or i == "C49":
                    tabular_cod.append("C47-C49")
                    tabular_glosa.append("Tumor maligno de Tejidos Blandos")
                elif i == "C50":
                    tabular_cod.append("C50")
                    tabular_glosa.append("Tumor maligno de la Mama")
                elif i == "C51":
                    tabular_cod.append("C51")
                    tabular_glosa.append("Tumor maligno de la Vulva ")
                elif i == "C52":
                    tabular_cod.append("C52")
                    tabular_glosa.append("Tumor maligno de la Vagina")
                elif i == "C53":
                    tabular_cod.append("C53")
                    tabular_glosa.append("Tumor maligno del Cuello del ??tero")
                elif i == "C54":
                    tabular_cod.append("C54")
                    tabular_glosa.append("Tumor maligno del Cuerpo del ??tero")
                elif i == "C55":
                    tabular_cod.append("C55")
                    tabular_glosa.append("Tumor maligno del ??tero, parte no especificada")
                elif i == "C56":
                    tabular_cod.append("C56")
                    tabular_glosa.append("Tumor maligno del Ovario")
                elif i == "C57":
                    tabular_cod.append("C57")
                    tabular_glosa.append("Tumor maligno de otros ??rganos genitales femeninos")
                elif i == "C58":
                    tabular_cod.append("C58")
                    tabular_glosa.append("Tumor maligno de la Placenta")
                elif i == "C60":
                    tabular_cod.append("C60")
                    tabular_glosa.append("Tumor maligno del Pene")
                elif i == "C61":
                    tabular_cod.append("C61")
                    tabular_glosa.append("Tumor maligno de la Pr??stata")
                elif i == "C62":
                    tabular_cod.append("C62")
                    tabular_glosa.append("Tumor maligno del Test??culo")
                elif i == "C63":
                    tabular_cod.append("C63")
                    tabular_glosa.append("Tumor maligno de otros ??rganos genitales masculinos")
                elif i == "C64":
                    tabular_cod.append("C64")
                    tabular_glosa.append("Tumor maligno del Ri??on, excepto Pelvis Renal")
                elif i == "C65":
                    tabular_cod.append("C65")
                    tabular_glosa.append("Tumor maligno de la Pelvis Renal")
                elif i == "C66":
                    tabular_cod.append("C66")
                    tabular_glosa.append("Tumor maligno del Ur??ter")
                elif i == "C67":
                    tabular_cod.append("C67")
                    tabular_glosa.append("Tumor maligno de la Vejiga Urinaria")
                elif i == "C68":
                    tabular_cod.append("C68")
                    tabular_glosa.append("Tumor maligno de otros ??rganos urinarios")
                elif i == "C69":
                    tabular_cod.append("C69")
                    tabular_glosa.append("Tumor maligno del Ojo y de sus Anexos")
                elif i == "C70" or i == "C71" or i == "C72":
                    tabular_cod.append("C70-C72")
                    tabular_glosa.append(
                        "Tumor maligno de las meninges del enc??falo y de otras partes del sistema nervioso central")
                elif i == "C73":
                    tabular_cod.append("C73")
                    tabular_glosa.append("Tumor maligno de la Gl??ndula Tiroides")
                elif i == "C74":
                    tabular_cod.append("C74")
                    tabular_glosa.append("Tumor maligno de la Gl??ndula Suprarrenal")
                elif i == "C75":
                    tabular_cod.append("C75")
                    tabular_glosa.append("Tumor maligno de otras gl??ndulas endocrinas y de estructuras afines")
                elif i == "C81":
                    tabular_cod.append("C81")
                    tabular_glosa.append("Enfermedad de Hodgkin")
                elif i == "C82" or i == "C83" or i == "C84" or i == "C85" or i == "C86" or i == "C96":
                    tabular_cod.append("C82-C86, C96")
                    tabular_glosa.append("Linfoma no Hodgkin")
                elif i == "C88":
                    tabular_cod.append("C88")
                    tabular_glosa.append("Enfermedades inmunoproliferativas malignas")
                elif i == "C90":
                    tabular_cod.append("C90")
                    tabular_glosa.append("Mieloma M??ltiple y tumores malignos de C??lulas Plasm??ticas")
                elif i == "C91":
                    tabular_cod.append("C91")
                    tabular_glosa.append("Leucemia linfoide")
                elif i == "C92" or i == "C93" or i == "C94":
                    tabular_cod.append("C92-C94")
                    tabular_glosa.append("Leucemia mieloide (total)")
                elif i == "C95":
                    tabular_cod.append("C95")
                    tabular_glosa.append("Leucemia de c??lulas de tipo no especificado")
                elif i == "D45":
                    tabular_cod.append("D45")
                    tabular_glosa.append("S??ndromes mieloproliferativos cr??nicos")
                elif i == "D46":
                    tabular_cod.append("D46")
                    tabular_glosa.append("S??ndromes mielodispl??sicos")
                elif i == "C26" or i == "C39" or i == "C76" or i == "C77" or i == "C78" or i == "C79" or i == "C80":
                    tabular_cod.append("C26, C39, C76-C80")
                    tabular_glosa.append("Primario desconocido")
                elif i == "C97":
                    tabular_cod.append("C97")
                    tabular_glosa.append("Tumores malignos (primarios) de sitios m??ltiples")
                elif i == "D37" or i == "D38" or i == "D39" or i == "D40" or i == "D41" or i == "D42" or i == "D43" or i == "D44"  or i == "D47" or i == "D48":
                    tabular_cod.append("D37-D44, D47-D48")
                    tabular_glosa.append("Otros tumores de comportamiento incierto o desconocido")
            df_agno_tabularx['tabular'] = tabular_cod
            df_agno_tabularx['tabular_glosa'] = tabular_glosa

            if sexo == 0 and region == 0 and comuna == 0:
                a = df_agno_tabularx.groupby(by=['tabular', 'tabular_glosa'], as_index=False).count()
                llave = []
                valor_1 = []
                valor_2 = []
                for codigo in a['tabular']:
                    llave.append(codigo.strip())
                for valor1 in a['CAPITULO_DIAG1']:
                    valor_1.append(valor1)
                for valor2 in a['tabular_glosa']:
                    valor_2.append(valor2.strip())
                valor = list(zip(valor_1, valor_2))
                muertes_grupo = dict(zip(llave, valor))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'], as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'], as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['REG_RES'].isin(reg)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 1')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabular_a = df_agno_tabularx.query('SEXO == 2')
                        df_agno_tabular_b = df_agno_tabular_a[df_agno_tabular_a['COMUNA'].isin(com)]
                        a = df_agno_tabular_b.groupby(by=['tabular', 'tabular_glosa'],
                                                      as_index=False).count()
                        llave = []
                        valor_1 = []
                        valor_2 = []
                        for codigo in a['tabular']:
                            llave.append(codigo.strip())
                        for valor1 in a['CAPITULO_DIAG1']:
                            valor_1.append(valor1)
                        for valor2 in a['tabular_glosa']:
                            valor_2.append(valor2.strip())
                        valor = list(zip(valor_1, valor_2))
                        muertes_grupo = dict(zip(llave, valor))
                        total_defunciones = muertes_grupo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)]
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'],
                                                  as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo
                elif comuna != 0:
                    df_agno_tabular_a = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)]
                    a = df_agno_tabular_a.groupby(by=['tabular', 'tabular_glosa'],
                                                  as_index=False).count()
                    llave = []
                    valor_1 = []
                    valor_2 = []
                    for codigo in a['tabular']:
                        llave.append(codigo.strip())
                    for valor1 in a['CAPITULO_DIAG1']:
                        valor_1.append(valor1)
                    for valor2 in a['tabular_glosa']:
                        valor_2.append(valor2.strip())
                    valor = list(zip(valor_1, valor_2))
                    muertes_grupo = dict(zip(llave, valor))
                    total_defunciones = muertes_grupo

    if (tabular == 3 or tabular == 4 or tabular == 5) and edad_quinquenal == True:
        edad = df_agno['EDAD_CANT'].values.tolist()
        edad_tipo = df_agno['EDAD_TIPO'].values.tolist()
        edades = list(zip(edad, edad_tipo))
        edad_quinquenal = list()
        for tupla in edades:
            if tupla[1] == 1:
                if tupla[0] >= 1 and tupla[0] <= 4:
                    edad_quinquenal.append(1)
                elif tupla[0] >= 5 and tupla[0] <= 9:
                    edad_quinquenal.append(2)
                elif tupla[0] >= 10 and tupla[0] <= 14:
                    edad_quinquenal.append(3)
                elif tupla[0] >= 15 and tupla[0] <= 19:
                    edad_quinquenal.append(4)
                elif tupla[0] >= 20 and tupla[0] <= 24:
                    edad_quinquenal.append(5)
                elif tupla[0] >= 25 and tupla[0] <= 29:
                    edad_quinquenal.append(6)
                elif tupla[0] >= 30 and tupla[0] <= 34:
                    edad_quinquenal.append(7)
                elif tupla[0] >= 35 and tupla[0] <= 39:
                    edad_quinquenal.append(8)
                elif tupla[0] >= 40 and tupla[0] <= 44:
                    edad_quinquenal.append(9)
                elif tupla[0] >= 45 and tupla[0] <= 49:
                    edad_quinquenal.append(10)
                elif tupla[0] >= 50 and tupla[0] <= 54:
                    edad_quinquenal.append(11)
                elif tupla[0] >= 55 and tupla[0] <= 59:
                    edad_quinquenal.append(12)
                elif tupla[0] >= 60 and tupla[0] <= 64:
                    edad_quinquenal.append(13)
                elif tupla[0] >= 65 and tupla[0] <= 69:
                    edad_quinquenal.append(14)
                elif tupla[0] >= 70 and tupla[0] <= 74:
                    edad_quinquenal.append(15)
                elif tupla[0] >= 75 and tupla[0] <= 79:
                    edad_quinquenal.append(16)
                elif tupla[0] >= 80:
                    edad_quinquenal.append(17)
            elif tupla[1] >= 2:
                edad_quinquenal.append(1)
        df_agno['EDAD_QUINQ'] = edad_quinquenal
        llave = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        if tabular == 5:
            df_agno_tabularx = df_agno.query(
                'CODIGO_GRUPO_DIAG1 == "C00-C14" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C30-C39" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C40-C41" | CODIGO_GRUPO_DIAG1 == "C43-C44" | CODIGO_GRUPO_DIAG1 == "C45-C49" | CODIGO_GRUPO_DIAG1 == "C50" | CODIGO_GRUPO_DIAG1 == "C51-C58" | CODIGO_GRUPO_DIAG1 == "C60-C63" | CODIGO_GRUPO_DIAG1 == "C64-C68" | CODIGO_GRUPO_DIAG1 == "C69-C72" | CODIGO_GRUPO_DIAG1 == "C73-C75" | CODIGO_GRUPO_DIAG1 == "C76-C80" | CODIGO_GRUPO_DIAG1 == "C81-C96" | CODIGO_GRUPO_DIAG1 == "C97" | CODIGO_GRUPO_DIAG1 == "D00-D09" | CODIGO_GRUPO_DIAG1 == "D10-D36" | CODIGO_GRUPO_DIAG1 == "D37-D48"').copy()

            if sexo == 0 and region == 0 and comuna == 0:
                a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'], as_index=False).count()
                b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                cod_grupo = list()
                edad_quinquenal = list()
                conteo_casos = list()
                for i in b['CODIGO_GRUPO_DIAG1']:
                    cod_grupo.append(i)
                for c in b['EDAD_QUINQ']:
                    edad_quinquenal.append(c)
                for d in b['DIAG1']:
                    conteo_casos.append(d)
                valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                contador = 0
                lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                for i in edad_quinquenal:
                    if i == 1:
                        lista[0].append(valores_1[contador])
                    elif i == 2:
                        lista[1].append(valores_1[contador])
                    elif i == 3:
                        lista[2].append(valores_1[contador])
                    elif i == 4:
                        lista[3].append(valores_1[contador])
                    elif i == 5:
                        lista[4].append(valores_1[contador])
                    elif i == 6:
                        lista[5].append(valores_1[contador])
                    elif i == 7:
                        lista[6].append(valores_1[contador])
                    elif i == 8:
                        lista[7].append(valores_1[contador])
                    elif i == 9:
                        lista[8].append(valores_1[contador])
                    elif i == 10:
                        lista[9].append(valores_1[contador])
                    elif i == 11:
                        lista[10].append(valores_1[contador])
                    elif i == 12:
                        lista[11].append(valores_1[contador])
                    elif i == 13:
                        lista[12].append(valores_1[contador])
                    elif i == 14:
                        lista[13].append(valores_1[contador])
                    elif i == 15:
                        lista[14].append(valores_1[contador])
                    elif i == 16:
                        lista[15].append(valores_1[contador])
                    elif i == 17:
                        lista[16].append(valores_1[contador])
                    contador += 1
                muertes_grupo = dict(zip(llave, lista))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['CODIGO_GRUPO_DIAG1']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['CODIGO_GRUPO_DIAG1']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0:
                    if sexo == 1:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['CODIGO_GRUPO_DIAG1']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['CODIGO_GRUPO_DIAG1']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['CODIGO_GRUPO_DIAG1']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['CODIGO_GRUPO_DIAG1']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['CODIGO_GRUPO_DIAG1']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo
                elif comuna != 0:
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'GLOSA_GRUPO_DIAG1'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'CODIGO_GRUPO_DIAG1', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['CODIGO_GRUPO_DIAG1']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo

        if tabular == 3:
            df_agno_tabularx = df_agno.query(
                'CODIGO_GRUPO_DIAG1 == "C00-C14" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C30-C39" | CODIGO_GRUPO_DIAG1 == "C15-C26" | CODIGO_GRUPO_DIAG1 == "C40-C41" | CODIGO_GRUPO_DIAG1 == "C43-C44" | CODIGO_GRUPO_DIAG1 == "C45-C49" | CODIGO_GRUPO_DIAG1 == "C50" | CODIGO_GRUPO_DIAG1 == "C51-C58" | CODIGO_GRUPO_DIAG1 == "C60-C63" | CODIGO_GRUPO_DIAG1 == "C64-C68" | CODIGO_GRUPO_DIAG1 == "C69-C72" | CODIGO_GRUPO_DIAG1 == "C73-C75" | CODIGO_GRUPO_DIAG1 == "C76-C80" | CODIGO_GRUPO_DIAG1 == "C81-C96" | CODIGO_GRUPO_DIAG1 == "C97" | CODIGO_GRUPO_DIAG1 == "D00-D09" | CODIGO_GRUPO_DIAG1 == "D10-D36" | CODIGO_GRUPO_DIAG1 == "D37-D48"').copy()
            tabular_glosa = []
            tabular_cod = []
            tabular_cuenta = []

            for i in df_agno_tabularx['CODIGO_CATEGORIA_DIAG1']:
                if i == \
                        "C00" or i == "C01" or i == "C02" or i == \
                        "C03" or i == "C04" or i == "C05" or i == \
                        "C06" or i == "C07" or i == "C08" or i == \
                        "C09" or i == "C10" or i == "C11" or i == \
                        "C12" or i == "C13" or i == "C14":
                    tabular_cod.append("C00-C14")
                    tabular_glosa.append("Tumores malignos del labio de la cavidad bucal y la faringe")
                    tabular_cuenta.append("***")

                elif i == "C15":
                    tabular_cod.append("C15")
                    tabular_glosa.append("Tumor malignos del es??fago")
                    tabular_cuenta.append("***")
                elif i == "C16":
                    tabular_cod.append("C16")
                    tabular_glosa.append("Tumor maligno del est??mago")
                    tabular_cuenta.append("***")
                elif i == "C18" or i == "C19" or i == "C20" or i == "C21":
                    tabular_cod.append("C18-C21")
                    tabular_glosa.append("Tumor maligno del colon, recto y ano")
                    tabular_cuenta.append("***")
                elif i == "C22":
                    tabular_cod.append("C22")
                    tabular_glosa.append("Tumor maligno del h??gado y de las v??as biliares intrahep??ticas")
                    tabular_cuenta.append("***")
                elif i == "C25":
                    tabular_cod.append("C25")
                    tabular_glosa.append("Tumor maligno del p??ncreas")
                    tabular_cuenta.append("***")
                elif i == "C32":
                    tabular_cod.append("C32")
                    tabular_glosa.append("Tumor maligno de la laringe")
                    tabular_cuenta.append("***")
                elif i == "C33" or i == "C34":
                    tabular_cod.append("C33-C34")
                    tabular_glosa.append("Tumor maligno de la tr??quea de los bronquios y del pulm??n")
                    tabular_cuenta.append("***")
                elif i == "C43":
                    tabular_cod.append("C43")
                    tabular_glosa.append("Melanoma maligno de la piel")
                    tabular_cuenta.append("***")
                elif i == "C50":
                    tabular_cod.append("C50")
                    tabular_glosa.append("Tumor maligno de la mama")
                    tabular_cuenta.append("***")
                elif i == "C53":
                    tabular_cod.append("C53")
                    tabular_glosa.append("Tumor maligno del cuello del ??tero")
                    tabular_cuenta.append("***")
                elif i == "C54" or i == "C55":
                    tabular_cod.append("C54-C55")
                    tabular_glosa.append("Tumor maligno de otras partes y las no especificadas del ??tero")
                    tabular_cuenta.append("***")
                elif i == "C56":
                    tabular_cod.append("C56")
                    tabular_glosa.append("Tumor maligno del ovario")
                    tabular_cuenta.append("***")
                elif i == "C61":
                    tabular_cod.append("C61")
                    tabular_glosa.append("Tumor maligno de la pr??stata")
                    tabular_cuenta.append("***")
                elif i == "C67":
                    tabular_cod.append("C67")
                    tabular_glosa.append("Tumor maligno de la vejiga urianria")
                    tabular_cuenta.append("***")
                elif i == "C70" or i == "C71" or i == "C72":
                    tabular_cod.append("C70-C72")
                    tabular_glosa.append(
                        "Tumor maligno de las meninges del enc??falo y de otras partes del sistema nervioso central")
                    tabular_cuenta.append("***")
                elif i == "C82" or i == "C83" or i == "C84" or i == "C85":
                    tabular_cod.append("C82-C85")
                    tabular_glosa.append("Linfoma no Hodgkin")
                    tabular_cuenta.append("***")
                elif i == "C90":
                    tabular_cod.append("C90")
                    tabular_glosa.append("Mieloma M??ltiple y tumores malignos de c??lulas plasm??ticas")
                    tabular_cuenta.append("***")
                elif i == "C91" or i == "C92" or i == "C93" or i == "C94" or i == "C95":
                    tabular_cod.append("C91-C95")
                    tabular_glosa.append("Leucemia")
                    tabular_cuenta.append("***")
                elif i == \
                        "C17" or i == "C23" or i == "C24" or i == \
                        "C26" or i == "C30" or i == "C31" or i == \
                        "C37" or i == "C38" or i == "C39" or i == \
                        "C40" or i == "C41" or i == "C44" or i == \
                        "C45" or i == "C46" or i == "C47" or i == \
                        "C48" or i == "C49" or i == "C51" or i == \
                        "C52" or i == "C57" or i == "C58" or i == \
                        "C60" or i == "C62" or i == "C63" or i == \
                        "C64" or i == "C65" or i == "C66" or i == \
                        "C68" or i == "C69" or i == "C73" or i == \
                        "C74" or i == "C75" or i == "C76" or i == \
                        "C77" or i == "C78" or i == "C79" or i == \
                        "C80" or i == "C81" or i == "C86" or i == \
                        "C88" or i == "C96" or i == "C97":
                    tabular_cod.append(
                        "C17, C23-C24, C26-C31, C37-C41, C44-C49, "
                        "C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, "
                        "C88,C96-C97")
                    tabular_glosa.append("Resto de tumores malignos")
                    tabular_cuenta.append("***")
                elif i == \
                        "D00" or i == "D01" or i == "D02" or i == \
                        "D03" or i == "D04" or i == "D05" or i == \
                        "D06" or i == "D07" or i == "D09" or i == \
                        "D10" or i == "D11" or i == "D12" or i == \
                        "D13" or i == "D14" or i == "D15" or i == \
                        "D16" or i == "D17" or i == "D18" or i == \
                        "D19" or i == "D20" or i == "D21" or i == \
                        "D22" or i == "D23" or i == "D24" or i == \
                        "D25" or i == "D26" or i == "D27" or i == \
                        "D28" or i == "D29" or i == "D30" or i == \
                        "D31" or i == "D32" or i == "D33" or i == \
                        "D34" or i == "D35" or i == "D36" or i == \
                        "D37" or i == "D38" or i == "D39" or i == \
                        "D40" or i == "D41" or i == "D42" or i == \
                        "D43" or i == "D44" or i == "D45" or i == \
                        "D46" or i == "D47" or i == "D48":
                    tabular_cod.append("D00-D48")
                    tabular_glosa.append("Resto de tumores")
                    tabular_cuenta.append("***")
            df_agno_tabularx['tabular'] = tabular_cod
            df_agno_tabularx['tabular_glosa'] = tabular_glosa

            if sexo == 0 and region == 0 and comuna == 0:
                a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'], as_index=False).count()
                b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                cod_grupo = list()
                edad_quinquenal = list()
                conteo_casos = list()
                for i in b['tabular']:
                    cod_grupo.append(i)
                for c in b['EDAD_QUINQ']:
                    edad_quinquenal.append(c)
                for d in b['DIAG1']:
                    conteo_casos.append(d)
                valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                contador = 0
                lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                for i in edad_quinquenal:
                    if i == 1:
                        lista[0].append(valores_1[contador])
                    elif i == 2:
                        lista[1].append(valores_1[contador])
                    elif i == 3:
                        lista[2].append(valores_1[contador])
                    elif i == 4:
                        lista[3].append(valores_1[contador])
                    elif i == 5:
                        lista[4].append(valores_1[contador])
                    elif i == 6:
                        lista[5].append(valores_1[contador])
                    elif i == 7:
                        lista[6].append(valores_1[contador])
                    elif i == 8:
                        lista[7].append(valores_1[contador])
                    elif i == 9:
                        lista[8].append(valores_1[contador])
                    elif i == 10:
                        lista[9].append(valores_1[contador])
                    elif i == 11:
                        lista[10].append(valores_1[contador])
                    elif i == 12:
                        lista[11].append(valores_1[contador])
                    elif i == 13:
                        lista[12].append(valores_1[contador])
                    elif i == 14:
                        lista[13].append(valores_1[contador])
                    elif i == 15:
                        lista[14].append(valores_1[contador])
                    elif i == 16:
                        lista[15].append(valores_1[contador])
                    elif i == 17:
                        lista[16].append(valores_1[contador])
                    contador += 1
                muertes_grupo = dict(zip(llave, lista))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'], as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'], as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo
                elif comuna != 0:
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo

        if tabular == 4:
            tabular_glosa = []
            tabular_cod = []
            df_agno_tabularx = df_agno.query(
                'CODIGO_GRUPO_DIAG1 == "C00-C14" | CODIGO_GRUPO_DIAG1 == "C15-C26"|'
                'CODIGO_GRUPO_DIAG1 == "C30-C39" | CODIGO_GRUPO_DIAG1 == "C40-C41"|'
                'CODIGO_GRUPO_DIAG1 == "C43-C44" | CODIGO_GRUPO_DIAG1 == "C45-C49"|'
                'CODIGO_GRUPO_DIAG1 == "C50" | CODIGO_GRUPO_DIAG1 == "C51-C58"|'
                'CODIGO_GRUPO_DIAG1 == "C60-C63" | CODIGO_GRUPO_DIAG1 == "C64-C68"|'
                'CODIGO_GRUPO_DIAG1 == "C69-C72" | CODIGO_GRUPO_DIAG1 == "C73-C75"|'
                'CODIGO_GRUPO_DIAG1 == "C76-C80" | CODIGO_GRUPO_DIAG1 == "C81-C96"|'
                'CODIGO_GRUPO_DIAG1 == "C97" | CODIGO_GRUPO_DIAG1 == "D00-D09" |'
                'CODIGO_GRUPO_DIAG1 == "D10-D36" | CODIGO_GRUPO_DIAG1 == "D37-D48"').copy()

            for i in df_agno_tabularx['CODIGO_CATEGORIA_DIAG1']:
                if i == "C00":
                    tabular_cod.append("C00")
                    tabular_glosa.append("Tumor maligno del Labio")
                elif i == "C01" or i == "C02":
                    tabular_cod.append("C01-C02")
                    tabular_glosa.append("Tumor maligno de la Lengua")
                elif i == "C03" or i == "C06":
                    tabular_cod.append("C03-C06")
                    tabular_glosa.append("Tumor maligno de la Cavidad Oral")
                elif i == "C07" or i == "C08":
                    tabular_cod.append("C07-C08")
                    tabular_glosa.append("Tumor maligno de las Gl??ndulas Salivales")
                elif i == "C09":
                    tabular_cod.append("C09")
                    tabular_glosa.append("Tumor maligno de la Am??gdala")
                elif i == "C10":
                    tabular_cod.append("C10")
                    tabular_glosa.append("Tumor maligno de la Orofar??nge")
                elif i == "C11":
                    tabular_cod.append("C11")
                    tabular_glosa.append("Tumor maligno de la Nasofaringe")
                elif i == "C12" or i == "C13":
                    tabular_cod.append("C12-C13")
                    tabular_glosa.append("Tumor maligno de la Hipofaringe")
                elif i == "C14":
                    tabular_cod.append("C14")
                    tabular_glosa.append(
                        "Tumor maligno de otros sitios y de los mal definidos del Labio, Cavidad Bucal y Faringe")
                elif i == "C15":
                    tabular_cod.append("C15")
                    tabular_glosa.append("Tumor maligno del Es??fago")
                elif i == "C16":
                    tabular_cod.append("C16")
                    tabular_glosa.append("Tumor maligno del Est??mago")
                elif i == "C17":
                    tabular_cod.append("C17")
                    tabular_glosa.append("Tumor maligno del Intestino Delgado")
                elif i == "C18":
                    tabular_cod.append("C18")
                    tabular_glosa.append("Tumor maligno del Colon")
                elif i == "C19" or i == "C20":
                    tabular_cod.append("C19-C20")
                    tabular_glosa.append("Tumor maligno del Recto")
                elif i == "C21":
                    tabular_cod.append("C21")
                    tabular_glosa.append("Tumor maligno del Ano y del Conducto Anal")
                elif i == "C22":
                    tabular_cod.append("C22")
                    tabular_glosa.append("Tumor maligno del H??gado y de las V??as Biliares Intrahep??ticas")
                elif i == "C23" or i == "C24":
                    tabular_cod.append("C23-C24")
                    tabular_glosa.append("Tumor maligno de la Ves??cula Biliar y de las V??as Biliares")
                elif i == "C25":
                    tabular_cod.append("C25")
                    tabular_glosa.append("Tumor maligno del p??ncreas")
                elif i == "C30" or i == "C31":
                    tabular_cod.append("C30-C31")
                    tabular_glosa.append("Tumor maligno de las Cavidades Nasales y Senos Paranasales")
                elif i == "C32":
                    tabular_cod.append("C32")
                    tabular_glosa.append("Tumor maligno de la Laringe")
                elif i == "C33" or i == "C34":
                    tabular_cod.append("C33-C34")
                    tabular_glosa.append("Tumor maligno de la Tr??quea de los Bronquios y del Pulm??n")
                elif i == "C37" or i == "C38":
                    tabular_cod.append("C37-C38")
                    tabular_glosa.append("Tumor maligno de otros ??rganos tor??cicos")
                elif i == "C40" or i == "C41":
                    tabular_cod.append("C40-C41")
                    tabular_glosa.append("Tumor maligno de los Huesos y de los Cart??lagos Articulares")
                elif i == "C43":
                    tabular_cod.append("C43")
                    tabular_glosa.append("Melanoma maligno de la piel")
                elif i == "C44":
                    tabular_cod.append("C44")
                    tabular_glosa.append("Otros tumores malignos de la piel")
                elif i == "C45":
                    tabular_cod.append("C45")
                    tabular_glosa.append("Mesotelioma")
                elif i == "C46":
                    tabular_cod.append("C46")
                    tabular_glosa.append("Sarcoma de Kaposi")
                elif i == "C47" or i == "C48" or i == "C49":
                    tabular_cod.append("C47-C49")
                    tabular_glosa.append("Tumor maligno de Tejidos Blandos")
                elif i == "C50":
                    tabular_cod.append("C50")
                    tabular_glosa.append("Tumor maligno de la Mama")
                elif i == "C51":
                    tabular_cod.append("C51")
                    tabular_glosa.append("Tumor maligno de la Vulva ")
                elif i == "C52":
                    tabular_cod.append("C52")
                    tabular_glosa.append("Tumor maligno de la Vagina")
                elif i == "C53":
                    tabular_cod.append("C53")
                    tabular_glosa.append("Tumor maligno del Cuello del ??tero")
                elif i == "C54":
                    tabular_cod.append("C54")
                    tabular_glosa.append("Tumor maligno del Cuerpo del ??tero")
                elif i == "C55":
                    tabular_cod.append("C55")
                    tabular_glosa.append("Tumor maligno del ??tero, parte no especificada")
                elif i == "C56":
                    tabular_cod.append("C56")
                    tabular_glosa.append("Tumor maligno del Ovario")
                elif i == "C57":
                    tabular_cod.append("C57")
                    tabular_glosa.append("Tumor maligno de otros ??rganos genitales femeninos")
                elif i == "C58":
                    tabular_cod.append("C58")
                    tabular_glosa.append("Tumor maligno de la Placenta")
                elif i == "C60":
                    tabular_cod.append("C60")
                    tabular_glosa.append("Tumor maligno del Pene")
                elif i == "C61":
                    tabular_cod.append("C61")
                    tabular_glosa.append("Tumor maligno de la Pr??stata")
                elif i == "C62":
                    tabular_cod.append("C62")
                    tabular_glosa.append("Tumor maligno del Test??culo")
                elif i == "C63":
                    tabular_cod.append("C63")
                    tabular_glosa.append("Tumor maligno de otros ??rganos genitales masculinos")
                elif i == "C64":
                    tabular_cod.append("C64")
                    tabular_glosa.append("Tumor maligno del Ri??on, excepto Pelvis Renal")
                elif i == "C65":
                    tabular_cod.append("C65")
                    tabular_glosa.append("Tumor maligno de la Pelvis Renal")
                elif i == "C66":
                    tabular_cod.append("C66")
                    tabular_glosa.append("Tumor maligno del Ur??ter")
                elif i == "C67":
                    tabular_cod.append("C67")
                    tabular_glosa.append("Tumor maligno de la Vejiga Urinaria")
                elif i == "C68":
                    tabular_cod.append("C68")
                    tabular_glosa.append("Tumor maligno de otros ??rganos urinarios")
                elif i == "C69":
                    tabular_cod.append("C69")
                    tabular_glosa.append("Tumor maligno del Ojo y de sus Anexos")
                elif i == "C70" or i == "C71" or i == "C72":
                    tabular_cod.append("C70-C72")
                    tabular_glosa.append(
                        "Tumor maligno de las meninges del enc??falo y de otras partes del sistema nervioso central")
                elif i == "C73":
                    tabular_cod.append("C73")
                    tabular_glosa.append("Tumor maligno de la Gl??ndula Tiroides")
                elif i == "C74":
                    tabular_cod.append("C74")
                    tabular_glosa.append("Tumor maligno de la Gl??ndula Suprarrenal")
                elif i == "C75":
                    tabular_cod.append("C75")
                    tabular_glosa.append("Tumor maligno de otras gl??ndulas endocrinas y de estructuras afines")
                elif i == "C81":
                    tabular_cod.append("C81")
                    tabular_glosa.append("Enfermedad de Hodgkin")
                elif i == "C82" or i == "C83" or i == "C84" or i == "C85" or i == "C86" or i == "C96":
                    tabular_cod.append("C82-C86, C96")
                    tabular_glosa.append("Linfoma no Hodgkin")
                elif i == "C88":
                    tabular_cod.append("C88")
                    tabular_glosa.append("Enfermedades inmunoproliferativas malignas")
                elif i == "C90":
                    tabular_cod.append("C90")
                    tabular_glosa.append("Mieloma M??ltiple y tumores malignos de C??lulas Plasm??ticas")
                elif i == "C91":
                    tabular_cod.append("C91")
                    tabular_glosa.append("Leucemia linfoide")
                elif i == "C92" or i == "C93" or i == "C94":
                    tabular_cod.append("C92-C94")
                    tabular_glosa.append("Leucemia mieloide (total)")
                elif i == "C95":
                    tabular_cod.append("C95")
                    tabular_glosa.append("Leucemia de c??lulas de tipo no especificado")
                elif i == "D45":
                    tabular_cod.append("D45")
                    tabular_glosa.append("S??ndromes mieloproliferativos cr??nicos")
                elif i == "D46":
                    tabular_cod.append("D46")
                    tabular_glosa.append("S??ndromes mielodispl??sicos")
                elif i == "C26" or i == "C39" or i == "C76" or i == "C77" or i == "C78" or i == "C79" or i == "C80":
                    tabular_cod.append("C26, C39, C76-C80")
                    tabular_glosa.append("Primario desconocido")
            df_agno_tabularx['tabular'] = tabular_cod
            df_agno_tabularx['tabular_glosa'] = tabular_glosa

            if sexo == 0 and region == 0 and comuna == 0:
                a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'], as_index=False).count()
                b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                cod_grupo = list()
                edad_quinquenal = list()
                conteo_casos = list()
                for i in b['tabular']:
                    cod_grupo.append(i)
                for c in b['EDAD_QUINQ']:
                    edad_quinquenal.append(c)
                for d in b['DIAG1']:
                    conteo_casos.append(d)
                valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                contador = 0
                lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                for i in edad_quinquenal:
                    if i == 1:
                        lista[0].append(valores_1[contador])
                    elif i == 2:
                        lista[1].append(valores_1[contador])
                    elif i == 3:
                        lista[2].append(valores_1[contador])
                    elif i == 4:
                        lista[3].append(valores_1[contador])
                    elif i == 5:
                        lista[4].append(valores_1[contador])
                    elif i == 6:
                        lista[5].append(valores_1[contador])
                    elif i == 7:
                        lista[6].append(valores_1[contador])
                    elif i == 8:
                        lista[7].append(valores_1[contador])
                    elif i == 9:
                        lista[8].append(valores_1[contador])
                    elif i == 10:
                        lista[9].append(valores_1[contador])
                    elif i == 11:
                        lista[10].append(valores_1[contador])
                    elif i == 12:
                        lista[11].append(valores_1[contador])
                    elif i == 13:
                        lista[12].append(valores_1[contador])
                    elif i == 14:
                        lista[13].append(valores_1[contador])
                    elif i == 15:
                        lista[14].append(valores_1[contador])
                    elif i == 16:
                        lista[15].append(valores_1[contador])
                    elif i == 17:
                        lista[16].append(valores_1[contador])
                    contador += 1
                muertes_grupo = dict(zip(llave, lista))
                total_defunciones = muertes_grupo
            elif sexo != 0 and region == 0 or comuna == 0:
                if sexo == 1:
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'], as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo
                elif sexo == 2:
                    df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'], as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo

            if sexo != 0 and (region != 0 or comuna != 0):
                if sexo != 0 and region != 0 and comuna == 0:
                    if sexo == 1:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                elif sexo != 0 and region == 0 and comuna != 0:
                    if sexo == 1:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 1').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
                    elif sexo == 2:
                        df_agno_tabularx = df_agno_tabularx.query('SEXO == 2').copy()
                        df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                        a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                     as_index=False).count()
                        b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                        cod_grupo = list()
                        edad_quinquenal = list()
                        conteo_casos = list()
                        for i in b['tabular']:
                            cod_grupo.append(i)
                        for c in b['EDAD_QUINQ']:
                            edad_quinquenal.append(c)
                        for d in b['DIAG1']:
                            conteo_casos.append(d)
                        valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                        contador = 0
                        lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                        for i in edad_quinquenal:
                            if i == 1:
                                lista[0].append(valores_1[contador])
                            elif i == 2:
                                lista[1].append(valores_1[contador])
                            elif i == 3:
                                lista[2].append(valores_1[contador])
                            elif i == 4:
                                lista[3].append(valores_1[contador])
                            elif i == 5:
                                lista[4].append(valores_1[contador])
                            elif i == 6:
                                lista[5].append(valores_1[contador])
                            elif i == 7:
                                lista[6].append(valores_1[contador])
                            elif i == 8:
                                lista[7].append(valores_1[contador])
                            elif i == 9:
                                lista[8].append(valores_1[contador])
                            elif i == 10:
                                lista[9].append(valores_1[contador])
                            elif i == 11:
                                lista[10].append(valores_1[contador])
                            elif i == 12:
                                lista[11].append(valores_1[contador])
                            elif i == 13:
                                lista[12].append(valores_1[contador])
                            elif i == 14:
                                lista[13].append(valores_1[contador])
                            elif i == 15:
                                lista[14].append(valores_1[contador])
                            elif i == 16:
                                lista[15].append(valores_1[contador])
                            elif i == 17:
                                lista[16].append(valores_1[contador])
                            contador += 1
                        muertes_grupo = dict(zip(llave, lista))
                        total_defunciones = muertes_grupo
            elif sexo == 0 and (region != 0 or comuna != 0):
                if region != 0:
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['REG_RES'].isin(reg)].copy()
                    a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                                 as_index=False).count()
                    b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                    cod_grupo = list()
                    edad_quinquenal = list()
                    conteo_casos = list()
                    for i in b['tabular']:
                        cod_grupo.append(i)
                    for c in b['EDAD_QUINQ']:
                        edad_quinquenal.append(c)
                    for d in b['DIAG1']:
                        conteo_casos.append(d)
                    valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                    contador = 0
                    lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                    for i in edad_quinquenal:
                        if i == 1:
                            lista[0].append(valores_1[contador])
                        elif i == 2:
                            lista[1].append(valores_1[contador])
                        elif i == 3:
                            lista[2].append(valores_1[contador])
                        elif i == 4:
                            lista[3].append(valores_1[contador])
                        elif i == 5:
                            lista[4].append(valores_1[contador])
                        elif i == 6:
                            lista[5].append(valores_1[contador])
                        elif i == 7:
                            lista[6].append(valores_1[contador])
                        elif i == 8:
                            lista[7].append(valores_1[contador])
                        elif i == 9:
                            lista[8].append(valores_1[contador])
                        elif i == 10:
                            lista[9].append(valores_1[contador])
                        elif i == 11:
                            lista[10].append(valores_1[contador])
                        elif i == 12:
                            lista[11].append(valores_1[contador])
                        elif i == 13:
                            lista[12].append(valores_1[contador])
                        elif i == 14:
                            lista[13].append(valores_1[contador])
                        elif i == 15:
                            lista[14].append(valores_1[contador])
                        elif i == 16:
                            lista[15].append(valores_1[contador])
                        elif i == 17:
                            lista[16].append(valores_1[contador])
                        contador += 1
                    muertes_grupo = dict(zip(llave, lista))
                    total_defunciones = muertes_grupo
                elif comuna != 0:
                    df_agno_tabularx = df_agno_tabularx[df_agno_tabularx['COMUNA'].isin(com)].copy()
                a = df_agno_tabularx.groupby(by=['EDAD_QUINQ', 'tabular', 'tabular_glosa'],
                                             as_index=False).count()
                b = a[['EDAD_QUINQ', 'tabular', 'DIAG1']].copy()
                cod_grupo = list()
                edad_quinquenal = list()
                conteo_casos = list()
                for i in b['tabular']:
                    cod_grupo.append(i)
                for c in b['EDAD_QUINQ']:
                    edad_quinquenal.append(c)
                for d in b['DIAG1']:
                    conteo_casos.append(d)
                valores_1 = [tuple(x) for x in zip(cod_grupo, conteo_casos)]
                contador = 0
                lista = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                for i in edad_quinquenal:
                    if i == 1:
                        lista[0].append(valores_1[contador])
                    elif i == 2:
                        lista[1].append(valores_1[contador])
                    elif i == 3:
                        lista[2].append(valores_1[contador])
                    elif i == 4:
                        lista[3].append(valores_1[contador])
                    elif i == 5:
                        lista[4].append(valores_1[contador])
                    elif i == 6:
                        lista[5].append(valores_1[contador])
                    elif i == 7:
                        lista[6].append(valores_1[contador])
                    elif i == 8:
                        lista[7].append(valores_1[contador])
                    elif i == 9:
                        lista[8].append(valores_1[contador])
                    elif i == 10:
                        lista[9].append(valores_1[contador])
                    elif i == 11:
                        lista[10].append(valores_1[contador])
                    elif i == 12:
                        lista[11].append(valores_1[contador])
                    elif i == 13:
                        lista[12].append(valores_1[contador])
                    elif i == 14:
                        lista[13].append(valores_1[contador])
                    elif i == 15:
                        lista[14].append(valores_1[contador])
                    elif i == 16:
                        lista[15].append(valores_1[contador])
                    elif i == 17:
                        lista[16].append(valores_1[contador])
                    contador += 1
                muertes_grupo = dict(zip(llave, lista))
                total_defunciones = muertes_grupo

    return total_defunciones


#######################################################################################################################
#######################################################################################################################
######### Nota : Si en la base de datos no hay defunciones por edad quinquenal devuelve un diccionario vac??o ##########
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# import pandas as pd
# import os
# print("***************")
# path = os.path.abspath("/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv")
# print("Cargando Dataframe")
# df = pd.read_csv(path, sep=";", encoding='Latin',
#                   dtype={21: str, 36: str, 37: str, 38: str, 39: str,
#                          40: str, 41: str, 42: str, 43: str, 44: str,
#                          45: str, 46: str, 47: str, 48: str, 49: str,
#                          50: str, 58: str, 60: str, 64: str, 67: str,
#                          69: str, 70: str, 71: str, 73: str, 76: str,
#                          82: str, 86: str, 89: str, 90: str, 91: str,
#                          93: str, 96: str, 97: str, 98: str, 99: str,
#                          100: str})
# print("ya se carg?? el dataframe")
# periodo = "2014-2018"
# tabular = 4
# region = 2
# comuna = 0
# sexo = 2
#
# print("la funci??n comenz?? a ejecutarse")
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=False)
# print(f"Valor obtenido: {defunciones}")
#
# periodo = "2014-2018"
# tabular = 2
# region = 2
# comuna = 0
# sexo = 0
#
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=True)
# print(f"Valor obtenido: {defunciones}")
#
# periodo = "2014-2018"
# tabular = 2
# region = 0
# comuna = 2101
# sexo = 0
#
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=True)
# print(f"Valor obtenido: {defunciones}")
#
#
# periodo = "2014-2018"
# tabular = 2
# region = 0
# comuna = 0
# sexo = 1
#
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=True)
# print(f"Valor obtenido: {defunciones}")
#
# periodo = "2014-2018"
# tabular = 2
# region = 0
# comuna = 0
# sexo = 2
#
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=True)
# print(f"Valor obtenido: {defunciones}")
#
#
# periodo = "2014-2018"
# tabular = 2
# region = 2
# comuna = 0
# sexo = 1
#
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=True)
# print(f"Valor obtenido: {defunciones}")
# periodo = "2014-2018"
# tabular = 2
# region = 0
# comuna = 2101
# sexo = 2
#
# defunciones = num_muertes_cancer(df, periodo, tabular, region, comuna, sexo,  edad_quinquenal=True)
# print(f"Valor obtenido: {defunciones}")