from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse(
        '''
        <h1>Contact...</h1>
        <a href = '/first_app/about/'>About</a>
        <a href = '/second_app/courses/'>Course</a>
        '''
        )
def about(request):
        return HttpResponse(
        '''
        <h1>About...</h1>
        <a href = '/first_app/contact/'>Contact</a>
        '''
        )
