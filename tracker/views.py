from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import(Application)
from .forms import ApplicationForm

# Create your views here.
def home(request):
    # return HttpResponse("Hello, this is home")
    # return render(request, 'home.html')
    apps = Application.objects.all()
    return render(request, 'home.html',{'apps': apps})

def add_application(request):
    form = ApplicationForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'add.html', {'form': form})

