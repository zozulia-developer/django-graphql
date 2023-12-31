# Generated by Django 5.0 on 2023-12-15 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('shop_type', models.CharField(choices=[('sport', 'Спорт'), ('food', 'Їжа'), ('electronics', 'Електроніка')], max_length=50, verbose_name='Тип')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Довгота')),
                ('sales_commission', models.FloatField(default=0, verbose_name='Комісія з продажів')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазини',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Вага')),
                ('keywords', models.TextField(blank=True, verbose_name='Ключові слова')),
                ('categories', models.ManyToManyField(to='shop.category', verbose_name='Категорії')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.shop', verbose_name='Магазин, якому належить цей товар')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product_images/', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Фото товару',
                'verbose_name_plural': 'Фото товарів',
            },
        ),
    ]
