from typing import Any
import jwt
from rest_framework import status
from rest_framework.response import Response

from BudgetApp import settings

class Authentication(object):

    def __init__(self, get_response) -> None:
        self.response = get_response

    def __call__(self, request) -> Any:
        if request.path in ["register", "verify-email", "signup", "login"]:
            return self.get_response(request)
        
        elif not request.headers.get('Authorization'):
            return Response(
                "message: Unauthorized - Access token is required",
                status = status.HTTP_401_UNAUTHORIZED
            )
        

        authorization_header = request.headers.get('Authorization')
        token = authorization_header.split(' ')[1]
        
        try:
            decoded = jwt.decode(token, settings.ACCESS_TOKEN_SECRET, algorithms='HS256')

        except jwt.ExpiredSignatureError:
            response_data = {
                "message" : "Token expired",
                "errorCode" : "401"
            }
            return Response(
                response_data,
                status = status.HTTP_401_UNAUTHORIZED
            )
        except jwt.InvalidTokenError:
            return Response(
                {"message" : "Invalid token"},
                status = status.HTTP_401_UNAUTHORIZED
            )
        
        request.user = decoded
        return self.get_response(request)