"""Rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import  UserDetailView
from django.conf import settings
from django.conf.urls.static import static
from rest_auth import views as rest_view




urlpatterns = [
    path('', include('product.urls')),
    path('comment/', include('comments.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),    
    path('password-reset-confirm/<uidb64>/<token>/', rest_view.PasswordResetConfirmView.as_view(),
    	name='password_reset_confirm'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)