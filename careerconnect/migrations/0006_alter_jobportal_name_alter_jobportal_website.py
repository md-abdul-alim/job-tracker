# Generated by Django 5.1 on 2024-08-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerconnect', '0005_jobportal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobportal',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='jobportal',
            name='website',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
