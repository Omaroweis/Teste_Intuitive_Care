import requests

from bs4 import BeautifulSoup
def readFile():

    url = "http://www.ans.gov.br/"
    contexto = "prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-marco-2021"
    req = requests.get(url+contexto) #faz uma requisicao ao site
    html = req.text #extrai o html da pagina
    soup = BeautifulSoup(html, 'html.parser')
    # busca = soup.findAll('a')
    urls = []


    for i,busca in enumerate(soup.findAll('a')): #busca pelo arquivo correspondente
        url_completa = url+str(busca.get('href'))

        if url_completa.endswith('.pdf'):
            urls.append(url_completa)
    for url in urls: #salva o arquivo .pdf no projeto
        arquivo = requests.get(url,stream=True)
        with open("arquivo.pdf", "wb") as f:
            for conteudo in arquivo.iter_content():
                f.write(conteudo)



