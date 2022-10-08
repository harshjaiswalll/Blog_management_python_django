from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views;
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('blogread/',views.blogread,name="blogread"),
    path('contact/',views.contact,name="contact"),
    path('showdata/',views.showdata,name="showdata"),
    path('delete/', views.delete, name="delete"),
    path('edit/', views.edit, name="edit"),
    path('update/', views.update, name="update"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.login, name="login"),
    path('createblok/',views.createblok, name="createblok"),
    path('blogshow/',views.blogshow,name="blogshow")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)