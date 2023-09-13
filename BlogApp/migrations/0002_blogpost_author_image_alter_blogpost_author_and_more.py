# Generated by Django 4.2.4 on 2023-09-07 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/author/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
