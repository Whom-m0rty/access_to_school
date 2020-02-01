from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    patronymic = serializers.CharField(max_length=100)
    created_date = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=254)
    in_school = serializers.CharField(max_length=10)
    last_use = serializers.CharField(max_length=30)