"""
URL configuration for compass_api project.

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
from django.urls import path, include
from django.http import JsonResponse

def connection(request):
    return JsonResponse({"connected": True})

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/v1/cohorts/', include("cohort_app.urls")),
    # removing for testing reasons, don't save
    #path('admin/', admin.site.urls),
    #path('api/v1/vocab/', include('vocab_app.urls')), 
=======
>>>>>>> 72bce2d9b4c3dcd1c600c9e11e675aa4fcafe918
    path('api/v1/test', connection),
    path('api/v1/auth/', include('auth_app.urls')),
    path('api/v1/users/', include('user_app.urls')),
]
