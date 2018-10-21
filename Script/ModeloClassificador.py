class ModeloClassificador:
    def __init__(self, DicionarioDadosTrainAumentado, DadosTest):
        self.DadosTrain = DicionarioDadosTrainAumentado
        self.DadosTest = DadosTest

    def KNN(self):
        import math
        import operator

        DistanciaClasses = {}
        for Classe in self.DadosTrain:
            DistanciaTotal = 0
            for Feature in self.DadosTrain[Classe]:
                DistanciaTotal += math.sqrt((self.DadosTest[0] - Feature[0])**2 + (self.DadosTest[1]- Feature[1])**2)
            DistanciaClasses[Classe] = DistanciaTotal
        ClassesRanqueadas = sorted(DistanciaClasses.items(), key=operator.itemgetter(1))
        return ClassesRanqueadas
