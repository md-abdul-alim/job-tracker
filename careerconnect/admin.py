from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name__icontains', 'industry__name__icontains', 'country__name__icontains']
    list_display = ['name', 'industry', 'country', 'website', 'linkedin_profile', 'remote', 'non_tech']
    list_filter = ['industry__name', 'country__name', 'remote', 'non_tech', 'is_employee_checked', 'is_applied']
    list_display_links = ['name']


@admin.register(JobPortal)
class JobPortalAdmin(admin.ModelAdmin):
    search_fields = ['name__icontains', 'website__icontains', 'country', 'is_remote']
    list_display = ['name', 'website', 'is_remote']
    list_filter = ['country', 'is_remote']


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(WorkPlace)
class WorkPlaceAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ConnectionCategory)
class ConnectionCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'job_title', 'company__name__icontains',
                     'job_category__name__icontains', 'connection_category__name__icontains', 'department__name__icontains']
    list_display = ['first_name', 'company__name', 'connection_category', 'country', 'work_place', 'job_location']
    list_filter = ['company', 'department', 'work_place', 'job_category', 'connection_category']


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(VisaOpportunity)
class VisaOpportunityAdmin(admin.ModelAdmin):
    search_fields = ['country__name__icontains', 'website__icontains',]
    list_display = ['country', 'website', ]
    list_filter = ['country', ]

