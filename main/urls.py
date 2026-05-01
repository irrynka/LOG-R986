from django.urls import path
from . import views #імпорт вюшки

urlpatterns = [
    path('', views.home), #головний маршрут
]