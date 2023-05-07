from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def calc(request, n1, n2):
    return HttpResponse(f'<h1>Calculadora<h1><h2>Soma<h2><p>{n1} + {n2} = {n1+n2}<p><br><h2>Subtração<h2><p>{n1} - {n2} = {n1-n2}<p><br><h2>Multiplicação<h2><p>{n1} * {n2} = {n1*n2}<p><br><h2>Divisão<h2><p>{n1} / {n2} = {n1/n2}<p><br>')
