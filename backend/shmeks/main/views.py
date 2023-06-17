from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about_us(request):
    return render(request, 'main/about_us.html')

class ReleasesView(ListView):
    template_name = 'main/releases.html'
    model = Releases
    context_object_name = 'releases'

class ReleasesDetailView(DetailView):
    model = Releases
    template_name = 'main/release_page.html'


class ShopView(ListView):
    template_name = 'main/shop.html'
    model = Merch
    context_object_name = 'shop'

class ShopDetailView(DetailView):
    model = Merch
    template_name = 'main/shop_page.html'


class TicketsView(ListView):
    template_name = 'main/tickets.html'
    model = TicketsShop
    context_object_name = 'tickets'
































