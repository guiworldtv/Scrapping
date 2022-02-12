from asyncio.windows_events import NULL
from http.client import PRECONDITION_FAILED
from urllib import response
from bs4 import BeautifulSoup
import requests
'''
prettify() == vai indentar o código para uma melhor anásile
{nome}={site}.find('div' , attrs={'class' : 'class_completa'})  == vai pegar
os codigos contidos dentro dessa div
print({nome}.prettify()) --> vai mandar o arquivo totalmente identado...


'''

valor = 1;

pesquisa = ''

def scrapping():
    contador =1
    url_base = f'https://lista.mercadolivre.com.br/{pesquisa}#D[A:{pesquisa}]'
    response = requests.get(url_base)
    site =  BeautifulSoup(response.text, 'html.parser') # content!=text
    produtos = site.findAll('div',attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'} )
    for produto in produtos:
        titulo = produto.find('h2', attrs={'class' : 'ui-search-item__title'})
        link_produto = produto.find('a' , attrs={'class': 'ui-search-item__group__element ui-search-link'})
        reais = produto.find('span', attrs={'class':'price-tag-fraction'})
        centavos = produto.find('span', attrs={'class': 'price-tag-cents'})
        #print(produto.prettify())
        #'''
        print(f"PRODUTO {contador}-------------------------------")
        contador = contador +1
        print(f'PRODUTO: {titulo.text}')
        if centavos:
            print(f'PREÇO: R${reais.text},{centavos.text}')
        else:
            print(f'PREÇO: R${reais.text}')
        print('LINK PARA O PRODUTO: ', link_produto['href'])
        print("------------------------------------------\n\n")
        #'''
    
    

pesquisa = str(input("Qual produto deseja pesquisa no Mercado Livre: "))
scrapping()

    



