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
        else:
            return Response(serializer.errors) #ver el error con datas
            
class Example1Detail(APIView):
    def get_object(self, id):
        try:
            return Example1.objects.get(pk = id)
        except Example1.DoesNotExist:
            return 404

    def get(self, request, id, format = None):
        print("Entro en get")
        example1 = self.get_object(id)
        if example1 == 404:
            return Response ("No hay datos")
        else:
            serializer = ExampleSerializers(example1)
            return Response(serializer.data)

    def put (self,request,id,format=None):
        mtdput = self.get_object(id)
        serializer = ExampleSerializers(mtdput,data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        else:
            return Response(serializer.errors)