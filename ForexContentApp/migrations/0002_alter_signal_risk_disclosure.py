# Generated by Django 4.2.4 on 2023-09-18 00:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ForexContentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='risk_disclosure',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
