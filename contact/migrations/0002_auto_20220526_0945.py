# Generated by Django 3.2 on 2022-05-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
