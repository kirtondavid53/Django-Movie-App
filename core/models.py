from django.db import models
from django.contrib.auth.models import User

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    