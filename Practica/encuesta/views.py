from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola, estás en el índice de encuestas.")

def principal(request):
    return HttpResponse("Hola, estás en la página principal, por el momento puedes ir a  http://127.0.0.1:3000/encuesta/ o a http://127.0.0.1:3000/admin/login/?next=/admin/")