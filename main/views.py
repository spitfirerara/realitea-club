from django.shortcuts import render
from .models import Item

def show_main(request):
    context = {
    'app_name': 'Realitea Club',
    'npm': '2406433112',
    'name': 'Naira Ammara Putri',
    'class': 'PBP B',
    }

    return render(request, "main.html", context)
