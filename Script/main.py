'''
Arquivo principal para o programa criado durante o hackathon Nasa SpaceApp
Comentários dos autores
a
b
c
'''

if __name__ == "__main__":
    from LeituraDados import LeituraDados
    from FiltraBaseDadosTrain import FiltraBaseDadosTrain
    from ExportaResultados import ExportaResultados
    from ModeloClassificador import ModeloClassificador
    from AplicaDataAugmentation import AplicaDataAugmentation

    NomeArquivoTrain = "RequisitosPlantinhas - Novo compilado.csv"
    NomeArquivoTest = "Test.csv"
    # Leitura dos arquivos de entrada
    # Para o usuario é algum local desejado
    DicionarioDadosTrain, DadosTest = LeituraDados(NomeArquivoTrain, NomeArquivoTest)

    # Filtra base de dados treino com base na violação ou não da temperatura ou humidade
    DicionarioDadosTrain = FiltraBaseDadosTrain(DicionarioDadosTrain, DadosTest)

    # Aumenta a base de dados de treino artificialmente
    DicionarioDadosTrain = AplicaDataAugmentation(DicionarioDadosTrain)

    # Normaliza os dados


    # Criacao do arquivo de saida do programa  # Para o usuário, uma lista de plantas ranqueadas é a saída
    # PlantinhaEscolhida = ModeloClassificador()
    # Criacao do modelo de classificacao (arvore de decisao)
    # GeraOutput = ExportaResultados()

    print('Término da simulação!')
    print(DicionarioDadosTrain)
    print(DadosTest)
