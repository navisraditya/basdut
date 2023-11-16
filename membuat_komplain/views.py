from django.shortcuts import render

# Create your views here.
def show_komplain(request):
    return render(request, "komplain.html")