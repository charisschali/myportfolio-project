from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
