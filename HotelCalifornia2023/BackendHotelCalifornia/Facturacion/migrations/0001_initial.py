# Generated by Django 4.2.1 on 2023-05-19 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GestionUsuarios', '0001_initial'),
        ('GestionReservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('tipoPagoId', models.AutoField(primary_key=True, serialize=False)),
                ('tipoPago', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Pago de las facturas',
                'verbose_name_plural': 'Tipos de pago',
                'db_table': 'tipoPagp',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('facturaId', models.AutoField(primary_key=True, serialize=False)),
                ('nroFactura', models.CharField(max_length=10, unique=True)),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionUsuarios.cliente')),
                ('hotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionUsuarios.hotel')),
            ],
            options={
                'verbose_name': 'Facturas emitidas por el hotel correspondientes a las resvervas',
                'verbose_name_plural': 'Facturas',
                'db_table': 'factura',
            },
        ),
        migrations.CreateModel(
            name='DetallePago',
            fields=[
                ('detallePagoId', models.AutoField(primary_key=True, serialize=False)),
                ('porcentajePago', models.PositiveSmallIntegerField(default=100)),
                ('facturaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facturacion.factura')),
                ('tipoPagoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facturacion.tipopago')),
            ],
            options={
                'verbose_name': 'Detalle de Pago de las facturas emitidas por el hotel',
                'verbose_name_plural': 'Detalles de pago',
                'db_table': 'detallePagp',
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('detalleId', models.AutoField(primary_key=True, serialize=False)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=20)),
                ('facturaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facturacion.factura')),
                ('reservaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionReservas.reserva')),
            ],
            options={
                'verbose_name': 'Detalle de las facturas emitidas por el hotel correspondientes a las resvervas',
                'verbose_name_plural': 'Detalles',
                'db_table': 'detalle',
            },
        ),
        migrations.AddConstraint(
            model_name='detallepago',
            constraint=models.CheckConstraint(check=models.Q(('porcentajePago__lte', 101)), name='Valor de porcentaje entre 0 y 100'),
        ),
    ]