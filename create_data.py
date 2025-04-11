import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

# Create categories
categories = [
    {'name': 'Smartphones'},
    {'name': 'Laptops'},
    {'name': 'Accessories'},
    {'name': 'Tablets'},
]

created_categories = []

for cat_data in categories:
    cat = Category.objects.create(name=cat_data['name'])
    created_categories.append(cat)
    print(f"Created category: {cat.name}")

# Create products
products = [
    {
        'name': 'iPhone 15 Pro',
        'price': 999.99,
        'description': 'The latest iPhone with advanced features',
        'count': 10,
        'is_active': True,
        'category': created_categories[0]
    },
    {
        'name': 'Samsung Galaxy S24',
        'price': 899.99,
        'description': 'Powerful Android smartphone with great camera',
        'count': 15,
        'is_active': True,
        'category': created_categories[0]
    },
    {
        'name': 'MacBook Pro M3',
        'price': 1999.99,
        'description': 'High-performance laptop for professionals',
        'count': 5,
        'is_active': True,
        'category': created_categories[1]
    },
    {
        'name': 'Dell XPS 15',
        'price': 1799.99,
        'description': 'Premium Windows laptop with excellent display',
        'count': 8,
        'is_active': True,
        'category': created_categories[1]
    },
    {
        'name': 'AirPods Pro',
        'price': 249.99,
        'description': 'Wireless earbuds with noise cancellation',
        'count': 20,
        'is_active': True,
        'category': created_categories[2]
    },
    {
        'name': 'iPad Pro',
        'price': 1099.99,
        'description': 'Powerful tablet for productivity and creativity',
        'count': 12,
        'is_active': True,
        'category': created_categories[3]
    },
    {
        'name': 'Samsung Galaxy Tab S9',
        'price': 899.99,
        'description': 'Premium Android tablet with S Pen support',
        'count': 7,
        'is_active': True,
        'category': created_categories[3]
    },
]

for product_data in products:
    product = Product.objects.create(
        name=product_data['name'],
        price=product_data['price'],
        description=product_data['description'],
        count=product_data['count'],
        is_active=product_data['is_active'],
        category=product_data['category']
    )
    print(f"Created product: {product.name}")

print("Sample data created successfully!") 