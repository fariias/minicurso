# -*- coding: utf-8 -*-
from django.shortcuts import render
import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime


def home(request):
    link = captura()
    return render(request,'home.html', {'link':link})


def captura():
    return 'retorne o link aqui'
