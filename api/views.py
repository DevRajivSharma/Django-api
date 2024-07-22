from .models import Name
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import NoteSerializer
# Create your views here.

@api_view(['PUT'])
def add_name(request):
    data = request.data
    f_name = data.get('f_name')
    l_name = data.get('l_name')
    
    if f_name and l_name:
        Name.objects.create(f_name=f_name, l_name=l_name)
        return Response('Done')
    else:
        return Response('Error', status=400)

@api_view(['GET'])    
def getRoutes(request):
    routes = Name.objects.all()
    serializer = NoteSerializer(routes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def check_name(request):
    names = Name.objects.all()
    serializer = NoteSerializer(names, many=True)
    return Response(serializer.data)
