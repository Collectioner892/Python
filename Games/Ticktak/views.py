from django.http import response
from django.shortcuts import render

# Create your views here.

def home(request):

    #return response.HttpResponse( "first page")
    return response.HttpResponse(f"<html><head></head><body><span>request:</span></br>{request}</body></html>")