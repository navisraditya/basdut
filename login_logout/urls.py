from django.urls import path
from login_logout.views import *

app_name = 'login_logout'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]