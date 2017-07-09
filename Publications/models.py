from django.db import models

# Create your models here.
class publication(models.Model):
    dept = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    Journal_name =models.CharField(max_length=50)
    year = models.DateField()

    def __str__(self):
        return self.title + ' - ' + self.author


