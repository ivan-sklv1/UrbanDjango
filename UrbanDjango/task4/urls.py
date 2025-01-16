from django.urls import path
from task4 import views


app_name = 'task4'

urlpatterns = [
    path('', views.main),
    path('games/', views.games_list),
    path('cart/', views.cart_list),
]
