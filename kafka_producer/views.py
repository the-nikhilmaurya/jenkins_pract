import json
from django.http import JsonResponse
from .kafka_utils import produce_event
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def produce_event_api(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            topic = body.get('topic', 'test-topic')  # Default topic
            key = body.get('key', None)             # Optional key
            message = body.get('message', '')

            if not message:
                return JsonResponse({"status": "error", "message": "Message content is required."}, status=400)

            result = produce_event(topic, key, message)
            return JsonResponse(result)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON payload."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed."}, status=405)
