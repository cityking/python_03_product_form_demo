from django import forms
from product import models
class ProductForm(forms.ModelForm):
	class Meta:
		model = models.Product
		fields=('name','spec','cate','stock','price','key')
