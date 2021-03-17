from django.contrib.auth.models import User
from .models import Profile
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserDetailSerializer


class UserDetailView(RetrieveUpdateAPIView):
	serializer_class = UserDetailSerializer
	queryset = Profile.objects.all()