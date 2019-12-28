## Análise dos locais que foram afetado por manchas de óleo, de acordo com dados do [IBAMA](http://www.ibama.gov.br/manchasdeoleo-localidades-atingidas)


### Como rodar o projeto
```
$ git clone https://github.com/karinnecristina/Aplicacao_web.git
$ cd Aplicacao_web
$ python3 -m venv .venv
$ pip install -r requirements.txt
```

### Configuração do projeto
Na raiz do projeto altere o arquivo ```settings.py``` com as credenciais do seu email que deseja usar.
```
CONFIG = {
	'sender': 'naruto@gmail.com',
	'password': 'YOUR_PASSWORD',
	'recipient': 'naruto@gmail.com'
}
```
Depois de realizado as configurações iniciais execute os arquivos ```crawler.py``` e ```app.py```
```
$ python3 crawler.py
$ python3 app.py
```
Acesse [http://localhost:5000/api/v1](http://localhost:5000/api/v1)

### Subindo o projeto no heroku
Acesso o [heroku](https://www.heroku.com/) e faça uma conta, caso não tenha.
Na raiz do projeto crie dois arquivos:
* Procfile
	```
	web: gunicorn app:app
	worker: python crawler.py
	```
* runtime.txt
	```
	python-3.7.3
	```
	ou a versão do python da sua escolha.

Após os arquivos criado e editados, na página inicial do heroku crie um app, e rode os comandos:
```
$ heroku login
$ git init
$ heroku git:remote -a nome-do-seu-app
$ git add .
$ git commit -am "first commit"
$ git push heroku master
```
No site do heroku na aba ```Resource``` edite e ative o segundo serviço. Agora acesse o endereço [https://test-neww.herokuapp.com/api/v1](https://nome-do-seu-app.herokuapp.com/api/v1).