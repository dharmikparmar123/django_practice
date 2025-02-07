from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:slug>', views.blog_detailView, name = 'blog_detail'),
    path('about/',views.about,name = 'about'),
    path('addwish/',views.addwish,name='addwish'),
    path('contact/',views.contact,name = 'contact'),
]


