# Generated by Django 4.2.16 on 2024-11-29 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mobile_devices", "0002_device_created_at_review_device"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="device",
            name="сategory",
        ),
        migrations.AddField(
            model_name="device",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="devices",
                to="mobile_devices.category",
            ),
        ),
    ]
