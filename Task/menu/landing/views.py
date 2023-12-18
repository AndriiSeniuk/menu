from django.shortcuts import render
from .models import MenuItem
# Create your views here.


def menu_view(request):
    language = request.GET.get('language', 'en')
    menu_items = MenuItem.objects.filter(language=language)
    return render(request, 'menu_template.html', {'menu_items': menu_items})