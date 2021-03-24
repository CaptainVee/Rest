from django.contrib.auth.models import User
from .models import Profile, Chat
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from .serializers import UserDetailSerializer, UserCreateSerializer, UserLoginSerializer, ChatSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserDetailView(RetrieveUpdateAPIView):
	serializer_class = UserDetailSerializer
	queryset = Profile.objects.all()
	permission_classes = [AllowAny]

class UserLoginAPIView(ObtainAuthToken):
	permission_classes = [AllowAny]
	# serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		response = super(UserLoginAPIView, self).post(request,*args, **kwargs)
		token = Token.objects.get(key=response.data['token'])
		return Response({	'token': token.key,
							'id': token.user_id,
							'email': token.user.email, 
							'username':token.user.username
						})

	# def post(self, request, *args, **kwargs):
	# 	data = request.data

	# 	token =  request.headers['Authorization']
	# 	serializer = UserLoginSerializer(data=data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		context = {
	# 		'data':serializer.data,
	# 		'token':token,
 #                  }
	# 		return Response(context, status=HTTP_200_OK)
	# 		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ChatCreateView(CreateAPIView):
	serializer_class = ChatSerializer
	queryset = Chat.objects.all()
