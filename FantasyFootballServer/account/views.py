from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from fantasy.models import User_Squad
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from rest_framework import status
from .models import UserData
import jwt, datetime
from django.http import JsonResponse

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserData.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = UserData.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
        return JsonResponse(serializer.data)
    
    def delete(self, request, id=None):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = UserData.objects.filter(id=payload['id']).first()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def getProfile(request, s):
    top = UserData.objects.filter(name=s, is_active = True)
    out = []
    for query in top:
        out.append({'id': query.id, 'name': query.name, 'score': query.score})
    res = {
        'user' : out
    }
    return JsonResponse(res)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
# class based views
class AccountList(APIView):
    def get(self, request):
        users = UserData.objects.all()
        return JsonResponse(UserSerializer(users, many=True).data, safe=False)

class AccountDetail(APIView):
    def get(self, request, id):
        user = UserData.objects.get(id=id)
        if user == None:
            return JsonResponse({"error": "Such user doesn't exist"})
        
        return JsonResponse(UserSerializer(user).data)

    def put(self,request, id):
        user = UserData.objects.get(id=id)
        if user == None:
            return JsonResponse({"error": "Such user doesn't exist"})
        
        serializer = UserSerializer(user, request.body)
        return JsonResponse(serializer.data)