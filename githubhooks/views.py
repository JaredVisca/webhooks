from django.http import HttpResponse
import json

def index(request):
    if request.method == 'POST':
        return HttpResponse(json.dumps(request), content_type="application/json")
    return HttpResponse("This message is because the request.method is not a POST.")