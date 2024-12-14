from django.db import models



class Books(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField() 
    created_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title