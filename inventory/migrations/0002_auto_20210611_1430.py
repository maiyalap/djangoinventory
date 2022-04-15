# Generated by Django 3.0 on 2021-06-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=20)),
                ('barcode', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=255)),
                ('location', models.CharField(max_length=20)),
                ('unit_id', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField()),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='StockItem',
        ),
    ]