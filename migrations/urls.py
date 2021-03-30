from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products')
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home')
]
