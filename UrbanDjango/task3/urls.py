from django.urls import path
from task3 import views


app_name = 'task3'

urlpatterns = [
    path('', views.main),
    path('games/', views.games_list),
    path('cart/', views.cart_list),
]
