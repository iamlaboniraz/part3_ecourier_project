from django.urls import path
from .import views
from .views import(
   delivery_request,
   wait_sms,
   sms_send
)
app_name='delivery_service'
urlpatterns = [
      path('', views.delivery_request, name='delivery_request'),
      path('sms_send/', views.sms_send, name='sms_send'),
      path('wait_sms',views.wait_sms,name='wait_sms')
]
