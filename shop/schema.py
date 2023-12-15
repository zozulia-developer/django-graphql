import graphene
from graphene_django.types import DjangoObjectType
from .models import Shop, Product, Category


class ShopType(DjangoObjectType):
    class Meta:
        model = Shop


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    cheapest_products = graphene.List(ProductType)

    def resolve_cheapest_products(self, info):
        products = Product.objects.all()

        cheapest_products = []
        for shop_type, _ in Shop.SHOP_CATEGORIES.CATEGORIES_CHOICES:
            for category in Category.objects.filter(shop_type=shop_type):
                cheapest_product = products.filter(
                    shop__shop_type=shop_type,
                    categories=category,
                ).order_by('price').first()

                if cheapest_product:
                    cheapest_products.append(cheapest_product)

        return cheapest_products


schema = graphene.Schema(query=Query)
