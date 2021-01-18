from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Supplier(models.Model):
    suppliername = models.CharField(max_length=200, null=True)
    pmname = models.CharField(max_length=200, null=True, blank=True)
    supplier_description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.suppliername


class ModelType(models.Model):
    typename = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.typename


class ModelName(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    modeltype = models.ForeignKey(ModelType, on_delete=models.CASCADE, null=True, blank=True)
    modelname = models.CharField(max_length=200)
    modeldescription = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.modelname


class SoftwareType(models.Model):
    softwaretype = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.softwaretype


class Software(models.Model):
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    modelname = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True, blank=True)
    software_type = models.ForeignKey(SoftwareType, on_delete=models.CASCADE, null=True)
    software_name = models.CharField(max_length=200, null=True, blank=True)
    software_full_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.software_full_name


class MajorIssue(models.Model):
    modelname = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True, blank=True)
    total_issue = (
        ('Camera Blur', 'Camera Blur'),
        ('Sound Noise', 'Sound Noise'),
        ('Network', 'Network'),
    )
    issue =MultiSelectField(max_length=200,choices=total_issue,blank=True,null=True)

class IssueSummary(models.Model):
    model = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    issue_analysis_version_wise = models.CharField(max_length=200, null=True)
    total_issue = models.IntegerField(max_length=2000, null=True)
    expected_software_date = models.DateField(null=True, blank=True)
    actual_software_date = models.DateField(null=True)
    feedback_expected_date = models.DateField(null=True)
    feedback_actual_date = models.DateField(null=True)
    new_issue = models.IntegerField(max_length=200, null=True)
    reopen_issue = models.IntegerField(max_length=200, null=True)
    is_mp = models.BooleanField(default=False)
    closed_issue = models.IntegerField(max_length=200, null=True)
    delay_team = (
        ('PM', 'PM'),
        ('QC', 'QC'),
        ('Supplier', 'Supplier'),
    )
    supplier_can_not_fixed = models.IntegerField(max_length=200, null=True, blank=True)
    issue_clsoed_by_pm = models.IntegerField(max_length=200, null=True, blank=True)
    delay = models.CharField(max_length=50, choices=delay_team, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    delay_by_pm = models.CharField(max_length=200, null=True, blank=True)
    delay_by_qc = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.expected_software_date is not None:
            self.delay_by_pm = self.actual_software_date - self.expected_software_date
        elif self.expected_software_date is None:
            self.delay_by_pm = self.feedback_actual_date - self.actual_software_date
        if self.feedback_expected_date is not None:
            self.delay_by_qc = self.feedback_actual_date - self.feedback_expected_date
        super(IssueSummary, self).save(*args, **kwargs)

    def __str__(self):
        return self.issue_analysis_version_wise


class IssueAnalysis(models.Model):
    model = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True)
    issue_name = models.CharField(max_length=200, null=True)
    imei = models.CharField(max_length=200, null=True)
    issue_source = models.CharField(max_length=200, null=True)
    problem = models.CharField(max_length=2000, null=True)
    qc_findings = models.TextField(null=True)
    hw_findings = models.TextField(null=True)
    root_cause = models.TextField(null=True, blank=True)
    evidence = models.FileField(upload_to='')
    posted_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.issue_name + " " + self.model.modelname
