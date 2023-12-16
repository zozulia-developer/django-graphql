import graphene
from graphene_django.types import DjangoObjectType
from .models import Shop, Product, Category


class ShopType(DjangoObjectType):
    class Meta:
        model = Shop


class ProductType(DjangoObjectType):
    shop = graphene.Field(ShopType)

    class Meta:
        model = Product

    def resolve_shop(self, info):
        return self.shop


class Query(graphene.ObjectType):
    cheapest_products = graphene.List(ProductType)

    def resolve_cheapest_products(self, info, **kwargs):
        shops = Shop.objects.all()

        cheapest_products = []
        for shop in shops:
            categories = Category.objects.filter(
                name__in=Category.get_allowed_categories(shop.shop_type)
            )
            for category in categories:
                cheapest_product = (
                    Product.objects.filter(shop=shop, categories=category)
                    .order_by('price')
                    .select_related('shop')
                    .first()
                )
                if cheapest_product:
                    cheapest_products.append(cheapest_product)

        return cheapest_products


schema = graphene.Schema(query=Query)