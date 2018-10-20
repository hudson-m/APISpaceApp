# Funcao 1 #
# Leitura dos arquivos de entrada  # Para o usuario, o local em que ele está é a entrada
# Pre-processamento (tratar dados vazios, por exemplo)
# Separar dados para treino, teste e validacao (70, 15, 15)


class LeituraDados:
    def __init__(self):
        import pandas as pd
        NomeArquivoCSV = "RequisitosPlantinhas - Theo Bruno e Alan.csv"
        Dados = pd.read_csv(NomeArquivoCSV)
        pass

    def LeituraDadosDeEntrada(self):
        return
