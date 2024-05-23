import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page =  requests.get(url)

# with open('./imdb.html', "r", encoding='utf-8') as file:
#     page = file.read()


soup = BeautifulSoup(page, 'lxml')

"""
Titulo - h3 class="ipc-title__text"
ano, duracao, faixa-etaria - span class="sc-b189961a-8 kLaxqf cli-title-metadata-item"
estrelas, avaliacao - span class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"
"""


header = ['Título', 'Ano', 'Duração', 'Faixa Etária', 'Avaliação']
df = pd.DataFrame(columns=header)

for filme in soup.find_all('li', {"class": "ipc-metadata-list-summary-item"}):

    titulo = filme.find("h3", {"class": "ipc-title__text"}).text

    dados_variados = filme.find_all('span', {"class": "sc-b189961a-8 kLaxqf cli-title-metadata-item"})
    
    ano = dados_variados[0].text
    duracao = dados_variados[1].text

    if len(dados_variados) > 2:
        faixa = dados_variados[2].text
    else:
        faixa = 'Not Rated'

    estrelas = filme.find("span", {"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text

    row = [titulo, ano, duracao, faixa, estrelas]
    df.loc[len(df)] = row

print(df)
