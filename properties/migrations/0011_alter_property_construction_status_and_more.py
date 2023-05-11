# Generated by Django 4.1.4 on 2023-05-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_property_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='construction_status',
            field=models.CharField(choices=[('to_completion', 'Do wykończenia'), ('ready', 'Do zamieszkania')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='heating',
            field=models.CharField(choices=[('urban', 'Miejskie'), ('gas', 'Gazowe')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='service_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='type_of_building',
            field=models.CharField(choices=[('detached_house', 'Wolnostojący'), ('semi_detached_house', 'Bliźniak'), ('terraced_house', 'Szeregowiec')], default=None, max_length=100, null=True),
        ),
    ]
