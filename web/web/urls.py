
from django.contrib import admin
from django.urls import path
from familia.views import bienvenida
from familia.views import create_member

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name = 'bienvenida'),
    path('create_member/', create_member, name = 'create_member'),
]
