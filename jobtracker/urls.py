"""
URL configuration for jobtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from tracker import views
from django.urls import path
# from tracker.views import home, add_application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add/', views.add_application),
    path('update/<int:id>/', views.update_application),
    path('delete/<int:id>/', views.delete_application),
    path('api/applications/', views.get_applications),
    path('api/applications/<int:id>/', views.application_detail),
    
]
