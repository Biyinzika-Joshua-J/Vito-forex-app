# Generated by Django 4.2.4 on 2023-09-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForexContentApp', '0003_dailystep_date_created_dailystep_date_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='buy',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
