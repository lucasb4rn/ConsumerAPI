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

	

	for obj in objetos:

		inicial = objetos[0]['ponto_inicial']
		final = objetos[0]['ponto_final']
		distancia = objetos[0]['distancia']

		ponto = Pontos(inicial, final, distancia)


	return render(request, 'exibir.html', { "pontos" : ponto })