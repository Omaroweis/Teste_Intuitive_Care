import pandas as pd
from tabula import read_pdf, convert_into
from zipfile import ZipFile
def makeCsvs():
    pdf = convert_into("arquivo.pdf", "arquivo.tsv", pages=80, output_format="tsv")
    df = pd.read_csv("arquivo.tsv", sep="\t")
    arquivos = []
    for i in df.values:
        for j in i:
            if str(j) == "30" or str(j) == "31" or str(j) == "32":
                aux = "Informacao da linha " + str(j) + ".csv";
                file = open(aux, "w");
                file.write(str(i))
                arquivos.append(aux)

    return arquivos;

def zipping(arquivos):
    for arq in arquivos:
            zip = ZipFile( "Teste_Intuitive_Care_Omar_Lopes.zip", "w")
            zip.write(arq)
