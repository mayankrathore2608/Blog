from django.shortcuts import render
from .models import PostModel
# Create your views here.


def index(request):
    post_object=PostModel.objects.all()
    payload={
        'ob':  post_object
        }
    return render(request,'index.html',payload)


def login(request):
    return render(request,'login.html')
