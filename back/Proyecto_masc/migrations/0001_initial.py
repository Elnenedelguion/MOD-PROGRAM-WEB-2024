# Generated by Django 4.2.1 on 2023-05-16 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Categoria de productos',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigodeBarras', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10, max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, max_length=10)),
                ('cantidad', models.IntegerField(default=0)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyecto_masc.categoria')),
            ],
            options={
                'verbose_name': 'Productos de mi kiosco',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
    ]