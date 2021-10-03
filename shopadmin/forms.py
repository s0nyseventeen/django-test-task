from django.forms import ModelForm
from .models import Shop, Product


class ShopForm(ModelForm):
	class Meta:
		model = Shop
		fields = ['title', 'description', 'imageUrl']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = [
			'description',
			'title',
			'amount',
			'price',
			'active',
			'image',
			'category'
		]
