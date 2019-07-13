from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .import models
from .models import Profile,driver_Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
# Create your views here.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import DriverRegisterForm, DriverUpdateForm, DriverProfileUpdateForm
from delivery_service.models import delivery_product
from django.db.models import Count
################### customer login, signup views ######################################
def login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not create")
        else:
            print("Someone tried to login and falied!")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'login.html',{})

def SignUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)

################### Driver login, signup views ######################################
def driver_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account not create")
        else:
            print("Someone tried to login and falied!")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'accounts/driver_login.html',{})

def DriverSignUp(request):
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! You are now able to log in')
            return redirect('driver_login/')
    else:
        form = DriverRegisterForm()
    return render(request, 'accounts/driver_signup.html', {'form': form})

@login_required
def driver_profile(request):
    if request.method == 'POST':
        u_form = DriverUpdateForm(request.POST, instance=request.user)
        p_form = DriverProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.driver_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('accounts/driver_profile')

    else:
        u_form = DriverUpdateForm(instance=request.user)
        p_form = DriverProfileUpdateForm(instance=request.user.driver_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/driver_profile.html', context)

class help(TemplateView):
    template_name='accounts/help.html'

class customer_service(TemplateView):
    template_name='accounts/customer_service.html'

####################################################################################################

def all_request_data(request):
    #delivery_details = delivery_product.objects.get(pk=id)
    x = delivery_product.objects.all().count()
    list = delivery_product.objects.annotate(count=Count('id')).order_by('-Date')
    context = {
        'list':list,
        'x':x,
        #'delivery_details':delivery_details
    }
    return render(request,'accounts/all_request_data.html',context)
# def DeliveryDetail(request,id):
# 	delivery_detail=delivery_product.objects.get(pk=id)
# 	context={
# 	'delivery_detail': delivery_detail
# 	}
# 	return render(request,'accounts/delivery_detail.html',context)
class DeliveryDetail(DetailView):
    template_name='accounts/delivery_detail.html'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(delivery_product,id=id_)

############## Driver list #######
def driver_list(request):
    # x = driver_Profile.objects.all().count()
    # list = delivery_product.objects.annotate(count=Count('id')).order_by('-Date')
    driver_list = driver_Profile.objects.all()
    context = {
        'driver_list':driver_list
    }
    return render(request,'accounts/driver_list.html',context)

def edit(request,id):
	driver_list=driver_Profile.objects.get(pk=id)
	context={
	'driver_list': driver_list
	}
	return render(request,'accounts/edit.html',context)

def update(request, id):
    driver_list = driver_Profile.objects.get(pk=id)
    driver_list.status = request.GET['status']
    driver_list.save()
    return redirect(driver_list)

# def update(request, id):
#     driver_list = driver_profile.objects.get(pk=id)
#     driver_list.status = request.GET['status']
#     driver_list.name = request.GET['name']
#     driver_list.car_details = request.GET['car_details']
#     driver_list.phone = request.GET['phone']
#     driver_list.save()
#     return redirect("/")
