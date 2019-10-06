import os
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,as_completed

# caminho para o binário do geckodriver.exe
bin_path = 'C:\\www\\olx-empregos\\geckodriver.exe'

# função para pegar os dados do emprego
def get_dados_emprego(url):
	try:
		browser = webdriver.Firefox(executable_path=bin_path)
		wait = WebDriverWait(browser, 15)

		browser.get(url)

		titulo = browser.find_element_by_css_selector('h1').text

		contato = []
		for div in browser.find_elements_by_css_selector('div'):
			if 'DescriptionMarginTop' in div.get_attribute('class'):

				# clicar em todos os números da descrição
				for a in div.find_elements_by_css_selector('a'):
					if '9' in a.text:
						a.click()

				for span in div.find_elements_by_css_selector('span'):
					if '9' in span.text:

						# regex de números brasileiros
						regex_result = re.findall(r'((\([0-9]{2}(\) )?|[0-9]{2}( )?|([0-9]{2})?)?[0-9]{5}( |-)?[0-9]{4})',span.text)
						for tel in regex_result:
							if len(tel[0])>4:
								contato.append(tel[0]) 
						break
					break

				mail = re.findall(r'[\w\.-]+@[\w\.-]+', div.text)
				if mail:
					contato.append(mail[0])

				descricao = div.text
				break

		if len(contato)==0:
			browser.quit()

		# esperando os dados serem carregados
		wait.until(ec.presence_of_element_located((by.CSS_SELECTOR, '#miniprofile')))

		anunciante = browser.find_element_by_css_selector('#miniprofile span').text

		return { 'titulo': titulo, 'anunciante': anunciante, 'contato': contato, 'descricao': descricao }

	except Exception as err:
		print(err)
	finally:
		browser.quit()


lista_links = []
for page in range(1,5):
	# sp.olx.com.br Busca em São Paulo
	# o={} Paginação
	result = requests.get('https://sp.olx.com.br/vagas-de-emprego?o={}'.format(page))

	# BeautifulSoup faz o parser no result colocando as tags
	soup = BeautifulSoup(result.text, features='html.parser')

	for li in soup.select('ul.list li.item a.OLXad-list-link-featured'):
		lista_links.append(li['href'])

empregos = []
# max_workers=3 pra não travar seu pc
# threading no python para executar mais rápido (de forma assíncrona)
with ThreadPoolExecutor(max_workers=3) as executor:
	for thread in as_completed({ executor.submit(get_dados_emprego,url): url for url in lista_links }):
		try:
			empregos.append(thread.result())
		except Exception as err:
			print(err)

for emprego in empregos:
	if emprego:
		print(emprego)
