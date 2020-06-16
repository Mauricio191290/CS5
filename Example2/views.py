from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#Modelos importaedos copia del 1
from Example2.models import Example2

#Serializers importados
from Example2.serializer import ExampleSerializers

class Example2List(APIView):
    def get(self, request, format = None):
        print("Entro en get Example2")
        queryset = Example2.objects.all()
        serializer = ExampleSerializers(queryset, many = True)
        return Response(serializer.data)

    def post (self, request, format=None):
        serializer = ExampleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)