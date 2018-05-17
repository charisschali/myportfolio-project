from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length="1000")
    image = models.ImageField(upload_to='images/')
    class Meta:
        ordering = ['-pub_date',]
    #a function to return a portion of text
    def summary(self):
        return self.body[:50]
    #print time without the actual time
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    #prints titlein django admin as an understable manner
    def __str__(self):
        return self.title    
