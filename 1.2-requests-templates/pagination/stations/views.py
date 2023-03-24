from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))






def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        CONTENT = list(csv.DictReader(f))
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(CONTENT, 10)
        context = {
            'bus_stations': paginator.get_page(page_number),
            'page': paginator.page(page_number),
        }
    return render(request, 'stations/index.html', context)
