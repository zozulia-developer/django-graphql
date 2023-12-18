from django import forms

from .models import Category, Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        if 'shop' in self.fields:
            if 'instance' in kwargs and kwargs['instance'] is not None:
                self.fields['categories'].queryset = Category.objects.filter(
                    name__in=Category.get_allowed_categories(kwargs['instance'].shop.shop_type)
                )

    def clean_categories(self):
        selected_categories = self.cleaned_data.get('categories')
        shop_type = self.cleaned_data.get('shop').shop_type
        allowed_categories = Category.get_allowed_categories(shop_type)

        for category in selected_categories:
            if category.name not in allowed_categories:
                raise forms.ValidationError(f"{category} is not an allowed category for the selected shop type.")

        return selected_categories
