from unicodedata import category
from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from tensorboard import summary
# Create your models here.
CATEGORY_CHOICES = (
    ("Action", "Action"),
    ("Adventure", "Adventure"),
    ("Puzzle", "Puzzle"),
    ("Strategy", "Strategy"),
    ("Sports", "Sports"),
    ("Board/Card Game", "Board/Card Game"),
    ("Other", "Other"),
)


class Profile(models.Model):
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(12)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    picture = models.URLField(null=True, blank=True)

class Game(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5)])
    max_level = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    image_url = models.URLField()
    summary = models.TextField(null=True, blank=True)
    