from django.urls import path
from .views import *

urlpatterns = [
    path('releases/', ReleasesView.as_view(), name='releases'),
    path('releases/<int:pk>/', ReleasesDetailView.as_view(), name='releases_detail'),
    path('tickets/', TicketsView.as_view(), name='tickets'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop_detail'),
    path('about_us/', about_us, name='about_us'),
    path('', index, name='index'),
]