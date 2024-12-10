from rest_framework import serializers
from catalogs.models import Catalog, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CatalogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'user', 'categories']
        read_only_fields = ['id', 'categories', 'user']
