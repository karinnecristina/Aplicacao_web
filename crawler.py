"""
Fontes:
	https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
	https://pypi.org/project/requests-html/
"""


import requests

from requests_html import HTMLSession
session = HTMLSession()

base_url = 'http://www.ibama.gov.br'

def crawler(url):
	r = session.get(url + '/manchasdeoleo-localidades-atingidas')

	date = r.html.xpath('.//tr[1]/td[1]/text()')[0]
	item = r.html.xpath('.//tr[2]/td[1]/a/@href')[0]
	item_information = r.html.xpath('.//tr[2]/td/text()')[0]

	data = {'date': date, 'link': item, 'informações do item': item_information}

	return data


def download(url, file_name_extention):
    # open in binary mode
    with open(file_name_extention, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


if __name__ == '__main__':

	c = crawler(base_url)
	download(base_url, 'test.xlsx')