import traceback
import json
from passlib.hash import bcrypt

from django.shortcuts import render,redirect
from django.core import serializers
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response

from usermanager.models import UserRegistry

def home(request):
    return render(request, "signin.html")

def make_response(version, response_code, _response_data):
    response_data = {
        'responseCode': response_code,
        'responseFormatVersion': version,
        'responseData': {
            "datatype": "JSON",
            "value": _response_data
        }
    }
    return response_data

def get_uid(uid):
    return int(uid)

def check_user_credentials(password, username=None):
    
    if(username != None):
        data = UserRegistry.objects.filter(username=username)
    
    data = serializers.serialize('json', data)
    data = json.loads(data)

    if data is None or len(data) == 0:
        return False, None
    else:
        # data = data[0]
        db_password = data[0]['fields']['password']
        return bcrypt.verify(password, db_password), data[0]

def app(request):
    userId=request.session.get('userId')
    print("sending user Id",userId)
    return render(request, "application.html",{"UserID":userId})

# user login
def signin(request):
    try:
       
        if(('password' not in list(request.POST.keys())) or
            (not any(item in ['username','email'] for item in list(request.POST.keys()))) or
            (request.POST['password'] == '')):
            messages.error(request, "Username or Password is required")
            return render(request, "signin.html")
        else:
            password = request.POST['password']
           
            if('username' in list(request.POST.keys())):
                username = request.POST['username']
                validation, data = check_user_credentials(password, username=username)
                
            
            if(not validation):
                messages.error(request, "Invalid Credentials!!")
                
                return render(request, "signin.html")
            else:
                
                
                print("successfully logged in")
                return render(request, "application.html")
            
    except :
        traceback.print_exc()
        messages.error(request, "Unable to process request")
        return render(request, "signin.html")

@api_view(['GET'])
def getUserData(request):
    try:
        
        user_data=UserRegistry.objects.all()
        user_data = json.loads(serializers.serialize('json', user_data))
        response_payload = make_response('v1', 0, {'user_data': { 'value': user_data}})
       
        return Response(response_payload, 200)
    except :
        traceback.print_exc()
        response_payload = make_response('v1', -1, {'errorMessage': 'Unable to process request'})
        return Response(response_payload, 500)
