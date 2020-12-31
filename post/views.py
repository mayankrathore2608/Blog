from django.shortcuts import render
from .models import PostModel
# Create your views here.


def index(request):
    post_object=PostModel.objects.get(post_id=1)
    print("pid : ",post_object.post_id)
    return render(request,'index.html')

