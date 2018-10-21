def FiltraBaseDadosTrain(DicionarioDadosTrain, DadosTest):
    from copy import deepcopy
    IndicaProblema = ['Temperatura', 'Umidade']
    NovoDicionarioDadosTrain = deepcopy(DicionarioDadosTrain)
    for Label in DicionarioDadosTrain:
        for IndiceTemperaturaOuUmidade, Feature in enumerate(DadosTest):
            RestricaoEscolhida = DicionarioDadosTrain[Label][IndiceTemperaturaOuUmidade]
            RestricaoInferior = RestricaoEscolhida[0]
            RestricaoSuperior = RestricaoEscolhida[1]
            if Feature < RestricaoInferior or Feature > RestricaoSuperior:
                print(Label, 'teve o indicador de', IndicaProblema[IndiceTemperaturaOuUmidade], 'violado.')
                NovoDicionarioDadosTrain.pop(Label)
                break

    return NovoDicionarioDadosTrain
