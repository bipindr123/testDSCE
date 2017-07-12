from django.db import models

# Create your models here.
class publication(models.Model):
    dept = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Journal_name =models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return self.title + ' - ' + self.author


