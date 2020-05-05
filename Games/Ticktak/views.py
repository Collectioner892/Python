from django.http import response


# Create your views here.

def home(request):
    return response.HttpResponse(f"<html><head></head><body><span>request:</span></br>{request}</body></html>")
