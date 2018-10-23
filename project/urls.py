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
from apps.views import InputCurrency, InputCurrencyRate, ListExchangeRate, ListExchangeRateTrend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inputcurrency', InputCurrency.as_view(), name='inputcurrency'),
    path('inputcurrencyrate', InputCurrencyRate.as_view(), name='inputcurrencyrate'),
    path('listexchangerate', ListExchangeRate.as_view(), name='listexchangerate'),
    path('listexchangeratetrend', ListExchangeRateTrend.as_view(), name='listexchangeratetrend'),
]
