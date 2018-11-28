from django.db import models
import requests
import json


if __name__ == '__main__':
	url = 'http://localhost:8000/Mapas/'

	response = requests.get(url)

	if response.status_code == 200:

		objetos = response.json()

		pontoInicialDoCliente = 'a'
		pontoFinalDoCliente ='d'
		valorLitro = 2.50
		autonomia = 10

		menorDistanciaInicial = 10000000
		menorDistanciaFinal = 1000000
		distanciaMesmoPonto = 1000000




		renanVetor = []


		for pontos in objetos:

			if pontos['ponto_inicial'].lower() == pontoInicialDoCliente.lower() and pontos['ponto_final'].lower() == pontoFinalDoCliente.lower():



				if distanciaMesmoPonto > int(pontos['distancia']):
					distanciaMesmoPonto = int(pontos['distancia'])
					pontoInicialMesmoPonto = pontos['ponto_inicial']
					pontoFinalMesmoPonto = pontos['ponto_final']




			if pontos['ponto_inicial'].lower() == pontoInicialDoCliente.lower() and pontos['ponto_final'].lower() != pontoFinalDoCliente.lower():

				if menorDistanciaInicial > int(pontos['distancia']):
					menorDistanciaInicial = int(pontos['distancia'])
					pontoInicialDistintoA = pontos['ponto_inicial']
					pontoFinallDistintoA = pontos['ponto_final']





			if pontos['ponto_final'].lower() == pontoFinalDoCliente.lower() and pontos['ponto_inicial'].lower() != pontoInicialDoCliente.lower():			

				if menorDistanciaFinal > int(pontos['distancia']):
					menorDistanciaFinal = int(pontos['distancia'])
					pontoInicialDistintoB = pontos['ponto_inicial']
					pontoFinallDistintoB = pontos['ponto_final']





		distanciaTotal = menorDistanciaInicial + menorDistanciaFinal

		if distanciaTotal > distanciaMesmoPonto:

			custo = (distanciaMesmoPonto / autonomia) * valorLitro

			print(pontoInicialMesmoPonto, pontoFinalMesmoPonto, distanciaMesmoPonto, custo)


		else:
			
			if pontoFinallDistintoA == pontoInicialDistintoB:

				custo = (distanciaTotal / autonomia) * valorLitro				

				print(pontoInicialDistintoA, pontoFinallDistintoA, pontoFinallDistintoB, distanciaTotal, custo)

			else:

				custo = (distanciaTotal / autonomia) * valorLitro

				print(pontoInicialDistintoA, pontoFinallDistintoA, pontoInicialDistintoB, pontoFinallDistintoB, distanciaTotal, custo)


class Pontos(object):
	def __init__(self, pontoA, pontoB, distanciaX):
		self.pontoA = pontoA
		self.pontoB = pontoB
		self.distanciaX = distanciaX