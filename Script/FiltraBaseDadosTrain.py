def FiltraBaseDadosTrain(DicionarioDadosTrain, DadosTest):
    IndicaProblema = ['Temperatura', 'Umidade']
    for IndiceTemperaturaOuUmidade, Feature in enumerate(DadosTest):
        for Label in DicionarioDadosTrain:
            RestricaoEscolhida = DicionarioDadosTrain[Label][IndiceTemperaturaOuUmidade]
            RestricaoInferior = RestricaoEscolhida[0]
            RestricaoSuperior = RestricaoEscolhida[1]
            if RestricaoInferior < Feature > RestricaoSuperior:
                print(Label, 'teve o indicador de', IndicaProblema[IndiceTemperaturaOuUmidade], 'violado.')
                DicionarioDadosTrain.pop(Label)
                break

    return DicionarioDadosTrain
