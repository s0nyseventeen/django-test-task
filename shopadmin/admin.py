from django.contrib import admin
from .models import Shop, Product, Order, ProductImage, Group


class ProductImageAdmin(admin.StackedInline):
	model = ProductImage


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = 'shop_id', 'title', 'imagetoupload', 'date'
	list_filter = 'title', 'date'
	search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = (
		'product_id',
		'title',
		'amount',
		'price',
		'active',
	)
	search_fields = ['product_id', 'title']
	inlines = [ProductImageAdmin]

	class Meta:
		model = Product


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = 'shop', 'product', 'date_created', 'status'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
	pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	pass
