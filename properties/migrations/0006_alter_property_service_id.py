# Generated by Django 4.1.4 on 2023-04-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_property_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='service_id',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
