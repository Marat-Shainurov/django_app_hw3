# Generated by Django 4.2.1 on 2023-05-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name='category_created_at'),
        ),
    ]
