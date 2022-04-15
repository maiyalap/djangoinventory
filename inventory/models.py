from django.db import models

#create your model here
class Post(models.Model):
    item_id = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=20)
    unit_id = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    qty = models.IntegerField()
