from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)  # Cambio a ManyToManyField
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    rating = models.DecimalField(max_digits=1, decimal_places=1)
    read_date = models.DateField()
    opinion = models.TextField()
    recommended = models.BooleanField()