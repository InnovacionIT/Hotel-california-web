# Generated by Django 4.2.1 on 2023-06-01 12:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('clienteId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('usuario', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=150)),
                ('fechaDeNacimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Todos los clientes registrados',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotelId', models.AutoField(primary_key=True, serialize=False)),
                ('razonsocial', models.CharField(max_length=150)),
                ('cuil', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='CUIL inválido', regex='^(20|2[3-7]|30|3[3-4])(\\d{8})(\\d)$')])),
                ('domicilio', models.CharField(max_length=150)),
                ('localidad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('cp', models.PositiveSmallIntegerField()),
                ('telefono', models.IntegerField()),
                ('categoria', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Todos los hoteles disponibles',
                'verbose_name_plural': 'Hoteles',
                'db_table': 'Hotel',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleadoId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('usuario', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=150)),
                ('domicilio', models.CharField(max_length=150)),
                ('localidad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('cp', models.PositiveSmallIntegerField()),
                ('telefono', models.IntegerField()),
                ('rol', models.CharField(max_length=70)),
                ('hotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionUsuarios.hotel')),
            ],
            options={
                'verbose_name': 'Todos los empleados registrados en el hotel',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
            },
        ),
    ]
