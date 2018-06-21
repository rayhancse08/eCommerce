# Generated by Django 2.0.3 on 2018-06-05 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_newarival_previous_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField(default=0)),
                ('previous_product_price', models.FloatField(default=0)),
                ('product_image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='newarival',
            name='category',
        ),
        migrations.DeleteModel(
            name='NewArival',
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ProductStatus'),
        ),
    ]