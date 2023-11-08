from django.shortcuts import render
from .models import BookStoreModel
from .serializers import BookStoreSerializer
from django.http import Http404
from rest_framework.views import APIView #Rest frame work er
from rest_framework.response import Response #Rest frame work er
from rest_framework import status #Rest frame work er

# Method 1 : concreteapi view

class bookListView(APIView):
    def get(self, request, format=None):
        model = BookStoreModel.objects.all()#Model theke data nilam
        serializer = BookStoreSerializer(model, many=True)#Json format a convert korlam
        return Response(serializer.data)#yes/no

    def post(self, request, format=None):
        serializer = BookStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#etar mane ei request ta accept hoise
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#etar mane ei request ta accept hoynai
    
class BookListUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return BookStoreModel.objects.get(pk=pk)
        except BookStoreModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookStoreSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookStoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Method 2 : concreteapi view

from rest_framework import generics
class BookListCreateAPIView(generics.ListCreateAPIView): # get, post request
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # update, delete, single element access
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer


# Method 3 : Shortcut / Model View Set
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer