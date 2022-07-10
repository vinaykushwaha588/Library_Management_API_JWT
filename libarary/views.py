from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BookModelSerializer
from django.http import Http404
# Create your views here.

@api_view(['GET','POST'])
def library_view(request):
    # permission_classs = ['Isauthenticated']
    if request.method=="GET":
        data = Book.objects.all()
        serializer = BookModelSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = BookModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def library_update_delete(request,bid):
    try:
        books = Book.objects.get(id = bid)
        print(books,"<-----------")
    except:
        # return Response({'status': status.HTTP_404_NOT_FOUND, 'data': 'Record not found!!'})
        raise Http404
    if request.method =="GET":
        serializer = BookModelSerializer(books)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookModelSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)    

    elif request.method =='DELETE':
        books.delete()
        return Response('Library Record Hass beed Deleted')