from django.shortcuts import render

# Create your views here.
from .models import Agenda,Compromisso,UsuarioAgenda,UsuarioCompromisso,Tipo
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from agenda.serializers import UserSerializer,AgendaSerializer,UsuarioAgendaSerializer,CompromissoSerializer,UsuarioCompromissoSerializer,TipoSerializer

'''def listaAgenda(request):
    retorno='<h1>Agendas</h1>'
    lista=Agenda.objects.all()
    for a in lista:
        retorno+='</br>Nome das Agendas:{}</br>'.format(a.nome)
    return HttpResponse(retorno)

def get_agenda_ID(request,id):
    retorno='<h1>Agenda</h1>'
    agenda=Agenda.objects.filter(tipo__nome='Publico',usuario__id=id)
    for a in agenda:
        retorno +='</br>Nome da Agenda:{}</br>'.format(a.nome)  
    return HttpResponse(retorno)

def agendaInstitucional(request):
    retorno = "<h1> TODOS OS COMPROMISSOS INSTITUCIONAIS </h1>"
    institucionais = Compromisso.objects.filter(agenda__tipo__nome='Institucional')
    for i in institucionais:
        retorno += '<br> Nome Compromisso: {} <br> <br> '.format(i.nome)
    return HttpResponse(retorno)'''

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset=Agenda.objects.all()
    serializer_class=AgendaSerializer

class UsuarioAgendaViewSet(viewsets.ModelViewSet):
    queryset=UsuarioAgenda.objects.all()
    serializer_class=UsuarioAgendaSerializer

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset=Compromisso.objects.all()
    serializer_class=CompromissoSerializer

class UsuarioCompromissoViewSet(viewsets.ModelViewSet):
    queryset=UsuarioCompromisso.objects.all()
    serializer_class=UsuarioCompromissoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset=Tipo.objects.all()
    serializer_class=TipoSerializer
