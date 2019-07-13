from django.shortcuts import render
from .forms import deliverForm
from .models import delivery_product,types_of_product
from notification.models import Notification
from django.shortcuts import render_to_response
# from django.views.generic import ListView
# Create your views here.

def delivery_request(request):
	if request.method == 'POST':
		form_delivery=deliverForm(request.POST,request.FILES)
		if form_delivery.is_valid():
			form_delivery.save()
			note = "Thanks for your request!! Wait a few minutes!! Car is on the way!!"
			new_form_delivery=deliverForm()
		else:
			note="failed.Try again!!"
		return render(request,'delivery_form.html',{'deliveryform':new_form_delivery,'note':note})
	else:
		form_delivery = deliverForm()
		return render(request,'delivery_form.html',{'deliveryform':form_delivery})

def wait_sms(request):
	return render(request,'wait.html')
def sms_send(request):
	n=Notification.objects.filter(user=request.user,viewed=False)
	return render_to_response("notification_msg.html",{'notification':n})
