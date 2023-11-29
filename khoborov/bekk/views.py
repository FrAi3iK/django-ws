from django.http import HttpResponse
from django.shortcuts import render

def task(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    IP = request.META['REMOTE_ADDR']
    return HttpResponse(f'HOST: {host} <br> User_agent: {user_agent} <br> IP: {IP}')

def errors_task(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Eror HELP")

def user_task(request, login='none', name_post='noname', id_post=0):
    return HttpResponse(f'Login: {login} <br> Name_post: {name_post} <br> Id_post: {id_post}')