from django.http import HttpResponse
import json

def index(request):
    return HttpResponse(json.dumps(request), content_type="application/json")
