# Generated by Django 4.2.1 on 2023-06-16 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_auth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
