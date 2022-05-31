"""testmyux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from client.views import *
from pages.views import *
from Tester.views import *
urlpatterns = [
    #  path('admin', auth_views.LoginView.as_view(template_name='adminpage/adminlogin.html'), name='admin'),
    path('admin/', admin.site.urls),
    path('client/register', client_reg_view, name="client-reg" ),
    path('', homepage, name="homepage" ),
    path('',include('Tester.urls')),
    path('client/login', client_login_view, name="client-login"),
    path('client/dashboard', client_dashoard, name='client-dash')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
