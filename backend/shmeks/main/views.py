from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from .forms import *
from .cart import Cart
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

class RegistrationFormView(FormView):
    template_name = 'main/entry.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Create a new user object but avoid saving it yet
        new_user = form.save(commit=False)
        # Set the chosen password
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return super().form_valid(form)

class SiteLoginView(LoginView):
    template_name = 'main/login.html'
    next_page = reverse_lazy('index')

class SiteLogoutView(LogoutView):
    next_page = reverse_lazy('index')



#@require_POST
def cart_add(request, merch_id):
    cart = Cart(request)
    merch = get_object_or_404(Merch, id=merch_id)
    cart.add(merch=merch)
    return redirect('cart_detail')

def cart_remove(request, merch_id):
    cart = Cart(request)
    merch = get_object_or_404(Merch, id=merch_id)
    cart.remove(merch)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/cart_detail.html', {'cart': cart})































