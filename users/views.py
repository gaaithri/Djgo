from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        qty = request.GET.get('qty', '1')
        ptype = request.GET.get('prodtype', 'pen')
        message = f" {request.path} request received {request.path_info}"
        return render(request, 'index.html')
        return HttpResponse('Hello, World!'+ qty+ ptype + message)
