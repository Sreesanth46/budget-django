import datetime
import jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from BudgetApp.settings import base as settings
from BudgetApp.apps.core.serializers.user_serializer import UserSerializer

def generate_token(payload, expiration_minutes, secret):
    now = datetime.datetime.utcnow()
    expiration_time = now + datetime.timedelta(minutes=expiration_minutes)
    token_payload = {
        **payload,
        'exp': expiration_time,
        'iat': now,
    }
    return jwt.encode(token_payload, secret, algorithm='HS256')

def generate_access_token(payload):
    return generate_token(payload, settings.ACCESS_TOKEN_EXPIRY_MINUTES, settings.ACCESS_TOKEN_SECRET)


def generate_refresh_token(payload):
    return generate_token(payload, settings.REFRESH_TOKEN_EXPIRY_HOURS * 24 * 60, settings.REFRESH_TOKEN_SECRET)

def generate_mail_token(payload):
    return generate_token(payload, settings.MAIL_TOKEN_EXPIRY_MINUTES, settings.MAIL_TOKEN_SECRET)

def generate_access_refresh_token(payload):
    access_token = generate_access_token(payload)
    refresh_token = generate_refresh_token(payload)

    return access_token, refresh_token

def decode_token(token, secret):
    try:
        return jwt.decode(token, secret, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return {"token_expired": True}
    except Exception as e:
        return None

@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')
    mail_token = generate_mail_token({'email': email, "message": "Please verify your email address"})

    response = {
        "token": mail_token,
        "status": 200,
        "message": "Please verify your email address"
    }

    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
def verify_email(request):
    token = request.GET.get('token')
    token_details = decode_token(token, settings.MAIL_TOKEN_EXPIRY_MINUTES)

    if "token_expired" in token_details:
        return Response("Token expired", status=status.HTTP_400_BAD_REQUEST)
    
    response = {
        "message" : "Email verification successful",
        "email": token_details["email"],
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response("Sign up successfull", status=status.HTTP_201_CREATED)
    else:
        return Response("Sign up unsuccessfull", status=status.HTTP_400_BAD_REQUEST)

    
    