from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponse(1)
    else:
        return HttpResponse(0)


@csrf_exempt
def login(request):
    # convert request from binary to plain text
    params = request.body.decode('utf-8')

    # covert from WSGI attribute to JSON/dict
    request_data = json.loads(params)
    # print(request_data)

    username = request_data.get('name')
    password = request_data.get('pass')
    print(username)
    print(password)

    response_data = {}
    response_data['username'] = username
    response_data['password'] = password

    return HttpResponse(json.dumps(response_data), content_type="application/json")
