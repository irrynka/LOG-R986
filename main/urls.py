from django.urls import path
# імпорт path для створення маршрутів

from . import views 
# імпорт views.py


urlpatterns = [

    path('', views.home), 
    # головна сторінка сайту

    path('history/', views.history, name='info'), 
    # маршрут до сторінки історії

    path('underground/', views.underground, name='underground'),
    # маршрут до підземної бази

    path('mision/', views.mision, name='mision'),
    # маршрут до сторінки місії

    path('planttoom/', views.planttoom, name='planttoom'),
    # маршрут до кімнати з рослинами

    path('scafandersroom/', views.scafandersroom, name='scafandersroom'),
    # маршрут до кімнати зі скафандрами

    path('wateroom/', views.wateroom, name='wateroom'),
    # маршрут до кімнати з водою

    path('storage/', views.storage, name='storage'),
    # маршрут до складу

    path('cafeteria/', views.cafeteria, name='cafeteria'),
    # маршрут до їдальні

    path('dormitorium/', views.dormitorium, name='dormitorium'),
    # маршрут до кімнат для сну

    path('infirmary/', views.infirmary, name='infirmary'),
    # маршрут до медичного пункту

    path('therapy/', views.therapy, name='therapy'),
    # маршрут до терапії

    path('breakroom/', views.breakroom, name='breakroom'),
    # маршрут до кімнати відпочинку

    path('soc/', views.soc, name='soc'),
    # маршрут до SOC

    path('VR/', views.VR, name='VR'),
    # маршрут до VR кімнати
]