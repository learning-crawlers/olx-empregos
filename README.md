# OLX Empregos

Extração de dados com Beautiful Soup + Selenium para encontrar empregos no OLX

## Instalação

```
pip install requests beautifulsoup4 selenium futures
```

## Modo de usar

Procure o path do python instalado no Windows:

```
/mnt/c/Users/alexb/AppData/Local/Programs/Python/Python37-32/python.exe buscar.py
```

## Resultado

```
{'titulo': 'Vagas para Motoboy - Delivery', 'anunciante': 'Luciano', 'contato': ['11 98536-0032', '11 99131-6719'], 'descricao': 'Vaga disponível para atender entregas via app (Ifood OL)\nTrabalhamos com escala \nAtendemos em 3 turnos diferentes:\n\nAlmoço 11:00 as 15:00 \nTarde 15:00 as 18:00 \nJantar 18:00 as 23:59 \nNecessário ter disponibilidade para rodar principalmente aos finais de semana e feriados.\nPagamento Quinzenal\nGANHOS DE R$1,000,00 A R$2,000,00 POR QUINZENA\n\npara mais informações entrar em contato através do whatsapp 11 98536-0032\n11 99131-6719\nFalar com o Clebison'}
{'titulo': 'Contrata-se Técnico com experiencia em Celulares e Notebooks', 'anunciante': 'Faelmgcorp', 'contato': ['faelgmg@icloud.com'], 'descricao': 'empresa promissora em expansão na cidade de sorocaba\n\ncontrata:\n\ntécnico com experiência em manutenção de celulares e notebooks.\n\npré requisito para a vaga:\n\nter conhecimento para notebooks em formatação, limpeza, troca de conector jac, troca de tela e teclado, reparo em resina. \n\ne para celulares em troca de telas, auto falantes microfones, e conectores de energia.\n\nhorário: de segunda a sexta das 08:00 às 18:00 e aos sábados das 08:00 ás 14:00.\n\nsalário: A COMBINAR\n\nenviar currículum para faelgmg@icloud.com\n\n* não responderemos mensagens via chat - enviar currículo no email acima'}
{'titulo': 'Vendedor Externo', 'anunciante': 'Jocam Distribuidora', 'contato': ['99131-6570', 'contato.jocam@gmaill.com'], 'descricao': 'Jocam Distribuidora necessita de vendedor externo filiado ao \n CORSESP . Com carteira de clientes e
m supermercados,mercearias, lojas de variedades,etc. E também em depósitos de material de construção . Para atuar na zona leste,. Interressados entrarem em contato pelo watsap com Campos pelo 11-99131-6570. Ou enviarem dados para contato.jocam@gmaill.com\nObrigado !'}
{'titulo': 'Vibro Kenko Contrata', 'anunciante': 'Vibrokenko', 'contato': ['1799766-1686'], 'descricao': 'Vendedores externos \nP a P Segunda a Sexta \nótimos Ganhos Mudança De Vida \nPrecisa Ter Disponibilidade de Horário \nPequenas Viagens pra Pousar Fora as Vezes chama no zap 01799766-1686'}
```