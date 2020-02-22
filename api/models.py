from django.db import models
from django.utils import timezone
from .gen_slug import gen_slug

class Post(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(max_length=20, unique=True, default=gen_slug)
    email = models.EmailField(max_length=254)
    in_school = models.CharField(max_length=10, default=False)
    last_use = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.slug