from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), #quando o path esta vazio ele indica a home
    # path('recipes/', include('recipes.urls'))#agora o path indicando um subdominio
    # exemplo: dominio.com/recipes/
]
