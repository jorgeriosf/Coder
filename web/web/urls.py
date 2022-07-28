
from django.contrib import admin
from django.urls import path
from familia.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name = 'bienvenida'),
]
