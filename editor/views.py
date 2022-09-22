from django.shortcuts import render
from .models import info
from .forms import InfoForm
# Create your views here.

def index(request):
    form = InfoForm
    return render(request, 'index.html',{'form':form})