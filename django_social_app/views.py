from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'django_social_app/home.html')
