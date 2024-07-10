# Generated by Django 5.0.6 on 2024-07-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_network', '0007_alter_suppliernode_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliernode',
            name='type',
            field=models.CharField(choices=[('entrepreneur', 'ИП'), ('factory', 'Завод'), ('retail_network', 'Розничная сеть')], max_length=30, verbose_name='Тип структуры'),
        ),
    ]
