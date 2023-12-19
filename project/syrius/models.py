from django.db import models
from django.contrib.auth.models import User


class Syrius(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title


#----------------API for external resource-------------------
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





