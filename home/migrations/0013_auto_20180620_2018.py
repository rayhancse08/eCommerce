# Generated by Django 2.0.3 on 2018-06-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_product_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.TextField(default='', null=True),
        ),
    ]
