"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from apps.views import GetDownloadData, GetLatestRate, GetDateRate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdownloaddata', GetDownloadData.as_view(), name='getdownloaddata'),
    path('rates/latest', GetLatestRate.as_view(), name='getratelatest'),
    url(r'^rates/(?P<date>\d{4}-\d{2}-\d{2})/$', GetDateRate.as_view(), name='getdaterate'),
]
