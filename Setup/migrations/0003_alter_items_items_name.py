# Generated by Django 3.2 on 2021-04-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Setup', '0002_customer_storage_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='items_name',
            field=models.CharField(max_length=80),
        ),
    ]