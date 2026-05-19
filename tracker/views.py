from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import(Application)
from .forms import ApplicationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ApplicationSerializer

# Normal Django CRUD (HTML Based).⬇️⬇️
def home(request):
    # return HttpResponse("Hello, this is home")
    # return render(request, 'home.html')
    apps = Application.objects.all()
    return render(request, 'home.html',{'apps': apps})


def add_application(request):
    form = ApplicationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'add.html', {'form': form})
    

def update_application(request, id):

    app = Application.objects.get(id=id)
    form = ApplicationForm(request.POST or None, instance=app)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'add.html', {'form': form})


def delete_application(request, id):
    app = Application.objects.get(id=id)
    app.delete()
    return redirect('/')

# DRF API CRUD (JSON Based).⬇️⬇️
@api_view(['GET', 'POST'])
def get_applications(request):

    if request.method == 'GET':
        apps = Application.objects.all()
        serializer = ApplicationSerializer(apps, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ApplicationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def application_detail(request, id):
    app = Application.objects.get(id=id)

    # Get single application
    if request.method == 'GET':
        serializer = ApplicationSerializer(app)
        return Response(serializer.data)
    
    # Update application
    elif request.method == 'PUT':
        serializer = ApplicationSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Delete application
    elif request.method == 'DELETE':
        app.delete()
        return Response("Application deleted")