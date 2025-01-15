from django.urls import path
from task2.views import main_page, MainPage2


app_name = 'task2'

urlpatterns = [
    path('main/', main_page),
    path('main2/', MainPage2.as_view()),
]
