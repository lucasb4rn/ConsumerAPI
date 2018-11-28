from django.shortcuts import render
from rotas import models
from rotas.models import Pontos
import requests
import json



# Create your views here.
def index(request):
	return render(request, 'index.html')

def exibir(request):

	url = 'http://localhost:8080/Mapas/'

	response = requests.get(url)

	objetos = response.json()

	pontosList = []

	for obj in objetos:

		inicial = obj['ponto_inicial']
		final = obj['ponto_final']
		distancia = obj['distancia']

		pontos = Pontos(inicial, final, distancia)
		
		pontosList.append(pontos)



	return render(request, 'exibir.html', { "lista" : pontosList})