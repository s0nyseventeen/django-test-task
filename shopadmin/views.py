from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ShopForm, ProductForm
from .filters import ShopFilter, ProductFilter, RangeFilter
from django.db.models import Count


def home(request):
	shops = Shop.objects.all()
	total_shops = shops.count()
	my_filter = ShopFilter(request.GET, queryset=shops)
	shops = my_filter.qs
	context = {
		'shops': shops,
		'total_shops': total_shops,
		'my_filter': my_filter,
	}
	return render(request, 'shopadmin/shops.html', context)


def products(request):
	products = Product.objects.all().order_by('price')
	total_products = products.count()
	my_filter = ProductFilter(request.GET, queryset=products)
	products = my_filter.qs
	context  = {
		'products': products,
		'total_products': total_products,
		'my_filter': my_filter,
	}
	return render(request, 'shopadmin/products.html', context)


def product_detail(request, pk):
	product = get_object_or_404(Product, product_id=pk)
	photos = ProductImage.objects.filter(product=product)
	context = {
		'product': product,
		'photos': photos
	}
	return render(request, 'shopadmin/product_detail.html', context)


def shop_detail(request, pk):
	shop = Shop.objects.get(shop_id=pk)
	orders = shop.order_set.all()
	context = {
		'shop': shop,
		'orders': orders,
	}
	return render(request, 'shopadmin/shop_detail.html', context)


def update_shop(request, pk):
	shop = Shop.objects.get(shop_id=pk)
	form = ShopForm(instance=shop)
	if request.method == 'POST':
		form = ShopForm(request.POST, instance=shop)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form': form
	}
	return render(request, 'shopadmin/orderform_shop.html', context)


def update_product(request, pk):
	product = Product.objects.get(product_id=pk)
	form = ProductForm(instance=product)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form': form
	}
	return render(request, 'shopadmin/orderform_product.html', context)
