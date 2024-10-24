from django.db import models

class AnalysedFood(models.Model):
    image = models.ImageField(upload_to="food_images")
    report = models.JSONField()