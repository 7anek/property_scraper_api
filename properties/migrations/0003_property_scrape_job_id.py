# Generated by Django 4.1.6 on 2023-02-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_area_property_description_property_floor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='scrape_job_id',
            field=models.UUIDField(default=None, null=True),
        ),
    ]
