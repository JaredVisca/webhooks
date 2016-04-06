from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

#comment cause jenkins sucks ass
@csrf_exempt
def index(request):
    if request.method == 'POST':
        request_body = request.body.decode('utf-8')
        body = json.loads(request_body)
        print body
        return HttpResponse(json.dumps(body), content_type="application/json")
    return HttpResponse("This message is because the request.method is not a POST.")