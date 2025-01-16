from django.urls import path
from task5 import views


app_name = 'task5'

urlpatterns = [
    path('django_form/', views.sign_up_by_django),
    path('html_form/', views.sign_up_by_html),
]
