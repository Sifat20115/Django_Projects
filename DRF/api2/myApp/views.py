from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt#Function base api er jonno.Function er upore boshe
from django.views import View
from django.utils.decorators import method_decorator#Class base er jonno.Class er upore boshe




@method_decorator(csrf_exempt,name='dispatch')
class studentApi(View):
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
            json_data = request.body #Json format : {"id": 1}
            stream = io.BytesIO(json_data) #Object fetch kore
            pyData = JSONParser().parse(stream) #Python Dict : {'id':1}
            id = pyData.get('id',None)
            if id is not None:
                stu = Student.objects.get(id = id)#Complex data
                serializer = StudentSerializer(stu)#Convert python dict
                json_data = JSONRenderer().render(serializer.data)#Convert Json Format
                return HttpResponse(json_data,content_type = 'application/json')
            
#DeSerialization Proccess....  
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pyData = JSONParser().parse(stream)
            serializer = StudentSerializer(data=pyData)
            if serializer.is_valid():
                serializer.save()
                res = {'msg':'Data Create'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type = 'application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
        
    def put(self,request,*args,**kwargs):
        json_data = request.body #Json format : {'id':1,'name':'Rifu','roll': 3 ,'city':'Dhaka'}
        stream = io.BytesIO(json_data) #Object fetch kore
        pyData = JSONParser().parse(stream) #Python Dict : {'id':1,'name':'Rifu','roll': 3 ,'city':'Dhaka'}
        id = pyData.get('id',None)
        stu = Student.objects.get(id = id)#Complex data
        serializer = StudentSerializer(stu,data=pyData,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Update'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')

    def delete(self,request,*args,**kwargs):
        json_data = request.body #Json format : {"id": 1}
        stream = io.BytesIO(json_data) #Object fetch kore
        pyData = JSONParser().parse(stream) #Python Dict : {'id':1}
        id = pyData.get('id',None)
        stu = Student.objects.get(id = id)#Complex data
        stu.delete()
        res = {'msg':'Data Delete'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')

