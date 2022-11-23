from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    
    
class Gener(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Books(models.Model):
    name = models.CharField(max_length=150)
    category = models.ManyToManyField(Categories)
    gener = models.ManyToManyField(Gener)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True)
    publisher = models.CharField(max_length=200, blank=True)
    total_copies = models.IntegerField()
    price = models.IntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)