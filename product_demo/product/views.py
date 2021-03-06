# coding: utf-8
from django.shortcuts import render,redirect
from product.models import Category,Keyword,Product
from django.core.paginator import Paginator
from product import forms
# Create your views here.

def add(request):
    if request.method == 'POST':
        post = request.POST
        product = Product.objects.create(
            name = post.get('product_name'),
            spec = post.get('product_spec'),
            cate_id = post.get('product_category'),
            stock = post.get('product_stock'),
            price = post.get('product_price'),
            desc = post.get('product_desc'))

        keylist = post.getlist('product_key')
        for key_id in keylist:
                product.key.add(key_id)
        return redirect('list')

    categorys = Category.objects.all()
    keywords = Keyword.objects.all()
    return render(request,'product/add.html',{'categorys':categorys,'keywords':keywords})

def update(request,id):

    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        post = request.POST
        product.name = post.get('product_name')
        product.spec = post.get('product_spec')
        product.cate_id = post.get('product_category')
        product.stock = post.get('product_stock')
        product.price = post.get('product_price')
        product.desc = post.get('product_desc')
        keylist = post.getlist('product_key')
        for key_id in keylist:
            key = Keyword.objects.get(pk=key_id)
            if key not in product.key.all():
                product.key.add(key_id)
        for key in product.key.all():
            if str(key.id) not in keylist:
                product.key.remove(key)
        product.save()

        return redirect('list')
    product = Product.objects.get(pk=id)
    categorys = Category.objects.all()
    keywords = Keyword.objects.all()
    return render(request, 'product/update.html', locals())

def delete(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('list')

def list(request):
	if request.method == 'POST':
		query_form = forms.QueryForm(request.POST)
		if query_form.is_valid():
			name = query_form.cleaned_data['name']
			products=Product.objects.filter(name=name)
	else:
		query_form = forms.QueryForm()
		products = Product.objects.order_by('-id')
	paginator = Paginator(products,3)
	try:
	    page = int(request.GET.get('page'))
	    products = paginator.page(page)
	except:
	    products = paginator.page(1)
	return render(request,'product/list.html',locals())
def add2(request):
	if request.method == 'POST':
		product_form = forms.ProductForm(request.POST)
		if product_form.is_valid():
        		product_form.save()
        		return redirect('list')
		
	product_form = forms.ProductForm()
	return render(request, 'product/add2.html', locals())
def update2(request, id):
	product = Product.objects.get(pk=id)
	if request.method == 'POST':
		product_form = forms.ProductForm(request.POST, instance=product)
		product_form.save()
		return redirect('list')
	product_form = forms.ProductForm()
	return render(request, 'product/update2.html', locals())
def add3(request):
	if request.method == 'POST':
		product_form = forms.ProductForm2(request.POST)
		if product_form.is_valid():
			name = product_form.cleaned_data['name']
			spec = product_form.cleaned_data['spec']
			cate = product_form.cleaned_data['cate']
			stock = product_form.cleaned_data['stock']
			price = product_form.cleaned_data['price']
			key = product_form.cleaned_data['key']
			desc = product_form.cleaned_data['desc']
			product = Product.objects.create(name=name, spec=spec, cate=cate, stock=stock, price=price, desc=desc)
			for k in key:
				product.key.add(k)

			return redirect('list')
	else:
		product_form = forms.ProductForm2()	
		return render(request,'product/add3.html',locals())

def update3(request, id):
	product = Product.objects.get(pk=id)
	if request.method == 'POST':
		product_form = forms.ProductForm2(request.POST)
		if product_form.is_valid():
			product.name = product_form.cleaned_data['name']
			product.spec = product_form.cleaned_data['spec']
			product.cate = product_form.cleaned_data['cate']
			product.stock = product_form.cleaned_data['stock']
			product.price = product_form.cleaned_data['price']
			product.desc = product_form.cleaned_data['desc']


			key = product_form.cleaned_data['key']
			for k in product.key.all():
				if k not in key:
					product.key.remove(k)
			for k in key:
				if k not in product.key.all():
					product.key.add(k)
			product.save()	
			return redirect('list')
	else:
		product_form = forms.ProductForm2(initial={
			'name':product.name, 	
                        'spec':product.spec, 
                        'cate':product.cate, 
                        'stock':product.stock,
                        'price':product.price,
                        'desc':product.desc, 
			'key':product.key.all(),

		})
		return render(request, 'product/update3.html', locals())
