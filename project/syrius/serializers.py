from rest_framework import serializers
from .models import Syrius
from drf_extra_fields.fields import Base64ImageField  




# class ImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Syrius
#         fields = ('id',
#                   'title',
#                   'content',
#                   'image')

    
class ImageBase64Serilizer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Syrius
        fields = ["title", "description", "image"]
        
        
    
    
    
    


# class SyriusSerialiazer(serializers.Serializer):
#     content = serializers.CharField()


#     def create(self, validated_data):
#         return Syrius.object.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.content = validated_data.get("content", instance.content)
#         instance.photo = validated_data.get("photo", instance.photo)
#         instance.save()
#         return instance