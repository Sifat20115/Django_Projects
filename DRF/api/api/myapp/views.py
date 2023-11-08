from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
def api(request):
    context = {'name': 'Sifat'}
    return render(request,'index.html',{'s':context})

from django.views import View
class apiclass(View):
    def get(self,request):
        context = {'name': 'Sifat'}
        return render(request,'index.html',{'s':context})
        

from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view (['GET','POST'])
def api2(request):
    if request.method == "POST":
        name = request.data["name"]
        return Response({"name":name})
    
    context = {'name': 'Sifat'}
    return Response(context)


from rest_framework.views import APIView
class apiclass2(APIView):
    def get(self,request):
        context = {'name': 'Sifat'}
        return Response(context)
    def post(self,request):
        name = request.data["name"]
        return Response({"name":name})
    
    
    
    
    
#Serialization Proccess....
def student_detail(request,num):
    OneStu = Student.objects.get(id = num)
    serializer = StudentSerializer(OneStu)
    #jsonData = JSONRenderer().render(serializer.data)
    #return HttpResponse(jsonData,content_type = 'application/json')
    return JsonResponse(serializer.data,safe=True)#Eta likhle uporer Dui line likha lagbe na

def student_list(request):
    OneStu = Student.objects.all()#Complex object
    serializer = StudentSerializer(OneStu, many=True)#python dict convert
    jsonData = JSONRenderer().render(serializer.data)#Json Data convert
    return HttpResponse(jsonData,content_type = 'application/json')