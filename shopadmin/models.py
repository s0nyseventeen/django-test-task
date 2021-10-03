from django.db import models


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True)
    imageUrl = models.URLField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    imagetoupload = models.ImageField(upload_to='images', null=True)

    class Meta:
        ordering = ['shop_id']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField(default=0, null=True)
    active = models.BooleanField(default=False)
    image = models.URLField(max_length=200, null=True, blank=True)
    category = models.ManyToManyField('Group')

    class Meta:
        ordering = ['product_id']

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.product.title


class Group(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    shop = models.ForeignKey(Shop, null=True,
                             on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True,
                                on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f'{self.product.title}'
