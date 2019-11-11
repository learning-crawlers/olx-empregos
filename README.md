# OLX Empregos

Extração de dados com Beautiful Soup + Selenium para encontrar empregos no OLX

## Instalação

```
pip install requests beautifulsoup4 selenium futures hashlib
```

## Modo de usar

Procure o path do python instalado no Windows:

```
/mnt/c/Users/alexb/AppData/Local/Programs/Python/Python37-32/python.exe run.py
```

## Resultado

**Header**

Url, Titulo, Anunciante, Contato, Descricao, Local, Data

**Dados**

```json
{
    "fonte": "OLX Empregos",
    "url": "https://sp.olx.com.br/sao-paulo-e-regiao/vagas-de-emprego/operadores-de-telemarketing-682896073",
    "titulo": "Operadores de Telemarketing",
    "anunciante": "CEDASPY",
    "contato": [
        "11 94067-2607",
        "callpinheiros@gmail.com"
    ],
    "descricao": "Empresa Nacional contrata operadora de telemarketing. Ira trabalhar 36 horas semanais. Oferecemos treinamento, VT, fixo + Comiss\u00f5es e plano. Interessados enviar curriculo para callpinheiros@gmail.com ou chamar no whats 11 94067-2607",
    "local": "S\u00e3o Paulo - Pinheiros",
    "data_publish": "2019-11-10T11:07:00"
}
```