from django.db import models
import datetime
from django.utils import timezone
from measurement.measures import Weight
from django_measurement.models import MeasurementField

# Create your models here.
class types_of_product(models.Model):
	title=models.CharField(max_length=100)
	def __str__(self):
		return self.title

class delivery_product(models.Model):
	from_location=models.CharField(max_length=100)
	to_location=models.CharField(max_length=100)
	product_type=models.ForeignKey(types_of_product,on_delete=models.CASCADE)
	weight = MeasurementField(measurement=Weight,null=True,blank=True)
	Date=models.DateTimeField(default=timezone.now)
	image=models.ImageField(upload_to='images/',null=True,blank=True)
	def __str__(self):
		return self.from_location
	# def get_absulate_url(self):
	# 	return reverse("accounts:DeliveryDetail", kwargs={"id": self.id})
