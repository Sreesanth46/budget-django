import jwt
from typing import Any
from decouple import config
from rest_framework import status
from django.http import JsonResponse

from BudgetApp import settings

class Authentication(object):
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        print(request.path)
        if request.path in ["/register", "/verify-email", "/signup", "/login"]:
            return self.get_response(request)
        
        elif not request.headers.get('Authorization'):
            return JsonResponse(
                {"message" : "Unauthorized - Access token is required"},
                status = status.HTTP_401_UNAUTHORIZED,
                safe=False
            )
        

        authorization_header = request.headers.get('Authorization')
        token = authorization_header.split(' ')[1]

        ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET", default="ACCESSS_TOKEN_SECRET-DEFAULT")

        try:
            decoded = jwt.decode(token, ACCESS_TOKEN_SECRET, algorithms='HS256')

        except jwt.ExpiredSignatureError:
            response_data = {
                "message" : "Token expired",
                "errorCode" : "401"
            }
            return JsonResponse(
                response_data,
                status = status.HTTP_401_UNAUTHORIZED
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"message" : "Invalid token"},
                status = status.HTTP_401_UNAUTHORIZED
            )
        
        request.user_details = decoded
        return self.get_response(request)