from django.urls import path
from . import views #імпорт вюшки

urlpatterns = [
    path('', views.home), #головний маршрут
    path('history/', views.history, name='info'),
    path('underground/', views.underground, name='underground'),
    path('mision/', views.mision, name='mision'),
    path('planttoom/', views.planttoom, name='planttoom'),
    path('scafandersroom/', views.scafandersroom, name='scafandersroom'),
    path('wateroom/', views.wateroom, name='wateroom'),
    path('storage/', views.storage, name='storage'),
    path('cafeteria/', views.cafeteria, name='cafeteria'),
    path('dormitorium/', views.dormitorium, name='dormitorium'),
    path('infirmary/', views.infirmary, name='infirmary'),
    path('therapy/', views.therapy, name='therapy'),
    path('breakroom/', views.breakroom, name='breakroom'),
    path('soc/', views.soc, name='soc'),
    path('VR/', views.VR, name='VR'),
]