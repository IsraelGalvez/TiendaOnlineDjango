# Generated by Django 4.0.2 on 2022-10-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_rename_categorys_producto_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.CharField(max_length=200, verbose_name='Imagen'),
        ),
    ]
