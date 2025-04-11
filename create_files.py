import os

# Create api/serializers.py
serializers_content = '''from rest_framework import serializers
from api.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "description", "count", "is_active", "category")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
'''

# Create api/urls.py
urls_content = '''from django.urls import path
from api.views import product_list, product_detail, category_list, category_detail, category_products

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:id>/', category_detail, name='category_detail'),
    path('categories/<int:id>/products/', category_products, name='category_products'),
]
'''

# Create shop_back/urls.py
main_urls_content = '''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
'''

# Write the files
with open('api/serializers.py', 'w') as f:
    f.write(serializers_content)

with open('api/urls.py', 'w') as f:
    f.write(urls_content)

with open('shop_back/urls.py', 'w') as f:
    f.write(main_urls_content)

print("Files created successfully!") 