from csvs import makeCsvs, zipping
from scraping import readFile


def main():
    readFile() #acessa ao site, le e cria um arquivo.pdf no projeto
    arquivos = makeCsvs() #extrai as informações do arquivo.pdf e cria arquivos .csv's no projeto retorna o nome dos arquivos criados
    zipping(arquivos) # zipa os arquivos csvs criados

main();
