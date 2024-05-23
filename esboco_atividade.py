import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
Elementos do site
cartão - card thumbnail:

    produto - title
    preço - price
    descrição - description
    reviews - review-count
    estrelas - data-rating / ws-icon-star
"""

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page =  requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dados = {
    'Produto': [],
    'Preço': [],
    'Descrição': [],
    'Reviews': [],
    'Estrelas': [],
}

for cada_cartao in soup.find_all('div', {'class': 'card thumbnail'}):
    produto = cada_cartao.find('a', {'class': 'title'}).text
    dados['Produto'].append(produto)

    preco = cada_cartao.find('h4', {'class': 'price'}).text
    dados['Preço'].append(preco)

    descricao = cada_cartao.find('p', {'class': 'description'}).text
    dados['Descrição'].append(descricao)

    reviews = cada_cartao.find('p', {'class': 'review-count'}).text
    dados['Reviews'].append(reviews)

    estrelas = len(cada_cartao.find_all('span', {'class':'ws-icon-star'}))
    dados['Estrelas'].append(estrelas)

df = pd.DataFrame(dados)

print(df)

df.to_csv('./dados.csv', index=False)
