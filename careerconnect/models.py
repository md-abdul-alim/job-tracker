from django.db import models


class SearchQuery(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class JobPortal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    website = models.URLField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    industry = models.ForeignKey(Industry, related_name='companies', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='companies', on_delete=models.CASCADE)
    website = models.URLField(null=True, blank=True, unique=True)
    linkedin_profile = models.URLField(null=True, blank=True, unique=True)
    remote = models.BooleanField(default=False)
    non_tech = models.BooleanField(default=False)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_employee_checked = models.BooleanField(default=False)
    is_applied = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class JobCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ConnectionCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    job_category = models.ForeignKey(JobCategory, related_name='employees', on_delete=models.CASCADE, null=True, blank=True)
    connection_category = models.ForeignKey(ConnectionCategory, related_name='employees', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, related_name='employees_country', on_delete=models.CASCADE)
    job_location = models.ForeignKey(Country, related_name='employees_location', on_delete=models.CASCADE, null=True)
    work_place = models.ForeignKey(WorkPlace, related_name='employees', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True, unique=True)
    target = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VisaOpportunity(models.Model):
    country = models.ForeignKey(Country, related_name='visa_country', on_delete=models.SET_NULL, null=True)
    website = models.URLField(max_length=255, unique=True)
    link_1 = models.URLField(max_length=255, unique=True, null=True, blank=True)
    link_2 = models.URLField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.website
