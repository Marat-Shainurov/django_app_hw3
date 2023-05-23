from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=50, verbose_name='product_name')
    description = models.TextField(verbose_name='product_description')
    img = models.ImageField(upload_to='media/', verbose_name='product_img')
    category = models.CharField(null=False, max_length=50, verbose_name='product_category')
    price = models.IntegerField(null=False, verbose_name='product_price')
    creation_date = models.DateTimeField(verbose_name='product_creation_date')
    last_change_date = models.DateTimeField(verbose_name='product_clast_change_date')

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name',)


class Category(models.Model):
    category_name = models.CharField(null=False, max_length=50, verbose_name='category_name')
    category_description = models.TextField(null=False, verbose_name='category_description')


    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('category_name',)
