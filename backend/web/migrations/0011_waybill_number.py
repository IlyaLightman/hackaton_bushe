# Generated by Django 4.2.2 on 2023-06-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0010_order_hub_alter_orderhistory_event_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="waybill",
            name="number",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
