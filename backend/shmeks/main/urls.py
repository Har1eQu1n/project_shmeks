from django.urls import path
from .views import *

urlpatterns = [
    path('cart_add/<int:merch_id>/', cart_add, name='cart_add'),
    path('card_remove/<int:merch_id>/', cart_remove, name='cart_remove'),
    path('cart/', cart_detail, name='cart_detail'),
    path('releases/', ReleasesView.as_view(), name='releases'),
    path('releases/<int:pk>/', ReleasesDetailView.as_view(), name='releases_detail'),
    path('tickets/', TicketsView.as_view(), name='tickets'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop_detail'),
    path('about_us/', about_us, name='about_us'),
    path('login/', SiteLoginView.as_view(), name='login'),
    path('logout/', SiteLogoutView.as_view(), name='logout'),
    path('entry/', RegistrationFormView.as_view(), name='entry'),
    path('', index, name='index'),
]