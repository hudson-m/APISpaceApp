# Funcao 3 #
# Criacao do arquivo de saida do programa  # Para o usuário, uma lista de plantas ranqueadas é a saída
def ExportaResultados(ClassesRanqueadas, LabelsRecusadas):
    import os
    import shutil

    # Cria a pasta para guardar os resultados de saida
    DiretorioOutput = os.path.join(os.path.dirname(__file__), 'Output')
    if os.path.exists(DiretorioOutput):
        shutil.rmtree(DiretorioOutput)
    os.makedirs(DiretorioOutput)

    # Cria o arquivo txt com resultados de saida
    with open(os.path.join(DiretorioOutput, 'Resultados.txt'), 'w') as Arquivo:
        print('Melhor(es) semente(s) para plantio nessa região:')
        Arquivo.write('-- Melhores a serem plantados --\n')
        for Classe in ClassesRanqueadas:
            print(Classe[0])
            Arquivo.write(Classe[0] + '\n')
        Arquivo.write('\n-- Classes recusadas --\n')
        for Classe in LabelsRecusadas:
            Arquivo.write(Classe + '\n')
