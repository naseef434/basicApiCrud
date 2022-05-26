from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response

# class Albumview(APIView):    
#     def get_object(self,pk):
#         try:
#             print("HH")
#             Album.objects.get(id=pk)
#         except Exception as e:
#             print(e)    
        
#     def get(request,self,*args, **kwargs):
#         queryset = Album.objects.all()
#         serializer_class=AlbumSerializer(queryset,many=True)
        
#         return Response(serializer_class.data)
#     def post(self, request, format=None):
        
#         serializer=AlbumSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def put(self,request,pk,format=None):
#         album=self.get_object(pk)
#         serializer = AlbumSerializer(album,data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)

# class Albumview(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
    
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
#     lookup_field = 'pk'
   
    # #List all 
    # def get(self,request,*arg, **kwargs):
    #     return self.list(request,*arg, **kwargs)
   
    # # create
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
   
    # # get single object
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(self, request, *args, **kwargs)
    
    # # update
    # def put(self, request, *args, **kwargs):
    #     return self.update(self, request, *args, **kwargs)
    
    # # delete
    # def delete(self, request, *args, **kwargs):
    #     return self(self, request, *args, **kwargs)
    
#Using generic class-based views 
class Albumview(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer