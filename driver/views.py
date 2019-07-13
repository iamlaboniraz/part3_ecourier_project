from django.shortcuts import render,redirect
# from .models import driver_profile
# # Create your views here.
# def driver(request):
#     driver_list = driver_profile.objects.all()
#     context = {
#         'driver_list':driver_list
#     }
#     return render(request,'driver_list.html',context)
#
# def edit(request,id):
# 	driver_list=driver_profile.objects.get(pk=id)
# 	context={
# 	'driver_list': driver_list
# 	}
# 	return render(request,'edit.html',context)
# def update(request, id):
#     driver_list = driver_profile.objects.get(pk=id)
#     driver_list.status = request.GET['status']
#     driver_list.name = request.GET['name']
#     driver_list.car_details = request.GET['car_details']
#     driver_list.phone = request.GET['phone']
#     driver_list.save()
#     return redirect("/")
