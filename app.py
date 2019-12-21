"""
Fontes:
	https://stackoverflow.com/questions/36378441/does-flask-jsonify-support-utf-8?rq=1
"""


import pandas as pd

from flask import Flask, jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

df = pd.read_excel('test.xlsx') # latitude, longitude e data_avist

@app.route('/api/v1', methods=['GET'])
def powerbi():

	columns = ['localidade', 'municipio', 'estado', 'Data_Avist', 'Latitude', 'Longitude']
	xlsx = df[columns]

	data = []

	for x in xlsx.values:
		data.append({
				'localidade': x[0],
				'municipio': x[1],
				'estado': x[2],
				'data_Avist': x[3],
				'latitude': str(x[4]),
				'longitude': x[5]
			})

	return jsonify({'features': data})


if __name__ == '__main__':
	app.run(threaded=True, port=5000)

