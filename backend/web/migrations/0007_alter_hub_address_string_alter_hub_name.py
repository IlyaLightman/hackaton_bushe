# Generated by Django 4.2.2 on 2023-06-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_waybill_status_alter_courier_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='address_string',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hub',
            name='name',
            field=models.TextField(),
        ),
    ]