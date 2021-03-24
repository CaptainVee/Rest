from rest_framework.serializers import ModelSerializer, SerializerMethodField

from django.contrib.auth.models import User
from user.models import Profile, Chat
from product.models import Product
from product.serializers import ProductListSerializer

from rest_framework import serializers
from django.contrib.auth import get_user_model


from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


class UserDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	email = SerializerMethodField()
	product = SerializerMethodField()
	# chat = SerializerMethodField()

	class Meta:		
		model = Profile
		fields = ('user', 'picture', 'email', 'product')

	def get_user(self, obj):
		return (obj.user.username)

	def get_email(self, obj):
		return (obj.user.email)

	def get_product(self, obj):
		product_queryset = Product.objects.filter(user=obj.id)
		product = ProductListSerializer(product_queryset, many=True).data
		return product

	# def get_chat(self, obj):
	# 	chat_queryset = Chat.objects.filter(author=obj.id)
	# 	chats = ChatSerializer(chat_queryset, many=True).data
	# 	return chats

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data


    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value



    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



class UserLoginSerializer(ModelSerializer):
    id = SerializerMethodField()
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    # def get_id(self, obj):
    #     user = Profile.objects.get(user=instance)
    #     print(user)
    #     return user

class ChatSerializer(ModelSerializer):
	class Meta:
		model = Chat
		fields = ['author', 'content', 'timestamp',]