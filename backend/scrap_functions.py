"""Funções para scrapping das descrições dos elementos no wiki."""
import aiohttp
import asyncio
import pprint
from bs4 import BeautifulSoup
from typing import List


async def fetch(session, url):
    """Função que faz a requisição no site, dentro de uma sessão já criada."""
    async with session.get(url) as response:
        return await response.text()


async def fetch_elements(list_elements) -> List:
    """Cria a sessão de cliente e requisita dados do wikipedia."""
    base_url = 'https://pt.wikipedia.org/wiki/'
    html_elements = []

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{ base_url }{ list_elements[0] }')
        html_elements.append(html)

    return html_elements
    
async def
loop = asyncio.get_event_loop()
elements_html = (loop.run_until_complete(fetch_elements(elements)))
elements = BeautifulSoup(elements_html[0], 'lxml')
elements = elements.select('#mw-content-text p:nth-child(3)')
# elements = elements.contents

print(elements[0].text)
