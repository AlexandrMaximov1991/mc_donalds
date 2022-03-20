# Generated by Django 4.0.1 on 2022-03-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc_donalds', '0002_remove_productorder_amount_productorder__amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='_amount',
        ),
        migrations.AddField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]