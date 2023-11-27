from rest_framework import serializers
from .models import Syrius
from drf_extra_fields.fields import Base64ImageField  
from .models import Victorina, Category


    
class ImageBase64Serilizer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Syrius
        fields = ["title", "description", "image"]
        
#---------------------------task 3---------------------------    
class VictorinSerializator(serializers.ModelSerializer):
    class Meta:
        model = Victorina
        fields = ['id','answer', 
                  'question', 'value', 
                  'airdate', 'created_at', 
                  'updated_at', 'category_id', 
                  'game_id']
    def create(self, validated_data):
        return Victorina.objects.create(**validated_data)

class CategorySerializator(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','created_at',
                  'updated_at','clues_count']
    
    def create(self, validated_data):
       return Category.objects.create(**validated_data)
