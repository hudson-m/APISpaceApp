def NormalizaDados(DicionarioDadosTrainAumentado, DadosTest, ListaTemperaturas, ListaUmidades ):
    TemperaturaMinima = min(ListaTemperaturas)
    TemperaturaMaxima = max(ListaTemperaturas)
    UmidadeMinima = min(ListaUmidades)
    UmidadeMaxima = max(ListaUmidades)

    # Aplica normalizacao min-max
    for Label in DicionarioDadosTrainAumentado:
        for VetorFeature in range(len(DicionarioDadosTrainAumentado[Label])):
            DicionarioDadosTrainAumentado[Label][VetorFeature][0] = (DicionarioDadosTrainAumentado[Label][VetorFeature][0] - TemperaturaMinima) / (TemperaturaMaxima - TemperaturaMinima)
            DicionarioDadosTrainAumentado[Label][VetorFeature][1] = (DicionarioDadosTrainAumentado[Label][VetorFeature][1] - UmidadeMinima) / (UmidadeMaxima - UmidadeMinima)

    DadosTest[0] = (DadosTest[0] - TemperaturaMinima) / (TemperaturaMaxima - TemperaturaMinima)
    DadosTest[1] = (DadosTest[1] - UmidadeMinima) / (UmidadeMaxima - UmidadeMinima)

    return DicionarioDadosTrainAumentado, DadosTest
