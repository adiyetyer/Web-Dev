# Shop Back API

This Django REST API project provides a backend for an online shop application.

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install django djangorestframework
   ```
3. Apply migrations:
   ```
   python manage.py migrate
   ```
4. Load sample data:
   ```
   python create_data.py
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

The API provides the following endpoints:

### Products

- **GET /api/products/** - List all products
  - Returns a JSON array of all products

- **GET /api/products/{id}/** - Get a specific product by ID
  - Returns a JSON object with product details

### Categories

- **GET /api/categories/** - List all categories
  - Returns a JSON array of all categories

- **GET /api/categories/{id}/** - Get a specific category by ID
  - Returns a JSON object with category details

- **GET /api/categories/{id}/products/** - List all products in a specific category
  - Returns a JSON array of products belonging to the specified category

## Models

### Category
- `id` - Auto-incrementing ID
- `name` - Category name (CharField)

### Product
- `id` - Auto-incrementing ID
- `name` - Product name (CharField)
- `price` - Product price (FloatField)
- `description` - Product description (TextField)
- `count` - Available quantity (IntegerField)
- `is_active` - Product availability status (BooleanField)
- `category` - Foreign key to Category model

## Sample Usage

```bash
# Get all products
curl http://localhost:8000/api/products/

# Get product with ID 1
curl http://localhost:8000/api/products/1/

# Get all categories
curl http://localhost:8000/api/categories/

# Get category with ID 1
curl http://localhost:8000/api/categories/1/

# Get all products in category with ID 1
curl http://localhost:8000/api/categories/1/products/
``` 