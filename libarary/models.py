from django.db import models
import datetime
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100,blank=True,null=True)
    book_title = models.CharField(max_length=200,blank=True,null=True)
    book_author = models.CharField(max_length=100,blank=True,null=True)
    publish_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.book_name