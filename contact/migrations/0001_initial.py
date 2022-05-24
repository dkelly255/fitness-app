# Generated by Django 3.2 on 2022-05-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]
