from django.db import models

# Create your models here.


class FundedProject(models.Model):
    title = models.CharField("Title",max_length=300)
    dept = models.CharField("Department",max_length=50)
    status = models.CharField("status", max_length=50,
                              choices=[('Completed', 'Completed'), ('OnGoing', 'OnGoing')])
    funding_agency = models.CharField("Funding Agency",max_length=100)
    pi_designation = models.CharField("PI and Designation",max_length=100)
    co_pi_designation = models.CharField("Co-PI and Designation",max_length=100, blank = True, null = True)
    start_date = models.DateField("Start Date", blank=True, null=True)
    end_date = models.DateField("End Date", blank=True, null=True)
    amount_sactioned = models.IntegerField("Amount Sanctioned",max_length=50)



    class Meta:
        pass

    def __str__(self):
        return self.title

class Proposal(models.Model):
    title = models.CharField("Title",max_length=300)
    dept = models.CharField("Department",max_length=50)
    funding_agency = models.CharField("Funding Agency",max_length=100)
    pi_designation = models.CharField("PI and Designation",max_length=100)
    co_pi_designation = models.CharField("Co-PI and Designation",max_length=100, blank = True, null = True)
    submission_date = models.DateField("Submission Date")
    amount_applied = models.CharField("Amount Applied",max_length=50)


    class Meta:
        pass

    def __str__(self):
        return self.title
