from django.db import models
from drf_extra_fields.fields import Base64ImageField



class Syrius(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/")
    
    def __str__(self):
        return self.title

#----------------task 3 ----------------------------------
class Victorina(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.TextField(max_length=255)
    question = models.TextField()
    value = models.IntegerField(null=True)
    airdate = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category_id = models.IntegerField()
    game_id = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.id

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    clues_count = models.IntegerField()


    def __str__(self):
        return self.title





