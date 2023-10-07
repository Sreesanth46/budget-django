import datetime
import jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from BudgetApp.apps.core.models.user_model import UserModel

from BudgetApp.settings import base as settings
from BudgetApp.apps.core.serializers.user_serializer import UserSerializer

def generate_token(payload, expiration_delta, secret):
    now = datetime.datetime.utcnow()
    expiration_time = now + expiration_delta
    token_payload = {
        **payload,
        'exp': expiration_time,
        'iat': now,
    }
    return jwt.encode(token_payload, secret, algorithm='HS256')

def generate_access_token(payload):
    return generate_token(
        payload,
        datetime.timedelta(minutes = settings.ACCESS_TOKEN_EXPIRY_MINUTES),
        settings.ACCESS_TOKEN_SECRET
    )


def generate_refresh_token(payload):
    return generate_token(
        payload,
        datetime.timedelta(hours = settings.REFRESH_TOKEN_EXPIRY_HOURS),
        settings.REFRESH_TOKEN_SECRET
    )

def generate_mail_token(payload):
    return generate_token(
        payload,
        datetime.timedelta(minutes = settings.MAIL_TOKEN_EXPIRY_MINUTES),
        settings.MAIL_TOKEN_SECRET
    )

def generate_access_refresh_token(payload):
    access_token = generate_access_token(payload)
    refresh_token = generate_refresh_token(payload)

    return access_token, refresh_token

def decode_token(token, secret):
    try:
        decoded = jwt.decode(token, secret, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
    return decoded

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

    if not token_details:
        return Response("Token expired", status=status.HTTP_400_BAD_REQUEST)
    
    response = {
        "message" : "Email verification successful",
        "email": token_details["email"],
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def sign_up(request):
    user_exists = UserModel.objects.filter(email=request.data.get('email')).exists()
    
    if user_exists:
        return Response("User already exists", status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    response_data = serializer.data
    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    try:
        user = UserModel.objects.get(email = request.data.get('email'))
    except UserModel.DoesNotExist:
        return Response("Invalid username or password", status=status.HTTP_400_BAD_REQUEST)

    password_matches = user.check_password(request.data.get('password'))

    if not password_matches:
        return Response("Invalid username or password", status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(user)

    access_token, refresh_token = generate_access_refresh_token(serializer.data)

    response_data = {
        "accessToken": access_token,
        "refreshToken": refresh_token,
        **serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def verify_access_token(request):
    return Response(request.user, status=status.HTTP_200_OK)
    