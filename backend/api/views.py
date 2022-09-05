import json

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpResponse -> Django
    # print(dir(request))
    #  request.body
    body = request.body  # byte string of JSON data

    data = {}
    try:
        data = json.loads(body)  # string of JSON data -> Python Dict
    except Exception:
        pass
    print(type(data), data)
    print(request.headers)
    print(request.content_type)

    print(request.GET)  # url query params
    # print(request.POST)

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
