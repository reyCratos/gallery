
from django.contrib import admin
from django.urls import path
from . import vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_genero/<str:nombre>', vista.lista_genero, name='lista_genero')
]
