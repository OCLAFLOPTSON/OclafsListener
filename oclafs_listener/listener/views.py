import http.server
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from json import loads, JSONDecodeError
from .models import Log
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from httplib2 import Response

@csrf_exempt
def upland_listener(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            print("Webhook received:", data)
            
            # Process the data here (e.g., save OTP, validate user, etc.)
            if data['type'] == "AuthenticationSuccess":
                Log.objects.create(
                    date=datetime.now(),
                    player_id=data['data']['userId'],
                    code=data['data']['code'],
                    access_token=data['data']['accessToken'],
                    message='None',
                    app_id='None'
                )
            elif data['type'] == "AuthenticationFailure":
                Log.objects.create(
                    date=datetime.now(),
                    player_id='None',
                    code=data['data']['code'],
                    access_token='None',
                    message=data['data']['message'],
                    app_id='None'
                )
            elif data['type'] == "UserDisconnectedApplication":
                Log.objects.create(
                    date=datetime.now(),
                    player_id=data['data']['userId'],
                    app_id=data['data']['appId'],
                    code='None',
                    access_token='None',
                    message='This was generated when a player disconnected their account.'
                )
            Log.save()
            # Send a response to confirm receipt
            print(Response(status=200))
            return Response(status=200)
        except JSONDecodeError:
            return HttpResponse(status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)