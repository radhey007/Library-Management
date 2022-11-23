from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from forms.books import CategoryForm
from django.contrib import messages
from books.models import Categories
from django.http import HttpResponse
# Create your views here.
class CategoryView(View):
    def get(self,request):
        greeting={}
        greeting['title'] = "Categories"
        greeting['pageview'] = "Books"
        return render(request,'books/category.html',greeting)
        
class GenerView(View):
    def get(self,request):
        greeting={}
        greeting['title'] = "Gener"
        greeting['pageview'] = "Books"
        return render(request,'books/gener.html',greeting)
    
class AuthorView(View):
    def get(self,request):
        greeting={}
        greeting['title'] = "Author"
        greeting['pageview'] = "Books"
        return render(request,'books/author.html',greeting)
        
    
    
            