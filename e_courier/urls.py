"""e_courier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account import views as user_views
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',user_views.profile, name='profile'),
    path('home',views.HomePage.as_view(),name='home'),
    path('account/',include('account.urls',namespace="account")),
    path('account/',include('django.contrib.auth.urls')),
    path('delivery_service/', include('delivery_service.urls')),
    path('notification/', include('notification.urls')),
    # path('', include('driver.urls')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThankstPage.as_view(), name='thanks'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
