from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import City


def home(request):
    return HttpResponse("<h1>Hello from Django!</h1>")


def city_list_page(request):
    cities = City.objects.select_related("region")
    total = cities.aggregate(total=Sum("population"))["total"]
    return render(request, "geodata/city_list.html", {"cities": cities, "total": total})


def city_detail(request, slug):
    city = get_object_or_404(City.objects.select_related("region"), slug=slug)
    return render(request, "geodata/city_details.html", {"city": city})


def city_list_api(request):
    data = list(City.objects.values("name", "slug", "region__name", "population"))
    return JsonResponse(data, safe=False)


def city_detail_api(request, slug):
    city = City.objects.filter(slug=slug).select_related("region").first()
    if city is None:
        return JsonResponse({"error": "City not found"}, status=404)
    return JsonResponse({
        "name": city.name,
        "region": city.region.name,
        "population": city.population,
        "area_km2": city.area_km2,
        "density": city.density,
    })