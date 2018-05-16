from django.shortcuts import render
#access items from the database,first we import the modal
from .models import Jobs

# Create your views here.
def home(request):
    jobs = Jobs.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
