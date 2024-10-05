from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import guestBook
from .serializers import guestBookSeri
from rest_framework import status


@api_view(['GET', 'POST'])
def guestbook_entries(request):
    if request.method == 'GET':
        entries = guestBook.objects.all()
        serializer = guestBookSeri(entries, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = guestBookSeri(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_guestbook_entry(request, entry_id):
    try:
        entry = guestBook.objects.get(id=entry_id)
    except guestBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    entry.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# Create your views here.
