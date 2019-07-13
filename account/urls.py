from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name='accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),#customer
    path('driver_login/', auth_views.LoginView.as_view(template_name='accounts/driver_login.html'), name='driver_login'),#driver
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp, name='signup'),#customer
    path('driver_signup/', views.DriverSignUp, name='DriverSignUp'),#driver
    path('profile/', views.profile, name='profile'),#customer
    path('driver_profile/', views.driver_profile, name='driver_profile'),#driver
    path('help/', views.help.as_view(), name='help'),
    path('customer_service/', views.customer_service.as_view(), name='customer_service'),

    path('driver_list/', views.driver_list, name='driver_list'),
    path('edit/<id>/', views.edit,name='edit'),
    path('DeliveryDetail/<int:id>/',views.DeliveryDetail.as_view(),name="DeliveryDetail" ),
    path('update/<id>/', views.update,name='update'),
    path('all_request_data/', views.all_request_data, name='all_request_data'),
]
