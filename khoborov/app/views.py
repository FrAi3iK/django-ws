from django.shortcuts import render
from django.http import HttpResponse

def index(request, name='anon', age=0):

    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'User: {name} <br> Age: {age}<br> host:{host} <br> browser {user_agent} <br> Path: {path}', headers={'SecretCode': '6237yefw'})