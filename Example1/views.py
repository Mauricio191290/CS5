from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#Modelos importaedos
from Example1.models import Example1

#Serializers importados
from Example1.serializer import ExampleSerializers

class ExampleList(APIView):
    def get(self, request, format = None):
        print("Entro en get")
        queryset = Example1.objects.all()
        serializer = ExampleSerializers(queryset, many = True)
        return Response(serializer.data)

    def post (self, request, format=None):
        serializer = ExampleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)