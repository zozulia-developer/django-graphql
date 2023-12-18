from django.urls import path

from .views import GetCategoriesView

app_name = 'shop'

urlpatterns = [
    path('admin/api/categories/', GetCategoriesView.as_view(), name='categories'),
]
