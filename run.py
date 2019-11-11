# -*- coding: utf-8 -*-
#######################################
##  Empregos OLX SP
##    Busca de empregos no olx com url, titulo, anunciante, contato, descricao, local, data
##
##    Author: Alex Benincasa Santos 
##    Mail: alexbenincasa@ymail.com
##    2019
#######################################

import os
import re
import time
import json
import hashlib
import requests
from datetime import datetime as date
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor,as_completed
from bs4 import BeautifulSoup

# caminho para o binário do geckodriver.exe
bin_path = 'C:\\www\\olx-empregos\\geckodriver.exe'

# função para pegar os dados do emprego
def salvarVaga(url):
	try:
		options = Options()
		#options.headless = True
		
		browser = webdriver.Firefox(executable_path=bin_path, options=options)
		wait = WebDriverWait(browser, 15)
		browser.get(url)

		titulo = browser.find_element_by_css_selector('h1').text.replace('/','')
		# print(f'[{titulo}] titulo')

		contato = []
		# print(f'[{titulo}] contato')
		for div in browser.find_elements_by_css_selector('#content div > div div'):
			if 'ver número' in div.text:

				# clicar em todos os números da descrição
				for a in div.find_elements_by_css_selector('a'):
					if '9' in a.text:
						a.click()

				# print(f'[{titulo}] svg in a.innerHTML')
				
				# print(f'[{titulo}] span in p')
				for span in div.find_elements_by_css_selector('p'):
					if '9' in span.text:

						# regex de números brasileiros
						regex_result = re.findall(r'((\([0-9]{2}(\) )?|[0-9]{2}( )?|([0-9]{2})?)?[0-9]{5}( |-)?[0-9]{4})',span.text.replace('.',''))
						for tel in regex_result:
							if len(tel[0])>4:
								contato.append(tel[0]) 

						break

					break

				for a in browser.find_elements_by_css_selector('#content a'):
					#print(a.get_attribute('innerHTML'))
					if 'svg' in a.get_attribute('innerHTML'):
						a.click()

				mail = re.findall(r'[\w\.-]+@[\w\.-]+', div.text)
				if mail:
					contato.append(mail[0])

				descricao = div.text

		for div in browser.find_elements_by_css_selector('#content div > div > div div'):
			if 'Publicado em' in div.text:
				ano = date.now().year
				data_published = div.text.replace('Publicado em ','').replace(' às ',f'/{ano} ').split('\n')[0]
				data_published = date.strptime(data_published, '%d/%m/%Y %H:%M').strftime('%Y-%m-%dT%H:%M:00')
				break

		# print(f'[{titulo}] descricao = div.text')
		if len(contato)==0:
			browser.quit()
			raise ValueError('Vaga não tem contato')

		anunciante = browser.find_element_by_css_selector('#miniprofile span').text
		# print(f'[{titulo}] anunciante')

		vaga = {}
		vaga['Url'] = url.strip()
		vaga['Titulo'] = titulo.strip()
		vaga['Anunciante'] = anunciante.strip()
		vaga['Contato'] = contato
		vaga['Descricao'] = descricao.strip()
		vaga['Local'] = ''
		vaga['Data'] = data_published

		local = None
		has_municipio = False
		has_bairro = False
		for info in browser.find_elements_by_css_selector('dt,dd'):
			if 'Município' in info.text:
				has_municipio = True
				continue

			if 'Bairro' in info.text:
				has_bairro = True
				continue

			if has_municipio:
				vaga['Local'] = info.text.strip()
				has_municipio = False
				local = vaga['Local']

			if has_bairro:
				bairro = info.text.strip()
				if local:
					vaga['Local'] += ' - '+bairro
				elif bairro:
					vaga['Local'] = bairro

				has_bairro = False

		anuncio = vaga['Titulo']+vaga['Anunciante']+vaga['Local']

		browser.quit()

		# o hash vai identificar a vaga
		hash = 'data/'+hashlib.sha224(anuncio.strip().encode('utf-8')).hexdigest()
		fname = hash+f'-{titulo}.json'.lower()
		if os.path.isfile(fname):
			raise ValueError('Vaga já foi cadastrada')

		# salvar o arquivo com os dados da vaga
		with open(fname, mode="w") as f:
			f.write(json.dumps(vaga, indent=4))

	except Exception as e:
		print(f'[{titulo}] '+str(e))
		browser.quit()

	exit()

links = []
for page in range(1,20):
	# sp.olx.com.br Busca em São Paulo
	# o={} Paginação
	result = requests.get('https://sp.olx.com.br/vagas-de-emprego?o={}'.format(page))

	# BeautifulSoup faz o parser no result colocando as tags
	soup = BeautifulSoup(result.text, features='html.parser')

	for li in soup.select('ul.list li.item a.OLXad-list-link-featured'):
		links.append(li['href'])

# max_workers=3 pra não travar seu pc
# threading no python para executar mais rápido (de forma assíncrona)
with ThreadPoolExecutor(max_workers=3) as executor:
	for thread in as_completed({ executor.submit(salvarVaga,url): url for url in links }):
		try:
			thread.result()
		except Exception as e:
			print(e)