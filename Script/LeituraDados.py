# Funcao 1 #
# Leitura dos arquivos de entrada  # Para o usuario, o local em que ele está é a entrada
# Pre-processamento (tratar dados vazios, por exemplo)
# Separar dados para treino, teste e validacao (70, 15, 15)


class LeituraDados:
    def __init__(self):
        import pandas as pd
        from sklearn.model_selection import train_test_split

        # Leitura do arquivo csvv
        NomeArquivoCSV = "RequisitosPlantinhas - Theo Bruno e Alan.csv"
        Dados = pd.read_csv(NomeArquivoCSV)

        # Leitura de labels e features
        ColunaLabel = ["Nome"]
        ColunasFeatures = ["Temp Min", "Temp Max", "Exposicao a luz solar", "Umidade relativa do ar (%)"]
        DadosLabel = Dados.loc[:, ColunaLabel]
        DadosFeatures = Dados.loc[:, ColunasFeatures]

        # Separa entre treino e teste
        XTrain, XTest, YTrain, YTest = train_test_split(DadosLabel, DadosFeatures, test_size=0.2, random_state=0)

        # Aplica pre-processamento das features
        oi = YTest.values.ravel()
        print(oi)
        pass
