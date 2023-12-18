from django.core.exceptions import ObjectDoesNotExist
from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import gettext as _

from .models import Category, Product, ProductImage, Shop


class ShopModelTest(TestCase):
    def setUp(self):
        self.shop_data = {
            'name': 'Test Shop',
            'description': 'Test description',
            'shop_type': Shop.SHOP_CATEGORIES.SPORT,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'sales_commission': 0.05,
        }

    def test_create_shop(self):
        shop = Shop.objects.create(**self.shop_data)

        self.assertEqual(shop.name, self.shop_data['name'])
        self.assertEqual(shop.description, self.shop_data['description'])
        self.assertEqual(shop.shop_type, self.shop_data['shop_type'])
        self.assertEqual(shop.latitude, self.shop_data['latitude'])
        self.assertEqual(shop.longitude, self.shop_data['longitude'])
        self.assertEqual(shop.sales_commission, self.shop_data['sales_commission'])

    def test_shop_str_representation(self):
        shop = Shop.objects.create(**self.shop_data)
        expected_str = self.shop_data['name']
        self.assertEqual(str(shop), expected_str)

    def test_shop_categories_choices(self):
        sport_category = Shop.SHOP_CATEGORIES.SPORT
        food_category = Shop.SHOP_CATEGORIES.FOOD
        electronics_category = Shop.SHOP_CATEGORIES.ELECTRONICS

        self.assertEqual(sport_category, 'sport')
        self.assertEqual(food_category, 'food')
        self.assertEqual(electronics_category, 'electronics')

        sport_display = _('Спорт')
        food_display = _('Їжа')
        electronics_display = _('Електроніка')

        self.assertEqual(Shop.SHOP_CATEGORIES.CATEGORIES_CHOICES[0], (sport_category, sport_display))
        self.assertEqual(Shop.SHOP_CATEGORIES.CATEGORIES_CHOICES[1], (food_category, food_display))
        self.assertEqual(Shop.SHOP_CATEGORIES.CATEGORIES_CHOICES[2], (electronics_category, electronics_display))


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category_data = {
            'name': 'Test Category',
        }

    def test_create_category(self):
        category = Category.objects.create(**self.category_data)
        self.assertEqual(category.name, self.category_data['name'])

    def test_category_str_representation(self):
        category = Category.objects.create(**self.category_data)
        expected_str = self.category_data['name']
        self.assertEqual(str(category), expected_str)

    def test_get_allowed_categories(self):
        sport_allowed_categories = ['Зима', 'Літо', 'Футбол']
        food_allowed_categories = ['Випічка', 'Солодощі', 'Алкоголь']
        electronics_allowed_categories = ['Ноутбуки', 'Смартфони', 'Навушники']

        self.assertEqual(Category.get_allowed_categories(Shop.SHOP_CATEGORIES.SPORT), sport_allowed_categories)
        self.assertEqual(Category.get_allowed_categories(Shop.SHOP_CATEGORIES.FOOD), food_allowed_categories)
        self.assertEqual(Category.get_allowed_categories(Shop.SHOP_CATEGORIES.ELECTRONICS),
                         electronics_allowed_categories)
        self.assertEqual(Category.get_allowed_categories('unknown_shop_type'), [])


class ProductModelTest(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test description',
            shop_type=Shop.SHOP_CATEGORIES.SPORT,
            latitude=40.7128,
            longitude=-74.0060,
            sales_commission=0.05,
        )

        self.category = Category.objects.create(name='Test Category')

        self.product_data = {
            'name': 'Test Product',
            'description': 'Test description',
            'shop': self.shop,
            'price': 19.99,
            'weight': 1.5,
            'keywords': 'test, product',
        }

    def test_create_product(self):
        product = Product.objects.create(**self.product_data)
        product.categories.add(self.category)

        self.assertEqual(product.name, self.product_data['name'])
        self.assertEqual(product.description, self.product_data['description'])
        self.assertEqual(product.shop, self.product_data['shop'])
        self.assertEqual(product.price, self.product_data['price'])
        self.assertEqual(product.weight, self.product_data['weight'])
        self.assertEqual(product.keywords, self.product_data['keywords'])
        self.assertEqual(product.categories.first(), self.category)

    def test_product_str_representation(self):
        product = Product.objects.create(**self.product_data)
        product.categories.add(self.category)

        expected_str = self.product_data['name']
        self.assertEqual(str(product), expected_str)


class ProductImageModelTest(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test description',
            shop_type=Shop.SHOP_CATEGORIES.SPORT,
            latitude=40.7128,
            longitude=-74.0060,
            sales_commission=0.05,
        )

        self.category = Category.objects.create(name='Test Category')

        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            shop=self.shop,
            price=19.99,
            weight=1.5,
            keywords='test, product',
        )

        self.product_image_data = {
            'product': self.product,
            'images': 'product_images/test_image.jpg',
        }

    def test_create_product_image(self):
        product_image = ProductImage.objects.create(**self.product_image_data)

        self.assertEqual(product_image.product, self.product)
        self.assertEqual(str(product_image), self.product.name)


class GetCategoriesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test description',
            shop_type=Shop.SHOP_CATEGORIES.SPORT,
            latitude=40.7128,
            longitude=-74.0060,
            sales_commission=0.05,
        )
        self.category_sport = Category.objects.create(name='Зима')

    def test_get_categories_view(self):
        url = reverse('shop:categories')
        response = self.client.get(url, {'shop': self.shop.pk})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn({'id': self.category_sport.id, 'name': 'Зима'}, data)

    def test_get_categories_view_invalid_shop_type(self):
        url = reverse('shop:categories')
        with self.assertRaises(ObjectDoesNotExist):
            response = self.client.get(url, {'shop': 999})
            self.assertEqual(response.status_code, 404)
