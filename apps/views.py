from django.shortcuts import render
from django.db.models import Avg, Min, Max
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.models import Currency, CurrencyRate
from datetime import datetime, timedelta

import os
import json

# Create your views here.
class InputCurrency(APIView):
    def post(self, request):
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        message = {}
        errors = []

        try:
            exists = Currency.objects.filter(from_currency=from_currency, to_currency=to_currency)
            if exists:
                errors.append(
                    {
                        "status" : status.HTTP_409_CONFLICT,
                        "field" : "name", 
                        "message" : "Currency already exists!" 
                    }
                )
        except Exception as e:
            errors.append(
                {
                    "status" : status.HTTP_400_BAD_REQUEST,
                    "message" : "Oops something when wrong" 
                }
            )
        
        if len(errors) > 0:
            message = {
                "errors" : errors
            }
            return Response(message, status = status.HTTP_400_BAD_REQUEST)

        currency = Currency(from_currency=from_currency, to_currency = to_currency)
        currency.save()
        data = {
            "from_currency" : currency.from_currency,
            "to_currency" : currency.to_currency
        }
        message = {
            "status" : status.HTTP_201_CREATED,
            "data" : data
        }
        return Response(message, status = status.HTTP_201_CREATED)
    def delete(self, request):
        id = int(request.POST.get('id'))
        message = {}
        errors = []
        try:
            exists = Currency.objects.get(id=id)
            if not exists:
                errors.append(
                    {
                        "status" : status.HTTP_409_CONFLICT,
                        "field" : "id", 
                        "message" : "Currency doesn't exists!" 
                    }
                )
        except Exception as e:
            errors.append(
                {
                    "status" : status.HTTP_400_BAD_REQUEST,
                    "message" : "Oops something when wrong" 
                }
            )
        if len(errors) > 0:
            message = {
                "errors" : errors
            }
            return Response(message, status = status.HTTP_400_BAD_REQUEST)

        currency = Currency.objects.get(id=id)
        message = {
            "status" : status.HTTP_204_NO_CONTENT
        }
        return Response(message, status=status.HTTP_204_NO_CONTENT)
        
class InputCurrencyRate(APIView):
    def post(self, request):
        date = request.POST.get('date')
        from_currency_name = request.POST.get('from_currency_name')
        to_currency_name = request.POST.get('to_currency_name')
        rate = request.POST.get('rate')
        message = {}
        errors = []

        try:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                errors.append(
                    {
                        "status" : status.HTTP_422_UNPROCESSABLE_ENTITY,
                        "field" : "date",
                        "message" : "Invalid date format! Date must be YYYY-MM-DD!" 
                    }
                )

            exists = Currency.objects.filter(from_currency=from_currency_name, to_currency=to_currency_name)
            if not exists:
                errors.append(
                    {
                        "status" : status.HTTP_404_NOT_FOUND,
                        "field" : "from_currency_name",
                        "message" : "Currency doesn't exists!" 
                    }
                )
            exists = CurrencyRate.objects.filter(from_currency_name=from_currency_name, to_currency_name=to_currency_name,date=datetime.strptime(date,'%Y-%m-%d'))
            if exists:
                errors.append(
                    {
                        "status" : status.HTTP_404_NOT_FOUND,
                        "field" : "date",
                        "message" : "Currency Rate already exists!" 
                    }
                )
        except Exception as e:
            errors.append(
                {
                    "status" : status.HTTP_400_BAD_REQUEST,
                    "message" : "Oops something when wrong" 
                }
            )
        
        if len(errors) > 0:
            message = {
                "errors" : errors
            }
            return Response(message, status = status.HTTP_400_BAD_REQUEST)

        CurrencyRate(date=date, from_currency_name=from_currency_name, to_currency_name=to_currency_name, rate=rate).save()
        data = {
            "date" : date,
            "from_currency_name" : from_currency_name,
            "to_currency_name" : to_currency_name,
            "rate" : rate
        }
        message = {
            "status" : status.HTTP_201_CREATED,
            "data" : data
        }
        return Response(message, status = status.HTTP_201_CREATED)

class ListExchangeRate(APIView):
    def get(self, request):
        date = request.POST.get('date')
        message = {}
        errors = []
        try:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                errors.append(
                    {
                        "status" : status.HTTP_422_UNPROCESSABLE_ENTITY,
                        "field" : "date",
                        "message" : "Invalid date format! Date must be YYYY-MM-DD!" 
                    }
                )
        except Exception as e:
            errors.append(
                {
                    "status" : status.HTTP_400_BAD_REQUEST,
                    "message" : "Oops something when wrong" 
                }
            )
        
        if len(errors) > 0:
            message = {
                "errors" : errors
            }
            return Response(message, status = status.HTTP_400_BAD_REQUEST)

        currencys = Currency.objects.all()
        datetime_until_obj = datetime.strptime(date,'%Y-%m-%d')
        datetime_from_obj = datetime_until_obj - timedelta(days=7)
        data = {}
        currency = []

        for cur in currencys:
            currency_rates = CurrencyRate.objects.filter(from_currency_name=cur.from_currency, to_currency_name=cur.to_currency, date=date)
            currency_avg = CurrencyRate.objects.filter(from_currency_name=cur.from_currency, to_currency_name=cur.to_currency, date__gte=datetime_from_obj, date__lte=datetime_until_obj).aggregate(Avg('rate'))
            
            if currency_rates:
                for currency_rate in currency_rates:
                    currency.append(
                        {
                            "from" : cur.from_currency,
                            "to" : cur.to_currency,
                            "rate" : currency_rate.rate,
                            "avg": currency_avg.get('rate__avg')
                        }
                    )
            else:
                currency.append(
                    {
                        "from" : cur.from_currency,
                        "to" : cur.to_currency,
                        "rate" : "insufficient data",
                        "avg": "-"
                    }
                )
        data = {
            "currency" : currency
        }
        message = {
            "status" : status.HTTP_200_OK,
            "data" : data
        }
        return Response(message, status = status.HTTP_200_OK)

class ListExchangeRateTrend(APIView):
    def get(self, request):
        message = {}
        currencys = Currency.objects.all()
        data = {}
        currency = []

        for cur in currencys:
            currency_rates = CurrencyRate.objects.filter(from_currency_name=cur.from_currency, to_currency_name=cur.to_currency)
            currency_avg = CurrencyRate.objects.filter(from_currency_name=cur.from_currency, to_currency_name=cur.to_currency).aggregate(Avg('rate'))
            currency_min = CurrencyRate.objects.filter(from_currency_name=cur.from_currency, to_currency_name=cur.to_currency).aggregate(Min('rate'))
            currency_max = CurrencyRate.objects.filter(from_currency_name=cur.from_currency, to_currency_name=cur.to_currency).aggregate(Max('rate'))
            
            if currency_rates:
                currency_rate = []
                for cr in currency_rates:
                    currency_rate.append(
                        {
                            "date" : cr.date,
                            "rate" : cr.rate
                        }
                    )
                currency.append(
                    {
                        "from" : cur.from_currency,
                        "to" : cur.to_currency,
                        "avg" : currency_avg.get('rate__avg'),
                        "varians" : currency_max.get('rate__max') - currency_min.get('rate__min'),
                        "current_rate" : currency_rate
                    }
                )
        data = {
            "currency" : currency
        }
        message = {
            "status" : status.HTTP_200_OK,
            "data" : data
        }
        return Response(message, status = status.HTTP_200_OK)