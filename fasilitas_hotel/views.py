from django.shortcuts import render

# Create your views here.
def show_daftar_fasilitas(request):
    return render(request, "daftar_fasilitas.html")

def show_tambah_fasilitas(request):
    return render(request, "tambah_fasilitas.html")

def show_update_fasilitas(request):
    return render(request, "update_fasilitas.html")