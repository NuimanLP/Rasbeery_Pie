from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import csv
def Home(request):
    with open("/home/pi/Desktop/LCD/DHT22-101.csv",newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data =list(fr)
        print('IOT-DATA',data)
        data.reverse()
        context = {'data':data}
    return render(request,'iot/home.html',context)

#{'device_id':'F1001','type':'temperature','temp':30.5,'humidity':50}
@api_view(['GET'])
def api_test(request):
    data = {'device_id': 'F1001', 'temperature': 30.5, 'humidity': 50}

    if request.method == 'GET':
        print("Data", request.query_params)
        return Response(data, template_name='rest_framework/api.html')

