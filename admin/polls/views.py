from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    redirect("/index.byeongsinscript/", 200)
    return render(request, 'polls/index.html')
