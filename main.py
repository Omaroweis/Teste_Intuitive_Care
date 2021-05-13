from csvs import makeCsvs, zipping
from scraping import readFile


def main():
    readFile()
    arquivos = makeCsvs()
    zipping(arquivos)

main();
