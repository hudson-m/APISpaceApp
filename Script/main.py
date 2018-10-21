#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    from AplicaDataAugmentation import AplicaDataAugmentation
    from NormalizaDados import NormalizaDados
    from ModeloClassificador import ModeloClassificador
    from ExportaResultados import ExportaResultados

    NomeArquivoTrain = "RequisitosPlantinhas - Novo compilado.csv"
    NomeArquivoTest = "Test.csv"
    # Leitura dos arquivos de entrada
    # Para o usuario é algum local desejado
    DicionarioDadosTrain, DadosTest, ListaTemperaturas, ListaUmidades = LeituraDados(NomeArquivoTrain, NomeArquivoTest)

    # Filtra base de dados treino com base na violação ou não da temperatura ou humidade
    DicionarioDadosTrain, LabelsRecusadas = FiltraBaseDadosTrain(DicionarioDadosTrain, DadosTest)

    # Aumenta a base de dados de treino artificialmente
    DicionarioDadosTrainAumentado = AplicaDataAugmentation(DicionarioDadosTrain)

    # Normaliza os dados
    DicionarioDadosTrainAumentado, DadosTest = NormalizaDados(DicionarioDadosTrainAumentado, DadosTest, ListaTemperaturas, ListaUmidades)

    # Criacao do modelo de classificacao (knn com um misto de arvore de decisao, considerando o que ja foi visto na etapa de filtragem)
    Classificador = ModeloClassificador(DicionarioDadosTrainAumentado, DadosTest)
    ClassesRanqueadas = Classificador.KNN()

    # Criacao do arquivo de saida do programa  # Para o usuário, uma lista de plantas ranqueadas é a saída
    GeraOutput = ExportaResultados(ClassesRanqueadas, LabelsRecusadas)
    
    print('Término da simulação!')
