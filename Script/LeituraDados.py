# Funcao 1 #
# Leitura dos arquivos de entrada  # Para o usuario, o local em que ele está é a entrada
# Pre-processamento (tratar dados vazios, por exemplo)
# Separar dados para treino, teste e validacao (70, 15, 15)


def LeituraDados(NomeArquivoTrain, NomeArquivoTest):
    import csv
    import os
    DicionarioDadosTrain = {}
    DadosTest = []
    ListaTemperaturas = []
    ListaUmidades = []

    with open(os.path.join('Input', NomeArquivoTrain), newline='') as ArquivoCSV:
        LeitorCSV = csv.reader(ArquivoCSV, delimiter=',')
        next(LeitorCSV)  # Pula a primeira linha, que eh o header
        for Linha in LeitorCSV:
            NomeLabel = Linha[0]
            TemperaturaMinima = float(Linha[1])
            TemperaturaMaxima = float(Linha[2])
            UmidadeRelativaMinima = float(Linha[3])
            UmidadeRelativaMaxima = float(Linha[4])
            DicionarioDadosTrain[NomeLabel] = [[TemperaturaMinima, TemperaturaMaxima], [UmidadeRelativaMinima, UmidadeRelativaMaxima]]
            # Coleta tambem o maximo e minimo valor de cada feature
            ListaTemperaturas.append(TemperaturaMinima)
            ListaTemperaturas.append(TemperaturaMaxima)
            ListaUmidades.append(UmidadeRelativaMinima)
            ListaUmidades.append(UmidadeRelativaMaxima)

    with open(os.path.join('Input',NomeArquivoTest), newline='') as ArquivoCSV:
        LeitorCSV = csv.reader(ArquivoCSV, delimiter=',')
        next(LeitorCSV)  # Pula a primeira linha, que eh o header
        for Linha in LeitorCSV:
            Temperatura = float(Linha[6])
            UmidadeRelativa = float(Linha[7])
            DadosTest = [Temperatura, UmidadeRelativa]  # Estou criando assim pois é uma premissa que dados test será apenas  uma entrada

    return DicionarioDadosTrain, DadosTest, ListaTemperaturas, ListaUmidades
