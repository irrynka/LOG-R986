from django.shortcuts import render
# імпорт функції render


def home(request):
    return render(request, "home.html") 
    # відкриває головну сторінку


def history(request):
    return render(request, "history.html") 
    # сторінка історії колонії


def underground(request):
    return render(request, "underground.html") 
    # сторінка підземної бази


def mision(request):
    return render(request, "mision.html") 
    # сторінка місії


def planttoom(request):
    return render(request, "planttoom.html")
    # кімната з рослинами


def scafandersroom(request):
    return render(request, "scafandersroom.html")
    # кімната зі скафандрами


def wateroom(request):
    return render(request, "wateroom.html")
    # кімната з водою


def storage(request):
    return render(request, "storage.html")
    # склад ресурсів


def cafeteria(request):
    return render(request, "cafeteria.html")
    # їдальня


def dormitorium(request):
    return render(request, "dormitorium.html")
    # кімнати для сну


def infirmary(request):
    return render(request, "infirmary.html")
    # медичний пункт


def therapy(request):
    return render(request, "therapy.html")
    # кімната терапії


def breakroom(request):
    return render(request, "breakroom.html")
    # кімната відпочинку


def soc(request):
    return render(request, "soc.html")
    # сторінка SOC


def VR(request):
    return render(request, "VR.html")
    # кімната VR