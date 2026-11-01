from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

CITIES = {"rabat": 577827, "casablanca": 3359818, "fes": 1112072}


def home(request):
    return HttpResponse("<h1>Hello from Django!</h1>")


def city_list_api(request):
    return JsonResponse(CITIES)


def city_detail_api(request, name):
    name = name.lower()
    if name in CITIES:
        return JsonResponse({"name": name, "population": CITIES[name]})
    return JsonResponse({"error": "City not found"}, status=404)


def city_list_page(request):
    context = {"cities": CITIES, "total": sum(CITIES.values())}
    return render(request, "geodata/city_list.html", context)