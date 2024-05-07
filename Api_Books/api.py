from .models import Book, Author
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer

##Se definen quien tiene los permisos para utilizar la API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer
