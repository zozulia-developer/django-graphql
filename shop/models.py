from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    class SHOP_CATEGORIES:
        SPORT = 'sport'
        FOOD = 'food'
        ELECTRONICS = 'electronics'

        CATEGORIES_CHOICES = (
            (SPORT, _('Спорт')),
            (FOOD, _('Їжа')),
            (ELECTRONICS, _('Електроніка')),
        )

    name = models.CharField(max_length=100, verbose_name=_('Назва'))
    description = models.TextField(blank=True, verbose_name=_('Опис'))
    shop_type = models.CharField(
        max_length=50,
        choices=SHOP_CATEGORIES.CATEGORIES_CHOICES,
        verbose_name=_('Тип'),
    )
    latitude = models.FloatField(verbose_name=_('Широта'))
    longitude = models.FloatField(verbose_name=_('Довгота'))
    sales_commission = models.FloatField(default=0, verbose_name=_('Комісія з продажів'))

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазини')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Назва'))

    class Meta:
        verbose_name = _('Категорія')
        verbose_name_plural = _('Категорії')
        ordering = ('name',)

    def __str__(self):
        return self.name

    @staticmethod
    def get_allowed_categories(shop_type):
        allowed_categories_mapping = {
            Shop.SHOP_CATEGORIES.SPORT: ['Зима', 'Літо', 'Футбол'],
            Shop.SHOP_CATEGORIES.FOOD: ['Випічка', 'Солодощі', 'Алкоголь'],
            Shop.SHOP_CATEGORIES.ELECTRONICS: ['Ноутбуки', 'Смартфони', 'Навушники'],
        }

        return allowed_categories_mapping.get(shop_type, [])


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Назва'))
    description = models.TextField(blank=True, verbose_name=_('Опис'))
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Магазин, якому належить цей товар'),
    )
    categories = models.ManyToManyField(Category, verbose_name=_('Категорії'))
    price = models.FloatField(verbose_name=_('Ціна'))
    weight = models.FloatField(blank=True, null=True, verbose_name=_('Вага'))
    keywords = models.TextField(blank=True, verbose_name=_('Ключові слова'))

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товари')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='product_images/', verbose_name=_('Фото'))

    class Meta:
        verbose_name = _('Фото товару')
        verbose_name_plural = _('Фото товарів')

    def __str__(self):
        return self.product.name
