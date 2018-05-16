from django.shortcuts import render
#grabbing inf from db using idea
from django.shortcuts import get_object_or_404

from .models import blog

# Create your views here.
def allblogs(request):
    blogs = blog.objects
    return render(request,'blogs/allblogs.html',{'blog':blogs})
def detail(request,blog_id):
    detailblog = get_object_or_404(blog,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':detailblog})
