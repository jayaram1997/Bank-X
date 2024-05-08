from aiohttp import request
from django.shortcuts import render
from django.http import HttpResponse
import requests

def index1(request):
    return render(request,'core/index1.html')
