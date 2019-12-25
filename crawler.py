"""
Fontes:
	https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
	https://pypi.org/project/requests-html/
	https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
	https://stackoverflow.com/questions/54657006/smtpauthenticationerror-5-7-14-please-log-n5-7-14-in-via-your-web-browser
"""
import os
import requests
import smtplib
import logging

from requests_html import HTMLSession
session = HTMLSession()

from settings import CONFIG


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

base_url = 'http://www.ibama.gov.br'

def crawler(url):
	r = session.get(url + '/manchasdeoleo-localidades-atingidas')

	date = r.html.xpath('.//tr[1]/td[1]/text()')[0]
	item = r.html.xpath('.//tr[2]/td[1]/a/@href')[0]
	item_information = r.html.xpath('.//tr[2]/td/text()')[0]



	data = {'data': date, 'link': item, 'informacoes': item_information}

	return data


def download(url, file_name_extention='files/file.xlsx'):
    # open in binary mode
    with open(file_name_extention, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)

def send_mail(sender, password, recipient, subject_matter, text_email):
    '''
        Informações
        -----------
        subject_matter:
            - assunto do email enviado
            - tipo string
        text_email:
            - texto que será enviado
            - tipo string
    '''

    msg = '\r\n'.join([
            'from: {}'.format(sender),
            'To: {}'.format(recipient),
            'Subject: {}'.format(subject_matter),
            '',
            '{}'.format(text_email)
        ]).encode(encoding='utf-8')

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, msg)
    server.quit()


def main():
	try:
		while True:
			c = crawler(base_url)

			new = c['link']
			former = open('links.txt', 'r').read()

			if new not in former:
				logging.info('Novo link: {}'.format(new))

				file = os.listdir('files')
				if file:
					if os.path.isfile('files/' + file[0]):
						os.remove('files/' + file[0])
						logging.info('Arquivo removido.')
					else:
						logging.info('Erro ao remover arquivo')

				download(url=base_url + c["link"], file_name_extention='files/{}.xlsx'.format(c['data'].replace('/', '_')))

				send_mail(sender=CONFIG['sender'], 
					password=CONFIG['password'], 
					recipient=CONFIG['recipient'], 
					subject_matter='Atualições do IBAMA - http://www.ibama.gov.br/manchasdeoleo-localidades-atingidas', 
					text_email='Novas atualizações: {} - {} - {}'.format(c['data'], base_url + c['link'], c['informacoes']))

				logging.info(f'E-mail enviado para {CONFIG['recipient']}, informando novas atualizações.')

				with open('links.txt', 'a') as f:
					f.write(new + '\n')


	except Exception as e:
		raise e


if __name__ == '__main__':
	main()