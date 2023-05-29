from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import csv

def Home(request):

    with open('/home/pi/Desktop/LCD/DHT22-101.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        print('IOT-DATA:',data)

        context = {'data':data}

    return render(request,'iot/home.html',context)
    

# {'device_id':'F1001','type':'temperature','temp':30.1, 'humidity':50}

@api_view(['GET'])
def api_test(request):

    # data = {'device_id':'F1001','temperature':30.5,'humidity':50}

    with open('/home/pi/Desktop/LCD/DHT22-101.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        #print('IOT-DATA:',data)

    if request.method == 'GET':
        #print("DATA", request.data)
        token = request.data.get('token')
        # print([token])
        if token == 'abc1234':
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error':'token is invalid'},status=status.HTTP_401_UNAUTHORIZED)