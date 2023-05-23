# Generated by Django 4.2.1 on 2023-05-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True, null=True, verbose_name='category_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='product_creation_date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='product_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='product_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='product_clast_change_date'),
        ),
    ]