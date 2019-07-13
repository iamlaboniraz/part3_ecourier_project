from django import forms

## -- from models -- ##
from .models import delivery_product,types_of_product
## ----

## -- for product delivery Form -- ##
class deliverForm(forms.ModelForm):
	class Meta:
		model=delivery_product
		fields=['from_location','to_location','product_type','image','weight','Date']
		labels={
		      'from_location':'From Location : ',
		      'to_location':'To Location : ',
		      'product_type' :'Product Type : ',
		      'weight':'Weight : ',
		      'image':'Product Picture :',
		      'Date':'Date :'
		     }
