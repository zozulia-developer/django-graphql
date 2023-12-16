from django.http import JsonResponse
from django.views import View

from .models import Category, Shop


class GetCategoriesView(View):
    def get(self, request, *args, **kwargs):
        shop_type = self.request.GET.get('shop', None)
        shop = Shop.objects.get(pk=shop_type)
        categories = Category.objects.filter(
            name__in=Category.get_allowed_categories(shop.shop_type),
        ).values(
            'id',
            'name',
        )
        return JsonResponse(list(categories), safe=False)
