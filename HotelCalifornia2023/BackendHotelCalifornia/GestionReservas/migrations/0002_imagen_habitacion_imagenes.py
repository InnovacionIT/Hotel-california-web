# Generated by Django 4.2.1 on 2023-06-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionReservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='img/perfil')),
            ],
        ),
        migrations.AddField(
            model_name='habitacion',
            name='imagenes',
            field=models.ManyToManyField(to='GestionReservas.imagen'),
        ),
    ]