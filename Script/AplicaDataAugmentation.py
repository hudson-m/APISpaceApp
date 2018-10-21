def AplicaDataAugmentation(DicionarioDadosTrain):
    DicionarioAumentadoTrain = {}
    for Label in DicionarioDadosTrain:
        DicionarioAumentadoTrain[Label] = []
        # Aquisita dados do dicionario de ranges
        MinimoTemperatura = DicionarioDadosTrain[Label][0][0]
        MaximoTemperatura = DicionarioDadosTrain[Label][0][1]
        MinimoUmidade = DicionarioDadosTrain[Label][1][0]
        MaximoUmidade = DicionarioDadosTrain[Label][1][1]
        ListaTemperatura = list(range(int(MinimoTemperatura), int(MaximoTemperatura) + 1))
        ListaUmidade = list(range(int(MinimoUmidade), int(MaximoUmidade) + 1))

        # Faz as combinacoes
        for i in ListaTemperatura:
            for j in ListaUmidade:
                DicionarioAumentadoTrain[Label].append([i, j])

    return DicionarioAumentadoTrain

