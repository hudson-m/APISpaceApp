class ModeloClassificador:
    def __init__(self, DicionarioDadosTrainAumentado, DadosTest):
        self.DadosTrain = DicionarioDadosTrainAumentado
        self.DadosTest = DadosTest

    def KNN(self):
        import math
        import operator

        # Aplicacao do KNN
        DistanciaClasses = {}
        for Classe in self.DadosTrain:
            DistanciaTotal = 0
            for Feature in self.DadosTrain[Classe]:
                DistanciaTotal += math.sqrt((self.DadosTest[0] - Feature[0])**2 + (self.DadosTest[1]- Feature[1])**2)
            DistanciaClasses[Classe] = DistanciaTotal

        # Normalizacao do resultado ranqueado
        SomatorioDistancias = sum(x for x in list(DistanciaClasses.values()))
        for Classe in DistanciaClasses:
            # 100 para deixar em porcentagem. Lembrar que quanto maior esse valor, menos parecido é o nosso modelo com essa classe
            DistanciaClasses[Classe] = (DistanciaClasses[Classe] / SomatorioDistancias) * 100
        # Ordenacao do resultado ranqueado
        ClassesRanqueadas = sorted(DistanciaClasses.items(), key=operator.itemgetter(1))

        return ClassesRanqueadas
