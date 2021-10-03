import django_filters
from django_filters import BooleanFilter, RangeFilter
from .models import *


class ShopFilter(django_filters.FilterSet):
	class Meta:
		model = Shop
		fields = ['title']


class ProductFilter(django_filters.FilterSet):
	active_sort = BooleanFilter(field_name='active')
	price = RangeFilter()

	class Meta:
		model = Product
		fields = ['product_id', 'title']
		exclude = ['active', 'price']
