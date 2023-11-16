from django.urls import path
from fasilitas_hotel.views import show_daftar_fasilitas, show_tambah_fasilitas, show_update_fasilitas

app_name = 'fasilitas_hotel'

urlpatterns = [
    path('daftar_fasilitas/', show_daftar_fasilitas, name='show_daftar_fasilitas'),
    path('tambah_fasilitas/', show_tambah_fasilitas, name='show_tambah_fasilitas'),
    path('update_fasilitas/', show_update_fasilitas, name='show_update_fasilitas'),
]