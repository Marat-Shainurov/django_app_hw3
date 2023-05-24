from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='product_name')
    description = models.TextField(verbose_name='product_description', **NULLABLE)
    img = models.ImageField(upload_to='media/', verbose_name='product_img', **NULLABLE)
    category = models.ForeignKey('Category', to_field='category_name', on_delete=models.CASCADE,
                                 verbose_name='product_category')
    price = models.IntegerField(verbose_name='product_price')
    creation_date = models.DateTimeField(verbose_name='product_creation_date', auto_now_add=True, **NULLABLE)
    last_change_date = models.DateTimeField(verbose_name='product_last_change_date', auto_now=True, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name',)


class Category(models.Model):
    category_name = models.CharField(null=False, max_length=50, unique=True, verbose_name='category_name')
    category_description = models.TextField(verbose_name='category_description', **NULLABLE)

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('category_name',)


class Contacts(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='company_name')
    address = models.TextField(verbose_name='company_address')
    phone = models.CharField(max_length=50, verbose_name='company_phone')
    email = models.CharField(max_length=50, verbose_name='company_email')

    def __str__(self):
        return f'{self.company_name} {self.phone} {self.email}'

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
