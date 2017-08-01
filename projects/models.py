from django.db import models

# Create your models here.


class Project(models.Model):
    dept = models.CharField("Department",max_length=50)
    funding_agency = models.CharField("Funding Agency",max_length=50)
    pi_designation = models.CharField("PI and Designation",max_length=50)
    co_pi_designation = models.CharField("Co-PI and Designation",max_length=50)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    amount_sactioned = models.IntegerField("Amount Sanctioned")


    class Meta:
        pass

    def __str__(self):
        return self.funding_agency
