# Generated by Django 3.2.12 on 2022-02-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querymanager', '0005_alter_companydata_year_founded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='current_employee_estimate',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='total_employee_estimate',
            field=models.CharField(max_length=256),
        ),
    ]
