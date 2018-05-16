from django.shortcuts import render
from .models import blog

# Create your views here.
def allblogs(request):
    blogs = blog.objects
    return render(request,'blogs/allblogs.html',{'blog':blogs})
