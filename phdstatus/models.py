from django.db import models


class PhdStatus(models.Model):
    name = models.CharField("Name", max_length=200)
    dept = models.CharField("Department", max_length=200)
    guide = models.CharField("Guide", max_length=200)
    uni = models.CharField("University where registered", max_length=200)
    year = models.DateField("year of registration")
    other = models.TextField("Any other details")

    class Meta:
        verbose_name_plural = "PHD Statuses"

    def __str__(self):
        return self.name + ' - ' + self.dept


class WorkDetailsTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    duration = models.CharField("Duration(Days)", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Work Detail"

    def __str__(self):
        return self.title


class ComprehensiveTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    duration = models.CharField("Duration(Days)", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Comprehensive viva voce"
        verbose_name = "Comprehensive viva voce"

    def __str__(self):
        return self.title


class PublicationsTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    duration = models.CharField("Duration(Days)", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Publications related to research topic"

    def __str__(self):
        return self.title


class WorkshopsTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    duration = models.CharField("Duration(Days)", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "workshops/seminar/conference attended"

    def __str__(self):
        return self.title


class TrainingTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    duration = models.CharField("Duration(Days)", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Any trainings attended for supporting chosen research topic"

    def __str__(self):
        return self.title


class FundedProjectsTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    duration = models.CharField("Duration(Days)", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Any funded porposal made  with respected research topic"

    def __str__(self):
        return self.title
