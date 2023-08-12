from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
        return HttpResponse(
        '''
        <h1>Courses...</h1>
        <a href = '/second_app/feedback/'>feedback</a>
        '''
        )
def feedback(request):
        return HttpResponse(
        '''
        <h1>feedback...</h1>
        <a href = '/second_app/courses/'>courses</a>
        '''
        )
