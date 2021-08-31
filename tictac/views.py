from django.http import response
from django.shortcuts import render
from django_ajax.decorators import ajax

# Create your views here.

def home(request):
    return render(request=request, template_name="master_page.htm")

@ajax
def getCellResponse(request):
    print(request.POST)
    return {'result': "test"}