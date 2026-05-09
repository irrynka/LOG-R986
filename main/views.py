from django.shortcuts import render


def home(request):
    return render(request, "home.html") #Показ користовачу сторінку

def history(request):
    return render(request, "history.html") 

def underground(request):
    return render(request, "underground.html") 

def mision(request):
    return render(request, "mision.html") 

def planttoom(request):
    return render(request, "planttoom.html")

def scafandersroom(request):
    return render(request, "scafandersroom.html")

def wateroom(request):
    return render(request, "wateroom.html")

def storage(request):
    return render(request, "storage.html")

def cafeteria(request):
    return render(request, "cafeteria.html")

def dormitorium(request):
    return render(request, "dormitorium.html")

def infirmary(request):
    return render(request, "infirmary.html")

def therapy(request):
    return render(request, "therapy.html")

def breakroom(request):
    return render(request, "breakroom.html")

def soc(request):
    return render(request, "soc.html")

def VR(request):
    return render(request, "VR.html")