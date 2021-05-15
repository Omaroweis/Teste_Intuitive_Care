import pandas as pd
from tabula import read_pdf, convert_into
from zipfile import ZipFile
def makeCsvs():
    pdf = convert_into("arquivo.pdf", "arquivo.tsv", pages=80, output_format="tsv") #extrai do arquivo.pdf a pagina correspondente às informações e transforma em .csv
    df = pd.read_csv("arquivo.tsv", sep="\t")
    arquivos = []
    for linha in df.values: #extrai as informações das linhas na tabela correspondente e cria um arquivo csv no projeto
        for palavra in linha:
            if str(palavra) == "30" or str(palavra) == "31" or str(palavra) == "32":
                aux = "Informacao da linha " + str(palavra) + ".csv";
                file = open(aux, "w");
                file.write(str(linha))
                arquivos.append(aux)

    return arquivos; #retorna a lista de arquivos criados

def zipping(arquivos):
    for arq in arquivos: #zipa todos os arquivos csv's
            zip = ZipFile( "Teste_Intuitive_Care_Omar_Lopes.zip", "w")
            zip.write(arq)

