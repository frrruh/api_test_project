from django.db import models
from drf_extra_fields.fields import Base64ImageField



class Syrius(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/")
    
    def __str__(self):
        return self.title
    












# class ImageSyrius(models.Model):
#     name = models.CharField(max_length=100, db_index = True)
#     img_field = Base64ImageField(required=False)
    
#     def __str__(self):
#         return self.name



    
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    
#     def __str__(self):
#         return self.name
