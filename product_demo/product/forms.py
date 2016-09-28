#coding: utf-8
from django import forms
from product import models
class ProductForm(forms.ModelForm):
	class Meta:
		model = models.Product
		fields=('name','spec','cate','stock','price','key','desc')

class ProductForm2(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"请输入产品名称","class":"input-xlarge", }))
	spec=forms.ChoiceField(choices=models.Product.spec_type,widget=forms.Select(attrs={'class':'input-xlarge','name':'product_spec'}))
	cate = forms.ModelChoiceField(queryset=models.Category.objects.all(),widget=forms.Select(attrs={'class':'input-xlarge'}))
	stock = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"请输入库存数量","name":"product_stock","class":"input-xlarge" }))
	price = forms.DecimalField(widget=forms.TextInput(attrs={"placeholder":"请输入产品价格","name":"product_price","class":"input-xlarge" }))
	key = forms.ModelMultipleChoiceField(queryset=models.Keyword.objects.all(),widget=forms.SelectMultiple(attrs={'class':'input-xlarge',}))
	desc = forms.CharField(widget=forms.Textarea(attrs={"name":"product_desc","rows":"2"}))
	#class Meta:
	#	model = models.Product
	#        fields=('name','spec','cate','stock','price','key','desc')
#	name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"请输入产品名称","class":"input-xlarge", }))
#	spec=forms.ChoiceField(choices=models.Product.spec_type,widget=forms.Select(attrs={'class':'input-xlarge','name':'product_spec'}))
#	cate=forms.ModelChoiceField(queryset=models.Category.objects.all(),widget=forms.Select(attrs={'class':'input-xlarge','name':'product_cate'}))
#	stock=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"请输入库存数量","name":"product_stock","class":"input-xlarge" }))
#	price=forms.DecimalField(widget=forms.TextInput(attrs={"placeholder":"请输入产品价格","name":"product_price","class":"input-xlarge" }))
#	key=forms.ModelMultipleChoiceField(queryset=models.Keyword.objects.all(),widget=forms.SelectMultiple(attrs={'class':'input-xlarge','name':'product_key'}))
#	desc=forms.CharField(widget=forms.Textarea(attrs={"name":"product_desc","rows":"2"}))
class QueryForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'请输入产品名','class':'input-xlarge'}))
