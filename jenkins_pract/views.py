

from django.http import JsonResponse


def test(request):
    print(request)
    return_object = {
        "text":"hello"
    }
    return JsonResponse(return_object)
