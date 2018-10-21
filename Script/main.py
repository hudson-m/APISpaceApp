'''
Arquivo principal para o programa criado durante o hackathon Nasa SpaceApp
Comentários dos autores
a
b
c
'''

if __name__ == "__main__":
    from LeituraDados import LeituraDados
    from ExportaResultados import ExportaResultados
    from ModeloClassificador import ModeloClassificador

    NomeArquivoTrain = "RequisitosPlantinhas - Novo compilado.csv"
    NomeArquivoTest = "Test.csv"
    # Leitura dos arquivos de entrada  # Para o usuario, o local em que ele está é a entrada
    DadosLidos = LeituraDados(NomeArquivoTrain, NomeArquivoTest)
    # Criacao do arquivo de saida do programa  # Para o usuário, uma lista de plantas ranqueadas é a saída
    PlantinhaEscolhida = ModeloClassificador()
    # Criacao do modelo de classificacao (arvore de decisao)
    GeraOutput = ExportaResultados()

    print('Término da simulação!')

