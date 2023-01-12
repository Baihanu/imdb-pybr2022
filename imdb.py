import requests
from bs4 import BeautifulSoup
from random import randint

class MeuRobo():

	def get_site(self):

		site = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

		content = site.content

		# Parseando o site

		parsed_html = BeautifulSoup(content, 'lxml')
		
		lista_crua = parsed_html.find('tbody', {'class': 'lister-list'})
		filmes_no_site = lista_crua.find_all('tr')

		filmes = []
		for filme in filmes_no_site:
			
			td_nome_ano = filme.find('td', {'class': 'titleColumn'})
			nome = td_nome_ano.find('a').text
			ano = td_nome_ano.find('span').text
			
			dicionario_filme = {
				'Nome do Filme': nome,
				'Ano': ano
			}
			filmes.append(dicionario_filme)

		return filmes




a = MeuRobo()
filmes = a.get_site()
print(filmes[randint(0, len(filmes))])
