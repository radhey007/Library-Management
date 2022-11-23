from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("categories",views.CategoryView.as_view(), name="categoryList"),
    path("gener",views.GenerView.as_view(), name="gener"),
    path("author",views.AuthorView.as_view(), name="author"),
]
