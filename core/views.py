from django.shortcuts import render
import urllib2
from BeautifulSoup import BeautifulSoup


def home(request):
    link = captura()
    return render(request,'home.html', {'link':link})


def captura():
    '''Função que captura e retorna o link '''
    return 'aqui retorne o link'
