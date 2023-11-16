from django.urls import path
from membuat_komplain.views import show_komplain

app_name = 'membuat_komplain'

urlpatterns = [
    path('komplain/', show_komplain, name='show_komplain'),
]