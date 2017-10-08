from rest_framework import  serializers, viewsets
from django.contrib.auth.models import User
from agenda.models import Agenda,UsuarioAgenda,Compromisso,UsuarioCompromisso,Tipo
#ViewsSets define the view dehavior.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','is_staff')
class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Agenda
        fields=('nome','data','tipo')
class UsuarioAgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UsuarioAgenda
        fields=('usuario','agenda')
class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Compromisso
        fields=('nome','data_inicio','data_Fim','local','agenda')
class UsuarioCompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UsuarioCompromisso
        fields=('proprietario','convidado','compromisso','aceite')
class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tipo
        fields=('nome',)
