from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request_body = request.body.decode('utf-8');
        print request_body
        body = json.loads(request_body)
        print body
        content = body['content']
        return HttpResponse(json.dumps(content), content_type="application/json")
    return HttpResponse("This message is because the request.method is not a POST.")