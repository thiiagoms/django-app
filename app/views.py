from django.shortcuts import render, HttpResponse
from .models import MyUser 
# Create your views here.
def read_all_users(request):
    users = MyUser.objects.all()
    return render(request, "index.html", {'users': users})