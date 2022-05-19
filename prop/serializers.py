from rest_framework import serializers
from . models import Contect_us


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contect_us
         #fields = ['id', 'title', 'author', 'email']
        fields = '__all__'