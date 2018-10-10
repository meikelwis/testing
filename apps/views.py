from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.models import CubeHeader, CubeDetail
from xml.dom import minidom
from urllib.request import urlopen

import os
import json
# Create your views here.
class GetDownloadData(APIView):
    def post(self, request):
        url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
        dom = minidom.parse(urlopen(url))
        cubelist = dom.getElementsByTagName('Cube')
        for cube in cubelist:
            cube_time_childs = cube.childNodes
            if len(cube_time_childs) > 0:
                for cube_time in cube_time_childs:
                    cube_time_childs = cube_time.childNodes
                    if len(cube_time_childs) > 0:
                        time = cube_time.attributes['time'].value
                        cube_header = CubeHeader(time = time)
                        cube_header.save()
                        for cube in cube_time_childs:
                            cube_detail = CubeDetail(cube_header_id = cube_header.id, currency = cube.attributes['currency'].value, rate = cube.attributes['rate'].value)
                            cube_detail.save()
        return Response("OK")


class GetLatestRate(APIView):
    def get(self, request):
        cube_header = CubeHeader.objects.all().order_by('time').last()
        cube_detail = CubeDetail.objects.filter(cube_header_id = cube_header.id)
        return Response(base)
            