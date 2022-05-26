from django.shortcuts import render
from rest_framework.views import APIView

from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response

class Albumview(APIView):    
    def get_object(self,pk):
        try:
            print("HH")
            Album.objects.get(id=pk)
        except Exception as e:
            print(e)    
        
    def get(request,self,*args, **kwargs):
        queryset = Album.objects.all()
        serializer_class=AlbumSerializer(queryset,many=True)
        
        return Response(serializer_class.data)
    def post(self, request, format=None):
        
        serializer=AlbumSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request,pk,format=None):
        album=self.get_object(pk)
        serializer = AlbumSerializer(album,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)