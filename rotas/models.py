from django.db import models
import requests


if __name__ == '__main__':
	url = 'http://localhost:8000/logistica/'

	response = requests.get(url)
	if response.status_code == 200:
		payload = response.json()


		pontoInicialDoCliente = 'a'
		pontoFinalDoCliente ='b'


		distanciaInicial = []
		distanciaFinal = []
		mapaDistanciaMesmoPonto = []



		for mapas in payload:

			if mapas['ponto_inicial'].lower() == pontoInicialDoCliente  and mapas['ponto_final'].lower() == pontoFinalDoCliente:
				
				mapaDistanciaMesmoPonto.append(mapas['distancia'])

			elif mapas['ponto_inicial'].lower() == pontoInicialDoCliente:

				distanciaInicial.append(mapas['distancia'])


			elif mapas['ponto_final'].lower() == pontoFinalDoCliente:

				distanciaFinal.append(mapas['distancia'])


		i = 0;
		j = 0;

		print(mapaDistanciaMesmoPonto)

		for distancia in distanciaFinal:

				distanciaInicial[i + 1]

			for distanciaI in distanciaInicial:
				
				distanciaComInicial = distanciaInicial[i] + distanciaFinal[j]

			j = j + 1

			

